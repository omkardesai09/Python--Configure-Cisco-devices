import telnetlib
import time

def telnet_conn(ip):
    port = 23
    telnet_timeout = 10
    read_timeout = 5
    #ip = '192.168.2.1'

    # Username and Password of target device
    username = 'omkar'
    password = 'cisco'

    # Start a connection
    conn_object = telnetlib.Telnet(ip,port,telnet_timeout)

    # Read until Username string and then write username
    wait = conn_object.read_until('Username:', read_timeout)
    conn_object.write(username + '\n')

    # Read until Password string and then write password
    wait = conn_object.read_until('Password:',read_timeout)
    conn_object.write(password + '\n')
    time.sleep(1)

    conn_object.write('enable\n')
    time.sleep(1)

    # Write a password to enter in enable mode
    wait = conn_object.read_until('Password:',read_timeout)
    conn_object.write(password + '\n')

    # Write command to display complete output without spacebar
    conn_object.write('terminal length 0\n')
    time.sleep(1)

    # Open file where configuration commands are written
    file1 = open('commands.txt','r')
    file1.seek(0)

    # Read each line from file and write on device console
    for line in file1.readlines():
        conn_object.write(line + '\n')
        time.sleep(1)

    # Close file
    file1.close()    
            
    # Read output from console
    wait = conn_object.read_very_eager()
    print wait

    # Close the socket
    conn_object.close()
    
telnet_conn('192.168.2.1')
