# Insatnces, State and Higher Order Functions
Instance is the same thing as Objects, and State is the same thing as attributes <br>
Today we created a turtle race game and a free draw game. <br>
To do this as you can imagine we have to be able to give instructions to the turtle via the keys
- To do this we use the two attributes for the screen class which is
  ```
  screen.listen()
  screen.onkey(key="UP", fun= move)
  ```
  This listen as the name suggests listens for specific inputs from the user via the onkey. Now this onkey needs two arguements the key ehich is to be pressed and the fun which is the function to be called upon
