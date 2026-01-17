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



    return