###Alcman

    devops use Alcman to  Batch Management System and Production Application
    devops使用Alcman进行批处理管理系统和生产应用


###执行流程
    config类读取yaml文件中待执行内容
    actuator类为执行器
    invoke类将config和actuator组装在一起
    task类执行上面组装完毕的内容

###支持python版本

    python2.7.11
    python3.5



###安装方式

    依赖PyYAML、paramiko
    pip2.7 install Alcman

###用法参考
server.yaml

    hosts:

    - {cmd: ls, ip: 192.168.56.101, passwd: '123456', username: root}
    - {cmd: uptime, ip: 192.168.56.101, passwd: '123456', username: root}


test.py

    from Alcman.Config import config

    from Alcman.Invoke import invoke

    from Alcman.Task import task


    iv = invoke()

    iv.set_config(config(filename='./servers.yaml'))



    d = task(iv)

    d.run()

    print d.get_result()
