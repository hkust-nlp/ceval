# README



### OpenAI, Moss, ChatGLM and MiniMax

* Place the data folder in the root directory and name it "data".

* Run the evaluation script `code/evaluator_series/eval.py` from the project root directory with the following optional arguments:

  ```
  --ntrain specifies the number of few-shot demos
  --openai_key specifies the OpenAI key
  --minimax_group_id and --minimax_key specifies the group-id and api-key used for MiniMax
  --few_shot whether to use few-shot learning
  --model_name specifies the model name, which can be moss, gpt-3.5-turbo, gpt-4
  --cot whether to use chain-of-thought
  --subject specifies subject to be tested
  --cuda_device specifies the cuda device to be used (for ChatGLM)
  ```

* Usage examples:

  * Evaluate gpt-3.5-turbo in answer-only setting on computer networks

    ```bash
    python code/evaluator_series/eval.py --openai_key OPENAI_KEY --model_name gpt-3.5-turbo --few_shot -s operating_system
    ```

  * Evaluate gpt-3.5-turbo in chain-of-thought setting on computer networks

    ```bash
    python code/evaluator_series/eval.py --openai_key OPENAI_KEY --model_name gpt-3.5-turbo --few_shot -s operating_system --cot
    ```

  * Evaluate MOSS in answer-only setting on computer architecture

    ```bash
    python code/evaluator_series/eval.py --model_name moss --few_shot --ntrain 5 -s "computer_architecture" 
    ```

  * Evaluate MOSS in chain-of-thought setting on computer architecture

    ```bash
    python code/evaluator_series/eval.py --model_name moss --few_shot --ntrain 5 -s "computer_architecture" --cot
    ```

  * Evaluate ChatGLM in answer-only setting on computer architecture

    ```bash
    python code/evaluator_series/eval.py --model_name chatglm --few_shot --ntrain 5 -s "computer_architecture" --cuda_device CUDA_INDEX
    ```
    It may take some time to download the model when running for the first time.

  * Evaluate ChatGLM in chain-of-thought setting on computer architecture

    ```bash
    python code/evaluator_series/eval.py --model_name chatglm --few_shot --ntrain 5 -s "computer_architecture" --cuda_device CUDA_INDEX --cot
    ```

  * Evaluate Minimax in answer-only setting on computer architecture

    ```bash
    python code/evaluator_series/eval.py --model_name minimax --minimax_group_id MINIMAX_GROUP_ID --minimax_key MINIMAX_KEY --few_shot --ntrain 5 -s "computer_architecture"
    ```
    It may take some time to download the model when running for the first time.

  * Evaluate Minimax in chain-of-thought setting on computer architecture

    ```bash
    python code/evaluator_series/eval.py --model_name minimax --minimax_group_id MINIMAX_GROUP_ID --minimax_key MINIMAX_KEY --few_shot --ntrain 5 -s "computer_architecture" --cot
    ```

### LLaMA

* Place the data folder in the root directory and name it "data".

* Download the LLaMA code from [LLaMA repo](https://github.com/facebookresearch/llama) released by Facebook Research and setup the required environments.

  ```bash
  git clone https://github.com/facebookresearch/llama && cd llama
  pip install -r requirements.txt
  pip install -e .
  ```

* Request for the LLaMA tokenizer and model files following the instruction in the LLaMA repo and download them after the request is approved.

* Run the evaluation script `code/evaluator_series/eval_llama.py` from the project root directory with the following optional arguments:
  
    ```
    --nproc_per_node specifies the number of GPUs to use, different models require different values
    --ckpt_dir specifies the path to the checkpoint file and tokenizer
    --param_size specifies the parameter size of the model
    --ntrain specifies the number of few-shot demos
    --few_shot whether to use few-shot learning
    --cot specifies whether to use chain-of-thought
    --subject specifies the subject to be tested
    ```

* Usage examples:

  * Evaluate LLaMA-13B in answer-only setting on computer networks

    ```bash
    torchrun --nproc_per_node 2 code/evaluator_series/eval_llama.py --ckpt_dir [PATH TO CKPT] --param_size 13 --few_shot --ntrain 5 --subject [SUBJECT NAME]
    ```
  
  * Evaluate LLaMA-65B in chain-of-thought setting on computer networks

    ```bash
    torchrun --nproc_per_node 8 code/evaluator_series/eval_llama.py --ckpt_dir [PATH TO CKPT] --param_size 65 --few_shot --cot --ntrain 5 --subject [SUBJECT NAME]
    ```
