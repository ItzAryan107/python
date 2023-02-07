from numpy import loadtxt as lt

print("3. ---> Reading array from disk, either from standard or custom formats")

arr = lt('simple.csv', delimiter=',', skiprows=1)
print(arr)
print(type(arr))
