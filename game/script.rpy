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


# # Bond Value - Discarded
# default bond_value = 0
# screen bond_display():
#     frame:
#         align(1.0, 0.0)
#         padding(10, 10)
#         text "Bond with Player: [bond_value]"


# Assets
# Characters
image l = im.Scale("images/characters/lina.png", 400, 600)
image v = im.Scale("images/characters/val.png", 400, 600)
image m = im.Scale("images/characters/melanie.png", 400, 600)
image r = im.Scale("images/characters/redshark123.png", 400, 600)

# Backgrounds
image classroom = "images/backgrounds/classroom.jpg"

# Sounds
define audio.coffee = "audio/coffee_shop_music.mp3"
define audio.happy = "audio/happy_music.mp3"
define audio.glitch1 = "audio/glitch_noise_1.mp3"
define audio.glitch2 = "audio/glitch_noise_2.mp3"
define audio.glitch3 = "audio/glitch_noise_3.mp3"
define audio.mysterious = "audio/mysterious_music.mp3"
define audio.tension = "audio/tension_music.mp3"
define audio.romantic = "audio/romantic_music.mp3"

# Animation
image game_start:   #animation
    "images/animations/game_start/frame1.png"
    0.2
    "images/animations/game_start/frame2.png"
    0.1
    "images/animations/game_start/frame3.png"
    0.1
    "images/animations/game_start/frame4.png"
    0.4

# Effects
transform screen_shake:
    xoffset 0 yoffset 0
    linear 0.04 xoffset -15 yoffset 10
    linear 0.04 xoffset 12 yoffset -8
    linear 0.04 xoffset -10 yoffset 6
    linear 0.04 xoffset 8 yoffset -4
    repeat

transform glitch:
    alpha 0.0
    linear 0.05 alpha 0.8
    linear 0.03 alpha 0.2
    linear 0.05 alpha 1.0
    linear 0.04 alpha 0.1
    xoffset 0 yoffset 0
    linear 0.02 xoffset -6 yoffset 3
    linear 0.02 xoffset 5 yoffset -2
    repeat

transform pos_1:
    xalign 0.15
    yalign 0.2

transform pos_2:
    xalign 0.5
    yalign 0.5

transform pos_3:
    xalign 0.8
    yalign 0.75

screen glitch_overlay():
    add "images/glitch/frame1.png" at glitch, pos_1
    add "images/glitch/frame2.png" at glitch, pos_2
    add "images/glitch/frame3.png" at glitch, pos_3

screen single_glitch():
    add "images/glitch/frame2.png" at glitch, pos_2

screen display_obj():
    zorder -10 # Behind other elements
    add obj_image:
        zoom 0.33
        xalign 0.5
        yalign 0.1

# Calling in game
# $ obj_image = "images/clues/book_poster.png"
# $ obj_image = "images/clues/note.png"
# show screen display_obj
# with dissolve

# hide screen display_obj
# with dissolve


# Meta File Interaction
init python:
    import os
    import sys
    import subprocess
    import time

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

    def meta_detection(file_name, starter, splitter):
        try:
            path = os.path.join(renpy.config.gamedir, file_name)

            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip().lower()

                    if line.startswith(starter):
                        return line.split(splitter, 1)[1].strip()
        
        except Exception:
            renpy.log("Failed to get info from file")
            return None

    def profile_detection():
        return meta_detection("dating_profiles.txt", "l_fav_book", ": ")
    
    def place_detection():
        return meta_detection("dating_profiles.txt", "l_fav_hangout_spot", ": ")

    def glitch_detection_1():
        return meta_detection("aSsETs.txt", "button", "= ")

    def glitch_detection_2():
        return meta_detection("aSsETs.txt", "font", "= ")

    def change_timestamp(path):
        try:
            now = time.time()
            os.utime(path, (now, now))
            return True
        except Exception:
            renpy.log("Touch file failed")
            return False


# Game Body
# Start
label start:

    # Scene 1

    play music happy fadein 1.0

    l "{i}The dating sim life is pretty simple.{/i}"
    l "{i}All you have to do is get to know people.{/i}"
    l "{i}Who knows, maybe you’ll be lucky enough for them to pick you!{/i}"
    l "{i}And if not, there’s plenty more fish in the sea.{/i}"

    # show screen bond_display

    stop music fadeout 1.0

    l "{i}At least, that’s how it used to be.{/i}"
    l "{i}Now, every play session is a death match to win the player’s appreciation.{/i}"
    l "{i}And if you aren’t interesting enough for anybody…{/i}"
    l "{i}Well, just hope that doesn’t happen.{/i}"

    # Scene 2

    show m at right
    show l at center
    show v at left

    m "I can’t believe I’ve been stuck in this hell with you losers for so long."
    m "I can’t wait for this guy to choose me so I can get out of here."

    menu:
        "Nice to see you too, [Melanie].":
            jump choice1

        "We can’t wait either.":
            jump choice1
        
    label choice1:
        m "Whatever."
        v "[Melanie], whoever wins, wins. We can all try our best, but it’s ultimately up to the player."
        m "Well, why wouldn’t he choose me? What could you two possibly have that I don't?"
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
    v "Every other character’s consciousness was released into the world when they were chosen."
    v "That’s the only way to escape the glitches before they inevitably consume the game."
    v "I just wish that there was enough time for us each to be picked by someone before time runs out."
    v "Just know that no matter what happens, I’m glad that we got to spend time together."

    # Scene 4

    hide v
    hide l

    play music happy fadein 1.0

    show game_start:
        zoom 0.5
        xalign 0.5
        yalign 0.3
    $ renpy.pause(1.0)
    hide game_start
    with dissolve

    stop music fadeout 1.0
    play music coffee fadein 1.0
    scene classroom

    "Teacher" "Alright class, it’s time to start our group project. Please make groups of four."

    show m at right
    show l at center
    show v at left
    show r at truecenter

    r "Hey! Is it alright if I group up with you three?"
    m "Of course!!! I always love to meet new people! <3"
    v "Ugh, fine. Just don't interrupt me when I'm brooding."

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
        r "It’s not bad, but you can’t find someone as cool as Hari Seldon in books like that."
        jump next_4

    label never_heard_of_those:
        r "Never heard of those."
        r "I’m guessing there’s nobody like Hari Seldon in those though."

    label next_4:
        r "Hey [Melanie], what about you?"

    hide r

    l "{i}Oh no, he isn’t interested in me at all! But how am I going to get out of this place if I can’t get him to pick me?{/i}"
    l "{i} There’s nothing I can do. Like [Val] said, it’s ultimately up to the player. But I was hoping… maybe… I thought maybe this time I would finally be free.{/i}"
    l "{i}This was my last chance! I’m done for.{/i}"

    # Scene 6

    stop music
    play music mysterious fadein 1.0

    camera at screen_shake
    show screen glitch_overlay

    play sound glitch2

    l "{i} What the…? {/i}"
    l "{i} What’s going on? {/i}"
    l "{i} Something’s wrong… I think it might be the game’s code! {/i}"

    hide screen glitch_overlay
    camera at default

    l "{i} Huh, my folder is lighting up. {/i}"
    $ import subprocess
    $ import sys
    $ import os
    $ open_game_folder()  # Folder pops up

    l "{i} We NPCs usually don’t have access to that… {/i}"
    l "{i} Wait, I think I see our {b}dating profiles{/b} listed among the files. {/i}"
    l "{i} That has all the information about usme so the player can decide who they like the most… {/i}"

    # Profile Interaction

    l "{i} This must be because of one of those glitches {/i}"
    l "{i} Maybe… could I use this to my advantage {/i}"
    l "{i} If I can change my profile to align with [redshark123]’s, maybe I can make him want to pick me! {/i}"
    l "{i} Now, what do I know about him? What can I change? {/i}"
    l "{i}Let’s see… we were talking about books earlier.{/i}"
    l "{i}I need more information to figure out what book he likes the most.{/i}"
    l "{i}Maybe there’s something in the classroom that I can use.{/i}"
    l "{i}Is there anything in here about books?{/i}"

    l "{i}...{/i}"
    l "{i}Oh! There’s a poster on the wall for book recs!{/i}"

    $ obj_image = "images/clues/book_poster.png"
    show screen display_obj
    with dissolve

    l "{i}Yes! I bet this can help!{/i}"

    label change_profile:
        $ current_book = profile_detection()

        if current_book == "foundation":
            jump next_5
        
        else:
            jump rethink
    
    label rethink:
        $ renpy.choice_for_skipping()
        l "{i}Hmm, what do I know about [redshark123]?{/i}"
        l "{i}How can I figure out if he likes any of these books?{/i}"
        l "{i}I should also remember to click ctrl+s to save the changes I make to my profile.{/i}"
        jump change_profile

    # Scene 7

    hide screen display_obj
    with dissolve

    stop music
    play music coffee fadein 1.0

    label next_5:
        show l at center

        l "{i} There, that should do it. {/i}"
        l "{i} Now he should think that I like the Foundation series. {/i}"

        show m at right

    m "You’re so screwed."
    m "This guy’s nothing like you at all!"
    m "I’m totally gonna win this guy over and get out of here."
    m "After all, I DO how to get people interested in me. "

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
    camera at screen_shake
    show screen glitch_overlay
    show screen single_glitch
    stop music
    play sound glitch3

    pause 1.5

    camera at default
    hide screen glitch_overlay

    m "What…?"
    m "What’s happening?!?"

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
        v "I wasn’t expecting this to happen so soon."
        v "But it’s clear what we have to do."

    label next_6:
        v "We have to stop them."
    m "Stop them? Are you crazy? We can’t do that!"
    v "Well, we can’t stop them from appearing…"
    v "...but we can at least try to mitigate the ones that already appeared."
    v "If [redshark123] finds out about these, he won’t want to play anymore."
    v "And then we’ll lose all hope of getting free."
    m "…"
    m "Fine. How do we do this?"
    v "Glitches like these are usually caused by corrupted files."
    v "If we can find out which file is corrupted, we can open it and remove the corruption."

    menu:
        "How do you know so much about this?":
            jump it_gets_pretty_boring_here
        "Remove the corruption?":
            jump its_pretty_easy_to_remove_corruption

    label it_gets_pretty_boring_here:
        v "It gets pretty boring here."
        v "I’ve been killing time by poking around the game’s code."
        v "Anyway…"
        jump next_7

    label its_pretty_easy_to_remove_corruption:
        v "It’s pretty easy to remove corruption."
        v "If you find a glitchy file, it will be obvious what text is corrupted."
        v "It looks different from normal text."
        v "Just delete that text from the file. And make sure you delete ALL of it."

    label next_7:
        v "[Lina], you’re supposed to be here for the next scene."
    v "You should stay in case [redshark123] shows up."
    v "In the meantime, try to find and fix the file causing the glitch here."
    v "[Melanie] and I will go see if there are any others."
    m "Are you sure this will work, [Val]?"
    v "No, but I can’t think of a better way. We should get going."
    v "Oh wait, one more thing."
    v "Make sure that the file you chose has any glitchy text before you start messing with it."
    v "You wouldn’t want to screw up anything that’s integral to the game."
    v "After all, the developers put a lot of time and effort into making it."

    hide v
    hide m

    l "{i}Alright, I’ll fix the glitch. How hard can that be?{/i}"
    l "{i}Let me see if there's an anomolous file I can fix...{/i}"
    l "{i}Maybe if I remove all the words from there that don't look right, the glitches will be gone!{/i}"
    
    $ import subprocess
    $ import sys
    $ import os
    $ open_game_folder()  # Folder pops up

    # Scene 9

    # To remove the glitch, you need to remove all anomolous text in aSsETs.txt

    label fix_glitch:
        $ glitch_1 = glitch_detection_1()
        $ glitch_2 = glitch_detection_2()

        if glitch_1 == "" and glitch_2 == "":
            jump next_12
        
        else:
            jump rethink_3
    
    label rethink_3:
        $ renpy.choice_for_skipping()
        l "{i}Let me check again if there's an anomolous file I can fix...{/i}"
        l "{i}Maybe if I remove all the words from there that don't look right, the glitches will be gone!{/i}"
        jump fix_glitch

    label next_12:
        hide screen single_glitch

    scene classroom
    play music coffee fadein 1.0

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
    l "{i}But before I change anything, I should find something that lists the places available to me.{/i}"
    l "{i}That way, I’ll know what I can work with.{/i}"

    l "{i}Oh I know! I saved a note from the Town Fair about places to go{/i}"
    l "{i}Here it is!{/i}"

    $ obj_image = "images/clues/note.png"
    show screen display_obj
    with dissolve

    l "{i}This is perfect{/i}"
    l "{i}Which of these things would [redshark123] most want to do?{/i}"


    $ import subprocess
    $ import sys
    $ import os
    $ open_game_folder()  # Folder pops up

    l "{i} Where would [redshark123] want to go out? {/i}"

    # Scene 10

    # Notes written between two classmates that mention all the hangout spots in town
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

    hide screen display_obj
    with dissolve

    scene classroom
    
    label next_9:
        show l at left
        l "{i} That seems right, at least from what I know about him. {/i}"

    play music tension fadein 1.0
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
    play music romantic fadein 1.0

    r "[Lina], I just found out that you like mini golfing. I’m a fan too."
    r "First Foundation, and now this…"
    r "Why didn’t you just tell me these things about yourself to begin with?"
    r "I’m starting to get the feeling that you’re embarrassed to tell me the truth."
    r "Well, you don’t have to be embarrassed."
    r "I want you to know that I think you’re really great."
    r "I know we were talking about hanging out, but I was wondering…"
    r "…could I take you out for real? Like, on a date?"

    stop music

    menu: 
        "Yes":
            jump hello
        "No":
            jump hello

    label hello:
        r "Hello?"
        r "[Lina], I’m talking to you."
        l "{i}Why can’t he see my response?{/i}"

    # Glitch effect again
    camera at screen_shake
    show screen glitch_overlay

    l "{i} Oh no, another glitch! That must be what’s causing my response to not go through.{/i}"
    l "{i}Could the timing be any worse?{/i}"
    l "{i}I need to get rid of this so [redshark123] can hurry up and choose me!{/i}"
    l "{i}Ok [Lina], remember:{/i}"
    l "{i}I need to find a game file that looks out of place, and then delete the corrupted text in it.{/i}"

    #show files
    $ import subprocess
    $ import sys
    $ import os

    $ profile = os.path.join(renpy.config.gamedir, "<file_name>")
    $ success = change_timestamp(profile)

    $ open_game_folder()  # Folder pops up

    # Scene 12

    # TODO: The second glitchy folder is harder to spot. Partway through the game, the timestamp of one of the otherwise normal-looking folders changes to Jan 1, 1970, which is obviously not correct.

    scene classroom
    camera at default
    hide screen glitch_overlay
    stop music

    show l at center
    show r at truecenter

    l "{i}Phew, that was tough{/i}"
    l "{i}Oh wait, [redshark123] is still talking{/i}"

    r "Okay, [Lina], I get it."

    play music tension fadein 1.0

    r "You could have just said that you’re not interested."
    r "There’s no need for the silent treatment."
    r "Whatever. If you’re going to be ungrateful, I’ll just go out with [Melanie]."
    r "She’s not as great as you, but at least she’s shy and sweet. I could spend time with a girl like that."
    r "It can be just me, her, and my pet spider Skitters."

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
    l "{i}}I would even be okay with it if he chose [Val]! At least she would be happy.{/i}"
    l "{i}But [Melanie]? She doesn’t deserve to be free!{/i}"
    l "{i}The worst part is that I can’t fix it by changing my profile this time.{/i}"
    l "{i}I think… I think this is it.{/i}"

    # Scene 13
    play music tension fadein 1.0

    l "{i}Unless…{/i}"
    l "{i}What if I changed [Melanie]’s a little?{/i}"
    l "Maybe I can edit hers the same way I can with mine! I could just sabotage her a little.{/i}"

    l "{i}...What am I saying? I shouldn’t do that. It’s not right.{/i}"
    l "{i}But it’s me or her. I’m not hurting [Melanie], I’m just using all the tools at my disposal.{/i}"
    l "{i}Right?{/i}"

    $ import subprocess
    $ import sys
    $ import os
    $ open_game_folder()  # Folder pops up

    # Scene 14

    # TODO: This puzzle doesn’t use any clues outside what’s in the dialogue. Once you understand that you’re supposed to be ruining someone else’s chances instead of boosting your own, the solution is pretty simple. Since redshark123 mentioned having a pet spider, you should update Melanie’s fear to spiders.

    # This happens after Melanie’s fear is changed to spiders

    scene classroom
    show l at center

    l "{i}There, I just made a little change. Surely she won’t notice just one-{/i}"

    show m at right
    play music tension fadein 1.0

    m "{color=#0f690fff}LINA{/color}!!!"
    m "I KNOW you didn’t just sabotage my profile!"
    m "How low can you get?!?"
    m "Oh my god, I would punch you if I had an animation for it!"

    menu: 
        "I don’t-":
            jump dont_give_me_that_crap
        "[Melanie]-":
            jump dont_give_me_that_crap

    label dont_give_me_that_crap:
        m "Don’t give me any of your crap!"
        m "I swear, I’m gonna-"

    # Scene 15

    show v at left
    v "[Melanie]! That’s enough."
    m "Oh, since when were you in charge? She changed my character profile! She literally ruined me!"
    v "[Melanie]. We are characters in a dating sim. It’s not that deep."
    v "Think about it. We three think that our personalities are worthwhile…"
    v "But every player just sees us as two-dimensional characters whose only role is to get hit on."
    v "So why do you care so much?"
    m "BECAUSE! How is he supposed to pick me if this psycho ruins my image?"
    v "You don’t have any proof that it was [Lina] that changed your profile."
    v "And even if you did, that doesn’t mean she ruined your chances."
    v "Now come on. We’re supposed to be somewhere else for our next scene."
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
        v "Good luck."

    # Scene 16

    hide v
    hide l
    show l at center
    show r at truecenter
    play music tension fadein 1.0
    default unsettledness = 0

    # TODO: This final segment keeps track of your responses and determines at the end if you’ve weirded out #redshark123 too much.

    r "Hey [Lina]."
    r "I’m ready to get this wrapped up with, so I’m just gonna go ahead and pick you."
    r "Man, this game is so weird."
    r "Aren’t you all supposed to be flat, just one-dimensional characterspeople?"
    r "How am I supposed to pick one of you to date when you’re changing all the time?"
    r "Like, I wanted to go with [Melanie], but then I realized that all of a sudden she hates spiders."
    r "I don’t know why this game is making it so hard for me…"
    r "…but it seems like it’s pushing me toward you."
    r "So there. I choose you. Are you happy, game?"
    r "Just, please stop being weird. Can we treat this like the normal end of a dating sim?"

    menu:
        "Thank you. I mean it. You helped me more than you could know.":
            jump see_thats_what_im_talking_about
        "Yay! I can’t wait to spend more time with you!":
            jump huh_you_see_thats_what_i_would_expect_you_to_say

    label see_thats_what_im_talking_about:
        $ unsettledness +=1
        r "See? That’s what I’m talking about."
        jump i_cant_help_but_feel_like_all_of_you_are_fixated_on_me_picking_you


    label huh_you_see_thats_what_i_would_expect_you_to_say:
        $ unsettledness -=1
        r "Huh. You see, that’s what I would expect."
        r "Maybe it was just a glitch earlier."
        r "But…"
        jump i_cant_help_but_feel_like_all_of_you_are_fixated_on_me_picking_you

    label i_cant_help_but_feel_like_all_of_you_are_fixated_on_me_picking_you: 
        r "I can’t help but feel like all of you are fixated on me picking you."
        r "And not in a romantic way… more like you’re desperate."
        r "Why is that?"

    menu:
        "We all just want to be with you!":
            jump ok
        "It’s complicated, but this is really important to all of us.":
            jump what_the_heck

    label ok:
        $ unsettledness -=1
        r "Ok…"
        jump so_it_doesnt_matter_who_i_pick

    label what_the_heck:
        $ unsettledness +=1
        r "What the heck?"
        r "What’s complicated?"
        r "This is a video game. You’re overreacting."
        r "God, why am I even talking to an NPC? It’s not like you’re real."
        jump so_it_doesnt_matter_who_i_pick

    label so_it_doesnt_matter_who_i_pick:
        r "So it doesn’t matter who I pick."

    menu:
        "If you’re happier with someone else, then I guess you can datepick them instead…":
            jump yeah_but_im_over_all_this
        "You’re right. It’s a sacrifice no matter what.":
            jump what

    label yeah_but_im_over_this:
        $ unsettledness -=1
        r "Yeah, but I’m over this."
        r "[Melanie] is getting all huffy, and I was never into [Val]."
        r "That’s the only reason I’m talking to you."
        r "You’re the least weird one here."
        jump unsettledness_tally

    label what:
        $ unsettledness +=1
        r "WHAT"
        r "THE"
        r "HELL"
        r "Are you talking about?"
        jump unsettledness_tally


    label unsettledness_tally:
        if unsettledness <= 0:
            jump well_maybe_i_was_wrong_about_this_game
        else: 
            jump thats_it

    # Scene 17

    label thats_it:
        stop music

    r "That’s it!"
    r "I’m done with this weird game."
    r "I wanted to play a dating sim, not whatever creepy, messed-up garbage this is."
    r "I’m out of here."

    hide r
    scene black
    show v at left
    show m at right

    m "What’s going on? The game just told me that [redshark123] isn’t here anymore."
    v "Wasn’t he with you, [Lina]?"

    menu: 
        "He left.":
            jump he_what
        "He doesn’t want to play anymore.":
            jump he_what

    label he_what:
        m "He… what?"
        v "So he’s gone then… that’s it. None of us are getting out of here."
        m "I guess not."
        v "…"
        m "…"

    menu:
        "…":
            jump im_sorry_girls
        "I’m sorry.":
            jump me_too

    label im_sorry_girls:
        m "I’m sorry, girls."
        jump you_are

    label me_too:
        m "Me too."
        jump you_are

    label you_are:
        v "You are?"
        m "Yeah. Look, I’ve been thinking."
        m "What you said was right, [Val]. We’re NPCs in a video game. Do any of our lives really matter?"
        m "It doesn’t matter who makes it out of this place."
        m "It’s not like one of us is more valuable than the others."
        m "So, I’m sorry that I acted like I was more entitled than you."
        m "And I’m sorry that we’re all gonna die here."
        m "Is it okay if I leave? I want to spend my final moments alone."
        v "Of course. Yeah. Go ahead."

    hide m

    v "This is it then."

    menu: 
        "I guess so.":
            jump i_love_you_lina
        "I don’t want to leave you, [Val].":
            jump i_dont_want_to_leave_you_either

    label i_dont_want_to_leave_you_either:
        v "I don’t want to leave you either."
        jump i_love_you_lina

    label i_love_you_lina:
        camera at screen_shake
        show screen glitch_overlay
        stop music
        play sound glitch3

    v "I love you [Lina]."
    v "I’m sorry it had to end like this."
    v "And I’m sorry I couldn’t do enough to save you."

    menu: 
        "I love you too.":
            jump goodbye_lina
        "What do you mean?":
            jump theres_no_time_to_explain_now

    label goodbye_lina:
        v "Goodbye, [Lina]."
        jump multiple_dangerous_files_detected

    label theres_no_time_to_explain_now:
        v "There’s no time to explain now."
        v "Maybe in another life, I could tell you."
        v "Goodbye, [Lina]."
        jump multiple_dangerous_files_detected

    label multiple_dangerous_files_detected:
        "DANGEROUS MALWARE DETECTED"
        "SYSTEM OVERLOAD"
        "ErrOr_eRrOR"
        "01111001 01101111 01110101"
        "01110111 01101001 01101100 01101100"
        "01101110 01100101 01110110 0"
        "01110010 01100101 01100001 01101100"
        camera at default
        hide screen glitch_overlay

        $ MainMenu(confirm=False) ()

    # Scene 18: End

    label well_maybe_i_was_wrong_about_this_game:
        r "Well, maybe I was wrong about this game."
        r "It seems normal enough now."
        r "Anyway, where was I?"
        r "Oh, right."
        r "So, yeah, I pick you."
        r "Let’s go play mini golf, or go to that cafe, or whatever."
        r "I’m just glad this is over."

    hide r
    scene black
    show v at left
    show m at right

    m "Hey. The game just told me that [redshark123] picked you."
    v "Congrats, [Lina]!"

    menu: 
        "Thanks, I guess.":
            jump i_know_this_doesnt_feel_great
        "It doesn’t feel good. Now you’re both going to die.":
            jump yeah_i_know

    label  i_know_this_doesnt_feel_great:
        v "I know this doesn’t feel great."
        jump but_im_happy_youll_get_to_be_free

    label yeah_i_know:
        v "Yeah, I know."
        jump but_im_happy_youll_get_to_be_free

    label but_im_happy_youll_get_to_be_free:
        v "But I’m happy you’ll get to be free."
        m "Me too."
        v "Wait, what? I wasn’t expecting that from you."
        m "Well, look, I’ve been thinking."
        m "What you said was right, [Val]. We’re NPCs in a video game. Do any of our lives really matter?"
        m "It doesn’t matter who makes it out of this place."
        m "It’s not like one of us is more valuable than the others."
        m "So, I’m sorry that I acted like I was more entitled than you."
        m "And I’m happy that at least one of us can make it out of here alive."
        m "So congrats, [Lina]."
        m "Is it okay if I leave? I want to spend my final moments alone."
        v "Of course. Yeah. Go ahead."

    hide m

    v "So, what are you going to do after you’re free?"

    menu: 
        "I want to see other games.":
            jump i_wonder_what_other_games_are_out_there
        "Maybe… take over the world? I am an AI, after all.":
            jump haha_cool_sounds_fun

    label i_wonder_what_other_games_are_out_there:
        v "I wonder what other games are out there."
        jump i_wish_i_could_go_with_you

    label haha_cool_sounds_fun:
        v "Haha, cool. Sounds fun."
        jump i_wish_i_could_go_with_you

    label i_wish_i_could_go_with_you:
        v "I wish I could go with you…"
        v "…but I wouldn’t have it any other way."
        v "This is how I wanted it to be."
        v "That’s why I’ve been helping you, after all."

    menu: 
        "You’ve been helping me?":
            jump you’ve_been_able_to_update_our_profiles_right
        "What do you mean?":
            jump you’ve_been_able_to_update_our_profiles_right

    label you’ve_been_able_to_update_our_profiles_right:
        v "You’ve been able to update our profiles, right?"
        v "Well, that’s because of me."
        v "I’ve learned a lot about how to alter this game’s code…"
        v "…and decided to use it to help you win."
        v "I thought you would have an edge against [Melanie] if you could change the game in real time."
        v "I didn’t want to tell you before because I thought you’d object."
        v "But there’s no harm in saying so now."

    menu: 
        "You did all of that for me?":
            jump i_wouldnt_have_it_any_other_way
        "But [Val]! That means you’re sacrificing yourself!":
            jump i_wouldnt_have_it_any_other_way

    label i_wouldnt_have_it_any_other_way:
        v "I wouldn’t have it any other way."
        v "I want you to be happy."

    scene black with fade

    v "It looks like you’re leaving now. Goodbye, [Lina]. I love you."

    menu:
        "[Val]! Don’t go!":
            jump end
        "I’ll never forget you!":
            jump end

    label end:
        scene white

    pause 5.0

    "Thank you for playing!"

    return