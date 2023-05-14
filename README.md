# C-Eval： A Multi-Level Multi-Discipline Chinese Evaluation Suite

<p align="center">
   🌐 <a href="https://cevalbenchmark.com/" target="_blank">网站</a> • 🤗 <a href="https://huggingface.co/datasets/ceval/ceval-exam" target="_blank">Hugging Face</a> • ⏬ <a href="https://onedrive.live.com/download?cid=19737A21B01C55D4&resid=19737A21B01C55D4!983&authkey=AGch_tVH959ZJiw" target="_blank">下载</a> •  ✉️ <a href="mailto:ceval.benchmark@gmail.com">邮箱</a> • 📃 <a href="https://google.com"" target="_blank">论文</a> <br>
</p>



### 介绍

C-Eval是一个综合性的语言模型中文评估组件，旨在评估语言模型在中文语境中的知识和推理能力。C-Eval 包括四个难度级别的多项选择题：初中、高中、大学和专业测试。这些问题涵盖 52 个不同的学科，包括STEM，人文科学，社会科学和其他四个大类。进一步探索C-Eval，请访问我们的[网站](https://cevalbenchmark.com/)。我们在网站上面给出了52个科目以及对应的[样例](https://cevalbenchmark.com/static/explore.html)。并且，您可以通过我们的网站上传测试结果，获得对应的分数，在[排行榜](https://cevalbenchmark.com/static/leaderboard.html)展示成绩。



### 排行榜



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



### C-Eval Hard排行榜

我们选取了C-Eval中具有挑战性的数学、物理和化学科目组成C-Eval Hard，包括：高等数学、离散数学、概率统计、大学化学、大学物理、高中数学、高中物理、高中化学八个科目。这些科目包含了复杂的LaTex公式，需要非凡的推理能力才能解决。

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



### 下载方法

* 方法一：[Onedrive](https://onedrive.live.com/download?cid=19737A21B01C55D4&resid=19737A21B01C55D4!983&authkey=AGch_tVH959ZJiw)下载

* 方法二：使用[Hugging Face](https://huggingface.co/datasets/ceval/ceval-exam)直接加载数据集，样例如下：

  ```python
  from datasets import load_dataset
  dataset=load_dataset(r"ceval/ceval-exam",name="advanced_mathematics")
  ```



### 科目

数据集主要包含52个科目，如下图所示。

<img src="https://cevalbenchmark.com/static/img/overview.png" style="zoom: 80%;" >



### 数据格式

* 我们将每一个科目分为dev，val和test三个集合。dev集主要用于Few-shot Learning（包含5条数据），val集用于模型调试，test集用于最终测试。

* 数据采用csv格式进行封装，采用utf-8编码格式。

* 以计算机网络为例：

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

* **注意：val集不包含explanation，test集不包含answer和explanation**。



### 使用

* 为了方便使用，我们整理了52个科目对应的文件名和中英文名称，参考subject_mapping.json。格式如下：

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
  	"中文名称"
  	"类别(STEM,Social Science,Humanities,Other四选一)"
  	]
  }
  ```

* 从[Hugging Face](https://huggingface.co/datasets/ceval/ceval-exam)使用，分为"dev"，"validation"和"test"三个集合

  ```python
  import json
  from datasets import load_dataset
  
  with open(r"subject_mapping.json",encoding="utf-8") as f:
      subject_mapping=json.load(f)
      
  for k in subject_mapping.keys():
      dataset=load_dataset(r"ceval/ceval-exam",name=k)
      print(dataset['dev'][1])
      print(dataset['validation'][1])
      print(dataset['test'][1])    
  ```

* [下载](google.com)压缩文件解压后，使用Pandas等库读取。例如：

  ```python
  import os
  import pandas as pd
  
  File_Dir="data"
  
  with open(r"subject_mapping.json",encoding="utf-8") as f:
      subject_mapping=json.load(f)
  
  for k in subject_mapping.keys():
      for s in ["dev","val","test"]:
          pd.read_csv(os.path.join(File_Dir,s,f"{k}_{s}.csv"))
  ```

  

### Licenses

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

本项目遵循 [MIT License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

[![License: CC BY-SA 4.0](https://camo.githubusercontent.com/bdc6a3b8963aa99ff57dfd6e1e4b937bd2e752bcb1f1936f90368e5c3a38f670/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d434325323042592d2d5341253230342e302d6c69676874677265792e737667)](https://creativecommons.org/licenses/by-sa/4.0/)

C-Eval数据集遵循 [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).
