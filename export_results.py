import os

path_scripts = "/local/Eiger-PORT/eval-scripts/data_proc_scripts/*"
def export(directory = "/local/Eiger-PORT/eval-scripts/experiments/dynamic/latest", vars = "2 4 8 16 32 64 128 256 512", num_trials = 1):
    os.system("cp -r " + path_scripts + " " + directory)
    os.system(f'cd {directory} ; sed -i "s/threads=.*/threads=\\"{vars}\\"/g" process_latency.bash ; sed -i "s/trials=.*/trials={str(num_trials)}/g" process_latency.bash')
    os.system(f'cd {directory} ; ./calc_latency_throughput.bash')

    