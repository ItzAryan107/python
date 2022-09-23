# set is heterogeneous, it can add different type of data type
# Essay way to make set is ... by using list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sFromList = set(l)
print(sFromList)
print(type(sFromList))

print()

s = set()  # empty set
# set won't add repeated values
s.add(1)
s.add(3)
s.add(1)
print(s)

print()

s1 = s.union({1, 3, 2})
print("Union of s with some other set --->", s1)

print()

print("Intersection --->", s1.intersection(s))

print()

print("Length of set --->", len(s1))

print()

print("Max element of s1 --->", max(s1))

print()

print("Two given set are disjoint or not --->", s.isdisjoint(s1))
# disjoint ---> two set have different element are said to be two disjoint set

print()

s.remove(3)
print("Removed an element from set --->", s)
