# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mf = Character("Mr. Frog Man", color="#02732c")


# The game starts here.

label start:

    # Show a background.

    scene start bg
    with fade

    # This shows a character sprite.

    show mrfrog

    # These display lines of dialogue.

    mf "Testing, testing, 1, 2, 3"

    mf "Oh hey! Welcome!"

    "This must be the famous \"FrogLand\" everyone talks about..."

    # example menu and jump

# declare rep_level
default rep_level = 0

menu:
    "Is this FrogLand?":
        jump frogland

    "Hey man, don't talk to me.":
        # decrement rep_level by 1
        $ rep_level = rep_level - 1
        jump aggro


label frogland:
    mf "Why it sure is! Glad you've heard of us!"
    jump moving_on

label aggro:
    hide mrfrog
    show mad mf
    with dissolve
    mf "Sheesh buddy, there's no need to be rude! Not a great first impression."

    hide mad mf
    show mrfrog
    with dissolve
    mf "I'm a forgiving frog though, so you get pass this time!"

    jump moving_on

label moving_on:
    mf "What brings you to FrogLand anyway?"

if rep_level == -1:
    'you get the feeling he doesn\'t like you very much...'

    # This ends the game.

    return
