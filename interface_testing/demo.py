# -*- coding:utf-8 -*-
import socket
#获取本机电脑名
from datetime import timezone

from requests import models

myname = socket.getfqdn(socket.gethostname())
#获取本机ip
myaddr = socket.gethostbyname(myname)
print(myaddr)
print(myname)
update_time = models.DateTimeField(verbose_name=u'更新时间', default=timezone.now)
print(update_time)
