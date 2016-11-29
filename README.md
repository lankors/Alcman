# Alcman
```
    在使用Ansible过程中觉得它更多是面向运维的，面对运维开发并不是很友好，在进行二次开发时，相对来讲来困难好多，运维工具中在没有Ansible和 saltstack 之前，都是在用paramiko在做管理，
    现在来讲不过是封装了一下功能，简化了运维操作却难为了运维开发。。。

    简化一下Ansible,只剩下配置 并发 和 parmiko 
``` 

#执行流程
    config类读取yaml文件中待执行内容
    actuator类为执行器
    invoke类将config和actuator组装在一起
    task类执行上面组装完毕的内容

#支持python版本
    ```
    python2.7.11
    python3.5 
    ```


#安装方式 
    ```
    依赖PyYAML、paramiko
    pip2.7 install Alcman
    ```
#用法参考
    ```
    from Alcman.Config import config
    from Alcman.Actuator import actuator
    from Alcman.Invoke import invoke
    from Alcman.Task import task


    iv = invoke()
    iv.set_config(config(filename='./servers.yaml'))

    iv.set_actuator(actuator(id_rsa="/root/.ssh/id_rsa", 
                            known_hosts="/root/.ssh/known_hosts", 
                            timeout=30,
                            log_to_file="/tmp/ssh.log"))

    d = task(iv)
    #d.run()
    d.run(cmd="ls")
    print d.get_result()
    ```


