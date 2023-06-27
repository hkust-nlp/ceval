<p align="center"> <img src="resources/title.png" style="width: 85%;" id="title-icon">       </p>

<p align="center">
   🌐 <a href="https://cevalbenchmark.com/" target="_blank">Website</a> • 🤗 <a href="https://huggingface.co/datasets/ceval/ceval-exam" target="_blank">Hugging Face</a> • ⏬ <a href="#data" target="_blank">Data</a> •   📃 <a href="https://arxiv.org/abs/2305.08322" target="_blank">Paper</a> 📖 <a href="resources/tutorial.md" target="_blank">Tutorial (ZH)</a>  <br>  <a href="https://github.com/SJTU-LIT/ceval/blob/main/README_zh.md">   中文</a> | <a href="https://github.com/SJTU-LIT/ceval/blob/main/README.md">English 
</p>

C-Eval is a comprehensive Chinese evaluation suite for foundation models. It consists of 13948 multi-choice questions spanning 52 diverse disciplines and four difficulty levels, as shown below. Please visit our [website](https://cevalbenchmark.com/) or check our [paper](https://arxiv.org/abs/2305.08322) for more details. 

We hope C-Eval could help developers track the progress and analyze the important strengths/shortcomings of their models.

📝 [Why C-Eval? How did we build it? (in Chinese)](https://yaofu.notion.site/C-Eval-6b79edd91b454e3d8ea41c59ea2af873)

<img src="resources/overview.png" style="zoom: 80%;" >



## Table of Contents

- [Leaderboard](#leaderboard)
- [C-Eval Hard Leaderboard](#c-eval-hard-leaderboard)
- [Results On Validation Split](#results-on-validation-split)
- [Data](#data)
- [How to Evaluate on C-Eval](#how-to-evaluate-on-c-eval)
- [How to Submit](#how-to-submit)
- [TODO](#todo)
- [Licenses](#licenses)
- [Citation](#citation)



## Leaderboard

Below are zero-shot and five-shot accuracies from the models that we evaluate in the initial release, please visit our official [Leaderboard](https://cevalbenchmark.com/static/leaderboard.html) for up-to-date models and their detailed results on each subject. We note that zero-shot performance is better than five-shot for many instruction-tuned models.

#### Zero-shot
| Model               | STEM | Social Science | Humanities | Other | Average |
| ------------------- | :--: | :------------: | :--------: | :---: | :-----: |
| GPT-4               | 65.2 |      74.7      |    62.5    | 64.7  |  66.4   |
| ChatGPT             | 49.0 |      58.0      |    48.8    | 50.4  |  51.0   |
| Claude-v1.3         | 48.5 |      58.6      |    47.3    | 50.1  |  50.5   |
| Bloomz-mt-176B           | 39.1 |      53.0      |    47.7    | 42.7  |  44.3   |
| GLM-130B            | 36.7 |      55.8      |    47.7    | 43.0  |  44.0   |
| Claude-instant-v1.0 | 38.6 |      47.6      |    39.5    | 39.0  |  40.6   |
| ChatGLM-6B          | 33.3 |      48.3      |    41.3    | 38.0  |  38.9   |
| LLaMA-65B           | 32.6 |      41.2      |    34.1    | 33.0  |  34.7   |
| MOSS                | 31.6 |      37.0      |    33.4    | 32.1  |  33.1   |
| Chinese-Alpaca-13B  | 27.4 |      39.2      |    32.5    | 28.0  |  30.9   |
| Chinese-LLaMA-13B   | 28.8 |      32.9      |    29.7    | 28.0  |  29.6   |

#### Five-shot
| Model               | STEM | Social Science | Humanities | Other | Average |
| ------------------- | :--: | :------------: | :--------: | :---: | :-----: |
| GPT-4               | 67.1 |      77.6      |    64.5    | 67.8  |  68.7   |
| ChatGPT             | 52.9 |      61.8      |    50.9    | 53.6  |  54.4   |
| Claude-v1.3         | 51.9 |      61.7      |    52.1    | 53.7  |  54.2   |
| Claude-instant-v1.0 | 43.1 |      53.8      |    44.2    | 45.4  |  45.9   |
| GLM-130B            | 34.8 |      48.7      |    43.3    | 39.8  |  40.3   |
| Bloomz-mt-176B      | 35.3 |      45.1      |    40.5    | 38.5  |  39.0   |
| LLaMA-65B           | 37.8 |      45.6      |    36.1    | 37.1  |  38.8   |
| ChatGLM-6B          | 30.4 |      39.6      |    37.4    | 34.5  |  34.5   |
| Chinese LLaMA-13B   | 31.6 |      37.2      |    33.6    | 32.8  |  33.3   |
| MOSS                | 28.6 |      36.8      |    31.0    | 30.3  |  31.1   |
| Chinese Alpaca-13B  | 26.0 |      27.2      |    27.8    | 26.4  |  26.7   |



## C-Eval Hard Leaderboard

We select 8 challenging math, physics, and chemistry subjects from C-Eval to form a separate benchmark, C-Eval Hard, which includes advanced mathematics, discrete mathematics, probability and statistics, college chemistry, college physics, high school mathematics, high school chemistry, and high school physics. These subjects often involve with complex LaTeX equations and require non-trivial reasoning abilities to solve. Zero-shot and five-shot accuracies are shown below.

| Model               | Zero-shot | Five-shot |
| ------------------- | :-------: | :-------: |
| GPT-4               |   53.3    |   54.9    |
| Claude-v1.3         |   37.6    |   39.0    |
| ChatGPT             |   36.7    |   41.4    |
| Claude-instant-v1.0 |   32.1    |   35.5    |
| Bloomz-mt           |   30.8    |   30.4    |
| GLM-130B            |   30.7    |   30.3    |
| LLaMA-65B           |   29.8    |   31.7    |
| ChatGLM-6B          |   29.2    |   23.1    |
| MOSS                |   28.4    |   24.0    |
| Chinese-LLaMA-13B   |   27.5    |   27.3    |
| Chinese-Alpaca-13B  |   24.4    |   27.1    |



## Results On Validation Split

Since we do not publicly release the labels for our test split, we provide the zero-shot and five-shot average accuracy on the validation split as a reference for developers. The validation split comprises a total of 1346 questions. We report the average answer-only accuracy across all subjects in table below. The average validation accuracy closely mirrors the average test accuracy as presented in [Leaderboard](#leaderboard).

| Model               | Zero-shot | Five-shot |
| ------------------- | :-------: | :-------: |
| GPT-4               |   66.7    |   69.9    |
| Claude-v1.3         |   52.1    |   55.5    |
| ChatGPT             |   50.8    |   53.5    |
| Bloomz-mt           |   45.9    |   38.0    |
| GLM-130B            |   44.2    |   40.8    |
| Claude-instant-v1.0 |   43.2    |   47.4    |
| ChatGLM-6B          |   39.7    |   37.1    |
| LLaMA-65B           |   38.6    |   39.8    |
| MOSS                |   35.1    |   28.9    |
| Chinese-Alpaca-13B  |   32.0    |   27.2    |
| Chinese-LLaMA-13B   |   29.4    |   33.1    |



## Data

#### Download

- Method 1: Download the zip file (you can also simply open the following link with the browser):
  ```
  wget https://huggingface.co/datasets/ceval/ceval-exam/resolve/main/ceval-exam.zip
  ```
  then unzip it and you may load the data with pandas:
  ```python
  import os
  import pandas as pd
  
  File_Dir="ceval-exam"
  test_df=pd.read_csv(os.path.join(File_Dir,"test","computer_network_test.csv"))
  ```

- Method 2: Directly load the dataset using [Hugging Face datasets](https://huggingface.co/datasets/ceval/ceval-exam):

  ```python
  from datasets import load_dataset
  dataset=load_dataset(r"ceval/ceval-exam",name="computer_network")
  
  print(dataset['val'][0])
  # {'id': 0, 'question': '使用位填充方法，以01111110为位首flag，数据为011011111111111111110010，求问传送时要添加几个0____', 'A': '1', 'B': '2', 'C': '3', 'D': '4', 'answer': 'C', 'explanation': ''}
  ```

#### Notes
To facilitate usage, we have organized the subject name handlers and English/Chinese names corresponding to 52 subjects. Please refer to [subject_mapping.json](https://github.com/SJTU-LIT/ceval/blob/main/subject_mapping.json) for details. The format is:

  ```
  # the dict key is the subject handler, and the dict value is (English name, Chinese name, category) tuple 
  {
      "computer_network": [
          "Computer Network",
          "计算机网络",
          "STEM"
      ],
      ...
      "filename":[
          "English Name",
          "Chinese Name"
          "Supercatagory Label(STEM, Social Science, Humanities or Other)"
      ]
  }
  ```

Each subject consists of three splits: dev, val, and test.  The dev set per subject consists of five exemplars with explanations for few-shot evaluation. The val set is intended to be used for hyperparameter tuning. And the test set is for model evaluation. Labels on the test split are not released, users are required to submit their results to automatically obtain test accuracy. [How to submit?](#how-to-submit) 

Below is a dev example from computer network:

  ```
id: 1
question: 25 °C时，将pH=2的强酸溶液与pH=13的强碱溶液混合，所得混合液的pH=11，则强酸溶液与强碱溶液 的体积比是(忽略混合后溶液的体积变化)____
A: 11:1
B: 9:1
C: 1:11
D: 1:9
answer: B
explanation: 
1. pH=13的强碱溶液中c(OH-)=0.1mol/L, pH=2的强酸溶液中c(H+)=0.01mol/L，酸碱混合后pH=11，即c(OH-)=0.001mol/L。
2. 设强酸和强碱溶液的体积分别为x和y，则：c(OH-)=(0.1y-0.01x)/(x+y)=0.001，解得x:y=9:1。
  ```



## How to Evaluate on C-Eval

Normally you can directly take the model's generations and extract the answer token (i.e. A,B,C,D) from it with simple regular expressions. In few-shot evaluation, the model usually follows the given template thus this is easy. Sometimes, however, especially in zero-shot evaluation for models without experiencing instruction tuning, the model may not follow the instruction well to give a well-formatted generation, in this case we recommend computing the probability of "A", "B", "C", "D" and take the most likely one as the answer -- this is a constrained decoding approach and was used in the official [MMLU test code](https://github.com/hendrycks/test/blob/4450500f923c49f1fb1dd3d99108a0bd9717b660/evaluate.py#L88). Such a probability approach is not applicable for chain-of-thought settings. [More detailed evaluation tutorial (in Chinese)](resources/tutorial.md). 

We use the following prompt when evaluating the models in our first release:
#### answer-only prompt
```
以下是中国关于{科目}考试的单项选择题，请选出其中的正确答案。

{题目1}
A. {选项A}
B. {选项B}
C. {选项C}
D. {选项D}
答案：A

[k-shot demo, note that k is 0 in the zero-shot case]

{测试题目}
A. {选项A}
B. {选项B}
C. {选项C}
D. {选项D}
答案：
```

#### chain-of-thought prompt
```
以下是中国关于{科目}考试的单项选择题，请选出其中的正确答案。

{题目1}
A. {选项A}
B. {选项B}
C. {选项C}
D. {选项D}
答案：让我们一步一步思考，
1. {解析过程步骤1}
2. {解析过程步骤2}
3. {解析过程步骤3}
所以答案是A。

[k-shot demo, note that k is 0 in the zero-shot case]

{测试题目}
A. {选项A}
B. {选项B}
C. {选项C}
D. {选项D}
答案：让我们一步一步思考，
1. 
```



## How to Submit

You need to first prepare a UTF-8 encoded JSON file with the following format, please refer to [submission_example.json](https://github.com/SJTU-LIT/ceval/blob/main/submission_example.json) for details.

  ```
  ## key within each subject is the "id" field from the dataset
  {
      "chinese_language_and_literature": {
          "0": "A",
          "1": "B",
          "2": "B",
          ...
      },
      
      "subject_name":{
      "0":"ans_1",
      "1":"ans_2",
      ...
      }
      ....
  }
  ```
  Then you can submit the prepared json file [here](https://cevalbenchmark.com/static/user_interface.html), **note that you need to first log in to access the submission page**.



## TODO

- [x] add zero-shot results
- [ ] incorporate into openai eval



## Licenses

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

This work is licensed under a [MIT License](https://lbesson.mit-license.org/).

[![CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

The C-Eval dataset is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).



## Citation

Please cite our paper if you use our dataset.
```
@article{huang2023ceval,
title={C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models}, 
author={Huang, Yuzhen and Bai, Yuzhuo and Zhu, Zhihao and Zhang, Junlei and Zhang, Jinghan and Su, Tangjun and Liu, Junteng and Lv, Chuancheng and Zhang, Yikai and Lei, Jiayi and Fu, Yao and Sun, Maosong and He, Junxian},
journal={arXiv preprint arXiv:2305.08322},
year={2023}
}
```
