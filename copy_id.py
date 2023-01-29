import os
import string

PLUS = True

def setup(hosts):
    #for host in hosts:
    #     username, domain = host.split("@")
    #     cmd = "ssh-keygen -f \"/home/luca/.ssh/known_hosts\" -R \"" +  domain + "\""
    #     os.system(cmd)
    cmd = " \" sudo usermod -s /bin/bash luca_mul ; cd /local ; sudo rm -r ./* ; git clone https://github.com/princeton-sns/Eiger-PORT.git ; mv /local/EIGER_PORT/* /local ; sudo rm -r EIGER_PORT ; sed -i 's/node-/node/g' /local/Eiger-PORT/eval-scripts/vicci_dcl_config/16_clients_in_kodiak /local/Eiger-PORT/eval-scripts/vicci_dcl_config/16_in_kodiak ; cd Eiger-PORT ; ./install-dependencies.bash ; cd Eiger-PORT ; ant ; ant ; ant ; ant; cd tools/stress ; ant ; cd ../../../eiger ; ant ; ant ; ant  ; ant ; cd tools/stress ; ant\""
    if PLUS: 
        cmd = " \" sudo usermod -s /bin/bash luca_mul ; cd /local ; sudo rm -r ./* ; git clone https://github.com/lucamul/EIGER_PORT.git ; mv /local/EIGER_PORT/* /local ; sudo rm -r EIGER_PORT ; sed -i 's/node-/node/g' /local/Eiger-PORT/eval-scripts/vicci_dcl_config/16_clients_in_kodiak /local/Eiger-PORT/eval-scripts/vicci_dcl_config/16_in_kodiak ; cd Eiger-PORT ; ./install-dependencies.bash ; cd Eiger-PORT ; ant ; ant ; ant ; ant; cd tools/stress ; ant ; cd ../../../eiger ; ant ; ant ; ant  ; ant ; cd tools/stress ; ant\""
    for host in hosts:
        print(host)
        #os.system(f"cat ~/.ssh/id_rsa.pub | ssh -o StrictHostKeyChecking=no {host} \"sudo mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys\"")
        os.system("ssh -o StrictHostKeyChecking=no " + host + cmd)


hosts_port_plus = [
"luca_mul@pc504.emulab.net",		
"luca_mul@pc518.emulab.net",		
"luca_mul@pc507.emulab.net",		
"luca_mul@pc488.emulab.net",		
"luca_mul@pc482.emulab.net",		
"luca_mul@pc480.emulab.net",		
"luca_mul@pc536.emulab.net",		
"luca_mul@pc549.emulab.net",		
"luca_mul@pc431.emulab.net",		
"luca_mul@pc545.emulab.net",		
"luca_mul@pc473.emulab.net",		
"luca_mul@pc557.emulab.net",		
"luca_mul@pc436.emulab.net",		
"luca_mul@pc516.emulab.net",		
"luca_mul@pc538.emulab.net",		
"luca_mul@pc521.emulab.net",		
"luca_mul@pc542.emulab.net",		
"luca_mul@pc500.emulab.net",		
"luca_mul@pc541.emulab.net",		
"luca_mul@pc487.emulab.net",		
"luca_mul@pc476.emulab.net",		
"luca_mul@pc512.emulab.net",		
"luca_mul@pc553.emulab.net",		
"luca_mul@pc534.emulab.net",		
"luca_mul@pc522.emulab.net",		
"luca_mul@pc508.emulab.net",		
"luca_mul@pc550.emulab.net",		
"luca_mul@pc529.emulab.net",		
"luca_mul@pc552.emulab.net",		
"luca_mul@pc420.emulab.net",		
"luca_mul@pc503.emulab.net",		
"luca_mul@pc427.emulab.net",		
"luca_mul@pc535.emulab.net"	
]

hosts_port = [
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

setup(hosts_port)