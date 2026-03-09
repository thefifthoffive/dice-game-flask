# create a class to manage the dice game
class DiceGame:

    # this runs when a new game object is created
    def __init__(self):
        # start on turn 1
        self.turn = 1

        # there is no point number yet
        self.point = None

        # the game is not finished at the beginning
        self.finished = False

        # start with an empty result message
        self.result = ""

    # this function checks if the roll is between 2 and 12
    def validate_roll(self, roll):
        # return True if valid, False if not valid
        return 2 <= roll <= 12

    # this function plays one turn of the game
    def play_turn(self, roll):

        # if the game already ended, do not keep playing
        if self.finished:
            return "Game already finished. Click Start New Game."

        # make sure the roll is valid
        if not self.validate_roll(roll):
            return "Error: roll must be between 2 and 12."

        # save the current turn number so we can display it correctly
        current_turn = self.turn

        # check if this is the first turn
        if self.turn == 1:

            # if the first roll is 2, 3, or 12, the player loses
            if roll in [2, 3, 12]:
                self.result = "You lose!"
                self.finished = True

            # if the first roll is 7 or 11, the player wins
            elif roll in [7, 11]:
                self.result = "You win!"
                self.finished = True

            # any other roll becomes the point number
            else:
                self.point = roll
                self.result = f"Point set to {self.point}"

                # move to the next turn
                self.turn += 1

        # if it is turn 2 or later
        else:

            # rolling a 7 after the point is set means lose
            if roll == 7:
                self.result = "You lose!"
                self.finished = True

            # rolling the point number again means win
            elif roll == self.point:
                self.result = "You win!"
                self.finished = True

            # any other roll means nothing happens and the game continues
            else:
                self.result = "No result. Roll again."

                # move to the next turn
                self.turn += 1

        # return a message showing the turn, roll, and result
        return f"Turn: {current_turn}, Roll: {roll}, Result: {self.result}"