label sm4:
    [   0] scene bg corridor
    [   1] with dissolve_scene_full
    [   2] unless persistent.content_warnings_enabled == True goto [5]
    [   3] 
    [   4] goto [5]
    [   5] pass
    [   6] play music "p7a"
    [   7] "Another day passes."
    [   8] "As usual, Monika is the first one to the clubroom."
    [   9] "With her is a printout of the revised Literature Club flier, complete with all the new ideas Monika and Sayori came up with."
    [  10] with None
    [  11] scene bg club_day
    [  12] with wipeleft
    [  13] show monika 1r at f11 zorder 3
    [  14] m "If only this was the flier we gave to that one reading girl the other day..."
    [  15] m "It's so much more attractive than the old one."
    [  16] m 1i "But..."
    [  17] "The new catchphrase is featured clearly in the center of the flier:"
    [  18] "Write the way into your heart!"
    [  19] "Surely, common sense would say that one writes <i>from</i> the heart, not <i>into</i> the heart."
    [  20] "But the message being delivered is that one can use writing to discover themselves."
    [  21] "Hopefully--Monika and Sayori had thought--that it would be enough to garner some curiosity from students."
    [  22] m 1p "Why do I feel so tense looking at this?"
    [  23] "Monika thinks back to the previous meeting, when she performed the writing exercise."
    [  24] m "Was I always this bad at expressing myself?"
    [  25] m "...How am I supposed to be President if I can't even demonstrate what the club is supposed to be about?"
    [  26] show monika at thide zorder 1
    [  27] hide monika
    [  28] "The Literature Club is truly beginning to take form."
    [  29] "But with that, the weight on Monika's shoulders only becomes heavier."
    [  30] "Debate Club was always about rigid structure--formulating airtight points and counterpoints, and delivering them with conviction."
    [  31] "It was about the person on the <i>outside</i>."
    [  32] "That's why Monika was so good at it--it existed entirely within her realm of comfort."
    [  33] show monika 1p at f11 zorder 3
    [  34] m "It's...suffocating."
    [  35] m 1r "I need to break through this mental wall."
    [  36] m 1i "I need to learn to express myself...for real."
    [  37] show monika at thide zorder 1
    [  38] hide monika
    [  39] "Monika pulls out a sheet of paper and grabs her pen."
    [  40] "She presses the tip of the pen firmly against the paper."
    [  41] 
    [  42] "...But her hand doesn't move."
    [  43] "Instead, a tiny blot of ink collects around the tip of her pen."
    [  44] "Monika lifts her pen and stares at the little blotch."
    [  45] "For some reason, she feels compelled to run her finger across it."
    [  46] "As she does so, the black ink smears across the paper, ruining Monika's canvas."
    [  47] m 1i "Ugh..."
    [  48] "Out of spite for herself, Monika presses her pen down once again, letting the ink collect."
    [  49] "She creates a second smear on the paper."
    [  50] m "Come on, Monika."
    [  51] m "Just move your hand!"
    [  52] "Monika writes."
    [  53] call showpoem(<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["poem_pm1"], constantObjects=[] }>, music=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[0], constantStrings=[], constantObjects=[] }>, paper=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["bg/poem_pm1.png"], constantObjects=[] }>)
    [  54] m "..."
    [  55] "Monika slides the paper away from her and puts her head down on the desk."
    [  56] with None
    [  57] scene black
    [  58] with Dissolve(2)
    [  59] 
    [  60] "The air conditioner seems louder today."
    [  61] 
    [  62] s "I'm here."
    [  63] m "Hi."
    [  64] "Monika hears Sayori approach her desk, then stop for a second, probably reading the piece of paper."
    [  65] "Then, she sits down in the adjacent desk."
    [  66] s "Bad day?"
    [  67] m "Mhm."
    [  68] 
    [  69] s "Me too."
    [  70] with None
    [  71] scene bg club_day
    [  72] with Dissolve(2)
    [  73] show monika 1d at f22 zorder 3
    [  74] m "You too?"
    [  75] 
    [  76] show sayori 1d at f21 zorder 3
    [  77] s "The new flier looks so good."
    [  78] s "You've been working so hard."
    [  79] s "On the club...but also something else, I think."
    [  80] 
    [  81] m 1p "...I can't do it."
    [  82] m "I'm sorry."
    [  83] m "It's so hard to just...be vulnerable."
    [  84] s "Mm."
    [  85] show sayori at thide zorder 1
    [  86] hide sayori
    [  87] show monika at thide zorder 1
    [  88] hide monika
    [  89] "Sayori takes the sheet of paper from Monika's desk."
    [  90] "She writes something down, then stares at it for a while."
    [  91] 
    [  92] show sayori 1k at f21 zorder 3
    [  93] s "Can I trust you?"
    [  94] show monika 2d at f22 zorder 3
    [  95] m "Of course."
    [  96] m "You can trust me with anything."
    [  97] show sayori at thide zorder 1
    [  98] hide sayori
    [  99] show monika at thide zorder 1
    [ 100] hide monika
    [ 101] "Sayori gazes at Monika with sadness in her eyes."
    [ 102] "Understanding the signal, Monika takes the paper from Sayori's desk and reads it."
    [ 103] stop music fadeout 2
    [ 104] 
    [ 105] call showpoem(<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["poem_ps3"], constantObjects=[] }>, music=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[0], constantStrings=[], constantObjects=[] }>, paper=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["bg/poem_pm1.png"], constantObjects=[] }>)
    [ 106] play music "p7c"
    [ 107] show monika 1a at f22 zorder 3
    [ 108] m 1g "Sayori..."
    [ 109] show sayori 1k at f21 zorder 3
    [ 110] s "..."
    [ 111] s "This is really...really...hard for me."
    [ 112] "Her voice shakes."
    [ 113] s 1t "So if I can do it..."
    [ 114] s "...Then you can, too."
    [ 115] s "Because..."
    [ 116] s "You're like a million times better than me."
    [ 117] m 2m "That's completely not true."
    [ 118] "Sayori takes a deep breath, trying to steady herself."
    [ 119] 
    [ 120] s 1l "That's something about me that I've never told anyone before."
    [ 121] s "Even now...my head is, like...screaming at me to stop."
    [ 122] m 1g "Wait! You don't...you don't have to force yourself!"
    [ 123] m "I mean, just because of the promise yesterday..."
    [ 124] s 1i "I want to."
    [ 125] s "It just...feels right."
    [ 126] s 1k "I mean...maybe it's part of the reason I came to this club in the first place."
    [ 127] 
    [ 128] s 1i "This is the Literature Club."
    [ 129] s "I trust you. More than I'm scared."
    [ 130] show sayori at thide zorder 1
    [ 131] hide sayori
    [ 132] show monika at thide zorder 1
    [ 133] hide monika
    [ 134] "At those words, Monika stands up."
    [ 135] "Sayori must have taken days to work up the courage for this."
    [ 136] "Were Monika's own futile--but genuine--efforts actually the push that Sayori needed?"
    [ 137] "Sayori's deliberate breaths can be heard over the air conditioner."
    [ 138] "As she prepares herself to continue, Monika waits in gentle silence."
    [ 139] 
    [ 140] show sayori 1k at f21 zorder 3
    [ 141] s "I have this...problem...where I get really upset when people worry too much about me."
    [ 142] s "I can't control it..."
    [ 143] s 1d "It's like...why waste your energy worrying about me when you can just be happy instead?"
    [ 144] s "So I never tell anyone about these kinds of thoughts that I have."
    [ 145] s 1k "It's so much easier to just smile and help everyone else be happy."
    [ 146] show monika 1g at f22 zorder 3
    [ 147] m "But that's..."
    [ 148] "Terrible."
    [ 149] "That's what Monika wants to say, but she stops herself in fear of saying the wrong thing."
    [ 150] s 1d "It's just that if everyone knew about it...they wouldn't treat me the same anymore."
    [ 151] s "Like whenever I'm not smiling, everyone would worry about me and ask me what's wrong."
    [ 152] s 1k "I know that...because it used to be like that."
    [ 153] "Sayori pauses, seeming to recall something in the past."
    [ 154] s 1g "I just want everyone to be happy."
    [ 155] s "That's the most important thing to me."
    [ 156] s 1k "And...letting people look inside my head doesn't bring happiness to anyone."
    [ 157] "Sayori pauses again, her solemn expression making her look almost like an entirely different person."
    [ 158] m 1g "How did you find the courage to tell me this?"
    [ 159] m "You're not...worried that I'll be one of those people too?"
    [ 160] s 1g "I am worried."
    [ 161] s "Part of me really hates myself for doing this."
    [ 162] s 1d "But another part of me...I think, just felt like it would be different this time."
    [ 163] s "Whenever we talk about what the club is supposed to mean, I kept feeling like it was right for me to do."
    [ 164] s 1l "Especially after you've been trying so hard to express yourself, too."
    [ 165] s "It just...made me feel like I could say it in confidence, and our friendship doesn't have to change."
    [ 166] s 1t "Ahaha."
    [ 167] s "It's so silly...the club is only two people, but it already means this much to me."
    [ 168] with None
    [ 169] scene black
    [ 170] with Dissolve(1)
    [ 171] "Monika feels a tightening sensation in her heart."
    [ 172] "A feeling of connection as Sayori's emotions radiate between them."
    [ 173] m "Me too."
    [ 174] m "I was...so lost until you showed up."
    [ 175] m "You're so brave, Sayori. You're so strong and brave. I don't even compare."
    [ 176] "Monika steps forward."
    [ 177] m "But...if nothing else, I can at least offer you some hug energy."
    [ 178] m "If you'd like."
    [ 179] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="bgm_hugenergy", UnlockId=3495209586 }
    [ 180] play music "p9" fadeout 2
    [ 181] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="sm_exclusive", UnlockId=3452813446 }
    [ 182] with None
    [ 183] scene sm_base
    [ 184] with Dissolve(2.0)
    [ 185] "Wordlessly, and without a smile, Sayori rests her forehead on Monika's shoulder."
    [ 186] "Through their contact, Monika can almost feel the torrent of thoughts swimming in Sayori's head."
    [ 187] "And in this moment, enchanted by the air of the club..."
    [ 188] "Monika realizes that of all the days that have passed, this is the one where she really, really hopes that nobody new walks through the door."
    [ 189] "She speaks softly."
    [ 190] show sm_m1 at 3a2574ac421797b488310624f70d9ada
    [ 191] show sm_m2 at 9d002be7974b1d14ea88d7ab6eee9587
    [ 192] m "You're like...the sweetest girl I've ever met."
    [ 193] m "You can say anything. I'll never judge you."
    [ 194] m "I promise."
    [ 195] "Sayori's breath begins to quiver."
    [ 196] "She takes several deep breaths, trying as hard as she can to start speaking, to say the things she never once dared to say out loud."
    [ 197] "Finally, she speaks in a choked voice."
    [ 198] show sm_m2 at 932881b674b4fa149bf609eca85b38db
    [ 199] show sm_s2 at 308cc71a15ef8b248bc0c0aac4c11f6a
    [ 200] show sm_s4 at b482d7b9b4b4dfd4890ca016c5c274f5 zorder 3
    [ 201] s "I'm...so worthless."
    [ 202] s "I'm worthless and everyone would be better off without me."
    [ 203] show sm_s5 at 304c43f01a0654e42806b4447522eea9 zorder 3
    [ 204] "She suppresses a sob as a tear falls down her cheek."
    [ 205] show sm_s3 at 6ba1040917ef90846ab8cad88f0f72de
    [ 206] s "I'm just...an inconvenience to everyone."
    [ 207] s "I'm not good at anything, and it just feels like everyone just has to put up with me, and I hate it. I hate it."
    [ 208] "The more Sayori speaks, the more she fails to control her voice, falling victim to the overwhelming sadness clutching at her throat and chest."
    [ 209] show sm_s1 at 3b9d1717af95ef5449a84c1c9d42c477
    [ 210] s "I don't want to have these thoughts. I want them to go away. And now I'm making you put up with me and I just want to die!"
    [ 211] show sm_m1 at 33c04da68db4cad49817b39a3ab47396
    [ 212] "As soon as Sayori loses her composure, Monika becomes determined to keep her own."
    [ 213] "She only wants to be what Sayori needs right now."
    [ 214] "So, she won't let any sadness show."
    [ 215] "Her voice comes through as soft and gentle."
    [ 216] show sm_m1 at bd9e4877e50a2bf47984d01a65ec1740
    [ 217] show sm_m2 at 47b50bf9ce3fffc4a9aa0f2b3d6a5868
    [ 218] m "This isn't putting up with you."
    [ 219] m "It's just being your friend."
    [ 220] show sm_s1 at e0a1651e06b2c474f8747c5212ba4dfe
    [ 221] "Monika offers a few words of comfort."
    [ 222] "But she knows--Sayori said it herself--that the thoughts Sayori experiences are ones that don't belong."
    [ 223] "And Monika can't magically make them go away."
    [ 224] "The most she can do is help Sayori battle them, like any good friend would do."
    [ 225] show sm_m1 at e7c8ce8df642a75479ae89f2eabbab36
    [ 226] m "You have so much value."
    [ 227] m "To me, and your other friends, too."
    [ 228] m "This club wouldn't have been the same without you."
    [ 229] m "I really, really mean that."
    [ 230] show sm_m1 at b66abd1166d74b0449d0ea42754a6360
    [ 231] m "You coming here was the best thing that could have happened."
    [ 232] m "Even if we never got any other members...I would still be happy."
    [ 233] m "That's what you brought here."
    [ 234] m "You brought us a vision...and you also brought happiness."
    [ 235] show sm_m1 at 451abbb4a4b9e8d4284b5f9f4267be99
    [ 236] m "And that's your favorite thing to do...right?"
    [ 237] "Sayori doesn't respond, but Monika feels her gently nod."
    [ 238] "No more words are needed between them."
    [ 239] with None
    [ 240] scene black
    [ 241] with Dissolve(2.0)
    [ 242] "The two share their embrace for a while longer, Monika letting Sayori take as much time as she needs."
    [ 243] "Once her breathing steadies and her sniffles fully cease, Sayori lifts her head and wipes her eyes."
    [ 244] play music "p1" fadeout 2
    [ 245] with None
    [ 246] scene bg club_day
    [ 247] with Dissolve(2.0)
    [ 248] show sayori 1l at f21 zorder 3
    [ 249] s "I guess I needed that."
    [ 250] s "Some days are harder than others."
    [ 251] show monika 1e at f22 zorder 3
    [ 252] m "Well, I'm here whenever you need me."
    [ 253] m "But any other time...I'll make sure that things are the way they usually are."
    [ 254] m "If that's what makes you happy."
    [ 255] s 1d "Mhm."
    [ 256] s "Thanks."
    [ 257] s 1q "You're the best."
    [ 258] m 2a "No, you are."
    [ 259] "The two exchange smiles."
    [ 260] m 2d "You know...I'm sorry to bring this up all of a sudden, but...have you considered talking to a professional?"
    [ 261] "Sayori nods."
    [ 262] s 1l "It's scary."
    [ 263] s "Since it's already so hard to tell people..."
    [ 264] m 2e "Yeah."
    [ 265] m "Well...of course it will always be your choice, but if you're ever looking to find the courage for it, I can do my best to help you."
    [ 266] s 1d "Thanks."
    [ 267] s "I think it helps knowing that you would."
    [ 268] "Sayori suddenly yawns and stretches."
    [ 269] s 4p "Wow, that made me tired!"
    [ 270] s "And hungry..."
    [ 271] m 1j "Ahaha."
    [ 272] m 1a "Well, I won't make you do any work today if you're not up for it."
    [ 273] s 1b "No, I want to!"
    [ 274] s 1a "I mean...I can say that it's definitely one thing that makes me happy."
    [ 275] show monika 1j at t22 zorder 2
    [ 276] "Monika smiles."
    [ 277] s 2l "...But I might want to get a snack first."
    [ 278] show sayori at thide zorder 1
    [ 279] hide sayori
    [ 280] show monika at thide zorder 1
    [ 281] hide monika
    [ 282] "All of a sudden, the sound of the door causes the two of them to turn their heads."
    [ 283] "The door opens halfway, then stops. A face peeks inside."
    [ 284] "A face that seems familiar..."
    [ 285] stop music fadeout 2
    [ 286] with None
    [ 287] scene black
    [ 288] with Dissolve(2.0)
    [ 289] 
    [ 290] return
