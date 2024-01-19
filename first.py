a = eval(input('enter a value :- '))
if type(a) in[ int ,float,complex,bool]:
    print(a**2)
else:
    print(3*len(a)+1)
 
