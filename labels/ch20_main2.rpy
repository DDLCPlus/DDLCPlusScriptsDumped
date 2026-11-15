label ch20_main2:
    [   0] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="act_2", UnlockId=3462751114 }
    [   1] dc "Don't Skip Previous Line on AutoSave"    # say, developer commentary
    [   2] 
    [   3] play music "t2"
    [   4] "It's an ordinary school day, like any other."
    [   5] "Mornings are usually the worst, being surrounded by couples and friend groups walking to school together."
    [   6] "Meanwhile, I've always walked to school alone."
    [   7] "I always tell myself it's about time I meet some girls or something like that..."
    [   8] "But I have no motivation to join any clubs."
    [   9] "I'm perfectly content just getting by on the average while spending my free time on games and anime."
    [  10] "There's always the anime club, but it's not like there would be any girls in it anyway..."
    [  11] scene bg class_day
    [  12] with wipeleft_scene
    [  13] "The school day is as ordinary as ever, and it's over before I know it."
    [  14] "After I pack up my things, I stare blankly at the wall, looking for an ounce of motivation."
    [  15] mc "Clubs..."
    [  16] "There really aren't any that interest me."
    [  17] "Besides, most of them would probably be way too demanding for me to want to deal with."
    [  18] "I guess I have no choice but to start with the anime club..."
    [  19] 
    [  20] m "...[player]?"
    [  21] window hide(None)
    [  22] show monika g2 at t11 zorder 2
    [  23] 
    [  24] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [  25] play sound "b46c4a351da220d42a7490e9bc1cc64f"
    [  26] 
    [  27] stop sound
    [  28] hide screen tear
    [  29] call screen_tear_hide
    [  30] window show(None)
    [  31] show monika 1 at t11 zorder 2
    [  32] mc "...Monika?"
    [  33] 
    [  34] m 1b "Oh my goodness, I totally didn't expect to see you here!"
    [  35] m 5 "It's been a while, right?"
    [  36] mc "Ah..."
    [  37] mc "Yeah, it has."
    [  38] "Monika smiles sweetly."
    [  39] "We do know each other - well, we rarely talked, but we were in the same class last year."
    [  40] "Monika was probably the most popular girl in class - smart, beautiful, athletic."
    [  41] "Basically, completely out of my league."
    [  42] "So, having her smile at me so genuinely feels a little..."
    [  43] mc "What did you come in here for, anyway?"
    [  44] m 1a "Oh, I've just been looking for some supplies to use for my club."
    [  45] m 1d "Do you know if there's any construction paper in here?"
    [  46] m "Or markers?"
    [  47] mc "I guess you could check the closet."
    [  48] mc "...You're in the debate club, right?"
    [  49] m 5 "Ahaha, about that..."
    [  50] m "I actually quit the debate club."
    [  51] mc "Really? You quit?"
    [  52] m "Yeah..."
    [  53] m 2e "To be honest, I can't stand all of the politics around the major clubs."
    [  54] m "It feels like nothing but arguing about the budget and publicity and how to prepare for events..."
    [  55] m "I'd much rather take something I personally enjoy and make something special out of it."
    [  56] mc "In that case, what club did you decide to join?"
    [  57] m 1b "Actually, I'm starting a new one!"
    [  58] m "A literature club!{nw}"
    [  59] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [  60] window hide(None)
    [  61] play sound "3ef6c0e590f08b344b885117bf06f413"
    [  62] 
    [  63] stop sound
    [  64] hide screen tear
    [  65] call screen_tear_hide
    [  66] window show(None)
    [  67] m "A literature club!{fast}"
    [  68] window auto
    [  69] mc "Literature...?"
    [  70] "That sounds kind of...dull?"
    [  71] mc "How many members do you have so far?"
    [  72] m 5 "Um..."
    [  73] m "Ahaha..."
    [  74] m "It's kind of embarrassing, but there are only three of us so far."
    [  75] m "It's really hard to find new members for something that sounds so boring..."
    [  76] mc "Well, I can see that..."
    [  77] m 3d "But it's really not boring at all, you know!"
    [  78] m "Literature can be anything. Reading, writing, poetry..."
    [  79] m 3e "I mean, one of my members even keeps her manga collection in the clubroom..."
    [  80] mc "Wait...really?"
    [  81] m 2k "Yeah, it's funny, right?"
    [  82] m 2e "She always insists that manga is literature, too."
    [  83] m "I mean, she's not wrong, I guess..."
    [  84] m "And besides, a member's a member, right?"
    [  85] "...Did Monika say \"she\"?"
    [  86] "Hmm..."
    [  87] m 1a "Hey, [player]..."
    [  88] m "By any chance...are you still looking for a club to join?"
    [  89] mc "Ah--"
    [  90] mc "I mean, I guess so, but..."
    [  91] m "In that case..."
    [  92] m 5 "Is there any chance you could do me a big favor?"
    [  93] m "I won't ask you to join, but..."
    [  94] m "If you could at the very least visit my club, it would make me really happy."
    [  95] m "Please?"
    [  96] mc "Um..."
    [  97] "Well, I guess I have no reason to refuse..."
    [  98] "Besides, how could I ever refuse someone like Monika?"
    [  99] mc "Sure, I guess I could check it out."
    [ 100] m 1k "Aah, awesome!"
    [ 101] m 1b "You're really sweet, [player], you know that?"
    [ 102] mc "I-It's nothing, really..."
    [ 103] m 1a "Shall we go, then?"
    [ 104] m "I'll look for the materials another time - you're more important."
    [ 105] stop music fadeout 2
    [ 106] scene bg corridor
    [ 107] with wipeleft_scene
    [ 108] "And thus, today marks the day I sold my soul to Monika and her irresistible smile."
    [ 109] "I dejectedly follow Monika across the school and upstairs - a section of the school I rarely visit."
    [ 110] "Monika, full of energy, swings open the classroom door."
    [ 111] scene bg club_day2
    [ 112] with wipeleft
    [ 113] play music "t3"
    [ 114] unless renpy.random.randint(0, 2) == 0 goto [117]
    [ 115] show monika g1 at l31
    [ 116] goto [118]
    [ 117] show monika 3b at l31
    [ 118] pass
    [ 119] m "I'm back~!"
    [ 120] m "And I brought a guest with me!"
    [ 121] show yuri 2t at t33 zorder 2
    [ 122] unless not config.skipping goto [125]
    [ 123] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [ 124] goto [125]
    [ 125] pass
    [ 126] y "Eh?"
    [ 127] y "A...a guest?"
    [ 128] show natsuki 4c at t32 zorder 2
    [ 129] n "Seriously? You brought a boy?"
    [ 130] n "Way to kill the atmosphere."
    [ 131] show monika 3m at f31 zorder 3
    [ 132] m "Don't be mean, Natsuki..."
    [ 133] m 3b "...But anyway, welcome to the club, [player]!"
    [ 134] show monika 3a at t31 zorder 2
    [ 135] mc "..."
    [ 136] "All words escape me in this situation."
    [ 137] "This club..."
    [ 138] "<i>...is full of incredibly cute girls!!</i>"
    [ 139] show natsuki at f32 zorder 3
    [ 140] n 5c "So, let me guess..."
    [ 141] n "You're Monika's boyfriend, right?"
    [ 142] show natsuki at t32 zorder 2
    [ 143] mc "Wha--"
    [ 144] mc "No, I'm not!"
    [ 145] show yuri at f33 zorder 3
    [ 146] y 2l "Natsuki..."
    [ 147] 
    [ 148] "The girl with the sour attitude, whose name is apparently Natsuki, is one I don't recognize."
    [ 149] "Her small figure makes her look like a first-year student."
    [ 150] show yuri at t33 zorder 2
    [ 151] show monika at f31 zorder 3
    [ 152] m 2l "A-Anyway, this is Natsuki, energetic as usual..."
    [ 153] m 2b "And this is Yuri, the Vice President!"
    [ 154] 
    [ 155] show monika 2a at t31 zorder 2
    [ 156] show yuri at f33 zorder 3
    [ 157] y 4 "I-It's nice to meet you..."
    [ 158] "Yuri, who appears comparably more mature and timid, seems to have a hard time keeping up with someone like Natsuki."
    [ 159] show yuri at t33 zorder 2
    [ 160] mc "Yeah... It's nice to meet both of you."
    [ 161] show monika at f31 zorder 3
    [ 162] m 1a "So, I ran into [player] in a classroom, and he decided to come check out the club."
    [ 163] m "Isn't that great?"
    [ 164] show monika at t31 zorder 2
    [ 165] show natsuki at f32 zorder 3
    [ 166] n 4e "Wait! Monika!"
    [ 167] n "Didn't I tell you to let me know in advance before you brought anyone new?"
    [ 168] n 4q "I was going to...well, you know..."
    [ 169] show natsuki at t32 zorder 2
    [ 170] show monika at f31 zorder 3
    [ 171] m 1e "Sorry, sorry!"
    [ 172] m "I didn't forget that, but I just happened to run into him."
    [ 173] show monika at t31 zorder 2
    [ 174] show yuri at f33 zorder 3
    [ 175] y 1a "In that case, I should at least make some tea, right?"
    [ 176] show yuri at t33 zorder 2
    [ 177] show monika at f31 zorder 3
    [ 178] m 1b "Yeah, that would be great!"
    [ 179] m "Why don't you come sit down, [player]?"
    [ 180] hide monika
    [ 181] hide natsuki
    [ 182] hide yuri
    [ 183] with wipeleft
    [ 184] "The girls have a few desks arranged to form a table."
    [ 185] "Yuri walks to the corner of the room and opens the closet."
    [ 186] "Meanwhile, Monika and Natsuki sit across from each other."
    [ 187] "Still feeling awkward, I take a seat next to Monika."
    [ 188] show monika 1a at t11 zorder 2
    [ 189] m "So, I know you didn't really plan on coming here..."
    [ 190] m "But we'll make sure you feel right at home, okay?"
    [ 191] m 1j "As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!"
    [ 192] mc "I'm surprised there aren't more people in the club yet."
    [ 193] mc "It must be hard to start a new club."
    [ 194] m 3b "You could put it that way."
    [ 195] m "Not many people are very interested in putting out all the effort to start something brand new..."
    [ 196] m "Especially when it's something that doesn't grab your attention, like literature."
    [ 197] m "You have to work hard to convince people that you're both fun and worthwhile."
    [ 198] m "But it makes school events, like the festival, that much more important."
    [ 199] m 2k "I'm confident that we can all really grow this club before we graduate!"
    [ 200] m "Right, Natsuki?"
    [ 201] show monika at t22 zorder 2
    [ 202] show natsuki 4q at t21 zorder 2
    [ 203] n "Well..."
    [ 204] n "...I guess."
    [ 205] "Natsuki reluctantly agrees."
    [ 206] "Such different girls, all interested in the same goal..."
    [ 207] "Monika must have worked really hard just to find these two."
    [ 208] "Yuri returns to the table, carrying a tea set."
    [ 209] "She carefully places a teacup in front of each of us before setting down the teapot in the middle."
    [ 210] show natsuki at thide zorder 1
    [ 211] show monika at thide zorder 1
    [ 212] hide natsuki
    [ 213] hide monika
    [ 214] show yuri 1a at t21 zorder 2
    [ 215] mc "You keep a whole tea set in this classroom?"
    [ 216] y "Don't worry, the teachers gave us permission."
    [ 217] y "After all, doesn't a hot cup of tea help you enjoy a good book?"
    [ 218] mc "Ah... I-I guess..."
    [ 219] show monika 4a at f22 zorder 3
    [ 220] m "Ehehe, don't let yourself get intimidated, Yuri's just trying to impress you."
    [ 221] show monika at t22 zorder 2
    [ 222] show yuri at hf21
    [ 223] y 3n "Eh?! T-That's not..."
    [ 224] "Insulted, Yuri looks away."
    [ 225] y 4b "I meant that, you know..."
    [ 226] show yuri at t21 zorder 2
    [ 227] mc "I believe you."
    [ 228] mc "Well, tea and reading might not be a pastime for me, but I at least enjoy tea."
    [ 229] show yuri at f21 zorder 3
    [ 230] y 2u "I'm glad..."
    [ 231] show yuri at t21 zorder 2
    [ 232] "Yuri faintly smiles to herself in relief."
    [ 233] show monika at thide zorder 1
    [ 234] hide monika
    [ 235] show yuri 1a at t32 zorder 2
    [ 236] y "So, [player], what kinds of things do you like to read?"
    [ 237] mc "Well... Ah..."
    [ 238] "Considering how little I've read these past few years, I don't really have a good way of answering that."
    [ 239] mc "...Manga..."
    [ 240] "I mutter quietly to myself, half-joking."
    [ 241] show natsuki 1c at t41 zorder 2
    [ 242] "Natsuki's head suddenly perks up."
    [ 243] "It looks like she wants to say something, but she keeps quiet."
    [ 244] show natsuki at thide zorder 1
    [ 245] hide natsuki
    [ 246] y 3u "N-Not much of a reader, I guess..."
    [ 247] mc "...Well, that can change..."
    [ 248] "What am I saying?"
    [ 249] "I spoke without thinking after seeing Yuri's sad smile."
    [ 250] mc "Anyway, what about you, Yuri?"
    [ 251] y 1l "Well, let's see..."
    [ 252] "Yuri traces the rim of her teacup with her finger."
    [ 253] y 1a "My favorites are usually novels that build deep and complex fantasy worlds."
    [ 254] y "The level of creativity and craftsmanship behind them is amazing to me."
    [ 255] y 1f "And telling a good story in such a foreign world is equally impressive."
    [ 256] "Yuri goes on, clearly passionate about her reading."
    [ 257] "She seemed so reserved and timid since the moment I walked in, but it's obvious by the way her eyes light up that she finds her comfort in the world of books, not people."
    [ 258] y 2m "But you know, I like a lot of things."
    [ 259] y "Stories with deep psychological elements usually immerse me as well."
    [ 260] y 2a "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?"
    [ 261] y "Anyway, I've been reading a lot of horror lately..."
    [ 262] mc "Ah, I read a horror book once..."
    [ 263] "I desperately grasp something I can relate to at the minimal level."
    [ 264] "At this rate, Yuri might as well be having a conversation with a rock."
    [ 265] show monika 1j at f33 zorder 3
    [ 266] m "Ahaha. I'd expect that from you, Yuri."
    [ 267] m 1a "It suits your personality."
    [ 268] show monika at t33 zorder 2
    [ 269] show yuri at f32 zorder 3
    [ 270] y 1a "Oh, is that so?"
    [ 271] y "Really, if a story makes me think, or takes me to another world, then I really can't put it down."
    [ 272] y "Surreal horror is often very successful at changing the way you look at the world, if only for a brief moment."
    [ 273] show yuri at t32 zorder 2
    [ 274] show natsuki 5q at f31 zorder 3
    [ 275] n "Ugh, I hate horror..."
    [ 276] show natsuki at t31 zorder 2
    [ 277] show yuri at f32 zorder 3
    [ 278] y 1f "Oh? Why's that?"
    [ 279] show yuri at t32 zorder 2
    [ 280] show natsuki at f31 zorder 3
    [ 281] n 5c "Well, I just..."
    [ 282] "Natsuki's eyes dart over to me for a split second."
    [ 283] n 5q "Never mind."
    [ 284] show natsuki at t31 zorder 2
    [ 285] show monika at f33 zorder 3
    [ 286] m 1a "That's right, you usually like to write about cute things, don't you, Natsuki?"
    [ 287] show monika at t33 zorder 2
    [ 288] show natsuki 1o at f31 zorder 3
    [ 289] n "W-What?"
    [ 290] n "What gives you that idea?"
    [ 291] show natsuki at t31 zorder 2
    [ 292] show monika at f33 zorder 3
    [ 293] m 3b "You left a piece of scrap paper behind last club meeting."
    [ 294] m "It looked like you were working on a poem called--"
    [ 295] show monika at t33 zorder 2
    [ 296] show natsuki 1p at f31 zorder 3
    [ 297] n "Don't say it out loud!!"
    [ 298] n "And give that back!"
    [ 299] show natsuki at t31 zorder 2
    [ 300] show monika at f33 zorder 3
    [ 301] m 1j "Fine, fine~"
    [ 302] show monika 1a at t33 zorder 2
    [ 303] mc "Natsuki, you write your own poems?"
    [ 304] show natsuki at f31 zorder 3
    [ 305] n 1c "Eh? Well, I guess sometimes."
    [ 306] n "Why do you care?"
    [ 307] show natsuki at t31 zorder 2
    [ 308] mc "I think that's impressive."
    [ 309] mc "Why don't you share them sometime?"
    [ 310] show natsuki at f31 zorder 3
    [ 311] n 5q "N-No!"
    [ 312] "Natsuki averts her eyes."
    [ 313] n "You wouldn't...like them..."
    [ 314] show natsuki at t31 zorder 2
    [ 315] mc "Ah...not a very confident writer yet?"
    [ 316] show yuri at f32 zorder 3
    [ 317] y 2f "I understand how Natsuki feels."
    [ 318] y "Sharing that level of writing takes more than just confidence."
    [ 319] y 2k "The truest form of writing is writing to oneself."
    [ 320] y "You must be willing to open up to your readers, exposing your vulnerabilities and showing even the deepest reaches of your heart."
    [ 321] show yuri at t32 zorder 2
    [ 322] show monika 2a at f33 zorder 3
    [ 323] m "Do you have writing experience too, Yuri?"
    [ 324] m "Maybe if you share some of your work, you can set an example and help Natsuki feel comfortable enough to share hers."
    [ 325] show yuri at s32
    [ 326] y 3o "..."
    [ 327] mc "I guess it's the same for Yuri..."
    [ 328] "We all sit in silence for a moment."
    [ 329] show monika at f33 zorder 3
    [ 330] m 5a "Hey, I just got an idea!"
    [ 331] m "How about this?"
    [ 332] show monika at t33 zorder 2
    [ 333] show natsuki 2k at f31 zorder 3
    [ 334] show yuri 3e at f32 zorder 3
    [ 335] ny "...?"
    [ 336] "Natsuki and Yuri look quizzically at Monika."
    [ 337] show natsuki at t31 zorder 2
    [ 338] show yuri at t32 zorder 2
    [ 339] show monika at f33 zorder 3
    [ 340] m 2b "Let's all go home and write a poem of our own!"
    [ 341] m "Then, next time we meet, we'll all share them with each other."
    [ 342] m "That way, everyone is even!"
    [ 343] show monika 2a at t33 zorder 2
    [ 344] show natsuki at f31 zorder 3
    [ 345] n 5q "U-Um..."
    [ 346] show natsuki at t31 zorder 2
    [ 347] show yuri 3v at f32 zorder 3
    [ 348] y "..."
    [ 349] show yuri at t32 zorder 2
    [ 350] show monika 2m at f33 zorder 3
    [ 351] m "Ah..."
    [ 352] m "I mean, I thought it was a good idea..."
    [ 353] show monika at t33 zorder 2
    [ 354] show yuri at f32 zorder 3
    [ 355] y 2l "Well..."
    [ 356] y "...I think you're right, Monika."
    [ 357] y 2f "We should probably start finding activities for all of us to participate in together."
    [ 358] y 2h "I did decide to take on the responsibility of Vice President, after all..."
    [ 359] y "I need to do my best to nurture the club as well as its members."
    [ 360] y 2a "Besides, now that we have a new member..."
    [ 361] y "It seems like a good step for us to take."
    [ 362] y "Do you agree as well, [player]?"
    [ 363] show yuri at t32 zorder 2
    [ 364] mc "Hold on...there's still one problem."
    [ 365] show monika at f33 zorder 3
    [ 366] m 1d "Eh? What's that?"
    [ 367] "Now that we've reached the most important topic, I bluntly come forth with what's been on my mind the entire time."
    [ 368] show monika at t33 zorder 2
    [ 369] mc "I never said I would join this club!"
    [ 370] mc "Monika may have convinced me to stop by, but I never made any decision."
    [ 371] mc "I still have other clubs to look at, and...um..."
    [ 372] show monika 1g
    [ 373] show natsuki 4g
    [ 374] show yuri 2e
    [ 375] "I lose my train of thought."
    [ 376] "All three girls stare back at me with dejected eyes."
    [ 377] show monika at s33
    [ 378] m 1p "B-But..."
    [ 379] show yuri at s32
    [ 380] y 2v "I'm sorry, I thought..."
    [ 381] show natsuki at s31
    [ 382] n 5s "Hmph."
    [ 383] mc "Eh...?"
    [ 384] "The girls exchange glances before Monika turns back to me."
    [ 385] show monika at f33 zorder 3
    [ 386] m 1m "I...guess I need to tell you the truth, [player]."
    [ 387] m "The thing is..."
    [ 388] m 1p "...We don't have enough members yet to form an official club."
    [ 389] m "We need four..."
    [ 390] m "And I've been trying really, really hard to find new members."
    [ 391] m "And if we don't find one more before the festival..."
    [ 392] show monika at t33 zorder 2
    [ 393] mc "..."
    [ 394] "I...I'm defenseless against these girls."
    [ 395] "How am I supposed to make a clear-headed decision when it's like this?"
    [ 396] "I would feel terrible for letting everyone down in this situation..."
    [ 397] "And besides, the club itself seems pretty relaxed..."
    [ 398] "So, if writing poems is the price I need to pay in order to spend every day with these beautiful girls..."
    [ 399] mc "...Right."
    [ 400] mc "Okay, I've decided, then."
    [ 401] mc "I'll join the Literature Club."
    [ 402] show monika 1e at t33 zorder 2
    [ 403] show yuri 3f at t32 zorder 2
    [ 404] show natsuki 1k at t31 zorder 2
    [ 405] "One by one, the girls' eyes light up."
    [ 406] show monika at f33 zorder 3
    [ 407] m "Oh my goodness, really?"
    [ 408] m "Do you really mean that, [player]?"
    [ 409] show monika at t33 zorder 2
    [ 410] mc "Yeah..."
    [ 411] mc "It could be fun, right?"
    [ 412] show yuri at f32 zorder 3
    [ 413] y 1m "You really did scare me for a moment..."
    [ 414] show yuri at t32 zorder 2
    [ 415] show natsuki at f31 zorder 3
    [ 416] n 5q "I mean, if you really just left after all this, I would be super pissed."
    [ 417] show natsuki at t31 zorder 2
    [ 418] show monika at f33 zorder 3
    [ 419] m "[player], I'm so happy..."
    [ 420] m 1k "We can become an official club now!"
    [ 421] m 1e "Thank you so much for this. You're really amazing."
    [ 422] m "I'll do everything I can to give you a great time, okay?"
    [ 423] show monika at t33 zorder 2
    [ 424] mc "Ah...thanks, I guess."
    [ 425] show yuri at thide zorder 1
    [ 426] show natsuki at thide zorder 1
    [ 427] show monika at t11 zorder 2
    [ 428] hide yuri
    [ 429] hide natsuki
    [ 430] m 3b "Okay, everyone!"
    [ 431] m "I think with that, we can officially end today's meeting on a good note."
    [ 432] m "Everyone remember tonight's assignment:"
    [ 433] m "Write a poem to bring to the next meeting, so we can all share!"
    [ 434] "Monika looks over at me once more."
    [ 435] m 1a "[player], I look forward to seeing how you express yourself."
    [ 436] show monika 5 at hop
    [ 437] m "Ehehe~"
    [ 438] mc "Y-Yeah..."
    [ 439] show monika at thide zorder 1
    [ 440] hide monika
    [ 441] "Can I really impress the class star Monika with my mediocre writing skills?"
    [ 442] "I already feel the anxiety welling up inside me."
    [ 443] "Meanwhile, the girls continue to chit-chat as Yuri cleans up the tea set."
    [ 444] mc "I guess I'll be on my way, then..."
    [ 445] show monika 5a at t11 zorder 2
    [ 446] m "Okay!"
    [ 447] m "I'll see you tomorrow, then."
    [ 448] m "I can't wait!"
    [ 449] scene bg residential_day
    [ 450] with wipeleft_scene
    [ 451] "With that, I depart the clubroom and make my way home."
    [ 452] "The whole way, my mind wanders back and forth between the three girls:"
    [ 453] show natsuki 4a at t31 zorder 2
    [ 454] "Natsuki,"
    [ 455] show yuri 1a at t32 zorder 2
    [ 456] "Yuri,"
    [ 457] show monika 1a at t33 zorder 2
    [ 458] "and, of course, Monika."
    [ 459] "Will I really be happy spending every day after school in a literature club?"
    [ 460] "Perhaps I'll have the chance to grow closer to one of these girls..."
    [ 461] hide natsuki
    [ 462] hide yuri
    [ 463] hide monika
    [ 464] with wipeleft
    [ 465] "Alright!"
    [ 466] "I'll just need to make the most of my circumstances, and I'm sure good fortune will find me."
    [ 467] "And I guess that starts with writing a poem tonight..."
    [ 468] stop music fadeout 2
    [ 469] with None
    [ 470] scene black
    [ 471] with dissolve_scene_full
    [ 472] 
    [ 473] 
    [ 474] 
    [ 475] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=False }
    [ 476] # WindowAuto: WindowAuto { show=False, command="call screen" }
    [ 477] # WaitForScreen: WaitForScreen { screen="confirm" }
    [ 478] unless _return goto [481]
    [ 479] call expression <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction], constantFloats=[0, 1], constantStrings=["poem_special_", "persistent", "special_poems", "str"], constantObjects=[] }>
    [ 480] goto [482]
    [ 481] pass
    [ 482] pass
    [ 483] return
