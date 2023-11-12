# implicit

a = 5
b = 2
value = a/b
print(value)
print(type(value))  # float

# auto kore felbe


q = 20
u = '10'

# r = q+u
# print(r) #error dibe Type error


r = q+int(u)  # explicit conversion
print(r)

# int to string

st = "my age is"

print(st+' '+str(q))

# tuple to list list to tuple

n = "hello this is emon"

vn = tuple(n)
print(vn)

l = list(n)
print(l)
