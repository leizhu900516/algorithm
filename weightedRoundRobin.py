# -*- coding: utf-8 -*-
# @author: chenhuachao
# @time: 2019/6/6
# weightedRoundRobin.py
# *********nginx轮询算法（带权重）**************


init_weight = [0,0,0]
current_weight_befor = []
current_weight_after = []
def add(data):
    _=0
    for i in data:
        _+=i
    return _

def wRr(hosts):
    '''
    :param host:[{主机名:weight},{主机名:weight},]
    :return:
    '''
    complate = False
    global current_weight_befor,current_weight_after,init_weight
    weight_list,host_list = [],[]
    for k,v in hosts.items():
        weight_list.append(v)
        host_list.append(k)
    if not current_weight_befor:
        current_weight_befor = weight_list
    if current_weight_after:
        current_weight_befor = []
        for i in range(len(hosts)):
            current_weight_befor.append(current_weight_after[i]+weight_list[i])

    max_weight = max(current_weight_befor)
    weight_sum = add(current_weight_befor)
    target_host = host_list[current_weight_befor.index(max_weight)]

    current_weight_after = []
    for i in current_weight_befor:
        if i == max_weight:
            if not complate:
                complate = True
                current_weight_after.append(i-weight_sum)
            else:
                current_weight_after.append(i)
        else:
            current_weight_after.append(i)
    return target_host,current_weight_befor,current_weight_after




'''
000      000
4 2 1    -3 2 1
1 4 2    1 -3 2

'''

if __name__ == '__main__':
    host = {"a":5,"b":2,"c":1}
    for i in range(9):
        a,b,c = wRr(host)
        print("计算后的值",a,b,c)

