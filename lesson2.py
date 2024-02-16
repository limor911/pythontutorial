
'''
###1###
inp1 = input(' 1: ')
inp2 = input(' 2: ')

if len(inp1)>len(inp2):
    print(f"111:{inp1}")
elif len(inp1)<len(inp2):
    print(f"222:{inp2}")
else:
    inp3=input("this is 3:")
'''

'''
###2###
password= "abcd56789"
guess=input("guess the password")

if len(guess)<6:
    print(f"guess is to short {guess}")
elif len(guess)>10:
    print(f"guess is to high {guess}")
elif guess!=password:
     print(f"not match  {guess}")
else :
     print(f"correct {guess}")
'''
'''
###3###
a= int(input('a:'))
b= int(input('b:'))
c= int(input('c:'))

if (a>b and a>c )and b%2==0 :
    print (1)
elif (a>b and a>c) and b%2==1 and c==10:
    print (2)
elif (a<=b or a<=c) and b==c:   
    print (3)
else:
     print ("none")
    

if a>b and a>c:
    if b%2==0:
        print (1)
    if b%2==1 and c==10:
        print (2)
elif (a<=b or a<=c) and b==c:   
    print (3)
else:
     print ("none")
'''


'''
##tuple
t1= (1,2,3)
t2 = ("a", True)
t3= (t1, t2, 3.7 )

print (t3[0], t3[-1])
print (f"\n this is len of tuple t3:{len(t3[1])}")

a,b,c=t1


###list 
l1=[1,2,3]
l2= ["a", True]
l3= [l1,l2,3.7]

l1.append(4) ## add 1  to last index
print(l1)
l1.insert(4,0) ## index and value 
print(l1)

l1.extend(["a","b"]) ## add multi to last index
print(l1)
l1.extend(["a"]) ## add 
print(l1)
l1.append("a,2") ## add 
print(l1)

l1.remove(4)
print(l1)

###set
s1= {1,2,1,1,1,}
print(s1) ## sorted and distinct
 '''

'''
###4###

a=input('a: ')
b=input('b: ')
c=input('c: ')

list=[a,b,c]



if list[0]=="num":
   print (list)
   if  list[1].isnumeric() and list[2].isnumeric():
       list[1] = int(list[1])
       list[2] = int(list[2])
       for i in range(list[1]):
           print (f"this is {list[2]}")
   else:
      print ("no numeric")
else:
    list.pop(1)
    for i in range(5):
     print (f"this is {list[:]}")



###5###
aaa=input('what you want? ')
wor=aaa.split()
print (wor)
wor.reverse()
print (wor)
arr=' '.join(wor)
print(arr)
wor=arr.split('a')
print(wor)
 '''

'''
###6###

list = []

for i in range(5):
    list.append(int(input('value ')))

print(list)

diff=[min(list), max(list)]

print(diff)

for num in diff:
    if num in list:
        print(True)
    else:
        print(False)
'''

###7###
l1 = []
l2 = []


for i in range(3):
    l1.append(int(input('value l1 ')))
    l2.append(int(input('value l2 ')))

#l1= 2*l2 ==true 

if sum(l1)==2*sum(l2) or l1==l2:
    print(True)
else:
    print(False)