# Debugging
Today was more like a lecture to guide us in debugging our code than any programming concepts<br>
The only programming concepts learrnt today was the try and except statement. It is good for when you are writing a code adn you know what kin of errors to expect so instead of the console giving you it' normal error messages it will give you your own custom made error message.
```
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("That's not a valid number!")

```
