label ch40_main:
    # nested label ch40_clearnormal starts at [417]
    # nested label ch40_clearall starts at [515]
    [   0] 
    [   1] 
    [   2] stop music fadeout 2
    [   3] scene bg residential_day
    [   4] with dissolve_scene_full
    [   5] python:    # runs C# ch40_main_inlinepythonblock_336172819
                
    [   6] 
    [   7] play music "t2"
    [   8] dc "Don't Skip Previous Line on AutoSave"    # say, developer commentary
    [   9] 
    [  10] "It's an ordinary school day, like any other."
    [  11] "As usual, I'm surrounded by couples and friend groups walking to school together."
    [  12] "I always tell myself it's about time I meet some girls or something like that..."
    [  13] show sayori 1a at t11
    [  14] s "Hey, [player]..."
    [  15] "...Well, there already is one girl."
    [  16] "That girl is Sayori, my neighbor and good friend since we were children."
    [  17] "We used to walk to school together every day..."
    [  18] "...And recently, we've picked up that habit once again."
    [  19] s "[player], are you proud of me?"
    [  20] mc "Eh? For what?"
    [  21] s 1c "You know..."
    [  22] s "For waking up on time!"
    [  23] mc "Well, you've been doing that for a while now..."
    [  24] s "Uh-huh!"
    [  25] s 4h "But you never even said anything about it!"
    [  26] show sayori at s11
    [  27] s "Even though we walk to school together every day..."
    [  28] mc "Well, yeah..."
    [  29] mc "I always thought it was implied."
    [  30] mc "It's embarrassing to say out loud."
    [  31] s 1d "C'mon, please?"
    [  32] s "It's good motivation~"
    [  33] mc "Fine, fine..."
    [  34] mc "I'm proud of you, Sayori."
    [  35] show sayori at t11
    [  36] s 1q "Ehehe~"
    [  37] show sayori at thide zorder 1
    [  38] hide sayori
    [  39] "We cross the street together and make our way to school."
    [  40] "As we draw near, the streets become increasingly speckled with other students making their daily commute."
    [  41] show sayori 3a at t11 zorder 2
    [  42] s "By the way, [player]..."
    [  43] s "Have you decided on a club to join yet?"
    [  44] mc "A club?"
    [  45] mc "I told you already, I'm really not--"
    [  46] "I start to say what I always do - that I'm not interested in joining any clubs."
    [  47] "But something tells me Sayori would take more offense to that now."
    [  48] "After all, how could I tell her that clubs are a waste of time..."
    [  49] "...when she's starting a club of her very own?"
    [  50] mc "...Actually, yeah."
    [  51] mc "I think I've decided on a club."
    [  52] show sayori at h11
    [  53] s 1m "Really?!"
    [  54] s 1r "Which one? Tell me!"
    [  55] mc "Hmm..."
    [  56] mc "I think I'll keep it a surprise."
    [  57] s 5d "Boo..."
    [  58] s "You meanie."
    [  59] mc "Be patient, you'll find out soon enough."
    [  60] "I used to ask myself why I let myself get lectured by such a carefree girl."
    [  61] "But I started to realize that in a way, I envy her."
    [  62] "When Sayori puts her mind to something, she can accomplish great things."
    [  63] "So that's why I feel like I should do something special for her."
    [  64] scene bg class_day
    [  65] with wipeleft_scene
    [  66] "The school day is as ordinary as ever, and it's over before I know it."
    [  67] "After I pack up my things, I stand up, gathering my motivation."
    [  68] mc "Let's see..."
    [  69] stop music fadeout 2
    [  70] scene bg corridor
    [  71] with wipeleft_scene
    [  72] "I recall the room number of the club from a flier I saw."
    [  73] "I walk across the school and upstairs - a section of the school I rarely visit."
    [  74] "Before long, I find the room."
    [  75] "I timidly open the door in front of me."
    [  76] scene bg club_day
    [  77] with wipeleft
    [  78] play music "t3"
    [  79] mc "Hello...?"
    [  80] show sayori 1m at t32
    [  81] s "Ah!"
    [  82] s "[player]...?!"
    [  83] s 1c "W-What are you doing here?"
    [  84] mc "Well...I just--"
    [  85] "Eh? I glance around the room."
    [  86] show natsuki 3a at f31
    [  87] n "Huh."
    [  88] n "So you're the [player] that Sayori's always talking about?"
    [  89] show natsuki at t31
    [  90] show yuri 2t at f33
    [  91] y "T-Thank you for stopping by!"
    [  92] y 2m "It's a pleasure to meet you, [player]."
    [  93] y "We're the Literature Club."
    [  94] y 3v "I-I hope you enjoy your visit!"
    [  95] show yuri at t33
    [  96] show natsuki at f31
    [  97] n 3g "C'mon, Yuri..."
    [  98] n "No need to be so formal."
    [  99] n "He's gonna think we're really strict or something..."
    [ 100] show natsuki at t31
    [ 101] 
    [ 102] 
    [ 103] show yuri at f33
    [ 104] y 3q "Ah..."
    [ 105] y "Sorry, Natsuki..."
    [ 106] show yuri at t33
    [ 107] "The tall one, whose name is apparently Yuri, seems to be quite shy compared to the others."
    [ 108] "In comparison, the girl named Natsuki - despite her size - seems like the assertive one."
    [ 109] mc "Well, it's nice to meet both of you."
    [ 110] mc "I look forward to working with you."
    [ 111] show sayori at f32
    [ 112] s 1n "W-Working...?"
    [ 113] s 1b "[player], don't tell me..."
    [ 114] s "You're..."
    [ 115] show sayori at t32
    [ 116] mc "That's right."
    [ 117] mc "The club I've decided to join is yours, Sayori."
    [ 118] mc "The Literature Club."
    [ 119] "Sayori's eyes light up."
    [ 120] show sayori at f32
    [ 121] s 1n "...No way."
    [ 122] s 1s "No way!"
    [ 123] show sayori at hf32
    [ 124] s 4s "Aaaahhhhhh!"
    [ 125] "Sayori wraps her arms around me, jumping up and down."
    [ 126] show sayori at t32
    [ 127] mc "H-Hey--"
    [ 128] show natsuki at f31
    [ 129] n 3y "Ehehe."
    [ 130] n "Well, if Sayori is this happy, then I'm sure it won't be so bad to have you around."
    [ 131] show natsuki 3a at t31
    [ 132] show yuri at f33
    [ 133] y 1s "Not to mention there's four of us now."
    [ 134] y "That means we can become an officially-recognized club."
    [ 135] show yuri at t33
    [ 136] show sayori at f32
    [ 137] s 1x "I don't know what to say!"
    [ 138] s "We have to celebrate!"
    [ 139] show sayori at t32
    [ 140] show yuri at f33
    [ 141] y 1m "Huhu."
    [ 142] y "What an appropriate day for that, isn't it?"
    [ 143] show yuri 1a at t33
    [ 144] show sayori at f32
    [ 145] s 1r "Yeah!"
    [ 146] s 1x "After all, Natsuki decided to--"
    [ 147] show sayori at t32
    [ 148] show natsuki at f31
    [ 149] n 1w "Hey, don't ruin the surprise!"
    [ 150] show natsuki at t31
    [ 151] show sayori at f32
    [ 152] s 5a "Ehehe, sorry..."
    [ 153] show sayori at t32
    [ 154] show natsuki at f31
    [ 155] n 1k "Everyone sit down at the table, okay?"
    [ 156] show natsuki at t31
    [ 157] show yuri at f33
    [ 158] y 1a "How about I make some tea as well?"
    [ 159] hide sayori
    [ 160] hide natsuki
    [ 161] hide yuri
    [ 162] with wipeleft
    [ 163] "The girls have a few desks arranged to form a table."
    [ 164] "Natsuki and Yuri walk over to the corner of the room, where Natsuki grabs a wrapped tray and Yuri opens the closet."
    [ 165] "Still feeling awkward, I take a seat next to Sayori."
    [ 166] "Natsuki proudly marches back to the table, tray in hand."
    [ 167] show natsuki 2z at t22 zorder 2
    [ 168] n "Okaaay, are you ready?"
    [ 169] n "...Ta-daa!"
    [ 170] show sayori 4m at t21 zorder 2
    [ 171] s "Uwooooah!"
    [ 172] "Natsuki lifts the foil off the tray to reveal a dozen white, fluffy cupcakes decorated to look like little cats."
    [ 173] "The whiskers are drawn with icing, and little pieces of chocolate were used to make ears."
    [ 174] show sayori at f21
    [ 175] s 4r "So cuuuute~!"
    [ 176] show sayori at t21
    [ 177] mc "Wow, those look amazing."
    [ 178] show natsuki at f22
    [ 179] n 2d "Ehehe. Well, you know."
    [ 180] n "Just hurry and take one!"
    [ 181] show natsuki at t22
    [ 182] "Sayori grabs one first, then I follow."
    [ 183] show sayori at f21
    [ 184] s 4q "It's delicious!"
    [ 185] show sayori at t21
    [ 186] "Sayori talks with her mouth full and has already managed to get icing on her face."
    [ 187] "I turn the cupcake around in my fingers, looking for the best angle to take a bite."
    [ 188] show sayori at thide zorder 1
    [ 189] hide sayori
    [ 190] show natsuki 1c at t32 zorder 2
    [ 191] "Natsuki is quiet."
    [ 192] "I can't help but notice her sneaking glances in my direction."
    [ 193] "Is she waiting for me to take a bite?"
    [ 194] "I finally bite down."
    [ 195] "The icing is sweet and full of flavor - I wonder if she made it herself."
    [ 196] mc "This is really good."
    [ 197] mc "Thank you, Natsuki."
    [ 198] n 42c "W-Well...of course it is!"
    [ 199] n "I'm a pro, after all!"
    [ 200] n 42a "There's no need to thank me or anything..."
    [ 201] show natsuki at thide zorder 1
    [ 202] hide natsuki
    [ 203] "As Natsuki struggles to accept the compliment, Yuri returns to the table, carrying a tea set."
    [ 204] "She carefully places a teacup in front of each of us before setting down the teapot next to the cupcake tray."
    [ 205] show yuri 1a at t11 zorder 2
    [ 206] mc "You keep a whole tea set in this classroom?"
    [ 207] y "Don't worry, the teachers gave us permission."
    [ 208] y "After all, doesn't a hot cup of tea help you enjoy a good book?"
    [ 209] mc "Ah... I-I guess..."
    [ 210] show natsuki 2y at f31
    [ 211] n "Ehehe. Already trying to impress our new member, Yuri?"
    [ 212] show natsuki at t31
    [ 213] show yuri at f11
    [ 214] y 3n "Eh?! T-That's not..."
    [ 215] show yuri at t11
    [ 216] show natsuki at thide
    [ 217] hide natsuki
    [ 218] "Insulted, Yuri looks away."
    [ 219] y 4b "I meant that, you know..."
    [ 220] mc "I believe you."
    [ 221] mc "Well, tea and reading might not be a pastime for me, but I at least enjoy tea."
    [ 222] y 2u "I'm glad..."
    [ 223] "Yuri faintly smiles to herself in relief."
    [ 224] y 1a "So, [player], what kinds of things do you like to read?"
    [ 225] mc "Well... Ah..."
    [ 226] "Considering how little I've read these past few years, I don't really have a good way of answering that."
    [ 227] mc "...Manga..."
    [ 228] "I mutter quietly to myself, half-joking."
    [ 229] show natsuki 1c at t41 zorder 2
    [ 230] "Natsuki's head suddenly perks up."
    [ 231] "It looks like she wants to say something, but she keeps quiet."
    [ 232] show natsuki at thide zorder 1
    [ 233] hide natsuki
    [ 234] y 3u "N-Not much of a reader, I guess..."
    [ 235] mc "...Well, that can change..."
    [ 236] "What am I saying?"
    [ 237] "I spoke without thinking after seeing Yuri's sad smile."
    [ 238] mc "Anyway, what about you, Yuri?"
    [ 239] y 1l "Well, let's see..."
    [ 240] "Yuri traces the rim of her teacup with her finger."
    [ 241] y 1a "My favorites are usually novels that build deep and complex fantasy worlds."
    [ 242] y "The level of creativity and craftsmanship behind them is amazing to me."
    [ 243] y 1f "And telling a good story in such a foreign world is equally impressive."
    [ 244] "Yuri goes on, clearly passionate about her reading."
    [ 245] "She seemed so reserved and timid since the moment I walked in, but it's obvious by the way her eyes light up that she finds her comfort in the world of books, not people."
    [ 246] y 2m "But you know, I like a lot of things."
    [ 247] y 2a "Don't feel intimidated if you don't read much, okay?"
    [ 248] y "I'm certain we can find something that we have in common."
    [ 249] show yuri at t22
    [ 250] show natsuki 2c at f21
    [ 251] n "Hey, Yuri..."
    [ 252] show natsuki at t21
    [ 253] show yuri at f22
    [ 254] y 2f "Eh?"
    [ 255] show yuri at t22
    [ 256] show natsuki at f21
    [ 257] n 2h "Well, about...you know, the first thing he said..."
    [ 258] show natsuki at t21
    [ 259] mc "Manga?"
    [ 260] show yuri at f22
    [ 261] y 2i "That's right..."
    [ 262] y "Natsuki tends to read manga in the clubroom--"
    [ 263] show yuri at t22
    [ 264] show natsuki at f21
    [ 265] n 1r "D-Don't just say it!!"
    [ 266] "For some reason, Natsuki seems embarrassed about it."
    [ 267] n 1q "Besides..."
    [ 268] n "Manga...is literature too, you know?"
    [ 269] n 1w "So...if [player] wants to read some of my manga, then don't try to stop him or anything!"
    [ 270] show natsuki 1i at t21
    [ 271] show yuri at f22
    [ 272] y 1l "Natsuki..."
    [ 273] y "I wouldn't do such a thing."
    [ 274] y 1i "However, it could also be nice for us to diversify ourselves a little..."
    [ 275] y "He can take this opportunity to try something new, as well."
    [ 276] y 1s "Wouldn't you agree, [player]?"
    [ 277] show yuri at t33
    [ 278] show natsuki at t32
    [ 279] show sayori 1l at f31
    [ 280] s "M-Maybe--"
    [ 281] "Sensing the tension, Sayori jumps in."
    [ 282] s 1x "Maybe we can all try something new!"
    [ 283] s 1l "I think it could be fun..."
    [ 284] s 1c "And we'll all get to know each other a little bit better, too!"
    [ 285] s 1l "I mean..."
    [ 286] s "That's the kind of thing literature clubs do...right?"
    [ 287] show sayori at t31
    [ 288] show yuri at f33
    [ 289] y 1v "..."
    [ 290] y "I-I don't disagree or anything..."
    [ 291] show yuri at t33
    [ 292] show natsuki at f32
    [ 293] n 2j "Yeah..."
    [ 294] n "You're right as usual, President."
    [ 295] show natsuki at t32
    [ 296] show sayori at f31
    [ 297] s 1q "Ehehe~"
    [ 298] show sayori at t31
    [ 299] show natsuki at f32
    [ 300] n 2c "Guess that means I should try picking up a novel or something, huh...?"
    [ 301] show natsuki at t32
    [ 302] mc "Well, that would make two of us..."
    [ 303] mc "I wouldn't mind doing it if I'm not the only one."
    [ 304] show sayori at thide
    [ 305] hide sayori
    [ 306] show natsuki at f21
    [ 307] show yuri at t22
    [ 308] n 2y "Then as for Yuri..."
    [ 309] show natsuki at t21
    [ 310] show yuri at f22
    [ 311] y 2n "Eh...?"
    [ 312] y "I...I have to read manga...?"
    [ 313] show yuri at t22
    [ 314] show natsuki at f21
    [ 315] n 4i "Jeez..."
    [ 316] n 4h "You were the one who suggested we diversify!"
    [ 317] n "You should be a little more open-minded..."
    [ 318] n 4u "It's kind of hurtful..."
    [ 319] show natsuki at t21
    [ 320] show yuri at f22
    [ 321] y 2t "Hurtful...?"
    [ 322] y 2v "I-I didn't realize..."
    [ 323] y "..."
    [ 324] "With a guilty expression, Yuri thinks to herself."
    [ 325] y 2w "I'm sorry for disrespecting your interests, Natsuki."
    [ 326] y "If...if you're into it, then I'm sure it's a worthy form of literature."
    [ 327] show yuri at t22
    [ 328] show natsuki at f21
    [ 329] n 5q "...Are you just saying that?"
    [ 330] show natsuki at t21
    [ 331] show yuri at f22
    [ 332] y "No..."
    [ 333] y "I've realized my error."
    [ 334] y 2t "So, if you're willing to consider starting a novel..."
    [ 335] y 2u "...Then I'll offer my gratitude by finding a manga to read as well."
    [ 336] show yuri at t22
    [ 337] show natsuki at f21
    [ 338] n 1l "Really?!"
    [ 339] n 12c "I-I mean..."
    [ 340] n "It...makes me happy that you'd do that for me, Yuri."
    [ 341] n 2c "You can trust me to find something that you'll really like, okay?"
    [ 342] show natsuki at t21
    [ 343] show yuri at f22
    [ 344] y 1m "Same here..."
    [ 345] y 1h "Perhaps I'll visit the bookstore after the club meeting."
    [ 346] show yuri at t22
    [ 347] show natsuki at f21
    [ 348] n 1q "Just...just you?"
    [ 349] show natsuki at t21
    [ 350] show yuri at f22
    [ 351] y 3q "A-Ah--"
    [ 352] y 4a "Would you...like to come along with me?"
    [ 353] show yuri at t22
    [ 354] show natsuki at f21
    [ 355] n 5s "Um..."
    [ 356] n "If you don't mind..."
    [ 357] show natsuki at t21
    [ 358] show yuri at f22
    [ 359] y 3t "Not at all!"
    [ 360] y "I always go alone, so..."
    [ 361] show yuri at t22
    [ 362] show natsuki at f21
    [ 363] n "Yeah, me too..."
    [ 364] show natsuki at t21
    [ 365] show sayori 4s at l41
    [ 366] s "This is so cute~!"
    [ 367] mc "Sayori, shut up..."
    [ 368] show sayori at lhide
    [ 369] hide sayori
    [ 370] show natsuki at f21
    [ 371] n 2j "I'll show you some manga there too, okay?"
    [ 372] show natsuki at t21
    [ 373] show yuri at f22
    [ 374] y 1a "Yes."
    [ 375] y "I look forward to it."
    [ 376] show natsuki at thide
    [ 377] show yuri at thide
    [ 378] hide natsuki
    [ 379] hide yuri
    [ 380] "Natsuki and Yuri start to clean up the food."
    [ 381] 
    [ 382] 
    [ 383] show sayori 1q at t11
    [ 384] s "Ehehe~"
    [ 385] s 1x "I guess the meeting's over, huh?"
    [ 386] mc "Yeah, looks like it..."
    [ 387] mc "It's nice to see everyone getting along."
    [ 388] s 1q "Isn't it?"
    [ 389] s 1d "I think everyone likes you too, [player]."
    [ 390] mc "You think so...?"
    [ 391] mc "Well, everyone always seems to get along a little better with you around, Sayori."
    [ 392] s 1y "Aww, [player]~"
    [ 393] s "Don't say something like that, it's embarrassing!"
    [ 394] mc "Well, whatever."
    [ 395] mc "I was surprised when you told me you were starting a club..."
    [ 396] mc "But I think you're pulling it off just fine."
    [ 397] s 1r "We're gonna make it the best club ever!"
    [ 398] s 1x "Now that you joined, every day is gonna be so much fun."
    [ 399] stop music fadeout 2
    [ 400] s 1a "Hey, [player]..."
    [ 401] s "I really want to thank you."
    [ 402] s "I mean, I'm really happy that you joined the club and everything..."
    [ 403] s "But the truth is, I already knew you were going to."
    [ 404] s 1q "Ehehe~"
    [ 405] s 1a "There's actually something else."
    [ 406] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="game_complete", UnlockId=2364778287 }
    [ 407] 
    [ 408] unless persistent.clearall goto [411]
    [ 409] call ch40_clearall
    [ 410] goto [412]
    [ 411] call ch40_clearnormal
    [ 412] pass
    [ 413] window hide(None)
    [ 414] window auto
    [ 415] 
    [ 416] return
    [ 417] label label ch40_clearnormal:    # nested entry point
    [ 418] show sayori 1a at t11 zorder 2
    [ 419] s "I wanted to thank you for getting rid of Monika."
    [ 420] play music "hb"
    [ 421] show black at e9ffb2e3996b0bc49a3006fac51072a2
    [ 422] show layer master at heartbeat
    [ 423] s 1b "That's right..."
    [ 424] s "I know everything that she did."
    [ 425] s 1x "Maybe it's because I'm the President now."
    [ 426] s "But I really know everything, [player]."
    [ 427] s 1q "Ehehe~"
    [ 428] s 1d "I know how hard you tried to make everyone happy."
    [ 429] s "I know about all of the awful things that Monika did to make everyone really sad..."
    [ 430] s 1b "But none of that matters anymore."
    [ 431] s "It's just us now.{nw}"
    [ 432] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [ 433] play sound "65e0ef0302f45184bb8ef448a8632f08"
    [ 434] 
    [ 435] stop sound
    [ 436] hide screen tear
    [ 437] call screen_tear_hide
    [ 438] show room_glitch at 24dd4a1813e09fc42ab04df31804bf62 zorder 1
    [ 439] s "It's just us now.{fast}"
    [ 440] hide room_glitch
    [ 441] s 1d "And you made me the happiest girl in the whole world."
    [ 442] s "I can't wait to spend every day like this..."
    [ 443] s "With you."
    [ 444] play sound "dfbf8d3ce31155d479ae14ef50bf36c1"
    [ 445] show room_glitch at d77486d685286d245b66bf9554a39a08 zorder 1
    [ 446] 
    [ 447] stop sound
    [ 448] s 1q "Forever and ever..."
    [ 449] hide sayori
    [ 450] show sayori 1a at face onlayer front zorder 101
    [ 451] s "F"
    [ 452] s "o"
    [ 453] s "r"
    [ 454] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [ 455] play sound "ff561d6bd0ec56b4b881729cafdad51c"
    [ 456] 
    [ 457] stop sound
    [ 458] hide screen tear
    [ 459] call screen_tear_hide
    [ 460] s "e"
    [ 461] s "v"
    [ 462] s "e"
    [ 463] window show(None)
    [ 464] stop music
    [ 465] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=False }
    [ 466] # WindowAuto: WindowAuto { show=False, command="call screen" }
    [ 467] # WaitForScreen: WaitForScreen { screen="dialog" }
    [ 468] show layer master
    [ 469] hide black
    [ 470] show sayori end-glitch onlayer front
    [ 471] s "...Eh?"
    [ 472] s "W-What's happening...?"
    [ 473] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=False }
    [ 474] # WindowAuto: WindowAuto { show=False, command="call screen" }
    [ 475] # WaitForScreen: WaitForScreen { screen="dialog" }
    [ 476] s "Who..."
    [ 477] s "I-It hurts--"
    [ 478] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [ 479] window hide(None)
    [ 480] play sound "9b0541b99c09b684f82a12204933790a"
    [ 481] hide sayori
    [ 482] 
    [ 483] stop sound
    [ 484] hide screen tear
    [ 485] call screen_tear_hide
    [ 486] window show(None)
    [ 487] s "Ah--"
    [ 488] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=False }
    [ 489] # WindowAuto: WindowAuto { show=False, command="call screen" }
    [ 490] # WaitForScreen: WaitForScreen { screen="dialog" }
    [ 491] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=False }
    [ 492] # WindowAuto: WindowAuto { show=False, command="call screen" }
    [ 493] # WaitForScreen: WaitForScreen { screen="dialog" }
    [ 494] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=False }
    [ 495] # WindowAuto: WindowAuto { show=False, command="call screen" }
    [ 496] # WaitForScreen: WaitForScreen { screen="dialog" }
    [ 497] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=False }
    [ 498] # WindowAuto: WindowAuto { show=False, command="call screen" }
    [ 499] # WaitForScreen: WaitForScreen { screen="dialog" }
    [ 500] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=False }
    [ 501] # WindowAuto: WindowAuto { show=False, command="call screen" }
    [ 502] # WaitForScreen: WaitForScreen { screen="dialog" }
    [ 503] 
    [ 504] # RenpyDialogueLine: RenpyDialogueLine {  }
    [ 505] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [ 506] window hide(None)
    [ 507] play sound "dc6188aa829d3a7438d403d4b2ab346b"
    [ 508] 
    [ 509] stop sound
    [ 510] hide screen tear
    [ 511] call screen_tear_hide
    [ 512] scene black
    [ 513] 
    [ 514] return
    [ 515] label label ch40_clearall:    # nested entry point
    [ 516] s "I wanted to thank you for spending so much time with us all."
    [ 517] play music "mend"
    [ 518] s 2d "You worked so hard to make each and every one of us happy."
    [ 519] s "You comforted us through our hard times."
    [ 520] s "And you helped us all get along with each other."
    [ 521] s 1a "Do you get it, [player]?"
    [ 522] s "Because I'm President now, I understand everything."
    [ 523] s 1q "You really didn't want to miss a single thing in this game, did you?"
    [ 524] s 1a "You saved and loaded so many times, just to make sure you could spend time with everyone."
    [ 525] s "Only someone who truly cares about the Literature Club would go that far."
    [ 526] s "But..."
    [ 527] s 4d "All along, that's all I ever wanted."
    [ 528] s "For everyone to be happy and care about each other."
    [ 529] s 4q "Ahaha..."
    [ 530] s 1t "It's kind of sad, you know?"
    [ 531] s "After all you've done for us, there isn't much I can do for you in return."
    [ 532] s "We've already reached the end of the game."
    [ 533] s 1y "So..."
    [ 534] s "This is where we say goodbye."
    [ 535] s 1d "Thank you for playing <i>Doki Doki Literature Club</i>."
    [ 536] s "I'm going to miss you, [player]."
    [ 537] s "Come visit sometime, okay?"
    [ 538] s "We'll always be here for you."
    [ 539] s 1t "We..."
    [ 540] with None
    [ 541] scene black
    [ 542] with dissolve_cg
    [ 543] s "We all love you."
    [ 544] stop music fadeout 2
    [ 545] scene black
    [ 546] with Dissolve(2.0)
    [ 547] return
