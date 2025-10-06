# Grid
Today our lecturs was mainly on grids
## Grid template
Grid template is a feature used to specify how many rows and columns there should be as well as the size. It is divided into two types which is the grid-template-columns and grid-template-rows.<br>
When specifying the specifications we use some certain values like
1. Fixed Rows and Columns
```
.container {
  display: grid;
  grid-template-columns: 150px 150px;
  grid-template-rows: 100px 200px;
}
```

2. Using fr Units
```
.container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  grid-template-rows: 1fr 1fr;
}
```

3. repeat() Function
```
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 3 equal columns */
  grid-template-rows: repeat(2, 150px);  /* 2 rows of 150px */
}
```

4. minmax() for Responsive Layout
```
.container {
  display: grid;
  grid-template-columns: repeat(2, minmax(100px, 1fr));
  grid-template-rows: auto;
}
```

5. Using auto and fit-content
```
.container {
  display: grid;
  grid-template-columns: auto fit-content(200px) 1fr;
  grid-template-rows: auto;
}
```

6. using grid-auto-rows: this is used when you include a div but you know that the specified fractions is out of its reach so you use this for any div not included in the specifications
```
.container {
  display: grid;
  grid-template-columns: auto fit-content(200px) 1fr;
  grid-template-rows: auto;
  grid-auto-rows: 300px
}
```

  CSS Grid Properties (for columns):

1.  grid-column:
- A shorthand that sets how many columns the grid item spans, or where it starts and ends (start / end).
- Example: grid-column: 1 / 3; → start at column line 1, end at 3.

2.  grid-column-start:
- Defines the vertical grid line where the item begins (from the left).
- Can use a line number, a named line, or the keyword "auto".
- Example: grid-column-start: 2; → start at grid line 2.

3.  grid-column-end:
- Defines the vertical grid line where the item ends (on the right).
- The item will occupy all columns between start and end (excluding the end line).
- Example: grid-column-end: 4; → ends *before* line 4.

4.  span (used with grid-column or grid-column-end):
- Instead of specifying an end line, you can tell the item to span a number of columns.
- Example: grid-column: span 2; → spans across 2 columns from its starting point.

  This also aplies for grid-row
