#!/bin/bash
#SBATCH -A research
#SBATCH --qos=low
#SBATCH -n 10
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=3000
#SBATCH --time=3-00:00:00
#SBATCH --mail-type=END

source "/home2/divy.kala/Music_Generation/MusicGen/bin/activate"
module load cuda/10.1
module load python/3.7.4

 
while python3 -u train.py > output.log; do true; done 
#python3 -u train.py > output.log
