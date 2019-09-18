import subprocess
status=subprocess.getoutput('docker start $(docker ps -aq)')
output=subprocess.getoutput('docker ps -q')
container_list=output.split('\n')
name_num = 1
for docker_name in container_list:
    print(docker_name)
    print(name_num)
    shell='docker exec %s bash -c "cd /usr/local/yyets_20190829/yyets_20190829;./install.sh stop;./install.sh start;"'%docker_name
    output=subprocess.getoutput(shell)
    print(output)
    name_num += 1
