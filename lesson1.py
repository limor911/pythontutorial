''''
veribales

limor=1
limor="limor"
limor= input("here")
print (f"why the hell {limor}")
'''

'''
###1###
pizza=True
buger=False

if pizza==True and buger==True:
    print(f"i like both")
elif pizza==False and burger==False:
    print (f"i dont like pizza or buger")
else:
    print("i like only one")
 '''              
'''    
####2####
yob=1991
if yob%2==1:
    print(1)
else:
    print(2)

this_year=2024

weeks=(this_year-yob)*12*4
print(weeks)

alan=2004
alan_month=(this_year-alan)*12

if weeks>(alan_month*4):
    print ("limor is bigger and greater")
else :
    print ("alan")
'''    
''' 
###3###
import math

radius=float(input("radius: "))
area=math.pi*radius**2
circ=math.pi*2*radius
print (f" this is area: {area} and this is circumference: {circ}")

if area>circ:
    print (True)
else:
    print (False)
''' 


''' 
limor='lim or'
lior="lior"
lidor='fg jkghgf
dfdf'

print(f"limor: {limor} and \' lior: {lior} and\n lidor: {lidor}")
''' 
''' 
###4###
password='qwerty50'
part1=input('part1:')
part2=input('part2:')


if len(part1)==part2:
    print (True)
else:
    print (False)


if password==(part1+part2):
    print (True)
else:
    print (False)

 ''' 

###5###
prof=input('put your name here')

num_o_app=int(input('how mouch you sorry?'))

print(f"im gonna say it for {num_o_app} times: \n")
print(f" will never forgot to do h.w again, {prof} \n"*(num_o_app))