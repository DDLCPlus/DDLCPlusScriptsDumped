label yuri_exclusive2_2_ch22:
    [   0] y 3a "Actually, I have a request..."
    [   1] y "...Do you mind if I make some tea first?"
    [   2] mc "Not at all."
    [   3] y 1c "Thanks very much."
    [   4] y 1a "If there's one thing that can make my reading time here any better, it's a nice cup of tea."
    [   5] y "Not to mention for yourself, as well."
    [   6] show yuri at thide zorder 1
    [   7] hide yuri
    [   8] "Yuri stands up and makes her way to the closet."
    [   9] "I follow and watch as she retrieves a small water pitcher from the shelf - the kind with a filter inside."
    [  10] show yuri 1f at t11 zorder 2
    [  11] y "Can you hold this for a second?"
    [  12] mc "Sure..."
    [  13] "Yuri hands me the water pitcher and also fetches an electric kettle."
    [  14] y "I'm going to plug this in at the teacher's desk, and then I'll go get some water."
    [  15] show yuri at thide zorder 1
    [  16] hide yuri
    [  17] "She walks past me and sets the kettle down on the teacher's desk."
    [  18] "I simply watch her movements."
    [  19] "To my surprise, the way she moves really contrasts her speaking mannerisms."
    [  20] "Especially because of her long legs, Yuri appears elegant and methodical."
    [  21] show yuri 1f at t11 zorder 2
    [  22] y "Okay, may I have the water pitcher?"
    [  23] y 1a "Thanks. I'll be right back."
    [  24] mc "Ah, I might as well walk with you..."
    [  25] y 1q "T-That's okay!"
    [  26] y "You stay here..."
    [  27] y "It won't take long."
    [  28] show yuri at thide zorder 1
    [  29] hide yuri
    [  30] "Pitcher in hand, Yuri hurries out of the classroom."
    [  31] show monika 2i at t11 zorder 2
    [  32] m "Ah..."
    [  33] m "Did Yuri leave you again?"
    [  34] mc "No, it's not like that this time."
    [  35] mc "She's just filling up the water pitcher to make tea."
    [  36] m 5 "Oh, okay!"
    [  37] m "Sorry for misunderstanding~"
    [  38] scene bg club_day
    [  39] with wipeleft_scene
    [  40] "..."
    [  41] "Ten minutes pass."
    [  42] "Yuri said it wouldn't take long..."
    [  43] "Is something holding her up?"
    [  44] "I'm bored just waiting here, so I decide to go look for her."
    [  45] scene bg corridor
    [  46] with wipeleft_scene
    [  47] 
    [  48] play music "645cfba5edebbe8428ad2fc73f32a15c"
    [  49] unless persistent.content_warnings_enabled == True goto [52]
    [  50] 
    [  51] goto [52]
    [  52] pass
    [  53] mc "Let's see..."
    [  54] "The most logical place for Yuri to be would be the nearest water fountain..."
    [  55] 
    [  56] "I start heading down the hallway."
    [  57] 
    [  58] y "Haah.....haah...."
    [  59] y "....Haah.....haah...."
    [  60] "...What's that noise?"
    [  61] "It's coming from around the corner..."
    [  62] "It sounds like breathing."
    [  63] y "Khhhhh--"
    [  64] "A sharp inhale, like someone is sucking the air through their teeth."
    [  65] "Are they in pain...?"
    [  66] "I reach the corner and peer around it."
    [  67] mc "Yuri...?"
    [  68] 
    [  69] show yuri cuts at t11 zorder 2
    [  70] y "Kya--!"
    [  71] 
    [  72] 
    [  73] 
    [  74] play music "t6r"
    [  75] show yuri at thide zorder 1
    [  76] hide yuri
    [  77] show noise at noise_alpha zorder 100
    [  78] show vignette at vignetteflicker(<compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction], constantFloats=[2.03], constantStrings=[], constantObjects=[] }>) zorder 100
    [  79] show layer master at rewind
    [  80] 
    [  81] mc "Y{cps=150}uri...?{/cps}{nw}"
    [  82] "{cps=150}I reach the corner and peer around it.{/cps}{nw}"
    [  83] "{cps=150}Are they in pain...?{/cps}{nw}"
    [  84] "{cps=150}A sharp inhale, like someone is sucking the air through their teeth.{/cps}{nw}"
    [  85] y "K{cps=150}hhhhh--{/cps}{nw}"
    [  86] "{cps=150}It sounds like breathing.{/cps}{nw}"
    [  87] "{cps=150}It's coming from around the corner...{/cps}{nw}"
    [  88] "{cps=150}...What's that noise?{/cps}{nw}"
    [  89] y ".{cps=150}...Haah.....haah....{/cps}{nw}"
    [  90] y "H{cps=150}aah.....haah....{/cps}{nw}"
    [  91] 
    [  92] "{cps=150}I start heading down the hallway.{/cps}{nw}"
    [  93] "{cps=150}The most logical place for Yuri to be would be the nearest water fountain...{/cps}{nw}"
    [  94] mc "L{cps=150}et's see...{/cps}{nw}"
    [  95] window hide(None)
    [  96] window auto
    [  97] scene bg club_day
    [  98] show noise at noise_alpha zorder 100
    [  99] show vignette at vignetteflicker(<compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction], constantFloats=[2.03], constantStrings=[], constantObjects=[] }>) zorder 100
    [ 100] show layer master at rewind
    [ 101] "{cps=150}I'm bored just waiting here, so I decide to go look for her.{/cps}{nw}"
    [ 102] "{cps=150}Is something holding her up?{/cps}{nw}"
    [ 103] "{cps=150}Yuri said it wouldn't take long...{/cps}{nw}"
    [ 104] "{cps=150}Ten minutes pass.{/cps}{nw}"
    [ 105] "{cps=150}...{/cps}{nw}"
    [ 106] 
    [ 107] unless poemwinner[0] == "yuri" and chapter == 3 goto [110]
    [ 108] jump yuri_exclusive2_2_ch23
    [ 109] goto [110]
    [ 110] pass
    [ 111] 
    [ 112] 
    [ 113] 
    [ 114] play music "t6r"
    [ 115] hide noise
    [ 116] hide vignette
    [ 117] show layer master
    [ 118] scene bg club_day
    [ 119] show yuri 1a at t11 zorder 2
    [ 120] y "I'm back."
    [ 121] y "Thanks for waiting patiently."
    [ 122] y "[player], do you like oolong tea?"
    [ 123] mc "Ah, yeah."
    [ 124] mc "Anything is fine."
    [ 125] y "Very well."
    [ 126] "Yuri sets the temperature on the kettle to 200 degrees."
    [ 127] y 1f "Now it's time to get the teapot."
    [ 128] mc "You really do this properly, don't you?"
    [ 129] y 1u "Of course..."
    [ 130] y "I shouldn't do any less when I'm making tea for others."
    [ 131] mc "Even if I'm not an expert on tea or anything...?"
    [ 132] y 2m "Huhu."
    [ 133] y 2a "In that case, you'll only be even more impressed."
    [ 134] mc "Ah...perhaps I will!"
    [ 135] show yuri at thide zorder 1
    [ 136] hide yuri
    [ 137] "Yuri fetches the teapot and begins measuring the tea leaves."
    [ 138] "To my surprise, she even starts humming a little to herself."
    [ 139] show yuri 1c at t11 zorder 2
    [ 140] mc "You must be in a good mood now..."
    [ 141] y 1a "Is that so?"
    [ 142] y "I was letting it show..."
    [ 143] y "And you noticed."
    [ 144] y 2u "I was doing a bit of thinking..."
    [ 145] y "And I decided that I would try expressing myself a little bit more."
    [ 146] y "It turns out it's not very hard for me to do..."
    [ 147] y 1c "When it's you who's around, anyway."
    [ 148] show yuri 1a
    [ 149] mc "Ah..."
    [ 150] mc "That's great, Yuri!"
    [ 151] mc "Just don't push yourself too much."
    [ 152] y 3u "You're always worrying about me, [player]..."
    [ 153] y "It's very endearing."
    [ 154] mc "That's..."
    [ 155] "Yuri wasn't kidding..."
    [ 156] "I don't even know if I can keep up with this...!"
    [ 157] "I watch Yuri pour a cup of tea for each of us."
    [ 158] y 1a "[player], I have another request."
    [ 159] y "Do you mind if we sit on the floor today?"
    [ 160] mc "Eh? Why's that?"
    [ 161] y 1h "It's a little bit easier on my back..."
    [ 162] y "I can read with my back against the wall rather than bending over at my desk."
    [ 163] mc "Ah, sorry, I didn't realize."
    [ 164] y 1a "No worries."
    [ 165] y "I just have back pain fairly regularly, so I do my best to manage it."
    [ 166] mc "Is that so?"
    [ 167] mc "I wonder why that is..."
    [ 168] y 1f "It's most likely because my--"
    [ 169] y 1n "Ah--"
    [ 170] y 1o "M-My..."
    [ 171] mc "Your posture, right?"
    [ 172] mc "Always hunched over like that while reading..."
    [ 173] y 2p "Yes!"
    [ 174] y 2q "I have terrible reading posture!"
    [ 175] y "So that's why we should sit on the floor."
    [ 176] mc "Fair enough."
    [ 177] mc "I'll go ahead and get the book."
    [ 178] show yuri at thide zorder 1
    [ 179] hide yuri
    [ 180] "I retrieve the book from my bag."
    [ 181] mc "Ah, I have some chocolate as well..."
    [ 182] "It's a bag of small chocolate candies."
    [ 183] "I take it, since it'll go well with the tea."
    [ 184] "Yuri and I then sit against the wall, teacups at our sides."
    [ 185] "As if in sync, we assume the same reading position as last time, each holding one half of the book."
    [ 186] "Except this time..."
    [ 187] "Our bodies are even closer to each other."
    [ 188] show yuri 2h at t11 zorder 2
    [ 189] y "I can't see too well..."
    [ 190] mc "--!"
    [ 191] show yuri 2e at d11
    [ 192] "Yuri slides closer until our shoulders are touching."
    [ 193] "How am I supposed to focus on reading like this...?!"
    [ 194] "Yuri was always kind of cute, but..."
    [ 195] "When she's being less apprehensive, it's almost more than I can handle!"
    [ 196] y 2f "Your teacup..."
    [ 197] "Yuri hands me my teacup."
    [ 198] "Holding it with my hand that's not holding the book, I end up in a position that makes it even harder to focus."
    [ 199] "Because now I need to worry about making sure I don't accidentally touch her chest...!"
    [ 200] "Meanwhile, Yuri hasn't noticed a single thing."
    [ 201] "She wears her intense reading expression, and I can only presume the world around her has faded away."
    [ 202] "I use all of my willpower to focus on reading."
    [ 203] "..."
    [ 204] "After a few minutes, I finally manage to relax a little."
    [ 205] "I put the teacup between my legs and fumble with the chocolate wrapper."
    [ 206] mc "Ah, sorry..."
    [ 207] "I briefly let go of the book to finish opening the wrapper."
    [ 208] mc "You can have as much as you want."
    [ 209] y 2s "Ah, that's..."
    [ 210] y "That's okay, I won't take any..."
    [ 211] mc "Eh? Are you sure?"
    [ 212] y 2v "Well..."
    [ 213] y "If I touch it, then it might get smudges on the pages..."
    [ 214] mc "Ah, you're right..."
    [ 215] mc "I didn't even think about that."
    [ 216] mc "My bad..."
    [ 217] y 2a "No need to apologize."
    [ 218] y "I'll hold the book, okay?"
    [ 219] mc "Are you sure...?"
    [ 220] y "Of course."
    [ 221] 
    [ 222] 
    [ 223] scene y_cg2_bg
    [ 224] show y_cg2_bg2 at y_cg2_bg2_t
    [ 225] show y_cg2_base
    [ 226] show y_cg2_details
    [ 227] show y_cg2_nochoc
    [ 228] show y_cg2_dust1
    [ 229] show y_cg2_dust2
    [ 230] show y_cg2_dust3
    [ 231] show y_cg2_dust4
    [ 232] with dissolve_cg
    [ 233] "Yuri opens the book with both hands."
    [ 234] "She holds it so that I don't have any harder of a time reading from it."
    [ 235] "But as a result, her left arm is practically resting on top of my leg."
    [ 236] mc "Well, in that case..."
    [ 237] "Yuri is already totally focused on reading again."
    [ 238] "I take a chocolate candy and pop it into my mouth."
    [ 239] "Then, I take another chocolate..."
    [ 240] "And I hold it up to Yuri."
    [ 241] "She doesn't even look away from the book."
    [ 242] "She simply parts her lips, as if this situation was completely natural."
    [ 243] "But that means I can't stop here!"
    [ 244] hide y_cg2_nochoc
    [ 245] "I apprehensively place the chocolate in her mouth."
    [ 246] "Just like that, Yuri closes her lips over it."
    [ 247] y "Eh...?"
    [ 248] show y_cg2_exp2
    [ 249] "Yuri's expression suddenly breaks."
    [ 250] y "Did..."
    [ 251] y "Did I just..."
    [ 252] "Yuri looks at me like she needs to confirm what just happened."
    [ 253] show y_cg2_exp3
    [ 254] show y_cg2_nochoc at 4828fc53b3b3f044ca3e9aa173ebf69e
    [ 255] hide y_cg2_exp2
    [ 256] y "U-Um..."
    [ 257] y "[player]..."
    [ 258] mc "S-Sorry!"
    [ 259] mc "I guess I shouldn't have done that..."
    [ 260] stop music
    [ 261] y "A-Ah..."
    [ 262] "Yuri starts to breathe heavily."
    [ 263] y "I..."
    [ 264] y "I can't..."
    [ 265] y "[player]..."
    [ 266] "Suddenly, Yuri forcefully grabs my arm and jerks me to my feet."
    [ 267] "My teacup gets knocked over."
    [ 268] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="bg_closet", UnlockId=1759050863 }
    [ 269] scene bg closet
    [ 270] with wipeleft
    [ 271] show yuri 2t at t11 zorder 2
    [ 272] y "[player]..."
    [ 273] play sound "closet_close"
    [ 274] show dark zorder 100
    [ 275] with wipeleft
    [ 276] y "My heart..."
    [ 277] y 2y6 "My heart won't stop pounding, [player]..."
    [ 278] y "I can't calm down."
    [ 279] y "I can't focus on anything anymore...!"
    [ 280] y "Can you feel it, [player]?"
    [ 281] "Yuri suddenly presses my hand against her chest."
    [ 282] play music "hb"
    [ 283] show layer master at heartbeat
    [ 284] y 3t "Why is this happening to me?"
    [ 285] y "I feel like I'm losing my mind..."
    [ 286] y 3y4 "I can't make it stop."
    [ 287] y 3y6 "It even makes me not want to read..."
    [ 288] y "I just want..."
    [ 289] y 3s "...to look..."
    [ 290] y "...at you."
    [ 291] hide yuri
    [ 292] 
    [ 293] show yuri_eyes_lc at truecenter
    [ 294] 
    [ 295] y "...Haah..."
    [ 296] 
    [ 297] y "...Haah..."
    [ 298] 
    [ 299] y "...Haah..."
    [ 300] 
    [ 301] play sound "closet_open"
    [ 302] stop music
    [ 303] show layer master
    [ 304] hide yuri_eyes_lc
    [ 305] hide yuripupils
    [ 306] 
    [ 307] show yuri 1n at face
    [ 308] with None
    [ 309] with None
    [ 310] show yuri 3n at t32
    [ 311] with None
    [ 312] hide dark
    [ 313] show monika 3l at f31 zorder 3
    [ 314] m "U-Um..."
    [ 315] m "It's...time to share poems..."
    [ 316] return
