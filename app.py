# import Flask so we can create the web app
from flask import Flask, render_template, request

# import the DiceGame class from the games folder
from games.dice_game import DiceGame

# import random so we can make random dice rolls
import random

# create the Flask application
app = Flask(__name__)

# create one game object that will store the game state
game = DiceGame()

# tell Flask to use this function when the user visits the home page
# and allow both GET and POST requests
@app.route("/", methods=["GET", "POST"])
def index():
    # use the global game variable so we can reset it if needed
    global game

    # start with an empty message
    message = ""

    # check if the user submitted the form
    if request.method == "POST":
        # get the value from the form field named "roll"
        roll = request.form.get("roll")

        # if the user clicked the reset button
        if roll == "reset":
            # create a brand new game
            game = DiceGame()

            # show a message on the page
            message = "New game started."

        # if the user clicked the random roll button
        elif roll == "random":
            # generate a random number from 2 to 12
            roll = random.randint(2, 12)

            # send the roll to the game logic and save the result
            message = game.play_turn(roll)

        # otherwise the user typed in a number
        else:
            try:
                # change the text input into an integer
                roll = int(roll)

                # play one turn with that number
                message = game.play_turn(roll)

            # if the user entered bad input, show an error message
            except:
                message = "Please enter a valid number between 2 and 12."

    # send data to the HTML page
    return render_template(
        "dice.html",      # name of the HTML template file
        message=message,  # the game result message
        turn=game.turn,   # current turn number
        point=game.point  # current point number
    )

# run the app only when this file is started directly
if __name__ == "__main__":
    # start the Flask development server
    app.run(debug=True)