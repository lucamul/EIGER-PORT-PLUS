import os

def setup(hosts):
    # for host in hosts:
    #     for i in range(33):
    #         cmd = " \"ssh-keygen -f \"/users/luca_mul/.ssh/known_hosts\" -R node" + str(i) + "\""
    #         os.system("ssh -o StrictHostKeyChecking=no " + host + cmd)
    # return
    # for host in hosts:
    #     host = host.split("@")[1]
    #     os.system("ssh-keygen -f \"/home/luca/.ssh/known_hosts\" -R \"" + host + "\"")
    # cmd = " \"rm -r /local/Eiger-PORT/ ; cd /local ; git clone https://github.com/princeton-sns/Eiger-PORT.git ; cd Eiger-PORT ; ./install-dependencies.bash ; cd Eiger-PORT ; ant ; ant ; ant ; cd tools/stress ; ant ; cd ../../../eiger ; ant ; ant ; ant  ; cd tools/stress ; ant\""
    #cmd = " \"sudo sed -i 's/^#MaxStartups/MaxStartups/g' /etc/ssh/sshd_config ; sudo sed -i 's/#ClientAliveInterval 0/ClientAliveInterval 0/g' /etc/ssh/sshd_config && sudo sed -i 's/#ClientAliveCountMax 3/ClientAliveCountMax 0/g' /etc/ssh/sshd_config ; sudo systemctl restart ssh\""
    cmd = " \" sudo usermod -s /bin/bash luca_mul ; cd /local ; sudo rm -r ./* ; git clone https://github.com/princeton-sns/Eiger-PORT.git ; sed -i 's/node-/node/g' /local/Eiger-PORT/eval-scripts/vicci_dcl_config/16_clients_in_kodiak /local/Eiger-PORT/eval-scripts/vicci_dcl_config/16_in_kodiak ; cd Eiger-PORT ; ./install-dependencies.bash ; cd Eiger-PORT ; ant ; ant ; ant ; ant; cd tools/stress ; ant ; cd ../../../eiger ; ant ; ant ; ant  ; ant ; cd tools/stress ; ant\""
    for host in hosts:
        print(host)
        os.system("ssh -o StrictHostKeyChecking=no " + host + cmd)




hosts1 = [
"luca_mul@pc428.emulab.net",		
"luca_mul@pc433.emulab.net",		
"luca_mul@pc417.emulab.net",		
"luca_mul@pc440.emulab.net",		
"luca_mul@pc486.emulab.net",		
"luca_mul@pc501.emulab.net",		
"luca_mul@pc453.emulab.net",		
"luca_mul@pc484.emulab.net",		
"luca_mul@pc478.emulab.net",		
"luca_mul@pc463.emulab.net",		
"luca_mul@pc430.emulab.net",		
"luca_mul@pc454.emulab.net",		
"luca_mul@pc490.emulab.net",		
"luca_mul@pc429.emulab.net",		
"luca_mul@pc548.emulab.net",		
"luca_mul@pc497.emulab.net",		
"luca_mul@pc470.emulab.net",		
"luca_mul@pc408.emulab.net",		
"luca_mul@pc446.emulab.net",		
"luca_mul@pc525.emulab.net",		
"luca_mul@pc407.emulab.net",		
"luca_mul@pc472.emulab.net",		
"luca_mul@pc438.emulab.net",		
"luca_mul@pc423.emulab.net",		
"luca_mul@pc457.emulab.net",		
"luca_mul@pc537.emulab.net",		
"luca_mul@pc509.emulab.net",		
"luca_mul@pc418.emulab.net",		
"luca_mul@pc551.emulab.net",		
"luca_mul@pc426.emulab.net",		
"luca_mul@pc437.emulab.net",		
"luca_mul@pc424.emulab.net",		
"luca_mul@pc425.emulab.net"
]

setup(hosts1)