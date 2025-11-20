from flask import Flask

app = Flask(__name__)
number = 3

@app.route("/")
def header():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')

@app.route("/<int:guess>")
def choice(guess):
    if guess == number:
        return ('<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3kyc2lybmxibzJoMGVlMGZieHBnODVkMXVidGtlZHdlMXMyeXpsYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RKA9WE5HGkLi8/giphy.gif">'
                '<h1>That is correct</h1>')
    elif guess < number:
        return ('<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
                '<h1>That is lower than the number</h1')
    elif guess > number:
        return ('<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
                '<h1>That is higher than the number</h1>')






if __name__ == "__main__":
    app.run(debug=True)
