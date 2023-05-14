# C-Eval： A Multi-Level Multi-Discipline Chinese Evaluation Suite

<p align="center">
   🌐 <a href="https://cevalbenchmark.com/" target="_blank">网站</a> • 🤗 <a href="https://huggingface.co/datasets/ceval/ceval-exam" target="_blank">Hugging Face</a> • ⏬ <a href="https://models.aminer.cn/glm/zh-CN/download/GLM-130B" target="_blank">下载</a> •  ✉️ <a href="mailto:ceval.benchmark@gmail.com">邮箱</a> • 📃 <a href="https://google.com"" target="_blank">论文</a> <br>
</p>



### 介绍

C-Eval是一个综合性的语言模型中文评估组件，旨在评估语言模型在中文语境中的知识和推理能力。C-Eval 包括四个难度级别的多项选择题：初中、高中、大学和专业测试。这些问题涵盖 52 个不同的学科，包括STEM，人文科学，社会科学和其他四个大类。进一步探索C-Eval，请访问我们的[网站](https://cevalbenchmark.com/)。我们在网站上面给出了52个科目以及对应的[样例](https://cevalbenchmark.com/static/explore.html)。并且，您可以通过我们的网站上传测试结果，获得对应的数据，在[Leaderboard](https://cevalbenchmark.com/static/leaderboard.html)展示成绩。



### 下载方法

* 方法一：Dropbox或者百度云

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

  





