import os
import re
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModel
from evaluators.evaluator import Evaluator

class ChatGLM_Evaluator(Evaluator):
    def __init__(self, choices, k, model_name, device):
        super(ChatGLM_Evaluator, self).__init__(choices, model_name, k)
        # try adding 'mirror="tuna"' and 'resume_download=True' if facing the 'read timed out' problem
        # or directly clone the model
        self.tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True, mirror="tuna")
        self.model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True, mirror="tuna", resume_download=True).half().to(device)

    def eval_subject(self, subject_name, test_df, dev_df=None, few_shot=False, cot=False, save_result_dir=None):
        correct_num = 0
        if save_result_dir:
            result = []
            score = []
        if few_shot:
            history = self.generate_few_shot_prompt(subject_name, dev_df, cot=cot)
        else:
            history = []
        answers = list(test_df['answer'])
        for row_index, row in tqdm(test_df.iterrows(), total=len(test_df)):
            question = self.format_example(row, include_answer=False, cot=cot)
            response, _ = self.model.chat(self.tokenizer, question, do_sample=False, history=history)
            response = response.strip()
            # For ChatGLM, we use answer extraction in answer-only mode too.
            ans, direct_extract = self.extract_cot_answer(row, response)
            if ans == answers[row_index]:
                correct_num += 1
                correct = 1
            else:
                correct = 0
            if save_result_dir:
                result.append(response)
                score.append(correct)
        correct_ratio = 100*correct_num/len(answers)
        
        if save_result_dir:
            test_df['model_output'] = result
            test_df['correctness'] = score
            test_df.to_csv(os.path.join(save_result_dir, f'{subject_name}_test.csv'))

        return correct_ratio
    
    def generate_few_shot_prompt(self, subject, dev_df, cot=False):
        message = []
        k = self.k
        if self.k == -1:
            k = dev_df.shape[0]
        message.append(self.format_example(dev_df.iloc[0, :], cot=cot, add_prompt=f"以下是中国关于{subject}考试的单项选择题，请选出其中的正确答案。\n\n"))
        for i in range(1, k):
            message.append(self.format_example(dev_df.iloc[i, :], cot=cot))
        return message
        
    def format_example(self, line, include_answer=True, cot=False, add_prompt=''):
        example = add_prompt + line['question']
        # print(example)
        for choice in self.choices:
            example += f'\n{choice}. {line[f"{choice}"]}'
        example += '\n答案：'
        if include_answer:
            if cot:
                ans = "让我们一步一步思考，\n" + line["explanation"] + f"\n所以答案是{line['answer']}。"
            else:
                ans = line["answer"]
            m = (example, ans)
            return m
        return example
    
    def extract_cot_answer(self, line, gen_ans):
        m = re.findall(r'所以答案是(.+?)。', gen_ans, re.M)
        if len(m) > 0 and m[-1] in self.choices:
            return m[-1], True
        answer_patterns = [
            r'([ABCD])是正确的',
            r'选项([ABCD])正确',
            r'答案为([ABCD])',
            r'答案是([ABCD])',
            r'答案([ABCD])',
            r'选择([ABCD])',
            r'答案：([ABCD])',
            r'选择答案([ABCD])'
        ]
        # RE extraction
        for answer_pattern in answer_patterns:
            m = re.search(answer_pattern, gen_ans, re.M)
            if m:
                answer = m.group(1)
                return answer, False
        # only containing one choice-character
        m = re.findall(r'[ABCD]', gen_ans, re.M)
        if len(m) == 1:
            answer = m[0]
            return answer, False
        answer_word_counter = 0
        # only containing one choice-context
        for c in self.choices:
            if str(line[f'{c}']) in gen_ans:
                answer = c
                answer_word_counter += 1
        if answer_word_counter == 1:
            return answer, False
        return '-', False