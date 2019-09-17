# Installcvnt
A script to install cvnt



意义
          
          
          
          各位矿工在参与CVNT项目时为了到达一机多挖的效果，选择了虚拟机Vmware等方式。但Vm占用资源高且安装效率慢。而docker则可以很好的解决这个问题。现为大家讲解，如何以最优雅的方式实现一机多挖。


————————————————---------------
          
（更新：1.机器重启后，自动恢复掉线的CVNT节点）

1.2.1 下载restart_cvnt.py文件：

1.2.2在矿机端执行 python3 restart_cvnt.py

执行后 掉线的节点会自动恢复，过一个小时，后台便会恢复状态。

————————————————----------------

一、必要配置以及准备（若有python3，则跳过此步骤）
           我们是基于python3开发的脚本，所以在运行一键安装CVNT脚本时，必须确保本机有装有python3。

1.1判断是否有python3

     请在服务器端打开终端输入python3 ,若出现python3.x的字样，则代表您已经安装过python3，可跳过配置阶段。


1.2安装python3

     1.2.1请复制链接并打开浏览器，点击download.zip（如图）：https://github.com/lsy-zhaoshuaiji/Installcvnt.git


1.2.2  解压文件

          解压后您将会看到两个文件installCvnt.py和python.sh，请将这两个文件复制到您的目录中，并在此目录中打开命令终端。         
1.2.3切换管理员权限，（切换root）

          请输入 su root   点击回撤，并输入密码 再点击回撤

           ps（小编抱怨一句）:不要问我为什么输入密码不显示，如果这个你都不懂 ，你自己请技术去安装。这类问题，也不要在群里问我，问我，我也不想说。

1.2.3安装python3.6

         请在终端输入：

          sh python.sh

         脚本会自动帮您安装python3，这个过程是编译安装，可能需要5-10分钟，机器会一直刷屏。请您耐心等待

1.2.4检验是否安装成功

       再次输入python3  若出现python3的字样就代表成功安装python3.

二、一键安装多台Cvnt（重点来了哦）
2.1下载脚本文件

      请复制链接并打开浏览器，点击download.zip（如图）：

      https://github.com/lsy-zhaoshuaiji/Installcvnt.git

2.2解压文件

     解压后您将会看到两个文件installCvnt.py和python.sh，请将这两个文件复制到您的目录中，并在此目录中打开命令终端。

     1.2.3切换管理员权限，（切换root）

     请输入 su root   点击回撤，并输入密码 再点击回撤

2.3挂载并获取硬盘挂载位置方法（若您已经挂载过，可跳过此步骤）：

请输入以下命令：

fdisk -l  
比如5.5T的硬盘，/dev/sda  这就是我要挂载的硬盘名，再输入：

mkdir /home/data1

mkfs.ext4 /dev/sda
mount /dev/sda /home/data1 



检查硬盘大小,请输入下面的命令，若出现了正确的大小，则代表挂载完成

df -h --total
其中/dev/sda为您的硬盘，请根据自己的硬盘名称填写

其中/home/data1为硬盘挂载点，也就是下文您mount_dev参数。请记住这个参数

开机自动挂载：（可跳过此步骤，请点击下面地址）

自动挂载https://blog.csdn.net/up_com/article/details/51264872

2.4执行安装程序脚本（重点）



1.在终端输入

python3 installCvnt.py docker_num(虚拟节点的个数)   cvnt_uid（您人人影视的uid） mount_dev(外接硬盘的挂载目录)

新版本加入了mount_dev参数，可根据此参数让虚拟节点内部存储到硬盘上、此参数可以为空。但由于固态空间比较小，如果您需要虚拟大于20个节点时，建议您在矿机上接一块硬盘。

例如：

python3 installCvnt.py 25 123456 /home/data2

#25为虚拟25个cvnt节点
#123456为UID值
#/home/data2 为硬盘挂载点

如果您虚拟的节点数量比较小，可以不填写mount_dev参数，让cvnt存储在固态硬盘上：

例如：

   

python3 installCvnt.py 5 123456

#5为虚拟5个cvnt节点
#123456为UID值



请按照自己的需求修改参数值，不改的话，您就没收益了，。

~~~代码执行过程中需要获取dockerHub的镜像，虽然我用阿里云加速了 但可以还是会等待很久，所以请您耐心等待5-10分钟（根据您的网速来决定）

2.4在web端开启挖矿（后续我会将基于selenium自动化一键开启挖矿的程序开源 ，目前您还是手动点击开启挖矿）

执行完脚本后会返回如下界面，其中[60001,60005.......]就是您的web开启端口，如图：



请在浏览器中输入您的公网ip+端口访问 并点击开启挖矿

您的本机IP可以在终端通过命令ip addr 或者 ifconfig获取

若您是UPNP则按照您实际的公网IP 填写

如在浏览器中输入----->     171.8.91.65:60001        (第一个节点)

                             ----->     171.8.91.65:600015       (第二个节点)

........等

2.5请在浏览器输入http://super-user.rrysapi.com/#/ 查看运行状态

在执行后上述操作后，在此后台可以查看矿机状态，大概一/二个小时就会显示公网ip

若显示了公网ip则代表安装成功。

到此安装教程结束，下面我们对源码进行说明（感兴趣的小伙伴可以看看，不感兴趣则跳过）

三、关键源码解读（如果您改善了源码，请联系我）
我的微信：laughing_jk      加人请备注来源

逻辑上我定义了这几个方法，如图：



其中：

# -*- coding:utf-8 -*-


#这个是让服务器能识别UTF-8编码的
1.检测安装docker

这个逻辑很简单：

1.根据which docker的返回值判断是否安装了docker

2.针对不同linux内核版本配置阿里源

3.安装并启动docker

def install_docker():
    '''
    判断系统内核，安装docker
    :return:
    '''
    output = subprocess.getoutput('which docker')
    if len(output) < 2:
        print('正在安装docker中.......')
        output = subprocess.getoutput('lsb_release -a')
        if 'CentOS' in output:
            print('您的系统为：CentOS')
            docker_shell = 'yum install -y yum-utils device-mapper-persistent-data lvm2 &&' \
                           'yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo &&' \
                           'yum makecache fast &&' \
                           'yum install docker-ce -y'
            output = subprocess.getoutput(docker_shell)
        elif 'Ubuntu' in output:
            print('您的系统为：Ubuntu')
            docker_shell='apt-get update &&' \
                         'apt-get -y install apt-transport-https ca-certificates curl software-properties-common &&' \
                         'curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add - &&' \
                         'add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable" &&' \
                         'apt-get  update &&' \
                         'apt-get -y install docker-ce'
        else:
            docker_shell ='apt-get -y install docker-ce && yum install docker-ce -y'
        output = subprocess.getoutput(docker_shell)
        subprocess.getoutput('systemctl enable docker && systemctl start docker && systemctl status docker')
        print("成功安装docker，正在安装CVNT------------>")
    else:
        print("您已经安装过docker了，无须安装，正在安装CVNT------------>")
2.pull镜像

这个我要重点讲一下封装的docker镜像，很多人用docker采集不到公网ip就是因为这一步骤：

1.首先我在封装镜像时使用的是centos，并将采集ip的所以工具手动装了上去，比如：
yum install lsb
dmidecode -t1
sudo ip link show
sudo ip addr show
yum install sudo
yum install dmidecode
因为CMDB的采集都会用到这些工具，我们不确定官网采集是用的什么方式，所以我们提前需要将采集工具封装在容器中。

这部分源码逻辑是：

1.判断docker images中是否有我封装的镜像

2.若无镜像，则修改docker源为阿里云，并pull镜像，若有则跳过。

def pull_docker():
    images_status = subprocess.getoutput("docker images|grep reg|awk '{print $(NF-6)}'")
    if images_status == "registry.cn-hangzhou.aliyuncs.com/cs_work/cvnt_work":
        print("已存在，跳过pull")
        return
    Change_docker_Source="sudo tee /etc/docker/daemon.json <<-'EOF'\n" \
                         "{\n" \
                         "  \"registry-mirrors\": [\"https://o4hd5pcr.mirror.aliyuncs.com\"]\n" \
                         "}\n" \
                         "EOF\n" \
                         "sudo systemctl daemon-reload\n" \
                         "sudo systemctl restart docker\n"
    subprocess.getoutput(Change_docker_Source)
    print("成功修改docker源......正在获取镜像.....请耐心等待几分钟......")
    output=subprocess.getoutput("docker pull registry.cn-hangzhou.aliyuncs.com/cs_work/cvnt_work:v1.0")
    print("容器Images为：%s"%output)
3.运行容器并修改容器配置文件

代码逻辑为：

1.定义映射端口，并随机生成mac地址

2.docker run 开启重启

3.docker exec -c 在进入容器时执行shell命令

def install_cvnt(docker_num,cvnt_uid):
    name_num = 1
    port_web = 60001
    port_list=[]
    for i in range(docker_num):
        mac=randomMAC()
        container_name = "cvnt{}".format(name_num)
        a = port_web + 1
        b = port_web + 2
        c = port_web + 3
        port_list.append(port_web)
        run_container = "docker run -d -it --name {} " \
                        " --net bridge --mac-address {} -p " \
                        "{}:10000 -p {}:59606 -p {}:59608 -p {}:59843 " \
                        "-h {} " \
                        "registry.cn-hangzhou.aliyuncs.com/cs_work/cvnt_work:v1.0 ".format(container_name, mac, port_web,
                                                                                          a, b, c, container_name)
        container_Id = subprocess.getoutput(run_container)
        start_cvnt = r'docker exec %s bash -c "cd /usr/local/yyets_20190829/yyets_20190829;cd conf;' \
                     r"echo -e '#本地账户信息\nuid=%d' > " \
                     r'user.conf;cd /usr/local/yyets_20190829/yyets_20190829;./install.sh start;"' % (container_Id,cvnt_uid)
        result=subprocess.getoutput(start_cvnt)
        print(result)

        port_web = c
        port_web += 1
        name_num += 1
    return port_list
4.随机生成mac地址

这部分安装mac地址的要求来生成即可，很简单，用随机数。



def randomMAC():
    mac = [0x52, 0x54, 0x00,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))
大概就是这些，其实程序本身只是用python、shell与docker交互并不困难。难点在于封装一个可用的docker容器。

当然在大容器管理下，我还是推荐用k8s集群化管理。







~~最后，小编会在这两天去开发一键点击web的程序，知道大家都懒，不想点击，所以小编就加加班啦。

下次再会~~~~~~~
