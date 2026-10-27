
# 1. copy()
a = [3, 1, 4]
b = a.copy()
print("copy:", b)

# 2. Assignment: same list object
a = [1, 2, 3]
b = a
b.append(4)
print("same object:", a, b)

# 3. index()
a = [10, 20, 30, 20]
print("index:", a.index(20))

# 4. count()
print("count:", a.count(20))

# 5. len()
print("len:", len(a))

# 6. min()
print("min:", min(a))

# 7. max()
print("max:", max(a))

# 8. sum()
print("sum:", sum(a))

# 9. any()
print("any:", any([0, False, 5]))

# 10. all()
print("all:", all([1, True, 5]))

# 11. Concatenation (+)
a = [1, 2]
b = [3, 4]
print("concatenation:", a + b)

# 12. Repetition (*)
print("repetition:", a * 3)

# 13. append()
a = [1, 2, 3]
a.append(4)
print("append:", a)

# 14. insert()
a = [10, 20, 30]
a.insert(1, 99)
print("insert:", a)

# 15. extend()
a = [1, 2]
a.extend([3, 4])
print("extend:", a)

# 16. remove()
a = [10, 20, 30, 20]
a.remove(20)
print("remove:", a)

# 17. pop()
a = [10, 20, 30]
x = a.pop(1)
print("pop returned:", x)
print("pop list:", a)

# 18. del by index
a = [10, 20, 30]
del a[1]
print("del index:", a)

# 19. Slicing [start:stop:step]
a = [0, 1, 2, 3, 4, 5]
print("slice:", a[1:5:2])
print("reverse slice:", a[::-1])
print("step -2:", a[::-2])

# 20. del by slice
a = [0, 1, 2, 3, 4, 5]
del a[1:5:2]
print("del slice:", a)

# 21. clear()
a = [1, 2, 3]
a.clear()
print("clear:", a)

# 22. sort() ascending, in place
a = [3, 1, 4, 2]
a.sort()
print("sort ascending:", a)

# 23. sorted() ascending, new list
a = [3, 1, 4, 2]
b = sorted(a)
print("sorted:", b)
print("original:", a)

# 24. sort(reverse=True), in place
a.sort(reverse=True)
print("sort descending:", a)

# 25. sorted(reverse=True), new list
a = [3, 1, 4, 2]
b = sorted(a, reverse=True)
print("sorted descending:", b)
print("original:", a)

# 26. reverse(), in place
a = [1, 2, 3, 4]
a.reverse()
print("reverse:", a)
