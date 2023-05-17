<p align="center"> <img src="resources/title.png" style="width: 85%;" id="title-icon">       </p>

<p align="center">
   🌐 <a href="https://cevalbenchmark.com/" target="_blank">网站</a> • 🤗 <a href="https://huggingface.co/datasets/ceval/ceval-exam" target="_blank">Hugging Face</a> • ⏬ <a href="#数据" target="_blank">数据</a> • 📃 <a href="https://arxiv.org/abs/2305.08322"" target="_blank">论文</a> <br> <a href="https://github.com/SJTU-LIT/ceval/blob/main/README.md">English|<a href="https://github.com/SJTU-LIT/ceval/blob/main/README_zh.md">中文</a>
</p>



C-Eval 是全面的中文基础模型评估套件，涵盖了52个不同学科的13948个多项选择题，分为四个难度级别，如下所示。更多详情，请访问我们的[网站](https://cevalbenchmark.com/)或查看我们的[论文](https://arxiv.org/abs/2305.08322)。

<img src="resources/overview.png" style="zoom: 80%;" >



## 目录

* [排行榜](#排行榜)
* [C-Eval Hard 排行榜](#c-eval-hard-排行榜)
* [验证集结果](#验证集结果)
* [数据](#数据)
* [如何提交](#如何提交)
* [Licenses](#licenses)
* [引用](#引用)



## 排行榜

下面列出了我们在初始版本中进行评估的模型，请访问我们官方[排行榜](https://cevalbenchmark.com/static/leaderboard_zh.html)了解最新模型及其在每个学科中的详细结果。

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



## C-Eval Hard 排行榜

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



## 验证集结果

因为我们不会公开发布测试数据集的标签，所以我们提供验证集的平均准确率作为参考。验证集总共有1346个问题，平均每个科目不到30个问题。因此，特定科目的准确率不具有参考价值。我们在下表中提供在所有科目上的平均准确率。Val集的平均准确率与[排行榜](#排行榜)中呈现的平均测试准确率非常接近。

| Model               | Average |
| ------------------- | :-----: |
| GPT-4               |  69.9   |
| Claude-v1.3         |  55.5   |
| ChatGPT             |  53.5   |
| MiniMax             |  48.4   |
| Claude-instant-v1.0 |  47.4   |
| GLM-130B            |  40.8   |
| LLaMA-65B           |  39.8   |
| Bloomz-mt           |  38.0   |
| ChatGLM-6B          |  37.1   |
| Chinese-LLaMA-13B   |  33.1   |
| MOSS                |  28.9   |
| Chinese-Alpaca-13B  |  27.2   |



## 数据

#### 下载

* 方法一：从 [Onedrive](https://onedrive.live.com/download?cid=19737A21B01C55D4&resid=19737A21B01C55D4!983&authkey=AGch_tVH959ZJiw) 下载，数据以 csv 格式存储，使用 UTF-8 编码。然后可以使用 pandas加载数据：

  ```
  import os
  import pandas as pd
  
  File_Dir="data"
  test_df=pd.read_csv(os.path.join(File_Dir,"test","advanced_mathematics_test.csv"))
  ```

* 方法二：使用[huggingface datasets](https://huggingface.co/datasets/ceval/ceval-exam)直接加载数据集。示例如下：

  ```python
  from datasets import load_dataset
  dataset=load_dataset(r"ceval/ceval-exam",name="advanced_mathematics")
  ```

#### 说明
为了方便使用，我们已经整理出了与 52 个科目对应的学科名称处理程序以及它们的中英文名称。具体细节请查看 [subject_mapping.json](https://github.com/SJTU-LIT/ceval/blob/main/subject_mapping.json)。格式如下：

```
{
	"computer_network": [
		"Computer Network",
		"计算机网络",
		"STEM"
	],
	...
	"filename":[
	"英文名称",
	"中文名称"
	"类别(STEM,Social Science,Humanities,Other四选一)"
	]
}
```

每个科目由三个部分组成：dev、val 和 test。每个科目的 dev 集包含五个示范实例以及为 few-shot 评估提供的解释。val 集旨在用于超参数调整。而 test 集则用于模型评估。test 集上的标签不会公开，需要用户提交其结果才能自动获得测试准确性。[如何提交？](#如何提交) 

下面是计算机网络的示例：

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



## 如何提交

您首先需要准备一个 UTF-8 编码的 JSON 文件，并按照以下格式编写。详情请参考[submission_example.json](https://github.com/SJTU-LIT/ceval/blob/main/submission_example.json)。

```
## 每个学科内部的键名是数据集中的"id"字段
{
    "chinese_language_and_literature": {
        "0": "A",
        "1": "B",
        "2": "B",
        ...
    },
    
    "学科名称":{
    "0":"答案1",
    "1":"答案2",
    ...
    }
    ....
}
```

然后你可以将准备好的JSON文件提交到[这里](https://cevalbenchmark.com/static/user_interface_zh.html)，**请注意，你需要先登录才能访问提交页面**。



## Licenses

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

本项目遵循 [MIT License](https://lbesson.mit-license.org/).

[![CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

C-Eval数据集遵循 [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).



## 引用

如果您使用了我们的数据集，请引用我们的论文。

```
@article{huang2023ceval,
title={C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models}, 
author={Huang, Yuzhen and Bai, Yuzhuo and Zhu, Zhihao and Zhang, Junlei and Zhang, Jinghan and Su, Tangjun and Liu, Junteng and Lv, Chuancheng and Zhang, Yikai and Lei, Jiayi and Qi, Fanchao and Fu, Yao and Sun, Maosong and He, Junxian},
journal={arXiv preprint arXiv:2305.08322},
year={2023}
}
```

