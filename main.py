import cmath

print ("""Quadratic Formula in standard form
ax²+bx+c=0
""")

a = float(input("a term? "))
b = float(input("b term? "))
c = float(input("c term? "))

d = (b**2) -4*a*c
denom = (2*a)

print ('''Solving Equation

       ''' )

astr = str('{0}'.format(a))

bstr = str('{0}'.format(b))

cstr = str('{0}'.format(c))

print (astr + "x²" + "+" + bstr + "x"+ "+" +cstr + " = 0") 

x1 = ((-b+cmath.sqrt(d))/ denom).real
x2 = ((-b-cmath.sqrt(d))/ denom).real

print ("Solutions : x1 = {0} and x2 = {1}".format(x1,x2))

