"""
we can use two module here
time and datetime
"""
import time

# let if you want o know whether the for loop print the number till 45 fast or while loop
# we will use time module e to find th execution time of a process
initial = time.time()
print(initial)
for i in range(1000):
    print("Saaallam Aryan Bhai")

print(f"The run time for For Loop is {time.time() - initial} seconds")

initial2 = time.time()
k = 0
while k < 1000:
    print("Saaallam Aryan Bhai")
    k += 1

print(f"The run time for while loop is {time.time()-initial2} seconds")


localtime = time.asctime(time.localtime(time.time()))
print(localtime)



