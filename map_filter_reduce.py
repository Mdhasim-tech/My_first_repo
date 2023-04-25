lst=[1,2,3,4,5,6,7]
for i in lst[:]:
    if i%2==0:
        print(i)
#map--HAR EK LIST KE VALUE PAR FUNCTION LAGEGA
val=list(map(lambda i:i**2,lst))
print(val)

#FILTER---LIST KO FILTER KAR DEGA HAMARE BATAYE HUA CONDITION KE ACCORDING
val1=list(filter(lambda i:i%2==0,lst))
print(val1)

#REDUCE---POORE LIST KO EK PARTICULAR VALUE ME REDUCE KAR DEGA
from functools import reduce
val2=reduce(lambda x,y:x+y,lst)
print(val2)