__author__ = 'admin'

from fabric.api import run
from fabric.api import env
#from fabric.api import local
env.user = 'root'
env.password = 'jinxiao#@10'

ips=[]
f = open('hosts.txt')
for hosts_ips in f.readlines():
    ips.append(hosts_ips.strip())

print ips

def set_hosts():
    env.hosts = open('hosts.txt','r').readlines()
env.hosts = ['192.168.118.138']
def install_vim():
    run('yum update -y')
