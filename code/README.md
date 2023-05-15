# README



### OpenAI and Moss

* Place the data folder in the root directory and name it "data".

* Run the evaluation script `code/openai_and_moss/eval.py` from the project root directory with the following optional arguments:

  ```
  --ntrain specifies the number of few-shot demos
  --openai_key specifies the OpenAI key
  --few_shot whether to use few-shot learning
  --model_name specifies the model name, which can be moss, gpt-3.5-turbo, gpt-4
  --cot whether to use chain-of-thought
  --subject specifies subject to be tested
  ```

* Usage examples:

  * Evaluate gpt-3.5-turbo in answer-only setting on computer networks

    ```bash
    python code/openai_and_moss/eval.py --openai_key OPENAI_KEY --model_name gpt-3.5-turbo --few_shot -s operating_system
    ```

  * Evaluate gpt-3.5-turbo in chain-of-thought setting on computer networks

    ```bash
    python code/openai_and_moss/eval.py --openai_key OPENAI_KEY --model_name gpt-3.5-turbo --few_shot -s operating_system --cot
    ```

  * Evaluate MOSS in answer-only setting on computer architecture

    ```bash
    python code/openai_and_moss/eval.py --model_name moss --few_shot --ntrain 5 -s "computer_architecture" 
    ```

  * Evaluate MOSS in chain-of-thought setting on computer architecture

    ```bash
    python code/openai_and_moss/eval.py --model_name moss --few_shot --ntrain 5 -s "computer_architecture" --cot
    ```

    

