import os
import argparse
import pandas as pd
import torch
from evaluators.chatgpt import ChatGPT_Evaluator
from evaluators.moss import Moss_Evaluator
from evaluators.chatglm import ChatGLM_Evaluator
from evaluators.minimax import MiniMax_Evaluator

import time
choices = ["A", "B", "C", "D"]

def main(args):

    if "turbo" in args.model_name or "gpt-4" in args.model_name:
        evaluator=ChatGPT_Evaluator(
            choices=choices,
            k=args.ntrain,
            api_key=args.openai_key,
            model_name=args.model_name
        )
    elif "moss" in args.model_name:
        evaluator=Moss_Evaluator(
            choices=choices,
            k=args.ntrain,
            model_name=args.model_name
        )
    elif "chatglm" in args.model_name:
        if args.cuda_device:
            os.environ["CUDA_VISIBLE_DEVICES"] = args.cuda_device
        device = torch.device("cuda")
        evaluator=ChatGLM_Evaluator(
            choices=choices,
            k=args.ntrain,
            model_name=args.model_name,
            device=device
        )
    elif "minimax" in args.model_name:
        evaluator=MiniMax_Evaluator(
            choices=choices,
            k=args.ntrain,
            group_id=args.minimax_group_id,
            api_key=args.minimax_key,
            model_name=args.model_name
        )
    else:
        print("Unknown model name")
        return -1

    subject_name=args.subject
    if not os.path.exists(r"logs"):
        os.mkdir(r"logs")
    run_date=time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
    save_result_dir=os.path.join(r"logs",f"{args.model_name}_{run_date}")
    os.mkdir(save_result_dir)
    print(subject_name)
    val_file_path=os.path.join('data/val',f'{subject_name}_val.csv')
    val_df=pd.read_csv(val_file_path)
    if args.few_shot:
        dev_file_path=os.path.join('data/dev',f'{subject_name}_dev.csv')
        dev_df=pd.read_csv(dev_file_path)
        correct_ratio = evaluator.eval_subject(subject_name, val_df, dev_df, few_shot=args.few_shot,save_result_dir=save_result_dir,cot=args.cot)
    else:
        correct_ratio = evaluator.eval_subject(subject_name, val_df, few_shot=args.few_shot,save_result_dir=save_result_dir)
    print("Acc:",correct_ratio)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ntrain", "-k", type=int, default=5)
    parser.add_argument("--openai_key", type=str,default="xxx")
    parser.add_argument("--minimax_group_id", type=str,default="xxx")
    parser.add_argument("--minimax_key", type=str,default="xxx")
    parser.add_argument("--few_shot", action="store_true")
    parser.add_argument("--model_name",type=str)
    parser.add_argument("--cot",action="store_true")
    parser.add_argument("--subject","-s",type=str,default="operating_system")
    parser.add_argument("--cuda_device", type=str)    
    args = parser.parse_args()
    main(args)