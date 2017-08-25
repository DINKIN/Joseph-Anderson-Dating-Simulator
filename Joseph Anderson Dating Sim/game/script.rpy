# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Joseph = Character("Joseph Blanderson")
define George = Character("Super Bunnyhop")
define Matthew = Character("Matthewmatosis")
define Sean = Character("Sean Murray")
define Todd = Character("Todd Howard") 
define GeorgeSocks = Character("George Socks")
define SecondJoseph = Character("Josehp Anderson") 
define Noah = Character("Noah Caldwell Gervais") 
define Hamish = Character("Hamish Black") 
define Squid = Character("SquidTheSid") 
define Bold = Character("Bold Guy") 
# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg room 
    play music "game.mp3" loop fadein 1.0
    $ boldpassword = "loser" 
    " \"Fair Use\" Edition detected. Now loading..."    
    "WARNING: This game is patently offensive and if you have any hope in humanity left, please exit immediately." 
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show joe maid at left
    # These display lines of dialogue.
    Joseph "I-It's not that I l-like making boring and unfunny videos for you g-guys or anything! Baka!"
    show georgeanime at right
    # use youtube poop for super bunnyhop
    George "Buy my socks"
    George "placeholder message --> reminds YOU --> the me <-- 00100to put in the YTP quotes in H E R E00100." 
    menu:
        "Hey George, nice socks!":
            jump georgenicesocks
        "Hey George, you make boring and unfunny videos.":
            jump georgeisboring
        "Experimental George Weidman Route!":
            jump experimentalgeorge
        "YTP supershitposting route is not done since my university's internet is always down since OIT is incompetent":  
            jump fuckOIT 
        "I would like a different husbando, thank you very much.":
            jump mainbranch2
            
            
label mainbranch2:
    menu: 
        "No Man's Sky is my favorite game":
            jump seanhowardappears
        "I prefer Matthew 'only slightly racist' Matosis over you, baka! (TL Note: Matthew is not racist)":
            jump matthewwhsu
        "I want to be embraced by the strong arms of Todd Howard":
            jump paidmodsreappear
        "I only love me, myself, and I": 
            jump josephwaifu
        "DOES JOE'S RIVAL APPEAR?":
            jump noahnoaudio
        "SCOTLAND YARD":
            jump hamishshotthesheriff 
        "He must be stopped": 
            jump sidthesquid 
        "Super Secret Special Routes?? :O": 
            jump secretroute 
            
            
            
    label georgenicesocks:
        George "I have been replaced by that which I have created. I am George no more, only his socks." 
        hide georgeanime
        with dissolve
        show george socks at right
        "Fair Use Edition audio override enabled" 
        # Original audio was Kaz Speech from MGSV, look it up on YouTube. 
        # uncomment the rest of the lines in this label if you're not on fair use edition. 
        # stop music fadeout 1.0
        # play music "kaz speech.mp3" 
        GeorgeSocks "Why are we still here? Just to suffer?" 
        GeorgeSocks "Every night, I can feel my leg... and my arm... even my fingers."
        GeorgeSocks "The body I've lost... the comrades I've lost... won't stop hurting..." 
        GeorgeSocks "It's like they're all still there. You feel it, too, don't you?" 
        GeorgeSocks "I'm gonna make them give back our past."
        # stop music fadeout 1.0
        # play music "game.mp3" loop fadein 1.0
        GeorgeSocks "Do you want (dank) Metal Gear Solid memes or Patreon memes?" 
        menu:
            "Since Konami hasn't DMCA'd my game yet, let's guarantee that!":
                jump DMCAmi 
            "W€££, I am a $€££out, so £€t'$ go for Patr€on m€m€$.":
                jump patreonpennies 

        return
        
    label experimentalgeorge:   
        "What did you expect? Much like everything else in this game, this route is blatantly unfinished since the developer lacks talent and creativity."
        "So he has to rely on dank memes to make a game - similar to Gearbox." 
        
        return 
   
    label fuckOIT: 
        "tECh fOCusEd SchOOl." 
        
        return
 
        
        
    label sidthesquid:
        George "I still can't believe that I actually exist﻿"
        hide georgeanime
        with dissolve
        "Warning, you are now approaching extreme amounts of shitposting and meta, please turn back. you have been warned."
        show sidimg at right 
        Squid "Just when you thought this shitty game couldn't have gotten any worse"
        Squid "It was all a simulation, Joe, now you have decide on how the world goes"
        Squid "Dammit, I can never remember the order of these damn pills. Sounds about right when you apply a goldfish's memory to a 20 year old movie series." 
        Squid "Great, I just ruined the big twist of this game. Well, just get one with your options, will you?" 
        menu: 
            "Should I take the blue pill and exit from this awful game? This game's {i}story{/i} ends if I do and you'll wake up in your cozy bed believing that video games were inherently good (unless you decide to replay this game or save scum for some reason. I don't know why).":
                jump bluepill
            "Or should I take the red pill and see how far this shithole goes? Who is the candy boy? Remember, I'm just lying to your face, nothing more.": 
                jump redpill 
        
        return
        
    label georgeisboring:
        George "no u"
        Joseph "no u" 
        George "no U" 
        Joseph "no U" 
        George "NO u"
        Joseph "NO u" 
        George "NO U" 
        Joseph "NO U" 
        "I can't continue writing this idiocy any more, can we agree that in this scenario, everybody is an idiot?"
        "In-Game Joseph and George for saying this dialogue, me for writing this scenario, and you for sticking around long enough to read this tripe." 
        "Oh yeah, I don't feel like making a proper ending to this route. Deal with it." 
       
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
        "This ending, much like the base ending for the game, is incomplete. To see the true ending to this route, you need to buy the DLC"
        
        return
    
    label kissmurray:
        "You try to kiss Murray, but it turns out, this relationship is actually singleplayer and you can't interact with him. Also, Joe, what is wrong with you?"
        
        return
        
        
    label matthewwhsu:
        show matthewmatosis at right
        Matthew "This will be the terd date in my series of evenings where I try to sleep with you"
        menu:
            "I don't date white dark souls 2 deniers, baka-hentai!": 
                jump matthewhen
            "No thanks, I'm still stroking it.":
                jump joestrokit
            "xD xD xD":
                jump matthewirelandisbest
    
        
    label matthewhen:
        Matthew "is this the part where the creator makes an edgy joke about neo-nazis?"
        "Damn, you beat me to the punch." 
        
        return
        
    label joestrokit:
        Joseph "I haven't masturbated in 3 hours"
        "It's a reference to a dank Dark Souls video, btw." 
        
        return
        
    label matthewirelandisbest:
        "These three lovebirds shared their innermost feelings about Dark Souls all night while Turbo Button watched in another room, left out :(" 
        
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
        menu: 
            "You know when dogs eat their shit and then shit that shit out as shit. Anime is that.": 
                jump animeisforjerks 
            "Your majestic tail is so kawaii desu~":
                jump joetheweeb
            "not enough futa":  
                jump joeswife
        return
        
    label noahnoaudio:
        George "I still can't believe that I actually exist﻿"
        hide georgeanime
        with dissolve
        show noah calwel gervais at right 
        Noah "hi there {b}HACK HACK{/b} jos {b}COUGH COUGH UGH{/b} ehp"
        Joseph "Well, I make bo.."
        Noah "{b}HACK HACK COUGH COUGH HACK HACK{/b}"
        "And Noah coughed until the heat death of the universe, the end."
        
        return
    
    label joeswife:
        "Why are you putting futas in the game, what sort of madness are you creating" 
        Joseph "futa is love, futa is life" 
        "Can't argue with that logic, since he's married to one :/ " 
        "Well, I'm creatively bankrupt, so this is all you get for now, dear reader." 
        
        return
        
    label joetheweeb: 
        Joseph "I'm so -kawaii- from the compliment! Konichiwa!"
        SecondJoseph "Uguu desu uguu desu uguu" 
        Joseph "we can be anime together forever" 
        "Seriously, what the fuck am I doing with my life? This is what I do at 1 p.m during weekdays? I've been told I'd never amount to much, and I can believe them. But hey, let's throw an Eric Andre quote here to be witty or something. xD" 
        
        return 
        
    label animeisforjerks: 
        SecondJoseph "your bad anime" 
        Joseph "I am become anime, destroyer of worlds." 
        "And thus, Joseph destroys life, the universe, and everything to purge the very existence of the scourge known as anime." 
        
        return 
        
    label hamishshotthesheriff:
        George "I still can't believe that I actually exist﻿"
        hide georgeanime
        with dissolve
        show hamishanime at right
        Hamish "How the fuck this game got made I have no idea but I'm glad it did." 
        Hamish "Hi, I'm Hamish Black, and Welcome to Writing on Games" 
        "Intimidated by the sheer size of Hamish's muscles, Joseph slowly backs away."
        Hamish "Do you want to go to the gym with me and become a jerk?" 
        menu: 
            "Fuck yes, I want to be ripped. ANCHOR ARMS!": 
                jump joeceps
            "Let me make some cringey prey puns so I can bore you before I run away.": 
                jump preyception 
                
        return 
        
    label DMCAmi:
        "Fuck Konami"
        
        return 
                 
    label patreonpennies:
        "patr€on i$ a wond€rfu£ w€b$it€ with gr€at p€op£€ and no doxxing or any $ort of bad p€op£€. $upport m€ on patr€on, p£€a$€. $$$" 
        
        return 
        
    label joeceps: 
        hide bg room
        with None
        scene da jim
        show joe maid at left
        show hamishanime at right
        Hamish "How shall we torture your body today?" 
        menu: 
            "Squats - Just fuck me up, fam": 
                jump deathsquats 
            "Cycling - So I can watch my animes while getting swole!": 
                jump animecycles
            "Lifting - So I can enjoy out romantic artifically-flavored vanillalose protein shake after we work out! ;) ": 
                jump shakelifters 
            "Hamish's Routine - I'll have what he's having!": 
                jump hamishsway 
                
         
        
    label deathsquats:
        Joseph "Jesus fucking Christ, why did you let me do this exercise?" 
        Hamish "Don't blame the player for your own inadequacies!"
        Joseph "I can't help it that the creator of this dumb game is a weeaboo and a pervent that threw together a dragon head on a maid's body in an anime art style!"
        "And so, slightly butthurt, I cut off Joseph's rant. What? You want closure? Clearly, you're not playing the right game." 
        
        return 
        
    label animecycles: 
        "Joseph proceeds to marathon Eromanga-sensei before being arrested by the FBI." 
        "You'll need to wait for the chained wings DLC to see the remainder of this route >:) " 
        
        return 
        
    label shakelifters:
        Joseph "Mmmm. Gotta love the all natural taste of sucralose, acesulfate potassium, and saccharin!"
        Hamish "No fair! Stop hogging all of the organic artificial vanilla-flavored protein shake!"
        Hamish "y u bulli?"
        Joseph "because u bulli 12 lines ago in the code." 
        "Squid is ultimate bulli since he made this game. bulli ends route." 
        
        return 
        
    label hamishsway:
        Hamish "Ha my workout now is bodyweight squats, push up, light bicep curls and military press" 
        Hamish "Crunches and planking too - that's pretty much it I guess?"
        Joseph "That's {i}it{/i}? I'm a shitty waifu! How am I supposed to even think about doing that?"
        Joseph "The best I can do is mumble uguu and desu nyaa. How will those help?" 
        Hamish "Time to become a real man now, Joseph." 
        "And thus, Joseph learned how much exercise days sucked."
        "The End"
        
        return 
        
    label preyception:
        "Fair Use Edition audio override enabled" 
        "Something something mind game. Insert Prey's cover art and maybe a todd howard reference."
        "Yes, I'm lazy."
        
        return 
        
    label bluepill:
        "You were never the candy boy"
        
        return 
    
    label redpill: 
        "Hey, so, you're actually colorblind and took the blue pill."
        "Well, why are you still here? Do you want a trophy?" 
        "Well, you don't get one."
        "I never got one, so why should you be so entitled to get one?" 
        "Leave here and never come back! (unless, ya know, you decide to save scum or replay this crappy game for some reason)"
        
        return          
    # This ends the game.

    label secretroute:
        "Do you have a passcode?" 
        menu: 
            "Yes":
                $ code = renpy.input("Input the passcode here.") 
                jump checkcode 
            "No": 
                "Well, then git out of here."
                jump mainbranch2 

    label checkcode: 
        if code == boldpassword:
            play sound "h3h3cough.mp3" 
            "You have unlocked the BOLD and the BEAUTIFUL route"
            jump boldandbeautiful
        else: 
            "You have entered an INVALID code, returning to the previous menu!" 
            jump mainbranch2
            
    label boldandbeautiful:
        George "I still can't believe that I actually exist﻿"
        hide georgeanime
        with dissolve
        stop music fadeout 1.0
        play music "Meatball Parade.mp3"
        show loser at right
        Bold " I don't chase girls, but I'll chase Ethan to the grave." 
        "If you thought Ethan and Hila defamed your character, you're in for a world of hurt, {i}loser{/i}" 
        menu: 
             "DENIED": 
                jump denied 
             "Justice served with a carrot in the ass, and mayonnaise in the mouth.": 
                jump mayonnaise
             "Wow Matt! Bad moves! Ashamed of you! Cut it out!": 
                jump parkourloser 

    label denied: 
        "We don't care about what you have to say anymore, Hoss. You're irrelevant. Goodbye and good riddance."
        
        return
        
    label mayonnaise: 
        "We don't care about what you have to say anymore, Hoss. You're irrelevant. Goodbye and good riddance."
        
        return 
    
    label parkourloser:
        "We don't care about what you have to say anymore, Hoss. You're irrelevant. Goodbye and good riddance."
        
        return 
        
    return