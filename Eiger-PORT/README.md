# Eiger-PORT+
## 1. Background
Eiger-PORT+ presents an imrpovement over the Eiger-PORT algorithm (https://github.com/princeton-sns/Eiger-PORT). This codebase is built upon the original Eiger-PORT one, with modifications on the code where necessary, meaning the Eiger-PORT folder in this codebase presents an implementation of Eiger-PORT+.

## 2. System Requirements
The experiments were run using Emulab d170 nodes on Ubuntu 16.04 STD. Unless stated otherwise 16 clients and 16 servers were used.

## 3. Build
Everything can be built from setup_cluster.py. First insert the list of nodes of your cluster (extra node to run from in position 0 of the list, we will call this node0). Then you may run the script as
    setup_cluster.py --setup
to configure passwordless ssh in between every node. Finally run:
    python3 setup_cluster.py if you want to run the original Eiger-PORT
    python3 setup_cluster.py --plus if you want to run Eiger-PORT+
    python3 setup_cluster.py --server_exp if you want to run the number of servers experiments and hence you ware working with 64+1 total machines.
This will copy and build the code on the codebase, from that moment onwards everything should be run on the node0 in the cluster.

## 4. Run Experiments
On node0 to run the experiments change directory to:
    cd /local/Eiger-PORT/eval-scripts/experiments
Then open latency_throughput.bash and edit it according to the experiment you want to perform, then finally run:
    ./latency_throughput.bash 16
You will have to run the Eiger-PORT+ code then re-run setup_cluster to switch the node to Eiger-PORT.

4.1 Number of Clients
For the number of clients and the latency vs. throughput experiment uncomment the 
    #for thread in 2 4 8 16 32 64 128 256 512; do 
line and comment out the
     for thread in 4; do
in latency_throughput.bash, then run. 

4.2 Latency vs. Throughput
Same as number of clients.

4.3 Number of Servers
For the number of clients and the latency vs. throughput experiment uncomment the 
    #for thread in 32; do 
line and comment out the
     for thread in 4; do
in latency_throughput.bash, then run as latency_throughput.bash numservers varying numservers accordingly to which data point you want to obtain.

4.4 Zipfian Constant
In dynamic_common chnage line 163 from:
    data_file_name=$1_$2_$3_$4_$5_$6_$7_$8_$9+${10}+data
to:
    data_file_name=$1_$2_$3_$4_$5_$6_$7_$8_$9_${10}+${13}+data
Then in latency_throughput.bash change:
    for thread in 4; do
to:
    for zipfian_constant in 0 0.7 0.8 0.9 0.99 1.1 1.2; do
then run.