import os
import string

PLUS = True
SETUP = False
CMD = "\"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCxvL9qE53SpT829WEMZgU6BGtSu7DmC8ju0ugF5vX4wL7EuaT97IlcOtR4rMCUoW/fNmfIJ+u1DZmgX5s7ZtzRVjLdazEF3my3Xk+FL8oJVu3LN7CeV986jJmyfANx3Kdb0W40wBBZ+nMtP0kTNar5+rwJ53y2Mdf3BiHSkwOqKdUVIdFkX4BU0pWO0uRpAxqQAphCBWuaxTfGOeJDu1db3zrJp6T+cLou4nK6S9IM55IzSBxFo4+NARHvxq2NAKRLtldoDPbZqrZnsr5nLY6CE8mASYjLvFQDhbwdYo0vhqNryByKr0rf+qa9ht6myKBuH3/5Nc8qfTKn2WE2uF3j luca_mul@node0.luca-mul-146592.pora.emulab.net\""
def setup(hosts):
    
    if SETUP:
        for host in hosts:
            
            username, domain = host.split("@")
            cmd = "ssh-keygen -f \"/home/luca/.ssh/known_hosts\" -R \"" +  domain + "\""
            os.system(cmd)
            if host != hosts[0]:
                cmd = " \"mkdir -p ~/.ssh && echo " + CMD + " >> ~/.ssh/authorized_keys && chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys\""
                os.system("ssh -o StrictHostKeyChecking=no " + host + cmd)
        return
    
    cmd = " \" sudo usermod -s /bin/bash luca_mul ; cd /local ; sudo rm -r ./* ; git clone https://github.com/princeton-sns/Eiger-PORT.git ; mv /local/EIGER_PORT/* /local ; sudo rm -r EIGER_PORT ; sed -i 's/node-/node/g' /local/Eiger-PORT/eval-scripts/vicci_dcl_config/16_clients_in_kodiak /local/Eiger-PORT/eval-scripts/vicci_dcl_config/16_in_kodiak ; cd Eiger-PORT ; ./install-dependencies.bash ; cd Eiger-PORT ; ant ; ant ; ant ; ant; cd tools/stress ; ant ; cd ../../../eiger ; ant ; ant ; ant  ; ant ; cd tools/stress ; ant\""
    if PLUS: 
        cmd = " \" sudo usermod -s /bin/bash luca_mul ; cd /local ; sudo rm -r ./* ; git clone https://github.com/lucamul/EIGER_PORT.git ; mv /local/EIGER_PORT/* /local ; sudo rm -r EIGER_PORT ; sed -i 's/node-/node/g' /local/Eiger-PORT/eval-scripts/vicci_dcl_config/16_clients_in_kodiak /local/Eiger-PORT/eval-scripts/vicci_dcl_config/16_in_kodiak ; cd Eiger-PORT ; ./install-dependencies.bash ; cd Eiger-PORT ; ant ; ant ; ant ; ant; cd tools/stress ; ant ; cd ../../../eiger ; ant ; ant ; ant  ; ant ; cd tools/stress ; ant\""
    for host in hosts:
        print(host)
        #os.system(f"cat ~/.ssh/id_rsa.pub | ssh -o StrictHostKeyChecking=no {host} \"sudo mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys\"")
        os.system("ssh -o StrictHostKeyChecking=no " + host + cmd)


hosts_port_plus = [
"luca_mul@pc419.emulab.net", 		
"luca_mul@pc552.emulab.net", 		
"luca_mul@pc549.emulab.net", 		
"luca_mul@pc434.emulab.net", 		
"luca_mul@pc461.emulab.net", 		
"luca_mul@pc436.emulab.net", 		
"luca_mul@pc538.emulab.net", 		
"luca_mul@pc475.emulab.net", 		
"luca_mul@pc458.emulab.net", 		
"luca_mul@pc405.emulab.net", 		
"luca_mul@pc459.emulab.net", 		
"luca_mul@pc522.emulab.net", 		
"luca_mul@pc431.emulab.net", 		
"luca_mul@pc462.emulab.net", 		
"luca_mul@pc550.emulab.net", 		
"luca_mul@pc420.emulab.net", 		
"luca_mul@pc422.emulab.net", 		
"luca_mul@pc471.emulab.net", 		
"luca_mul@pc411.emulab.net", 		
"luca_mul@pc432.emulab.net", 		
"luca_mul@pc540.emulab.net", 		
"luca_mul@pc414.emulab.net", 		
"luca_mul@pc450.emulab.net", 		
"luca_mul@pc466.emulab.net", 		
"luca_mul@pc547.emulab.net", 		
"luca_mul@pc467.emulab.net", 		
"luca_mul@pc557.emulab.net", 		
"luca_mul@pc449.emulab.net", 		
"luca_mul@pc439.emulab.net", 		
"luca_mul@pc469.emulab.net", 		
"luca_mul@pc427.emulab.net", 		
"luca_mul@pc442.emulab.net", 		
"luca_mul@pc468.emulab.net" 		
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

setup(hosts_port_plus)