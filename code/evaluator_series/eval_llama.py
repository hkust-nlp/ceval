import json
import os
import time
from evaluators.llama import LLaMA_Evaluator
from pathlib import Path
from typing import Tuple

import fire
import pandas as pd
import torch
from fairscale.nn.model_parallel.initialize import initialize_model_parallel
from llama import ModelArgs, Tokenizer, Transformer

choices = ["A", "B", "C", "D"]

generate_args = {
    "max_gen_length": 256,
    "temperature": 0.8,
    "top_p": 0.95,
}

def setup_model_parallel() -> Tuple[int, int]:
    local_rank = int(os.environ.get("LOCAL_RANK", -1))
    world_size = int(os.environ.get("WORLD_SIZE", -1))
    if not torch.distributed.is_initialized():
        torch.distributed.init_process_group("nccl")
        initialize_model_parallel(world_size)
        torch.cuda.set_device(local_rank)
        torch.manual_seed(1)
    return local_rank, world_size


def load(
    ckpt_dir,
    param_size,
    ntrain,
    max_seq_len
) -> LLaMA_Evaluator:
    start_time = time.time()
    local_rank, world_size = setup_model_parallel()
    model_path = Path(ckpt_dir) / f"{param_size}B"
    tokenizer_path = f"{ckpt_dir}/tokenizer.model"
    checkpoints = sorted(Path(model_path).glob("*.pth"))

    assert world_size == len(
        checkpoints
    ), f"Loading a checkpoint for MP={len(checkpoints)} but world size is {world_size}"

    ckpt_path = checkpoints[local_rank]
    if local_rank == 0:
        print("Loading")
    checkpoint = torch.load(ckpt_path, map_location="cpu")

    with open(Path(model_path) / "params.json", "r") as f:
        params = json.loads(f.read())

    model_args = ModelArgs(
        max_seq_len=max_seq_len,
        **params
    )

    tokenizer = Tokenizer(
        model_path=tokenizer_path
    )

    model_args.vocab_size = tokenizer.n_words
    torch.set_default_tensor_type(torch.cuda.HalfTensor)
    model = Transformer(model_args)
    torch.set_default_tensor_type(torch.FloatTensor)
    model.load_state_dict(checkpoint, strict=False)

    evaluator = LLaMA_Evaluator(
        model=model,
        tokenizer=tokenizer,
        choices=choices,
        k=ntrain,
    )
    if local_rank == 0:
        print(f"Loaded in {time.time() - start_time:.2f} seconds")
    return evaluator


def main(
        ckpt_dir: str,
        param_size: int = 13,
        ntrain: int = 5,
        few_shot: bool = False,
        cot: bool = False,
        subject: str = "operating_system",
        max_seq_len: int = 2048,
):
    evaluator = load(
        ckpt_dir,
        param_size=param_size,
        ntrain=ntrain,
        max_seq_len=max_seq_len
    )
    
    subject_name = subject
    run_date = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
    save_result_dir = os.path.join(
        r"logs", f"LLaMA_{param_size}{'_CoT' if cot else ''}_{run_date}")
    os.makedirs(save_result_dir, exist_ok=True)
    
    local_rank, _ = setup_model_parallel()
    if local_rank == 0:
        print(f"Start evaluating {subject_name}")
    
    val_file_path = os.path.join('data/val', f'{subject_name}_val.csv')
    val_df = pd.read_csv(val_file_path)

    if few_shot:
        dev_file_path = os.path.join('data/dev', f'{subject_name}_dev.csv')
        dev_df = pd.read_csv(dev_file_path)
        correct_ratio = evaluator.eval_subject(
            subject_name,
            val_df,
            dev_df,
            few_shot=few_shot,
            save_result_dir=save_result_dir,
            cot=cot,
            **generate_args
        )
    else:
        correct_ratio = evaluator.eval_subject(
            subject_name,
            val_df,
            save_result_dir=save_result_dir,
            cot=cot,
            **generate_args
        )
    
    if local_rank == 0:
        print("Acc:", correct_ratio)


if __name__ == "__main__":
    fire.Fire(main)
