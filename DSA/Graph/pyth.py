from array import *
'''
num = array('i' , [])

rolno = int(input('enter your no: '))
i = 0
j = 0
while i < rolno:
    num.append(int(input('enter no :')))
    i += 1


while j < len(num):
    print(num[j])
    j += 1 '''


no = array('i' , [100, 101, 102])
no2 = array('i' , [500,205,299,305,400])

no.insert(3 , 50)
no.extend(no2)
no.reverse()
m = len(no)
for i in no:
    print(i)
    


