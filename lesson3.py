
'''
## implement ! function
num=5
print(f"this is num {num}")

c=1
sum=1
while c!=num:
    sum *=num
    num=num-1
    print(f"this is num {num}")
    

print(f"this is sum {sum}")
'''
'''
##fibbonachi 
begin_f=1 
end_f=10
d=0
##1,1,2,3,5,8,13,21,34,55
c=[]

while True:
    c.append(begin_f)
    begin_f+=begin_f
    end_f-= 1
    if end_f == 0:
        break

c.append(begin_f)
print(f" this is begin {begin_f} , \n this is end {end_f} \n this is c {c}")
'''

'''
end_f = 10  # Initialize end_f
begin_f = 1  # Initialize begin_f
d = 0  # Initialize d
c = []  # Initialize c
 
while end_f > 0:  # Corrected while loop with a colon
    if begin_f == 1:
        c.append(begin_f)
    else:
        c.append(d)
    d = begin_f + begin_f  # Update d
    end_f -= 1  # Decrement end_f
    if end_f == 0:  # Check if end_f is 0
        break  # Exit the loop if end_f is 0

print(c)  # Output: [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
'''

# Pointers example

a = [1,2,3,4]

b = a

b.append(5)

b

import copy ## copy pointers
import collections

a = [1,2,3,4]
b = copy.copy(a)

b.append(5)
a