# Flex box
We talked about flex today and how by default it acts like a block bt this can actually be changed.<br>
instead of using `display: flex;`, you can use `display: inline-flex;` to make the flex act like an inline element.<br>
A flex acts in two positions the x-axis and the y-axis. Now you can just see this as row and column, if you want to make your flex which has a default of row to be in the format of columns we use 
`flex-direction: columns;`<br>
Now this is very important for the next thing i want to talk about, there is a css property called flex-basis which is used to incraese the size of an element based on the direction it goes if you are using the row direction then it is trhe width that will be inreased but if you are using the columns the height is what will be increased. e.g <br>
`flex-basis: 100px;` <br>
>[!NOTE]
>in the last lesson i talked about ways to give css properties to different elements, now if you want the property to apply to all the direct descendants we use `parent > *{}`
- by default the elements in a flex is arranged by default way it is shown in the code but there is a way to change the order it was arranged. We acn manually assign orders to the elemnts but know by default all the elements have an order of 0.<br> e.g <br>
  ```
  p{
  order:1;
  }
  ```
- When elements in flex arrange themselves they like to be arranged in one line that means even if the line has finished it forces it's way to continue going to that same line. This default behaviour is what we call nowrap`flex-wrap: nowrap;`. To make the contents go the next line we use the wrap value `flex-wrap: wrap;`.
## flex layout
There are certain properties that can be used to change the layut of a flex which are
1. flex-direction: Defines the main axis direction.<br><br>
  Values:
  - row (default) — left to right
  - row-reverse — right to left
  - column — top to bottom
  - column-reverse — bottom to top
2. flex-wrap: Controls whether flex items wrap or not.<br><br>
Values:

- nowrap (default) — all items on one line

- wrap — items wrap onto multiple lines

- wrap-reverse — items wrap onto multiple lines in reverse order

3. justify-content: Aligns items along the main axis.<br><br>
Values:

- flex-start (default) — items packed toward the start

- flex-end — items packed toward the end

- center — items centered

- space-between — items evenly spaced, first at start, last at end

- space-around — items evenly spaced with equal space around

- space-evenly — items spaced with equal space between and around

4. align-items: Aligns items along the cross axis.<br><br>
Values:

- stretch (default) — items stretch to fill container

- flex-start — items aligned to start

- flex-end — items aligned to end

- center — items centered

- baseline — items aligned along their text baseline

5. align-content: Aligns multiple rows along the cross axis (when there’s wrapping).<br><br>
Values:

- stretch (default)

- flex-start

- flex-end

- center

- space-between

- space-around

### Item Properties (applied to flex items):

1. flex-grow<br>
Defines how much a flex item will grow relative to others. <br>
Default: 0 (do not grow)<br>
Positive integer or float values.

2. flex-shrink<br>
Defines how much a flex item will shrink relative to others.<br>
Default: 1 (shrink if needed)<br>
Positive integer or float values.

3. flex:<br>
Shorthand for flex-grow, flex-shrink, and flex-basis.<br>
Examples:

- flex: 1 (grow=1, shrink=1, basis=0%)

- flex: 2 1 100px


Finally to cap off everything that we treated today, she made mention of width. She said that applying normal widths to a flex will not affect it if you want to change the width of a flex you should use the min and max width attributes
