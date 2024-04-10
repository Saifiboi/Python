from flask import Flask
import random
import time

app = Flask(__name__)
nmbr = 0


@app.route('/')
def hello():
    global nmbr
    nmbr = random.randint(0, 9)
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src=" https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


winner = "https://media.giphy.com/media/hz6L3FwCc3hI2zUAFI/giphy.gif"
looser = ["https://media.giphy.com/media/wmYBxqCGu7R4SfIXuA/giphy.gif",
          "https://media.giphy.com/media/3ohc1h1vy6Gtv4uOLC/giphy.gif",
          "https://media.giphy.com/media/3ohhwtQ3U0wsyytaIU/giphy.gif",
          "https://media.giphy.com/media/z7Rtz6bPxpQ2c/giphy.gif"]


@app.route("/<int:numbr>")
def check(numbr):
    global nmbr, winner, looser
    if numbr == nmbr:
        return '<h1>You get it.</h1>' \
               f'<img src={winner}>'
        time.sleep(5)
    elif numbr < nmbr:
        return '<h1 color="red">Too Low,try another one.</h1>' \
               f'<img src={random.choice(looser)}>'

    elif numbr > nmbr:
        return '<h1 color="red">Too High,try another one.</h1>' \
               f'<img src={random.choice(looser)}>'


if __name__ == "__main__":
    app.run(debug=True)
