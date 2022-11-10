"""
                 Operators in python
Arithmatic Operator - use to have numerical calculation
Assignment Operator
Logical Operator
Identity operator
Membership operator
Bitwise Operator
"""

# Arithmatic operators
print("5 + 6 -->", 5 + 6)
print("5 - 6 -->", 5 - 6)
print("5 * 6 -->", 5 * 6)
print("5 / 6 -->", 5 / 6)
print("5 // 6 -->", 15 // 6)  # it will the integer value, it is call floor division operator

print("5 ** 6 -->", 5 ** 3)  # double star operator

print("5 % 6 -->", 5 % 6)  # modulus operator, which give remainder

# Assignment Operator
print()
x = 5  # '=' is a assignment operator
x += 7
print("x += 7 -->", x)  # increases the value of x by 7
"""
/=
*=
-=
%=   ---> x = x % 3
//=  ---> x = x // 3
"""

x %= 7
print("x %= 7 -->", x)
x //= 3
print("x //= 3 -->", x)

# Comparison operators
print()
print("a == b --->", 1 == 5)
print("a <= b --->", 1 <= 5)
print("a >= b --->", 1 >= 5)
print("a > b --->", 1 > 5)
print("a < b --->", 1 < 5)

#  Logical operator
print()
a = True
b = False

print("a and b --->", a and b)
print("a or b --->", a or b)

# identity operator
print()
print("a is b --->", a is b)  # kya a, b ha?
print("a is not b --->", a is not b)  # kya a, b nhi ha?

# membership operator
print()
list01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7.8]
print("in ---> ", 345 in list01)
print("not in ---> ", 787 not in list01)

# bitwise operator
print()
"""
0 - 00
1 - 01
2 - 10
3 - 11
"""
print("0 & 1 (Bitwise and)--->", 0 & 1)
print("0 | 1 (Bitwise Or)--->", 0 | 1)
print("1 | 2 --->", 1 | 2)

"""
a = 10 = 1010 (Binary number system)

~a = ~1010
   = -(1010 + 1)
   = -(1011)
   = -11 (Decimal number system)
"""
x = 67
print("~a (Bitwise not)--->", ~x)
y = 10
z = 4
print("a ^ b (Bitwise XOR)--->", y ^ z)

print("a>>1 (Bitwise right shift)--->", x >> 1)
print("a<<1 (Bitwise left shift)--->", x << 1)
