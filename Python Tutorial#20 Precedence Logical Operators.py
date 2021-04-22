

'''
T - True
F - False
'''

'''
condition1 = 1 > 2 and 2 > 2 and 7 == 7 or 0 != 10


print(condition1)
'''


x = 1
y = 2
z = 3

condition2 = (x > y) or (x == 5) and (x <= z) or not (z == 1)
                F   or     F      and    T    or    T
                
                     F      and       T  or  T
                     
                     F      and          T
                     
                            F
                
                



print(condition2)
