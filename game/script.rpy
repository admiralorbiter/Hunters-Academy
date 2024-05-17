# Declare characters used by this game. The color argument colorizes the name of the character.
define e = Character("Chloe", color="#c8c8ff")

image bg title1 = "hunters-academy-title.jpg"
image bg title2 = "hunters-academy-title.png"
image bg title3 = "huntersacademy-title.png"
image bg title4 = "hunters-academy-crest.jpg"

# Define images
image black = Solid("#000")                                       # Solid black image
image bg forest = im.Scale("forest.png", 1920, 1080)                # Forest background image scaled to 1920x1080
image chloe headshot = im.Scale("chloe-headshot.png", 400, 600)     # Chloe headshot scaled to 400x600
image chloe emote = im.Scale("chloe-emote.png", 600, 900)             # Chloe side image scaled to 400x600
image chloe happy = im.Scale("chloe-happy.png", 600, 900)           # Chloe happy side image scaled to 400x600
image chloe side = im.Scale("chloe-side.png", 600, 900)             # Chloe side image scaled to 400x600
image chloe side flipped = im.Scale(im.Flip("chloe-side.png", horizontal="True"), 600, 900)# Flipped Chloe headshot image
image intro = Movie(size=(1920, 1080),  play="intro.webm", loop=False)
# The game starts here.
label start:
    play music "intro.mp3" fadein 1.0
    show intro
    pause
    # Jump to the introduction scene
    jump introduction

# Introduction scene
label introduction:

    # Show the solid black background

    # After the introduction, jump to the main label
    jump main

label main:

    # Show the solid black background
    scene black

    # Show the scaled forest background image with transparency
    show bg forest

    # Show a character sprite.
    show chloe headshot at Position(xalign=0.5, yalign=0.75)  # Adjust position as needed

    e "Welcome to Hunters Academy new student!"
    e "I'm Chloe, your guide for today. There's a lot to learn, so let's get started!"
    e "It is 1863, Portland Maine, and things are a bit different here..."

    show chloe happy at Position(xalign=0.9, yalign=0.75)  # Adjust position as needed

    e "Witches."
    e "Vampires."
    e "Werewolves."
    e "Even humans.. all roam the streets together. Kept in balance by a old prophecy that if one species goes extinct, the rest will follow."
    e "Everything changed when vampires started overfeeding killing humans for sport."

    show chloe side flipped at Position(xalign=0.1, yalign=0.75)  # Adjust position as needed

    e "The humans retaliated, and the hunters were born."
    e "It was a war that lasted for years, but eventually the hunters teamed up with the witches and werewolves to banish the vampires."
    e "Now, the witches and werewolves left stay on an island, only talked about in whispers with modern day humans."
    e "The humans continue on while we live on our island, Hunters Academy."

    show chloe happy at Position(xalign=0.1, yalign=0.75)  # Adjust position as needed

    stop music fadeout 1.0
    # This ends the game.
    return
