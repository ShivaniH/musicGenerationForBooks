#!/bin/bash
#SBATCH -A research
#SBATCH --qos=low
#SBATCH -n 10
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=3000
#SBATCH --time=4-00:00:00


source "/home2/divy.kala/Music_Generation/MusicGen/bin/activate"
module load cuda/10.1
module load python/3.7.4

 
# python3 -u generate.py > output.log
python3 -u generate.py --styles 12 > output.log
