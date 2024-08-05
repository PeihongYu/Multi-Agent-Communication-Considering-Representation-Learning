import subprocess
import os
from itertools import product
from types import SimpleNamespace as SN


# Define the maximum number of jobs for each account
# max_job_nums = [4, 2, 2, 8]
max_job_nums = [2]
account_combinations = [
    # ["nexus", "tron", "medium"],      # 2 days, for qmix, 4 jobs max
    ["cml-tokekar", "cml-dpart", "cml-medium"],     # 3 days, for ippo/dm2, 2 jobs max
    # ["cml-tokekar", "cml-dpart", "cml-high"],     # 1.5 days, for qmix, 2 jobs max
    # ["cml-tokekar", "cml-dpart", "cml-high_long"],    # 14 days, for ippo/dm2, 8 jobs max, but actually 2 jobs max due to resources
]

# Define the parameters you want to iterate over
# parameters = {
#     "env": ["appleDoor_a", "centerSquare6x6_2a"], 
#     "algo": ["mappo", "mappo_ns", "ippo", "ippo_ns", "qmix"],
#     "lr": [0.0001, 0.00005, 0.00001], 
#     "tau": [0.01, 200]
# }
parameters = {
    "seed": [112358, 1285842, 78590, 119527, 122529],
    # "seed": [1285842, 78590, 119527, 122529],
    # "seed": [112358],
}

root_dir = "/fs/nexus-scratch/peihong/smac_results_2410"
smac_dir = "/fs/nexus-scratch/peihong/3rdparty/StarCraftII_2410"

param_names = list(parameters.keys())
param_values = [v for v in parameters.values()]
combinations = list(product(*param_values))

algo_name = "masia"
map_name = "1o_10b_vs_1r"
# map_name = "3s_vs_5z"
# map_name = "bane_vs_hM"
# python_command = "python src/main.py --env-config=sc2 --config=default_ippo_5v6 --alg-config=ippo with env_args.map_name=5m_vs_6m rew_type='env' update_gail=False t_max=10050000 name='ippo'"
python_command = f"python src/main.py --env-config=sc2 --config=masia with env_args.map_name={map_name} t_max=20050000 name='masia'"

# python src/main.py --env-config=sc2 --config=masia with env_args.map_name=bane_vs_hM t_max=20050000 name='masia'

# Iterate over parameter combinations
jobs_num = 0
for combo in combinations:
    job_name = "__".join([f"{name}_{value}" for name, value in zip(param_names, combo)])
    job_name = f"{algo_name}__{map_name}__{job_name}"
    param_dict = {key: value for key, value in zip(param_names, combo)}
    param = SN(**param_dict)

    # get qos info
    remainder = jobs_num % sum(max_job_nums)
    for j, val in enumerate(max_job_nums):
        if remainder < sum(max_job_nums[:j+1]):
            account, partition, qos = account_combinations[j]
            print(f"job num: {jobs_num}, account: {account}, partition: {partition}, qos: {qos}")
            break
    jobs_num += 1

    # Create a unique job script for each combination 
    # note: change time accordingly
    job_script_content = f'''#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --output={root_dir}/slurm_logs/%x.%j.out
#SBATCH --time=36:00:00
#SBATCH --account={account}
#SBATCH --partition={partition}
#SBATCH --qos={qos}
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64gb
#SBATCH --gres=gpu:1

# Load any necessary modules
# For example, if you need Python, you might load a Python module
CONDA_BASE=$(conda info --base)
source $CONDA_BASE/etc/profile.d/conda.sh
conda activate marl
export SC2PATH={smac_dir}

# Your Python script with parameters
srun bash -c "{python_command} seed={param.seed}"
''' 

    # Write the job script to a file
    job_script_path = f'{root_dir}/slurm_scripts/submit_job__{job_name}.sh'
    with open(job_script_path, 'w') as job_script_file:
        job_script_file.write(job_script_content)

    # Submit the job using sbatch
    subprocess.run(['sbatch', job_script_path])

    # Print the job submission info
    result = ", ".join([f"{name}: {value}" for name, value in zip(param_names, combo)])
    print(f'Job submitted for parameters: {result}')