# Nested lists and dictionaries
In this lesson we talked about how lists can be nested inside lists and also dictionaries, and dictionaries being nested in other dictionaries <br>
An examole of list being nested in aother list is
```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])      # [1, 2, 3]
print(matrix[1][2])   # 6

```

An example of a list being nested in a dictionary is
```
student = {
    "name": "Alice",
    "grades": [85, 90, 78],
    "hobbies": ["reading", "chess", "cycling"]
}


print(student["grades"])        # Output: [85, 90, 78]
print(student["grades"][1])     # Output: 90

print(student["hobbies"][0])    # Output: reading

```
