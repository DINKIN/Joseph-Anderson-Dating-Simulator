# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Joseph = Character("Joseph Anderson")
define George = Character("Super Bunnyhop")
define Matthew = Character("Matthewmatosis")
define Sean = Character("Sean Murray")
define Todd = Character("Todd Howard") 
define GeorgeSocks = Character("George Socks")
define SecondJoseph = Character("Joseph Anderson 2") 
define Noah = Character("Noah Caldwell Gervais") 

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene bg room 
    
    "Today, we're going to play a game regretfully made by SquidTheSid"
    "On that note, today is a great day for shitposting...." 
    
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    
    show joe maid at left
    # These display lines of dialogue.

    Joseph "Hello, my name is Joseph Anderson and I make boring and unfunny videos."
    
    show georgeanime at right
    
    George "Buy my socks"
    menu:
        "Hey George, nice socks!":
            jump georgenicesocks
        "Hey George, you make boring and unfunny videos.":
            jump georgeisboring
        "No Man's Sky is my favorite game":
            jump seanhowardappears
        "I prefer Matthew 'only slightly racist' Matosis over you, baka!":
            jump matthewwhitesupremecist
        "I want to be embraced by the strong arms of Todd Howard":
            jump paidmodsreappear
        "I only love me, myself, and I": 
            jump josephwaifu
        "DOES JOE'S RIVAL APPEAR?":
            jump noahnoaudio
            
    label georgenicesocks:
        George "I have been replaced by that which I have created. I am George no more, only his socks." 
        hide georgeanime
        with dissolve
        show george socks at right
        GeorgeSocks "Where is your God now?"
        return
    label georgeisboring:
        George "no u"
        return
    label seanhowardappears:
        George "I still can't believe that I actually exist﻿"
        hide georgeanime
        with dissolve
        hide joe maid
        with dissolve
        hide bg room
        with None
        scene nomanssky
        show joe maid at left
        show sean murray at right
        Sean "You are about to play No Man's Sky and I don't know what you'll think. I know I'm proud of it, I'm incredibly proud of the tiny team that is making a game at a scale that's never been done before." 
        menu: 
            "Should I kill Sean Murray?":
                jump killmurray
            "Or should I kiss him?":
                jump kissmurray
        label killmurray:
            "Joseph plunges his massive horns into Murray's chest. Murray's fragile heart explodes as he sinks to the ground. His soul emanates from the corpse, approaching the sky for no men - which is DLC"
            return
        label kissmurray:
            "You try to kiss Murray, but it turns out, this relationship is actually singleplayer and you can't interact with him. Also, Joe, what the fuck?"
            return
        
        
    label matthewwhitesupremecist:
        show matthewmatosis at right
        Matthew "This will be the terd date in my series of evenings where I try to sleep with you"
        menu:
            "I don't date white supremecists, baka-hentai!":
                jump matthewhentai
            "No thanks, I'm still stroking it.":
                jump joestrokingit
            "I love me a good Irish game analyst. SIGN. ME. UP!!!!!!!!!!!!":
                jump matthewirelandisbest
    
        label matthewhentai:
            Matthew "I guess I need to drink bleach now"
            return
        label joestrokingit:
            Joseph "I haven't masturbated in 3 hours"
            return
        label matthewirelandisbest:
            "These three lovebirds fucked all night" 
            return
            
    label paidmodsreappear:
        George "I still can't believe that I actually exist﻿"
        hide georgeanime
        with dissolve
        hide joe maid
        with dissolve
        hide bg room
        with None
        scene fallout4
        show joe maid at left
        show toddhoward at right
        Todd "you have to preorder my heart with $60 at the start"
        menu: 
                "Should I preorder Todd's heart?":
                    jump preorderheart
                "Or should I save up my money for paid mods?": 
                    jump saveformods
                "Or should I just kill Todd?":
                    jump killtoddhoward
                    
        label preorderheart:
            Todd "See That Mountain? You Can Climb It. Now preorder the season pass for my heart"
            menu:
                    "Should I preorder Todd's heart's season pass?":
                        jump preorderheartseasonpass
                    "Or should I not?":
                        jump dontpreorderheartseasonpass
        label saveformods:
            "You're a shill that makes boring and unfunny videos. Grats."
            return
        label killtoddhoward:
            "As you reach out to kill Howard, reallife.exe has crashed, meaning that you fall over and impale yourself on your own tail. Feels bad man. :( "
            return
        label preorderheartseasonpass:
            Todd "So Legendary Dragons are THAT hard?"
            "Thus, Joseph and Todd Howard live happily ever after, at least until the new season pass appears"
            return
        label dontpreorderheartseasonpass:
            "Well, you're not a huge huge shill, but you're still a shill. And you still make boring and unfunny videos"
            return
         
    label josephwaifu:
        George "I still can't believe that I actually exist﻿"
        hide georgeanime
        with dissolve
        show joseph 2 at right
        SecondJoseph "We're alone now"
        SecondJoseph "I too make boring and unfunny videos" 
        SecondJoseph "Notice me, senpai! ~uguu" 
        return
        
    label noahnoaudio:
        George "I still can't believe that I actually exist﻿"
        hide georgeanime
        with dissolve
        show noah calwel gervais at right 
        Noah "Whats audio editing"
        return 
        
        
    # This ends the game.

    return
