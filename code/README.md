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
