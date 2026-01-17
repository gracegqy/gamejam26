# Characters
define l = Character("Lina", who_color="#0f690fff")
define r = Character("red_shark123", who_color= "#000000")
define v = Character("Val", who_color= "#6717a1ff")
define m = Character("Melanie", who_color= "#9a2151ff")


# Name Highlighting in Text
default lina = "{color=#0f690fff}Lina{/color}"
default rs = "{color=#000000}red_shark123{/color}"
default val = "{color=#6717a1ff}Val{/color}"
default melanie = "{color=#9a2151ff}Melanie{/color}"


# Dialogue History
define config.history_current_dialogue = True
define config.history_length = 200


# Game Body
# Start
label start:

    # Scene 1

    # play music <[happy]>

    l "{i}The dating sim life is pretty simple.{/i}"
    l "{i}All you have to do is get to know people.{/i}"
    l "{i}Who knows, maybe you’ll be lucky enough for them to pick you!{/i}"
    l "{i}And if not, there’s plenty more fish in the sea.{/i}"

    # stop music

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
    m "I can’t wait for this dweeb to choose me so I can get out of here.""

    menu:
	    "Nice to see you too, Melanie.":
		jump <whatever>
	“We can’t wait either.”:
		jump <whatever>

label <whatever>
	m “Whatever.”
	v “Melanie, whoever wins, wins. We can all try our best, but it’s ultimately up to the player.”
	m “Well, why wouldn’t he choose me? What could you possibly have that I don’t?”
	m “Now if you’ll excuse me, I need to go prepare. I have a player to impress.”

	hide m

#happy music

“The dating sim life is pretty simple.”
“All you have to do is get to know people.
“Who knows, maybe you’ll be lucky enough for them to pick you!”
“And if not, there’s plenty more fish in the sea.”

stop music

“At least, that’s how it used to be”
“Now, every play session is a death match to win the player’s appreciation”
“If you aren’t favorable in anybody’s eyes…”
“Well, just hope that doesn’t happen.”

show m at right
show l at center
show v at left

m “And then there were three.”
m “I can’t believe I’ve been stuck in this hell with you losers for so long.”
m “I can’t wait for this dweeb to choose me so I can get out of here.”

menu:
	“Nice to see you too, Melanie.”:
		jump <whatever>
	“We can’t wait either.”:
		jump <whatever>

label <whatever>
	m “Whatever.”
	l “Melanie, whoever wins, wins. We can all try our best, but it’s ultimately up to the player.”
	m “Well, why wouldn’t he choose me? What could you possibly have that I don’t?”
	m “Now if you’ll excuse me, I need to go prepare. I have a player to impress.”


    hide l
	show l at right

	v “So, Melanie hasn’t changed.”

	menu:
		“You said it.”
			jump <how are you feeling about this>
		“How are you doing?”
			jump <i dont know>

label <how are you feeling about this>
	v “How are you feeling about this?”
	
	menu:
		“Pretty confident!”
			jump <you should be>
		“Nervous.”
			jump <theres no need to be>

label <i dont know>
	v “I don’t know.”
	v “If one of us wins, the other loses.”
	v “Like, I’d be happy for you if you made it out, but at the same time… well, you know.”
	v “How about you?”

menu:
		“Pretty confident!”
			jump <you should be>
		“Nervous.”
			jump <theres no need to be>

label <you should be>
	v “You should be!”
	jump <who in their right mind wouldnt choose you>

label <theres no need to be>
	v “There’s no need to be.”
	jump <who in their right mind wouldnt choose you>

label <who in their right mind wouldnt choose you>
    v “Who in their right mind wouldn’t choose you?”
    v “I just wish this wasn’t the only way.”
    v “Everybody else had their consciousness erased when they were chosen.”
    v “That’s the only way for us to not feel the pain when the glitches consume us.”
    v “Just know that no matter what happens, I’m glad that we got to spend time together.” 



    return

