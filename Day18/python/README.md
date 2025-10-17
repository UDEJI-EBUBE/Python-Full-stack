# Turtle Graphics
Today we learnt about the turtle module in order to make different things with it
## Setting Up a Turtle Graphics Project
```
from turtle import Turtle

timmy_the_turtle = Turtle()
```
- This is Turtle class is what will define everything we do with our turtle. when you run the code by printing the object you will notice that there is a flash which is the the screen that the turtle will be displayed in.
```
from turtle import Turtle, Screen

screen = Screen()
screen.exitonclick()
```
- Now with this Screen class we can control the actions of the screen lik ehow tall, wide, color and even how it comes and go. <br>
  With this exit on click the screen will not disappear until you click on it.

## Attributes
There are different attributes and methods for the Turtle and screen class
### Turtle
1. timmy_the_turtle.shape(""): This is used to choose the shape of the turtle whuch is by default a pointer, a turtle is a shape here.
2. timmy_the_turtle.color(""): This is used to choose the color of the turtle.
3. timmy_the_turtle.forward(10): This is a method that is used to move the turtle forward by some distance
4. timmy_the_turtle.right(90): This method is used to turn the turtle by a certain degree
5. timmy_the_turtle.circle(10): This is used to draw a circle with the radius of a circle
6. timmy_the_turtle.setheading(90): This is used to set the direction of the turtle with the argument being the direction to face.
7. timmy_the_turtle.heading(): This is used to know the direction the turtle is facing

