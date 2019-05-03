element1 = [1 , 2 , 3 , 4 , 5 , 6, 7 , 8 , 9]
element2 = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G']
element3 = ['Rakitic' , 'Dembele' , 'Coutinho' , 'Suarez' , 'Messi']

def elementbalik(x):
    lenx=len(x)
    list=[]
    for i in range(lenx):
        list.append(x[lenx-1-i])
    return list

print (elementbalik(element1))
print (elementbalik(element2))
print (elementbalik(element3))