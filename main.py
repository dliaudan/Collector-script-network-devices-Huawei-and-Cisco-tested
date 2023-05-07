import paramiko
import time

c = open("C:\\Users\\user_path_for_command_list", "r") #define path for command which will be entered
command_list = c.read().split("\n")
d = open("C:\\Users\\user_path_for_device_list", "r") #define path where IP addresses for colelcting logs will be taken
hosts = d.read().split("\n")
print(hosts)
port = 22

username = "user" #here define SSH username and password below
password = "user_password"

logs = []
logs1 = []

for ip in hosts: #loop for checking each IP logs
    print("Try to login:", ip)
    conn = paramiko.SSHClient() #create SSH session
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #auto negotiation SSH keys
    conn.connect(ip, port, username, password)
    comm = conn.invoke_shell() #opening shell for command input to network device terminal
    for command in command_list:
        i = 0
        print(command) #showing current command in terminal
        comm.send('%s \n' % command) #send commands to terminal
        time.sleep(3)
        output = comm.recv(65535)
        output = output.decode("utf-8")
        print(output) #showing current output
        logs = output.split("xxxxx")
        print("logs", logs)
        logs1.extend(logs)
    i = i + 1
    logs1 = ''.join(map(str, logs1))
    print(logs1)
    with open("{}.txt".format(ip), "w") as f:
        f.write(logs1)
    logs1 = []
    comm.close() #closing SSH session