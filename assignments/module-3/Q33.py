# Write a Python script to sort (ascending and descending) a dictionary by value.


my_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}

asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))

desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending order:", asc_sorted)
print("Descending order:", desc_sorted)
