# OOOP
Today we dealt with object oriented programming which is all about these things
1. class: this is like a blueprint or template used to create things. It defines how sth acts or behaves, but it's not the actual thing yet<br> e.g
```
class Dog:
    pass
```

2. objects: this is the real thubg created from the class. when you are creating something you are bringing it to life. <br> e.g
`
my_dog = Dog()
`<br>
Each onject has its own unique data and behaviour like how there are different dogs but they are not the same
3. Attributes: These are the variables that belong to an object (they hold its data or properties). e.g
   ```
   class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
   ```
   Now if we create an object we give it it's own unique attributes. e.g
   ```
   my_dog = Dog("Buddy", "Brown")
   print(my_dog.name)
   print(my_dog.color)
    ```
4. Methods: These are functions inside a class that define what the object can do (its actions).
   ```
   class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} is barking!")
   ```
   Now if you want to call it we do
   ```
   dog1 = Dog("Rex")
   dog1.bark()
  ```
