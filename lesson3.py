# defaultdict

from typing import List
'''
def calculate_avg_list(l:list[float])->float:
        return sum(l)/len(l)


calculate_avg_list ([2,3])
print(calculate_avg_list)


limor="limor"

def my_name():
    print(limor)

print (my_name())


def print_list(l:list, dir)->list:
  if dir:
    return l[::-1]
  else:
    return l
  
print (print_list([1,2,3,4],1))



def fibbonachi(results:list)->list:
    length  = len(results)
    a,b = 0,1
    results = []
    if length <= 0:
        results = []
    elif length == 1:
         results = [0]
    elif length == 2:
        results = [0,1]
    else:
          while a < length:
            results.append(a)
            a,b = b,a+b
    return results

print (fibbonachi([1,2,3]))


  


from statistics import median
from collections import defaultdict

nvidia=[10,20,30,40,10,20,40,50,60,55,57,40,33,40,66,77,100,110,120]
##>>>(0,"buy"),(1,"sell"),(0,"hold")

def stock_logic(stock:list):
  
    mediane=median(stock)
    dic =defaultdict(list)

nformation["buy"].append(i)
    

    for j,i in enumerate(stock):
        if stock[i] < mediane:
             dic = {stock[i], 'buy'}
        elif stock[i]==mediane:
             hold.append=stock[i]
        else:
          sell.append=stock[i]
    
    return action


print (stock_logic(nvidia))
'''

l1= [0,1,2,3,4,5,6]
l2= [10,11,12,13,14,15,16]

print(l1[1:4])
print(l1[1:4:2])

print (20 in l1, 11 in l2, 12 in l2), 
print(l1.index(1))

###