# Characters
define l = Character("Lina", who_color="#0f690fff")
define r = Character("redshark123", who_color= "#000000")
define v = Character("Val", who_color= "#6717a1ff")
define m = Character("Melanie", who_color= "#9a2151ff")


# Name Highlighting in Text
default Lina = "{color=#0f690fff}Lina{/color}"
default redshark123 = "{color=#000000}redshark123{/color}"
default Val = "{color=#6717a1ff}Val{/color}"
default Melanie = "{color=#9a2151ff}Melanie{/color}"


# Dialogue History
define config.history_current_dialogue = True
define config.history_length = 200


# Bond Value
default bond_value = 0
screen bond_display():
    frame:
        align(1.0, 0.0)
        padding(10, 10)
        text "Bond with Player: [bond_value]"


# Meta File Interaction
init python:
    import os
    import sys
    import subprocess

    def open_game_folder():
        try:
            path = renpy.config.gamedir

            if sys.platform == "darwin":    #Mac OS
                subprocess.call(["open", path])
            elif sys.platform.startswith("win"):    #Windows
                os.startfile(path)
            else:
                subprocess.call(["xdg-open", path]) #Linux
        
        except Exception:
            renpy.log("Failed to open game folder.")

    def profile_detection():
        try:
            path = os.path.join(renpy.config.gamedir, "dating_profiles.txt")

            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip().lower()

                    # TODO: Fill in profile content
                    if line.startswith("l_fav_book"):
                        return line.split(": ", 1)[1].strip()
        
        except Exception:
            renpy.log("Failed to get favorite book")
            return None
    
    def place_detection():
        try:
            path = os.path.join(renpy.config.gamedir, "dating_profiles.txt")

            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip().lower()

                    # TODO: Fill in profile content
                    if line.startswith("l_fav_hangout_spot"):
                        return line.split(": ", 1)[1].strip()
        
        except Exception:
            renpy.log("Failed to get favorite place")
            return None


# Game Body
# Start
label start:

    # Scene 1

    # TODO: play music <[happy]>

    l "{i}The dating sim life is pretty simple.{/i}"
    l "{i}All you have to do is get to know people.{/i}"
    l "{i}Who knows, maybe you’ll be lucky enough for them to pick you!{/i}"
    l "{i}And if not, there’s plenty more fish in the sea.{/i}"

    show screen bond_display

    stop music

    l "{i}At least, that’s how it used to be.{/i}"
    l "{i}Now, every play session is a death match to win the player’s appreciation.{/i}"
    l "{i}If you aren’t interesting enough for anybody…{/i}"
    l "{i}Well, just hope that doesn’t happen.{/i}"

    # Scene 2

    show m at right
    show l at center
    show v at left

    m "And then there were three."
    m "I can’t believe I’ve been stuck in this hell with you losers for so long."
    m "I can’t wait for this dweeb to choose me so I can get out of here."

    menu:
        "Nice to see you too, [Melanie].":
            jump choice1

        "We can’t wait either.":
            jump choice1
        
    label choice1:
        m "Whatever."
        v "[Melanie], whoever wins, wins. We can all try our best, but it’s ultimately up to the player."
        m "Well, why wouldn’t he choose me? What could you possibly have that I don't?"
        m "Now if you’ll excuse me, I need to go prepare. I have a player to impress."

    hide m

    # Scene 3

    hide l
    show l at right

    v "So, [Melanie] hasn’t changed."

    menu:
        "You said it.":
            jump hyf
        "How are you doing?":
            jump idk
        
    label hyf:
        v "How are you feeling about this?"
        jump next_1
    
    label idk:
        v "I don’t know."
        v "If one of us wins, the other loses."
        v "Like, I’d be happy for you if you made it out, but at the same time… well, you know."
        v "How about you?"

    label next_1:
        menu:
                "Pretty confident!":
                    jump ysb
                "Nervous.":
                    jump nntb

    label ysb:
        v "You should be!"
        jump next_2

    label nntb:
        v "There’s no need to be."

    label next_2:
        v "Who in their right mind wouldn’t choose you?"
    
    v "I just wish this wasn’t the only way."
    v "Everybody else had their consciousness erased when they were chosen."
    v "That’s the only way for us to not feel the pain when the glitches consume us."
    v "Just know that no matter what happens, I’m glad that we got to spend time together."

    # Scene 4

    hide v
    hide l

    # call screen

    # TODO: play music [happy]

    # TODO: [start button animation]

    stop music
    # TODO: play music [coffee shop]

    "Teacher" "Alright class, it’s time to start our group project. Please make groups of four."

    show m at right
    show l at center
    show v at left
    show r at truecenter

    r "Hey! Is it alright if I group up with you three?"
    m "Of course!!! I always love to meet new people! <3"
    v "Ugh, fine. Just don't interrupt me while I'm brooding."

    menu:
        "Welcome to the group!":
            jump thanks
        "What’s your name?":
            jump im_redshark123_nice_to_meet_you

    label thanks:
        r "Thanks."
        jump next_3

    label im_redshark123_nice_to_meet_you:
        r "I’m [redshark123]. Nice to meet you!"

    label next_3:
        hide l
    
    hide m
    hide v
    hide r

    "About an hour goes by..."

    # Scene 5

    show l at right
    show r at left

    r "So, [Lina], I heard that you really like books? What kind of stuff do you read?"

    menu:
        "I really like fantasy.":
            jump huh_weird
        "I’ve been reading through the Chronicles of Narnia recently.":
            jump never_heard_of_those

    label huh_weird:
        r "Huh, weird. I’m not really into stuff like that." 
        r "It’s not bad, but you can’t find someone like Hari Seldon in books like that."
        jump next_4

    label never_heard_of_those:
        r "Never heard of those."
        r "I’m guessing there’s nobody like Hari Seldon in those though."

    label next_4:
        r "Hey [Melanie], what about you?"

    hide r
    hide l
    show l at truecenter

    l "{i}Oh no, he isn’t interested in me at all! But how am I going to get out of this place if I can’t get him to pick me?{/i}"
    l "{i} There’s nothing I can do. Like [Val] said, it’s ultimately up to the player. But I was hoping… maybe… I thought maybe this time I would finally be free.{/i}"
    l "{i}I guess that’s it then. I’m done for.{/i}"

    # Scene 6

    stop music
    # TODO: play music [mysterious]

    # TODO: [game breaking animation]
    # TODO: play sound [glitchy sounds]

    l "{i} What the…? {/i}"
    l "{i} What’s going on? {/i}"
    l "{i} Something’s wrong… I think it might be the game’s code! {/i}"

    l "{i} Huh, my folder is lighting up. {/i}"
    $ import subprocess
    $ import sys
    $ import os
    $ open_game_folder()  # Folder pops up

    l "{i} Usually that’s where I keep stuff I collect as the game goes on, but maybe something’s up with it. {/i}"
    l "{i} Wait, what? Why is my {b}dating profile{/b} in my folder? {/i}"
    l "{i} That has all the information about me so the player can decide if they like me… {/i}"
    l "{i} …but usually I’m not able to access it. {/i}"

    # Profile Interaction

    l "{i} Wait, I can change stuff? I’ve never been able to do that before!{/}"
    l "{i} This must be because of one of those glitches {/i}"
    l "{i} Maybe… could I use this to my advantage {/I}"
    l "{i} If I can my profile align with [redshark123]’s, maybe I can make him want to pick me {/i}"
    l "{i} Now, what do I know about him? What can I change? {/i}"

    label change_profile:
        $ current_book = profile_detection()

        if current_book == "foundation":
            jump next_5
        
        else:
            jump rethink
    
    label rethink:
        $ renpy.choice_for_skipping()
        l "{i}Hmm... If I align my profile with [redshark123]’s, maybe I can make him want to pick me.{/i}"
        l "{i}Now, what do I know about him? What can I change?{/i}"
        jump change_profile

    # Scene 7

    # TODO: A poster in the classroom that can be added to the folder and viewed when clicked (I can design it)

    # TODO: scene [classroom]
    # TODO: music [coffee shop]

    label next_5:
        show l at center

        l "{i} There, that should do it. {/i}"
        l "{i} Now he should think that I like the Foundation series. {/i}"

        show m at right

    m "You’re so screwed."
    m "This guy’s nothing like you at all!"
    m "I’m totally gonna win this guy over and get out of here."
    m "After all, I DO how to make the guys swoon. "

    menu:
        "We’ll see.":
            jump its_okay_to_admit_defeat_you_know
        "Then how come you haven’t escaped yet?":
            jump i_shut_up

    label its_okay_to_admit_defeat_you_know:
        m "It’s okay to admit defeat, you know."
        m "I’m sure getting destroyed by the glitches can’t be that bad."

    label i_shut_up:
        m "I- shut up."
        m "You can be so annoying, you know that?"

    m "Anyway, I’ve got to go now."
    m "I just wanted to drop in and let you know how doomed you are."

    # Scene 8

    # TODO: glitches appear (graceguqianying@uchicago.edu This could be an animation)
    stop music
    # TODO: play sound [glitch]
    # TODO: A single glitch remains onscreen (show glitch)

    m "What…?"
    m "What’s happening?!?"

    # TODO: glitches stop
    show v at left

    v "Did you see that too?"
    m "Um, yeah! How could we not?"
    v "The glitches are spreading quicker than we realized."

    menu:
        "What do we do?":
            jump theres_only_one_thing_we_can_do
        "But the game only just started!":
            jump i_know

    label theres_only_one_thing_we_can_do:
        v "There’s only one thing we can do."
        jump next_6

    label i_know:
        v "I know."
        v "None of us were expecting this to happen yet."
        v "But it’s clear what we have to do."

    label next_6:
        v "We have to stop them."
    m "Stop them? Are you crazy? We can’t do that!"
    v "Well, we can’t stop them from appearing…"
    v "...but we can at least try to mitigate the ones that already appeared."
    v "If the [redshark123] finds out about these, he won’t want to play anymore."
    v "And then we’ll lose all hope of our consciousness being erased."
    m "…"
    m "Fine. How do we do this?"
    v "All of the glitches are breaks in the game’s code."
    v "If we get a closer look at them, we can see what’s wrong with the code and try to fix it."

    menu:
        "How do you know so much about this?":
            jump it_gets_pretty_boring_here
        "Fix it?":
            jump different_glitches_have_different_causes

    label it_gets_pretty_boring_here:
        v "It gets pretty boring here."
        v "I’ve been killing time by poking around the game’s code."
        jump next_7

    label different_glitches_have_different_causes:
        v "Different glitches have different causes."
        v "You won’t know how to fix a glitch until you take a look and mess around a little bit."

    label next_7:
        v "[Lina], you’re supposed to be here for the next scene."
    v "You should stay in case [redshark123] shows up."
    v "In the meantime, try to fix the glitch here."
    v "[Melanie] and I will look for glitches at our next scenes."
    m "Are you sure this will work, [Val]?"
    v "No, but I can’t think of a better way. We should get going."

    hide v
    hide m

    l "{i}Alright, I’ll fix the glitch. How hard can that be?{/i}"

    # Scene 9

    # TODO: This is a puzzle that involves sliding blocks of different lengths either left/right or up/down to create a free path to remove a smaller block, kind of like this: Rush Hour. If this is too hard to code, the puzzle can be changed.

    # TODO: scene [classroom]
    # TODO: play music [coffee shop]


    show l at center

    l "{i}I did it!{/i}"

    show r at truecenter

    r "Hey [Lina]! How are you doing?"

    menu:
        "Oh, hi [redshark123].":
            jump i_heard_that_you_really_like_foundation
        "Honestly, things are a little chaotic right now":
            jump oh_i_hope_the_project_isnt_stressing_you_out

    label i_heard_that_you_really_like_foundation:
        r "I heard that you really like Foundation."
        r "That’s actually one of my favorite book series! What are the chances?"
        jump next_8

    label oh_i_hope_the_project_isnt_stressing_you_out:
        r "Oh, I hope the project isn’t stressing you out."
        r "By the way, I heard that you really like Foundation."

    label next_8:
        r "That’s actually one of my favorite book series! What are the chances?"
    r "I was wondering… would you want to hang out some time outside of class?"
    r "You know, just to talk about the books and stuff."

    menu: 
        "That sounds great!":
            jump awesome_where_do_you_want_to_meet
        "Sure, I guess.":
            jump awesome_where_do_you_want_to_meet

    label awesome_where_do_you_want_to_meet:
        r "Awesome! Where do you want to meet?"

    menu:
        "There’s a pretty good cafe down the street…":
            jump oh
        "Have you heard of the Serenetea cafe?":
            jump oh

    label oh:
        r "Oh."
        r "I’m honestly not a big fan of hanging out at cafes."
        r "If I’m with somebody else, I usually want to DO something, not just around."
        r "Also, I’m not sure if the cafe has outdoor seating. I hate being cooped up."
        r "Thanks anyway, though."

    hide r

    l "{i} This guy is impossible! {/i}"
    l "{i} My profile says my favorite place to spend time is a cafe, but I guess this guy really hates those. {/i}"
    l "{i} Maybe… maybe I can mess with my profile a little again. {/i}"
    l "{i} Where would [redshark123] want to go out? {/i}"

    # Scene 10

    # TODO: A map that can be added to the folder and viewed in on when you click it (I think I can design the map, but I might need your help with the art
    # The ability to change the “favorite place” via dropdown or text entry
    # The game to continue when the favorite place spot is changed to mini golf

    label change_place:
        $ current_place = place_detection()

        if current_place == "mini golf":
            jump next_9
        
        else:
            jump rethink_2
    
    label rethink_2:
        $ renpy.choice_for_skipping()
        l "{i}So, I can mess with my profile a little again.{/i}"
        l "{i}Where would [redshark123] want to go out?{/i}"
        jump change_place

    # TODO: scene [classroom]
    
    label next_9:
        show l at left
        l "{i} That seems right, at least from what I know about him. {/i}"

    # TODO: play music [tension]
    show r at right

    m "So, you like Foundation now?"
    m "[redshark123] told me all about it."
    m "I could have sworn your character only liked fantasy books…"
    m "I know you’re up to something, [Lina]."

    menu: 
        "Mind your own business, [Melanie].":
            jump my_own_business
        "I don’t know what you’re talking about":
            jump yeah_right

    label my_own_business:
        m "My own business?"
        m "This is all of our business!"
        jump next_10

    label yeah_right:
        m "Yeah, right."
        
    label next_10:
        m "If you keep messing with the game like this, you’ll ruin it for everyone."
    m "I know you’re up to something, [Lina]."
    m "I just can’t believe you would ever get this desperate."

    # Scene 11

    show r at truecenter

    r "Hey [Melanie], is it okay if I talk to [Lina] alone for a second?"
    m "Wha-why? I mean…"
    m "Of course you can, cutie! Teehee."

    hide m
    hide l
    show l at truecenter
    # TODO: play music [romantic]

    r "[Lina], I just found out that you like mini golfing. I’m a fan too."
    r "First the books, and now this…"
    r "Why didn’t you just tell me about those to begin with?"
    r "I’m starting to get the feeling you’re embarrassed to tell me the truth."
    r "Well, you don’t have to be embarrassed."
    r "I want you to know that I think you’re really great."
    r "I know we were talking about hanging out, but I was wondering…"
    r "…could I take you out for real? Like, on a date?"

    stop music
    # TODO: Menu options that say “Yes” and “No” show up, but before the player can click either of them, #another glitch animation plays and glitch sprites block the options. While this is going on, redshark123 #asks the player why they’re not responding, but they’re powerless about it (how much of this is doable    #graceguqianying@uchicago.edu? I thought this would be cool, but we definitely don’t need all of it.

    l "{i} Oh no, another glitch! Could the timing be any worse? {/i}"
    l "{i} I need to get rid of this so [redshark123] can pick me! {/i}"

    # Scene 12

    # TODO: For the second glitch puzzle, I was thinking of something different than rush hour. Another puzzle that I think could work well in ren.py is a nonogram, in which you have a 10x10 grid with numbers next to each row and column. The numbers tell you how many squares should be filled in their respective row/column, and you must fill them accordingly. Here’s an example: Do you think you can code this, graceguqianying@uchicago.edu? Again, if not, we can always change the puzzle.

    # TODO: scene [classroom]
    stop music
    show l at center
    show r at truecenter

    l "{i}Phew, that was tough{/i}"
    l "{i}Oh wait, [redshark123] is still talking{/i}"

    r "Okay, [Lina], I get it."

    # TODO: play music [tension]

    r "You could have just said that you’re not interested."
    r "There’s no need for the silent treatment."
    r "Whatever. If you’re going to be ungrateful, I’ll just go out with [Melanie]."
    r "She’s not as great as you, but at least she’s shy and sweet. I could spend time with a girl like that."

    menu: 
        "Wait!":
            jump bye_lina
        "No, you don’t understand!":
            jump bye_lina

    label bye_lina:
        r "Bye, [Lina]."
        hide r

    l "{i}Aargh! I was so close!{/i}"
    l "{i}He was about to give me a ticket out of this place!{/i}"
    l "{i}I need him to pick me. I don’t want to be left to suffer here.{/i}"
    l "{i}Even if he chose [Val], I would be okay with it. At least she would be happy.{/i}"
    l "{i}But [Melanie]? She doesn’t deserve to be free!{/i}"
    l "{i}The worst part is that I can’t fix it by changing my profile this time.{/i}"
    l "{i}I think… I think this is it.{/i}"

    # Scene 13
    # TODO: play music [mysterious]

    $ import subprocess
    $ import sys
    $ import os
    $ open_game_folder()  # Folder pops up again

    l "{i}Again with the folder?{/i}"

    # TODO: When players click on the folder, they’ll find a new file, Melanie’s profile (I’ll design it)

    l "{i}{color=#9a2151ff}MELANIE{/color}’s profile?!?{/i}"
    l "{i}What’s that doing in my folder?{/i}"
    l "{i}This is so weird. Why is this all happening to me?{/i}"
    l "{i}Wait…{/i}"
    l "{i}I wonder… could I use this to my advantage too?{/i}"
    l "{i}I can’t make [redshark123] like me more by changing my own profile…{/i}"
    l "{i}But what if I sabotage [Melanie]’s? Maybe I can edit hers the same way I can with mine!{/i}"

    # TODO: When players click on Melanie’s profile, they’ll be taken to a screen that says it’s locked with a pin code. #There’s a hint that says MM/DD.

    l "{i}It’s locked? Dang it.{/i}"
    l "{i}Maybe I can figure out the password somehow.{/i}"
    l "{/i}...I shouldn’t be doing this. It’s not right.{/i}"
    l "{/i}But it’s me or her. I’m not hurting [Melanie], I’m just using all the tools at my disposal.{/i}"
    l "{i}Right?{/i}"

    # Scene 14

    # TODO: This is the last puzzle. The interactive features needed are:
    # A note sheet that can be added to the folder and viewed when clicked (I’ll design it)
    # An input asking for four numbers when Melanie’s profile is clicked
    # Melanie’s profile shows up after the code 1018 is entered
    # At least one interactive aspect of Melanie’s profile that can be changed to something less desirable (like changing her traits to something redshark123 doesn’t like)

    # This happens after Melanie’s profile is changed

    # TODO: scene [classroom]
    show l at center

    l "{i}There, I just made a little change. Surely she won’t notice just one-{/i}"

    show m at right
    # TODO: play music [angry]

    m "{color=#0f690fff}LINA{/color}!!!"
    m "I KNOW you just didn’t sabotage my profile!"
    m "How low can you get?!?"
    m "Oh my god, I would punch you if I had an animation for it!"

    menu: 
        "I don’t-":
            jump dont_give_me_that_crap
        "[Melanie]-":
            jump dont_give_me_that_crap

    label dont_give_me_that_crap:
        m "Don’t give me that crap!"
        m "I swear, I’m gonna-"

    # Scene 15

    show v at left
    v "[Melanie]! That’s enough."
    m "Oh, since when were you in charge? Didn’t you see what she did to me? She literally ruined me!"
    v "[Melanie]. We are characters in a dating sim. It’s not that deep."
    v "Think about it. We three think that our personalities are worthwhile…"
    v "But every player just sees us as two-dimensional characters whose only role is to get hit on."
    v "So why do you care so much?"
    m "BECAUSE! How is he supposed to pick me if this psycho ruins my image?"
    v "You don’t have any proof that it was [Lina] that changed your profile."
    v "And even if you did, that doesn’t mean she ruined your chances."
    v "Now come on. We’re supposed to be here for our next scene."
    v "We need to leave before [redshark123] sees us."
    m "But- I- ugh. Fine."

    hide m

    v "Hey [Lina]? I just wanted to say…"
    v "I’m rooting for you. I think you’ve got this."

    menu: 
        "Thank you.":
            jump of_course
        "I’m rooting for you too.":
            jump x

    label of_course:
        v "Of course!"
        v "You deserve to be free from this hell."
        jump next_11

    label x:
        v "..."
        v "Thanks."

    label next_11:
        v "You’ve got this."

    # TODO: Ending

    return