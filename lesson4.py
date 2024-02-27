
'''

# defaultdict

from typing import List

listi=[1,2,3]
#2

def calculate_avg_list(list)
    return sum(listi)/len(listi)
'''    



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

'''
  

'''
from statistics import median
from collections import defaultdict

nvidia=[10,20,30,40,10,20,40,50,60,55,57,40,33,40,66,77,100,110,120]
##>>>(0,"buy"),(1,"sell"),(0,"hold")

def stock_logic(stock:list):
    avg_list=sum(stock)/len(stock)
    stock_doing=defaultdict(list)

    for i  in range(len(stock)):
        if stock[i]<avg_list:
            stock_doing[stock[i]].append("buy")
        elif stock[i]>avg_list:
            stock_doing[stock[i]].append("sell")
        else:
            stock_doing[stock[i]].append("hold")
    return stock_doing

print (stock_logic(nvidia))
'''
  
'''
# Visualizing

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sample Plot')
plt.show()
'''

##








###
'''
graph = {
    'a':['b','c'],
    'b': ['a','d'],
    'c':['d']
}

'''
##Homework : Create functions that calaulctae the sortest path between given two nodes, if path does not exist return -1 and return the shortest path
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}




city_network = {
    'New York': ['Philadelphia', 'Boston'],
    'Philadelphia': ['New York', 'Washington D.C.'],
    'Boston': ['New York', 'Providence'],
    'Washington D.C.': ['Philadelphia', 'Richmond'],
    'Providence': ['Boston', 'Hartford'],
    'Richmond': ['Washington D.C.', 'Raleigh'],
    'Hartford': ['Providence', 'New Haven'],
    'Raleigh': ['Richmond', 'Charlotte'],
    'New Haven': ['Hartford']
}

social_network = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
    'E': ['C', 'D'],
    'H': ['D', 'E']
}


def shorter_direction_path(dictiontree, pointa, pointb):
    path=[]
    path=path + [pointa]
    if pointb in dictiontree.get(pointa, []):
        return dictiontree.get(pointa, [])
    else:
        for num in path[pointa]:
            if 
    
print (shorter_direction_path(social_network, 'A','G'))

