

# C-Eval： A Multi-Level Multi-Discipline Chinese Evaluation Suite

<p align="center">
   🌐 <a href="https://cevalbenchmark.com/" target="_blank">Website</a> • 🤗 <a href="https://huggingface.co/datasets/ceval/ceval-exam" target="_blank">Hugging Face</a> • ⏬ <a href="https://onedrive.live.com/download?cid=19737A21B01C55D4&resid=19737A21B01C55D4!983&authkey=AGch_tVH959ZJiw" target="_blank">Download</a> •  ✉️ <a href="mailto:ceval.benchmark@gmail.com">Email</a> • 📃 <a href="https://google.com"" target="_blank">Paper</a> <br>  <a href="https://github.com/SJTU-LIT/ceval/blob/main/README.md">中文</a>|<a href="https://github.com/SJTU-LIT/ceval/blob/main/README_en.md">English 
</p>

## Table of Contents

- [Introduction](#introduction)
- [Leaderboard](#leaderboard)
- [C-Eval Hard Leaderboard](#c-eval-hard-leaderboard)
- [Download](#download)
- [Subjects](#subjects)
- [Data Format](#data-format)
- [Usage](#usage)
- [License](#license)



### Introduction

C-Eval is a comprehensive language model Chinese evaluation component, aimed at evaluating the knowledge and reasoning ability of language models in the Chinese context. C-Eval includes multiple-choice questions at four levels of difficulty: middle school, high school, college, and professional tests. These questions cover 52 different subjects, including STEM, humanities, social sciences, and four other categories. For further exploration of C-Eval, please visit our [website](https://cevalbenchmark.com/). We provide the 52 subjects and corresponding samples on the website. Additionally, you can submit test results through our website, and obtain corresponding score, which will be displayed on the [leaderboard](https://cevalbenchmark.com/static/leaderboard.html)



### Leaderboard

| Model               | STEM | Social Science | Humanities | Other | Average |
| ------------------- | :--: | :------------: | :--------: | :---: | :-----: |
| Random              | 25.0 |      25.0      |    25.0    | 25.0  |  25.0   |
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



### C-Eval Hard Leaderboard

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



### Download

- Method 1: Download from [Onedrive](https://onedrive.live.com/download?cid=19737A21B01C55D4&resid=19737A21B01C55D4!983&authkey=AGch_tVH959ZJiw)

- Method 2: Directly load the dataset using [Hugging Face](https://huggingface.co/datasets/ceval/ceval-exam). Example is as follows

  ```python
  from datasets import load_dataset
  dataset=load_dataset(r"ceval/ceval-exam",name="advanced_mathematics")
  ```



### Subjects

The Question in C-Eval span 52 diverse disciplines in the table shown below.

<img src="https://cevalbenchmark.com/static/img/overview.png" style="zoom: 80%;" >





### Data Format

* We have divided each subject into three sets: dev, val, and test.  The dev set per subject consists of five exemplars to facilitate few-shot evaluation.  The val set is intended to be used for hyperparameter tuning. And the test set is for model evaluation.

* The data is stored in the csv format and using the utf-8 encoding format.

* Take computer network as an example:

  ```python
  id: 1
  question: 滑动窗口的作用是____。
  A: 流量控制
  B: 拥塞控制
  C: 路由控制
  D: 差错控制
  answer: A
  explantion: 1. 滑动窗口是一种流量控制机制，用于控制发送方向接收方发送数据的速率，以避免接收方无法处理过多的数据而导致数据丢失或拥塞。
  ```

* **Note: The explanation is not included in the val set, and the answer and explanation have been removed from the test set to prevent data leak.**



### Usage

* To facilitate usage, we have organized the file names and English/Chinese names corresponding to 52 subjects. Please refer to [subject_mapping.json](https://github.com/SJTU-LIT/ceval/blob/main/subject_mapping.json) for details. The format is as follows:

  ```
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

* Load from [Hugging Face](https://huggingface.co/datasets/ceval/ceval-exam). We have divided dataset into three sets: dev, validation, and test.

  ```python
  from datasets import load_dataset
  dataset=load_dataset(r"ceval/ceval-exam",name="advanced_mathematics")
  ```

* After downloading and unzipping the compressed file, use libraries such as Pandas to read it. For example:

  ```python
  import os
  import pandas as pd
  
  File_Dir="data"
  test_df=pd.read_csv(os.path.join(File_Dir,"test","advanced_mathematics_test.csv"))
  ```

  



### Licenses

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

This work is licensed under a [MIT License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

[![License: CC BY-SA 4.0](https://camo.githubusercontent.com/bdc6a3b8963aa99ff57dfd6e1e4b937bd2e752bcb1f1936f90368e5c3a38f670/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d434325323042592d2d5341253230342e302d6c69676874677265792e737667)](https://creativecommons.org/licenses/by-sa/4.0/)

The C-Eval dataset is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).
