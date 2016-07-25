# Alcman
```
    简化运维操作中的 ssh 批量执行指令，使用python中的paramiko和yaml模块实现
``` 

#安装方式 

pip2.7 install Alcman

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
d.run()
print d.get_result()
```


