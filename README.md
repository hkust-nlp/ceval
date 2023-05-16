<p align="center"> <img src="resources/title.png" style="width: 85%;" id="title-icon">       </p>

<p align="center">
   🌐 <a href="https://cevalbenchmark.com/" target="_blank">Website</a> • 🤗 <a href="https://huggingface.co/datasets/ceval/ceval-exam" target="_blank">Hugging Face</a> • ⏬ <a href="#download" target="_blank">Download</a> •   📃 <a href="https://arxiv.org/abs/2305.08322" target="_blank">Paper</a>  <br>  <a href="https://github.com/SJTU-LIT/ceval/blob/main/README_zh.md">   中文</a>|<a href="https://github.com/SJTU-LIT/ceval/blob/main/README.md">English 
</p>

C-Eval is a comprehensive Chinese evaluation suite for foundation models. It consists of 13948 multi-choice questions spanning 52 diverse disciplines and four difficulty levels, as shown below. Please visit our [website](https://cevalbenchmark.com/) or check our [paper](https://arxiv.org/abs/2305.08322) for more details. 

<img src="resources/overview.png" style="zoom: 80%;" >



## Table of Contents

- [Leaderboard](#leaderboard)
- [C-Eval Hard Leaderboard](#c-eval-hard-leaderboard)
- [Data](#data)
- [How to Submit](#how-to-submit)
- [Licenses](#licenses)
- [Citation](#citation)


## Leaderboard
Below are from the models that we evaluate in the initial release, please visit our official [Leaderboard](https://cevalbenchmark.com/static/leaderboard.html) for up-to-date models and their detailed results on each subject.

| Model               | STEM | Social Science | Humanities | Other | Average |
| ------------------- | :--: | :------------: | :--------: | :---: | :-----: |
| GPT-4               | 67.1 |      77.6      |    64.5    | 67.8  |  68.7   |
| ChatGPT             | 52.9 |      61.8      |    50.9    | 53.6  |  54.4   |
| Claude-v1.3         | 51.9 |      61.7      |    52.1    | 53.7  |  54.2   |
| MiniMax             | 40.6 |      60.3      |    56.6    | 46.6  |  49.0   |
| Claude-instant-v1.0 | 43.1 |      53.8      |    44.2    | 45.4  |  45.9   |
| GLM-130B            | 34.8 |      48.7      |    43.3    | 39.8  |  40.3   |
| Bloomz-mt           | 35.3 |      45.1      |    40.5    | 38.5  |  39.0   |
| LLaMA-65B           | 37.8 |      45.6      |    36.1    | 37.1  |  38.8   |
| ChatGLM-6B          | 30.4 |      39.6      |    37.4    | 34.5  |  34.5   |
| Chinese LLaMA-13B   | 31.6 |      37.2      |    33.6    | 32.8  |  33.3   |
| MOSS                | 28.6 |      36.8      |    31.0    | 30.3  |  31.1   |
| Chinese Alpaca-13B  | 26.0 |      27.2      |    27.8    | 26.4  |  26.7   |



## C-Eval Hard Leaderboard

We select 8 challenging math, physics, and chemistry subjects from C-Eval to form a separate benchmark, C-Eval Hard, which includes advanced mathematics, discrete mathematics, probability and statistics, college chemistry, college physics, high school mathematics, high school chemistry, and high school physics. These subjects often involve with complex LaTeX equations and require non-trivial reasoning ability to solve.

| Model               | Accuracy |
| ------------------- | :------: |
| GPT-4               |   54.9   |
| ChatGPT             |   41.4   |
| Claude-v1.3         |   39.0   |
| Claude-instant-v1.0 |   35.5   |
| LLaMA-65B           |   31.7   |
| Bloomz-mt           |   30.4   |
| GLM-130B            |   30.3   |
| Chinese LLaMA-13B   |   27.3   |
| MiniMax             |   27.3   |
| Chinese Alpaca-13B  |   27.1   |
| MOSS                |   24.0   |
| ChatGLM-6B          |   23.1   |



## Data

#### Download
- Method 1: Download from [Onedrive](https://onedrive.live.com/download?cid=19737A21B01C55D4&resid=19737A21B01C55D4!983&authkey=AGch_tVH959ZJiw), the data is stored in the csv format and using utf-8 encoding. Then the data may be loaded with pandas:
  ```python
  import os
  import pandas as pd
  
  File_Dir="data"
  test_df=pd.read_csv(os.path.join(File_Dir,"test","advanced_mathematics_test.csv"))
  ```

- Method 2: Directly load the dataset using [Hugging Face](https://huggingface.co/datasets/ceval/ceval-exam). Example is as follows

  ```python
  from datasets import load_dataset
  dataset=load_dataset(r"ceval/ceval-exam",name="advanced_mathematics")
  ```

To facilitate usage, we have organized the subject name handlers and English/Chinese names corresponding to 52 subjects. Please refer to [subject_mapping.json](https://github.com/SJTU-LIT/ceval/blob/main/subject_mapping.json) for details. The format is as follows:

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
  question: 滑动窗口的作用是____。
  A: 流量控制
  B: 拥塞控制
  C: 路由控制
  D: 差错控制
  answer: A
  explantion: 1. 滑动窗口是一种流量控制机制，用于控制发送方向接收方发送数据的速率，以避免接收方无法处理过多的数据而导致数据丢失或拥塞。
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

  

## Licenses

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

This work is licensed under a [MIT License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

```
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]
```

[![CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].



## Citation

Please cite our paper if you use our dataset.
```
@article{huang2023ceval,
title={C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models}, 
author={Huang, Yuzhen and Bai, Yuzhuo and Zhu, Zhihao and Zhang, Junlei and Zhang, Jinghan and Su, Tangjun and Liu, Junteng and Lv, Chuancheng and Zhang, Yikai and Lei, Jiayi and Qi, Fanchao and Fu, Yao and Sun, Maosong and He, Junxian},
journal={arXiv preprint arXiv:2305.08322},
year={2023}
}
```
