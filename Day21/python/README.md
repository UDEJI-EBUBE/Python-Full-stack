# Inheritance and Slice
Today we talked about when classes inherit from other classes and slicing in tuples and lists <br>
Inheritance means a class can get features (attributes and methods) from another class — just like a child can inherit traits from a parent. <br>
It allows you to reuse code and avoid repetition.
This is the format for a class to inherit
```
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
```

The class to be inheited from will be passed in as an argument in the child class <br>
Super().__init__() is used inside a child class to call the parent class’s constructor (__init__() method)

## Slicing in tuples and lists
A tuple is a collection used to store multiple items in a single variable — just like a list —
but the difference is that tuples cannot be changed (they are immutable). e.g 
```
fruits = ("apple", "banana", "cherry")
print(fruits)
```
**Slicing** means cutting out a part (or section) of a tuple —  
just like taking a few pieces from a long loaf of bread 🍞.

It helps you **extract specific elements** from a tuple using **index numbers**.

---

## 🧩 Basic Syntax

```python
tuple_name[start:end:step]
