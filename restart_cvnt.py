import subprocess
status=subprocess.getoutput('docker start $(docker ps -aq)')
output=subprocess.getoutput('docker ps -q')
container_list=output.split('\n')
for docker_name in container_list:
    shell='docker exec %s bash -c "cd /usr/local/yyets_20190829/yyets_20190829;./install.sh start;"'%docker_name
    print(shell)