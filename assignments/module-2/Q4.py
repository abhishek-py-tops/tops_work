# # How memory is managed in Python?

# Automatic: Python manages memory on its own — no need to allocate or free memory manually.

# Reference Counting: Every object keeps count of how many times it's used. When the count is 0, Python deletes it.

# Garbage Collector: Cleans up unused memory, especially in cases where objects refer to each other (circular references).

# Dynamic Typing: Memory is allocated at runtime based on the type of value stored in a variable.

# Memory is stored in Heap: All variables and objects live in a private heap memory, managed by Python.