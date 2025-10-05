Full-stack
We covered three main things today
1. Display
2. Position
3. Media queries
For position:
There are 4 types of position
a. Static position: this is the default positioning taht you see in a page it cannot be moved
b. Realtive position: this is when the element is positioned relative to the psge so any positioning it undergoes is decided based on the nrowser position
c. Absolute position: this is same as the realtive positioning but here it is positioned to the nearest parent conatiner that has position realtive if there is no position Absolute it positions itself to the page.
d. Fixed position: this is when the elemnt is positioned relative to the browser not the page.

For display, there are many types of display that we have in CSS. We have the grid display, we have the flex display. These two displays are used to help in responsiveness of the website.

We also talked about float which can appear to tge right or left so that a text can appear around it
The clear is also used when  the float is applied to prevent that element from experiencing a float
Clear: right/ left/ both

Lastly, we talked about media queries, which are used to adjust the size and layout of elements—such as images—based on different screen sizes. You can set conditions using properties like `min-width` or `max-width` to make your design responsive and adapt smoothly to various devices.

Example:
@media (max-width: 600px) {
  img {
    width: 100%;
    height: auto;
  }
}

In this example, when the screen width is 600px or smaller, the image will automatically resize to fit the screen while keeping its original aspect ratio.
