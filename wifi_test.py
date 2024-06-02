#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：getwindev.py
from netifaces import interfaces, ifaddresses, AF_INET
import winreg as wr
import os
 
def get_ipinfo():
 #获取所有网络接口卡的键值
    #id = interfaces()
 #存放网卡键值与键值名称的字典
    key_name = {}
    try:
        #建立链接注册表，"HKEY_LOCAL_MACHINE"，None表示本地计算机
        reg = wr.ConnectRegistry(None,wr.HKEY_LOCAL_MACHINE)
        # 打开r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}'，固定的
        reg_key = wr.OpenKey(reg , r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
    except :
        return ('路径出错或者其他问题，请仔细检查')
 
    for ifaceName in interfaces():
        try:
 
            #尝试读取每一个网卡键值下对应的Name
            reg_subkey = wr.OpenKey(reg_key , ifaceName + r'\Connection')
            #如果存在Name，写入key_name字典
            #print(wr.QueryValueEx(reg_subkey , 'Name')[0])
            addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
            key_name[wr.QueryValueEx(reg_subkey , 'Name')[0]] = addresses[0]
            
        except FileNotFoundError:
            #print('未找到信息')
            pass
    return key_name
 
if __name__ == '__main__':
    print(get_ipinfo())
	
os.system('pause')