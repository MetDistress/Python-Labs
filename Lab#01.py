base = input("Enter your base:")
exp = input("Enter your exponent:")
base = int(base)
exp = int(exp)

num = base

print("Base =>", hex(id(base)))
print("Exponent =>", hex(id(exp)))

def calc(x, y):
    z = x ** y
    return z

for i in range (0, exp):
    z = calc(base, i)
    print(base, "**", i, "=", z)

"""for i in range(0, exp):
    print(base, "**", i, "=", num)
    num *= base

print("Final number is ", base, "**", i, "=", num )"""



