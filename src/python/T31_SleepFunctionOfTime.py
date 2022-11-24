import time

for i in range(100):
    """here every line will print in 2 seconds"""
    print(f"I am in for loop {time.asctime(time.localtime(time.time()))}")
    time.sleep(2)

k = 0
while k < 100:
    print(f"I am in while loop {time.asctime(time.localtime(time.time()))}")
    k += 1


