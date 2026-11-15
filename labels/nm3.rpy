label nm3:
    [   0] scene black
    [   1] with None
    [   2] scene bg corridor
    [   3] with Dissolve(2.0)
    [   4] play music "p3"
    [   5] show natsuki 5e at f21 zorder 3
    [   6] n "This sucks. Why is Monika such a jerk?"
    [   7] n "She should be grateful that I even joined her stupid club. It's not like she can find any members."
    [   8] show sayori 4h at f22 zorder 3
    [   9] s "Monika's usually really nice!"
    [  10] s "She cares so much about everyone in the club being happy."
    [  11] n 5q "Yeah, right."
    [  12] s 1g "Well...she usually does..."
    [  13] n "Maybe when she's not busy being so judgmental."
    [  14] n 5u "So what if I'm into manga?"
    [  15] n "Why can't just one person accept that, instead of being so condescending about it?"
    [  16] s 1h "I accept it!"
    [  17] s 1q "I think it's cute."
    [  18] n 4e "Oh, come on! That's condescending too!"
    [  19] s 1l "I'm sorry, I didn't mean it like that..."
    [  20] s 1d "I just wanna support you."
    [  21] "Natsuki sighs."
    [  22] n 1s "I know. Thanks."
    [  23] n "It just really sucks."
    [  24] s 1c "Do you want me to talk to Monika?"
    [  25] n "I don't know."
    [  26] n 4g "It's not like it's gonna change her opinion of me."
    [  27] n "Like, even if you were to convince her to back off..."
    [  28] n 4s "That wouldn't suddenly make me feel like I'm actually welcome in the club."
    [  29] n 4u "I should just find another club."
    [  30] s 4h "Wait, you don't have to do that!"
    [  31] s "We can figure this out. Please?"
    [  32] s 1l "I mean, I'm the Vice President...or at least I think I am..."
    [  33] s 1d "And I don't want you to leave. Everyone deserves to feel welcome, and to be happy. So...I want to make that happen. For you."
    [  34] n 5s "..."
    [  35] s 1b "Um, I was wondering..."
    [  36] s "What was the reason that you decided to join the Literature Club?"
    [  37] n 5h "Well--"
    [  38] "Natsuki hesitates."
    [  39] n 5s "It's kind of dumb."
    [  40] s 1d "Aw, don't say that."
    [  41] s "There's no such thing as a dumb reason when everyone is welcome."
    [  42] n 5q "I wasn't welcome..."
    [  43] s 4h "You were to me!"
    [  44] s "So..."
    [  45] n 5u "..."
    [  46] n "Just don't tell anyone, okay?"
    [  47] n "Especially Monika."
    [  48] s 1a "I promise."
    [  49] "Natsuki sighs."
    [  50] n 1g "I'm just...tired of everyone judging me all the time."
    [  51] n "I can't enjoy any of the stuff I'm into without people making snotty comments about it."
    [  52] n 42c "Not that I care about what anyone else thinks."
    [  53] n "But you know, the signs for the Literature Club said that you can...be yourself, or whatever."
    [  54] n 5c "So I decided it was at least worth a shot."
    [  55] n 5s "But that was a lie, apparently."
    [  56] "Natsuki dejectedly kicks the toe of her shoe against the wall."
    [  57] n 5s "Oh, and I like writing, too..."
    [  58] s 4m "Really?!"
    [  59] s "How come you didn't say that to Monika?"
    [  60] show sayori 1b at t22 zorder 2
    [  61] n 4e "Because!"
    [  62] n "She was being so judgmental that I didn't...just want to tell her something she wanted to hear."
    [  63] n 4q "She didn't deserve that kind of satisfaction."
    [  64] n 4r "And if she knew I was into writing, then she would just be like everyone else, and try to push me away from the manga, in favor of the more 'mature' thing."
    [  65] s 1f "Mm..."
    [  66] show sayori at thide zorder 1
    [  67] hide sayori
    [  68] show natsuki at thide zorder 1
    [  69] hide natsuki
    [  70] "The two of them remain silent for a while."
    [  71] "Sayori understands that it's out of the question for Natsuki to return to the clubroom for today, at least."
    [  72] "But Natsuki has a reason for wanting to join the club, just like everyone else."
    [  73] "It's part of the club vision for her to be welcome."
    [  74] show sayori 4h at f22 zorder 3
    [  75] s "You deserve to express yourself as much as everyone else does."
    [  76] s "That's supposed to be what the club is for."
    [  77] s "So..."
    [  78] s 1j "I'm going to do everything I can to fix this."
    [  79] s "I promise."
    [  80] show sayori at thide zorder 1
    [  81] hide sayori
    [  82] stop music fadeout 2
    [  83] with None
    [  84] scene bg corridor
    [  85] with dissolve_scene_full
    [  86] unless persistent.content_warnings_enabled == True goto [89]
    [  87] 
    [  88] goto [89]
    [  89] pass
    [  90] play music "p7a"
    [  91] "It's lunchtime the next day."
    [  92] "The cafeteria and hallways are bustling with students rushing to meet with their friends and make the most out of their limited break time."
    [  93] show monika 2g at f11 zorder 3
    [  94] m "Where could she be...?"
    [  95] "Among them is Monika, who always eats lunch in her classroom--but she has some additional business today."
    [  96] "Fearing Natsuki would avoid coming to the club, Monika decided to try to find her during lunch so that she could make amends."
    [  97] with None
    [  98] scene bg corridor
    [  99] with wipeleft_scene
    [ 100] "After searching for an extensive time, Monika finally spots her."
    [ 101] "Despite her short stature, Natsuki's bright hair helps her stand out from the crowd."
    [ 102] show monika 1p at f11 zorder 3
    [ 103] m "Oh gosh..."
    [ 104] show monika at thide zorder 1
    [ 105] hide monika
    [ 106] "Suddenly feeling awkward, Monika is afraid to get closer."
    [ 107] "Natsuki is with some friends whom Monika doesn't recognize, and they're all energetically chatting together."
    [ 108] "It would be really tactless to just interrupt them."
    [ 109] play music "p3" fadeout 2
    [ 110] show nf1 1 at f33 zorder 3
    [ 111] nf1 "Oh yeah, did you end up joining that Literature Club, or what?"
    [ 112] show nf1 at t33 zorder 2
    [ 113] show natsuki 1c at f32 zorder 3
    [ 114] show natsuki 1c at f32 zorder 3
    [ 115] n "Huh? Of course I joined. Why wouldn't I?"
    [ 116] show nf2 1 at f31 zorder 3
    [ 117] nf2 "Hah! I told you she would join!"
    [ 118] show nf2 at t31 zorder 2
    [ 119] show nf1 at f33 zorder 3
    [ 120] nf1 "Ahahaha! Come on, you know she only joined because you wouldn't stop giving her crap about the Anime Club."
    [ 121] show nf1 at t33 zorder 2
    [ 122] n 4e "I told you, I never even wanted to join that stupid club!"
    [ 123] show nf1 2 at f33 zorder 3
    [ 124] nf1 2 "Oh, sure."
    [ 125] show nf1 at t33 zorder 2
    [ 126] show nf2 at f31 zorder 3
    [ 127] nf2 "Well, you have to give her some credit for at least making an effort to finally grow past that trash."
    [ 128] show nf2 at t31 zorder 2
    [ 129] show nf1 at f33 zorder 3
    [ 130] nf1 "Ahaha, true. Well, congrats on finally graduating middle school, Natsuki. We're proud of you."
    [ 131] show nf1 at t33 zorder 2
    [ 132] n 5w "Shut up, just let me do my thing."
    [ 133] show natsuki 5s at t32 zorder 2
    [ 134] show nf1 1 at f33 zorder 3
    [ 135] nf1 1 "I'm just joking. You know we love you."
    [ 136] show nf1 at t33 zorder 2
    [ 137] show nf2 at f31 zorder 3
    [ 138] nf2 "Yeah, once the Literature Club makes you a famous writer, we'll be the first ones to buy your book."
    [ 139] show nf2 at t31 zorder 2
    [ 140] show nf1 at f33 zorder 3
    [ 141] nf1 "What, you're gonna buy her smutty fan fiction?"
    [ 142] show nf1 at t33 zorder 2
    [ 143] show nf2 2 at f31 zorder 3
    [ 144] nf2 2 "Ahahahaha! Well, obviously! I want a signed copy!"
    [ 145] show nf2 at t31 zorder 2
    [ 146] n 4r "That was like years ago! You don't think I've grown out of it by now?"
    [ 147] show nf1 at f33 zorder 3
    [ 148] nf1 "I told you, I was joking. Besides, it's a good reminder of how far you've come since then."
    [ 149] nf1 "Not to mention you couldn't have done it without us. That gives us a pass to joke about it."
    [ 150] show nf1 at t33 zorder 2
    [ 151] n 4s "Yeah, sure."
    [ 152] show nf2 1 at f31 zorder 3
    [ 153] nf2 1 "They grow up so fast. It brings a tear to my eye."
    [ 154] show nf2 at t31 zorder 2
    [ 155] show natsuki 4g at t32 zorder 2
    [ 156] "Natsuki suddenly glances in Monika's direction, prompting Monika to quickly turn away and distance herself."
    [ 157] play music "p7a" fadeout 2
    [ 158] with None
    [ 159] scene bg corridor
    [ 160] with wipeleft_scene
    [ 161] show monika 1g at f11 zorder 3
    [ 162] m "What the heck...?"
    [ 163] m "That was horrible..."
    [ 164] m "I should have said something to defend her! Why do I have to be so conflict-avoidant?"
    [ 165] m 1p "...Not that I deserve to say anything. I'm hardly better than them, after the way I treated her..."
    [ 166] m 1o "Ugh, I'm so awful... I'm not doing anything right."
    [ 167] stop music fadeout 2
    [ 168] with None
    [ 169] scene bg club_day
    [ 170] with dissolve_scene_full
    [ 171] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="bgm_lavendermist", UnlockId=1951224588 }
    [ 172] play music "p4"
    [ 173] "After school ends, Monika distractedly makes her way to the clubroom."
    [ 174] "She finds Yuri already inside, eyes on a book as usual."
    [ 175] "Monika picks a desk and slumps into it--something she seems to be doing rather often lately."
    [ 176] show monika 1g at f21 zorder 3
    [ 177] m "Yuri, I don't think I can be Club President."
    [ 178] m "I suck at handling anything that doesn't go like, exactly my way."
    [ 179] show yuri 1e at t22 zorder 2
    [ 180] "Yuri looks up from her book."
    [ 181] m 2p "It's like, the Literature Club is a place where you get to express yourself...unless it's in a way that I don't like. I'm so mad at myself."
    [ 182] m 2r "And I'm especially mad that I didn't have the self-reflection skills to realize what I was doing. So much for maturity."
    [ 183] m 2g "Sorry, I really shouldn't be complaining out loud like this. There's just like, a lot on my mind."
    [ 184] show yuri 2v at f22 zorder 3
    [ 185] y "No..."
    [ 186] m 2c "Hm?"
    [ 187] y "I enjoy listening."
    [ 188] m 2d "Really??"
    [ 189] y "Mhm."
    [ 190] m "...Why?"
    [ 191] "Yuri shrugs."
    [ 192] y 3u "It just...makes me feel nice."
    [ 193] m 1d "Oh. Well, okay...I guess I'll just continue, then."
    [ 194] "Yuri nods."
    [ 195] show yuri at thide zorder 1
    [ 196] hide yuri
    [ 197] m 1r "Yeah..."
    [ 198] m 1d "I just...well, Natsuki has kind of a blunt attitude, you know?"
    [ 199] m "It made me feel like she wasn't taking the club seriously. I couldn't even figure out why she wanted to join."
    [ 200] m 1p "I saw her friends talking to her in the hallway during lunch...and they were just so mean to her."
    [ 201] m "Telling her to grow up and stuff like that. That the Literature Club would help her grow out of her manga."
    [ 202] m 4i "It just made me so mad, like...just let her enjoy it! It makes her happy! Why are you trying to take that away from her?"
    [ 203] m 2p "And when I had that thought, it was when I came to the realization that I was...kind of doing the same thing. Just, in a roundabout way."
    [ 204] m 2g "I should have made her feel good about being passionate about something. But I just dismissed it. No, I was actually trying to avoid acknowledging it at all."
    [ 205] m 2i "I even did that with you, Yuri! When you first joined the club!"
    [ 206] show yuri 3t at f22 zorder 3
    [ 207] y "You...you did?"
    [ 208] m 1d "Yeah, I remember. Fantasy isn't really my thing, so I was kind of trying to dismiss it, but then Sayori jumped in and took over the conversation."
    [ 209] m 1m "I should have reflected on that, but I didn't, because I just let Sayori handle it instead."
    [ 210] m 1r "And now, I'm repeating the same mistake, except I really hurt someone this time."
    [ 211] "Monika shakes her head."
    [ 212] m "I'm so tired of being afraid of things I'm not comfortable with."
    [ 213] m "It's so stupid."
    [ 214] m 1g "Like...I can just picture how much joy it would bring Natsuki if I let her share her passion a little."
    [ 215] m 1i "I'm so angry that her friends were treating her like that. I'm going to get them back for it."
    [ 216] y 3f "Get them back...?"
    [ 217] m 2i "Yeah."
    [ 218] m "I'll get them back...by making sure that this is the Literature Club that Natsuki wants. Not the one that they want."
    [ 219] show yuri at thide zorder 1
    [ 220] hide yuri
    [ 221] show monika at thide zorder 1
    [ 222] hide monika
    [ 223] "Suddenly, Sayori bursts through the door, making Monika and Yuri jump."
    [ 224] "With a rare, stern face, she marches over to Monika's desk and sits down next to her."
    [ 225] show sayori 4j at f21 zorder 3
    [ 226] s "I'm having an intervention!"
    [ 227] s 1q "I can do that because I'm Vice President."
    [ 228] show monika 1a at f22 zorder 3
    [ 229] m 1d "Is this about Natsuki?"
    [ 230] s 4j "Yes!"
    [ 231] m 2p "Yeah... I know."
    [ 232] m "I messed up. I'm super sorry."
    [ 233] m "I was just talking to Yuri about it."
    [ 234] s 4m "Really??"
    [ 235] m 1g "I was so dismissive of her passion that she felt threatened, and probably just unwelcome."
    [ 236] m "Literally the opposite of what the Literature Club is supposed to be."
    [ 237] m 1r "...I really need to make it up to her."
    [ 238] s 1g "Oh."
    [ 239] s 4r "...Yay, I did it!"
    [ 240] m 2a "Ahaha. Thanks for the intervention, Sayori. I'm glad we're on the same page."
    [ 241] s 1x "Friendship wins again!"
    [ 242] s "So how do you want to make it up to her?"
    [ 243] m 2d "...I have a plan."
    [ 244] m "Sayori, do you know if Natsuki is coming to the club meeting today?"
    [ 245] s 1l "She's...I don't think she is..."
    [ 246] m 2g "I see..."
    [ 247] show sayori at thide zorder 1
    [ 248] hide sayori
    [ 249] show monika at thide zorder 1
    [ 250] hide monika
    [ 251] "Monika was afraid of that. Not because of her plan, but because she's facing the consequences of the damage that she's inadvertently caused."
    [ 252] "But the only way to do the right thing is to face it head on."
    [ 253] "It's so easy to just duck away from conflict and wait for it to blow over."
    [ 254] "But that's not enough."
    [ 255] "To truly respect someone's feelings after you've hurt them is to face them and admit your wrongdoing."
    [ 256] "Not the wrongdoing of mismanaging the club--but the wrongdoing of disrespecting Natsuki's feelings."
    [ 257] show monika 2d at f22 zorder 3
    [ 258] m "Okay. Do you think you can get her to come to the meeting tomorrow?"
    [ 259] show sayori 1a at f21 zorder 3
    [ 260] s "I can do that!"
    [ 261] m 2b "Okay, awesome."
    [ 262] m "Yuri, you don't have to worry about anything, but thank you for being my friend. You're a good listener."
    [ 263] show sayori 1a at t31 zorder 2
    [ 264] show monika 2b at t32 zorder 2
    [ 265] show yuri 4e at f44 zorder 3
    [ 266] y 4e "Mm..."
    [ 267] show yuri at thide zorder 1
    [ 268] hide yuri
    [ 269] "Fidgeting with her hair, Yuri turns away to hide a smile."
    [ 270] m 2a "Well, I guess for today, it's going to be a pretty quiet club meeting."
    [ 271] m "I'm going to step out for a bit, is that okay?"
    [ 272] s 1x "Yeah, I'm just gonna read with Yuri!"
    [ 273] s 2b "Hey, is this one of Natsuki's books? How come it's out here?"
    [ 274] "Sayori picks up a manga that was resting on an adjacent desk."
    [ 275] m 3l "Oh... That? Um, Natsuki probably just left it out by accident..."
    [ 276] s 1c "But I thought she hasn't been coming to the club...?"
    [ 277] show yuri 1h at f44 zorder 3
    [ 278] y "Actually, Monika's been--"
    [ 279] m 5a "Okay, Yuri, I'm sure it was just someone else who was using this classroom, then. Okay?"
    [ 280] y "..."
    [ 281] show monika 2j at t32 zorder 2
    [ 282] "Monika smiles at them both."
    [ 283] "Then, with a wave, she exits the clubroom."
    [ 284] stop music fadeout 2
    [ 285] with None
    [ 286] scene black
    [ 287] with Dissolve(2.0)
    [ 288] m "I really shouldn't have left that out..."
    [ 289] m "If Sayori catches on, she'll definitely tell Natsuki, and that would get really awkward..."
    [ 290] 
    [ 291] m "Now...I wonder if there's a keyboard I could borrow from the music room?"
    [ 292] with None
    [ 293] scene black
    [ 294] with Dissolve(2.0)
    [ 295] jump nm4
