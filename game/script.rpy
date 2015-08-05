# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg bedroom = "images/bedroom.png"

# Declare characters used by this game.
define u = Character('You', color="#888888")

# The game starts here.
label start:
    scene bg bedroom
    with dissolve
    "I wake up."
    "I brush my teeth."
    "Today is a new day."
    return
