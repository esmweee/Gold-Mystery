# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Maomao = Character("Maomao", color="#64a34b")
define Jinshi = Character("Jinshi", color="#9263b1")
define Gaoshun = Character ("Gaoshun")
define Xiaolan = Character("Xiaolan", color="#e6b440")
define Lishu = Character("Lishu", color="#fbadd3")




# The game starts here.

label start:

scene bg rearpalace

play music "audio/normalconversation.mp3" volume 0.5

"After the garden party..."
show xiaolan normal
"Xiaolan" "Oh right! Maomao, I've been meaning to ask you..."
"Xiaolan" "What are you going to do with all the hairpins you received?"
"Xiaolan" "I mean, really, who gets FOUR hairpins?"
show maomao normal at right
"Maomao" "I actually don't know yet. You did say it's possible to leave the rear palace with them..."
"Maomao" "... so that's probably what I'll be doing."

"Xiaolan" "You get to skip work and eat snacks!"
"Xiaolan" "Maomao! Take me with you."
"Xiaolan" "Our friendship is as valuable as gold, take me won't you!"
hide maomao normal
hide xiaolan normal
"Xiaolan and Maomao playfully bicker, yet suddenly a thought pops into Maomao's head."

show xiaolan normal
show maomao normal at right

"Maomao" "That reminds me of something."
"Maomao" "After the garden party, don't you think Lady Lishu was acting a bit odd?"
"Maomao" "I couldn't exactly get a good look at her, but she looked very... out of sorts."

"Not wanting to word it wrongfully, Maomao stops for a second and says nervously:"

"Maomao" "I-I mean, odd as in, she wasn't her usual self. Knowing her past history with her ladies-in-waiting, it wouldn't surprise me if they tried another scheme on her once again."

"Xiaolan" "Yeah, some rumours have recently been spreading around the rear palace."
"Xiaolan" "There were some reports that after the garden party was over she was rushed to the Diamond Pavillion."
"Xiaolan" "Some ladies-in-waiting also reported that she seemed somewhat fragile and pale, looking very frightened."

"Maomao" "Poor girl... Well, her situation is poor atleast."
"Maomao" "There's really been a handful of cases recently, haven't there?"
"Maomao" "..."
"Maomao" "I need a vacation."

"Xiaolan" "Haha! There sure have! You must keep yourself so busy Maomao."

"Maomao" "Yeah, I wonder what purple-haired individual's fault that is. "

"Xiaolan" "Are you referring to Master Jinshi? You know, you're super lucky to be so close to him all the time!"
"Xiaolan" "A lot of the girls here easily faint at just the sight of him. His looks are really no small deal..."

"Maomao stares deeply at Xiaolan, with some sort of playful grossed-out look on her face."
"Meanwhile, Xiaolan is deeply fascinated by Jinshi's visuals, not paying attention to her surroundings at all."

"Maomao" "Sure... Well, it's time for me to get going anyways. Here, take this."

hide maomao normal
hide xiaolan normal

"Maomao hands Xiaolan a box filled with dumplings."

show xiaolan normal
show maomao normal at right

"Xiaolan" "Maomao! Thank you so much! You're always so thoughtful, I really appreciate your company."

"Maomao" "Don't worry about it, Xiaolan. I'll be sure to stop by some other time with more snacks for you, alright?"

"Xiaolan" "Alright! I'll be waiting for you. Take care Maomao!"

label end: 
