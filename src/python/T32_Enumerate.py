l1 = ["Bhindi", "Aalu", "chopsticks", "chowmein"]  # ignore the itme at even POSITION
t1 = ("Bhindi", "Aalu", "chopsticks", "chowmein")

i = 1
for item in l1:
    """
    here the interpreter first printing item then increasing i
    somewhere this program is getting increase
    to make it small we use enumerator
    """
    if i % 2 != 0:
        print(f" Jarvis Plz buy {item}")
    i += 1

print()
print("Using enumerator")
print()

# Enumerate give two things >>>> index and item
for index, item in enumerate(t1):
    """ it can take tuple also together with list"""
    if index % 2 == 0:
        print(f"Jarvis Plz buy {item}")
