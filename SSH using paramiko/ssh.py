import paramiko
import re
import time
import sys

def ssh_conn(ip):
    password = 'cisco'
        
    # Logging into device
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Connect to a device using username and password
    session.connect(ip, username = 'omkar', password = 'cisco')
    
    # Invoke shell inside device
    conn = session.invoke_shell()

    # Write following command on device's shell using send function
    conn.send('enable\n')
    time.sleep(1)
    conn.send(password + '\n')
    time.sleep(1)
    
    conn.send('terminal length 0\n')
    time.sleep(1)
    conn.send('sh run | include int\n')
    time.sleep(1)
    conn.send('sh ip int br\n')
    time.sleep(1)    

    # Checking shell output of device and print on local host
    output = conn.recv(65535)
    time.sleep(1)
    print output + '\n'
    session.close()

ssh_conn('192.168.2.1')    