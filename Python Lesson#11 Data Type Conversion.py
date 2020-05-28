'''
convert to int -> int()
convert to float -> float()
convert to bool -> bool()
convert to string-> str()


can't convert string with float 

'''

var_integer = 3
var_float = 1.2
var_boolean = True
var_string = "1.2"

var = int(float(var_string))
var1 = int(var_float)

print(var)
print(var1)
print(type(var))


#print(len(var_string))

