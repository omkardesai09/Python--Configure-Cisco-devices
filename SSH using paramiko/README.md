
# SSH a device using Python script
After running this python script, user will be able to access Cisco device (switch, router) using SSH on port no. 22

Addition to this, one can give any text file as a input in above python script and configure target Cisco device. 

### Prerequisites

Build the topology as shown in screenshot.png in GSN3 to check output. Virtualbox VM (Debian 7) is used as a host in GNS topology.


### Initial Configurations on router(R1)

Refer Initial_config_SSH.txt file and do similar steps on router R1.

### Final Steps
Commands to configure on target device are stored on host (Debian 7 VM) in commands.txt file.

Run ssh.py script on host (Debian 7 VM) 