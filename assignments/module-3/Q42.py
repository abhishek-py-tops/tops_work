# Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200,'d':400}


result = {}

for key in d1:
    result[key] = d1.get(key, 0) + d2.get(key, 0)


for key in d2:
    if key not in result:
        result[key] = d1.get(key, 0) + d2.get(key, 0)

print("Combined Dictionary:", result)