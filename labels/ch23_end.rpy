label ch23_end:
    [   0] stop music fadeout 1
    [   1] scene black
    [   2] with wipeleft_scene
    [   3] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=False }
    [   4] # WindowAuto: WindowAuto { show=False, command="call screen" }
    [   5] # WaitForScreen: WaitForScreen { screen="confirm" }
    [   6] unless _return goto [12]
    [   7] call expression <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction], constantFloats=[2, 1, 0], constantStrings=["poem_special_", "persistent", "special_poems", "str"], constantObjects=[] }>
    [   8] with None
    [   9] scene black
    [  10] with Dissolve(1.0)
    [  11] goto [13]
    [  12] pass
    [  13] pass
    [  14] scene bg club_day2
    [  15] show monika 4b at t32 zorder 2
    [  16] with wipeleft_scene
    [  17] play music "t3"
    [  18] m "Okay, everyone!"
    [  19] m "It's time to figure out the festival preparations."
    [  20] m 1i "Let's hurry and get this over with."
    [  21] unless n_appeal >= 2 goto [25]
    [  22] show natsuki 4q at f31 zorder 3
    [  23] n "..."
    [  24] goto [29]
    [  25] show natsuki 4q at f31 zorder 3
    [  26] n "Jeez..."
    [  27] n "Why is the mood so weird today?"
    [  28] n "Look, even Yuri isn't immune to it."
    [  29] pass
    [  30] show natsuki at t31 zorder 2
    [  31] show yuri 4b at f33 zorder 3
    [  32] y "Uu..."
    [  33] y "Stagnating air is common foreshadowing that something terrible is about to happen..."
    [  34] show yuri at t33 zorder 2
    [  35] show monika at f32 zorder 3
    [  36] m 2r "Look, can we just get this done?"
    [  37] m 2d "I'm going to be printing and assembling all the poetry pamphlets."
    [  38] unless n_appeal >= 2 goto [47]
    [  39] m 2i "Natsuki, you can make cupcakes."
    [  40] m "I know you're at least good at that."
    [  41] show monika at t32 zorder 2
    [  42] show natsuki at f31 zorder 3
    [  43] n 5u "..."
    [  44] show natsuki at t31 zorder 2
    [  45] show monika at f32 zorder 3
    [  46] goto [55]
    [  47] m "Natsuki, I was thinking--"
    [  48] show monika at t32 zorder 2
    [  49] show natsuki at f31 zorder 3
    [  50] n 2d "I want to make cupcakes!"
    [  51] show natsuki 2a at t31 zorder 2
    [  52] show monika at f32 zorder 3
    [  53] m 2a "...Yeah, that."
    [  54] m "Glad we're on the same page."
    [  55] pass
    [  56] m 1m "Yuri, you can..."
    [  57] m 1r "...Well, it doesn't matter."
    [  58] m 1i "Do whatever you want, as long as you think it'll help."
    [  59] show monika at t32 zorder 2
    [  60] show yuri at f33 zorder 3
    [  61] y 2h "Monika..."
    [  62] y "I'm not useless, you know!"
    [  63] show yuri at t33 zorder 2
    [  64] show monika at f32 zorder 3
    [  65] m 2p "I-I know that!"
    [  66] show monika at t32 zorder 2
    [  67] show yuri at f33 zorder 3
    [  68] y 1l "I already know what I'd like to do."
    [  69] y 1h "We can't run a successful poetry event without having the right atmosphere for the occasion."
    [  70] y "So I'm going to make decorations and set up some nice mood lighting."
    [  71] show yuri at t33 zorder 2
    [  72] show monika at f32 zorder 3
    [  73] m 2j "There, see?"
    [  74] m "That's a great idea!"
    [  75] m 1a "And that gives us all something to do."
    [  76] show monika at t32 zorder 2
    [  77] show yuri at f33 zorder 3
    [  78] y 2f "Eh?"
    [  79] y "What about [player]?"
    [  80] show yuri at t33 zorder 2
    [  81] show monika at f32 zorder 3
    [  82] m 2b "[player] is going to help me."
    [  83] show monika 2a at t32 zorder 2
    [  84] show natsuki at f31 zorder 3
    [  85] n 4e "Wait, you?"
    [  86] n "You have the easiest job, Monika!"
    [  87] show natsuki at t31 zorder 2
    [  88] show monika at f32 zorder 3
    [  89] m 1i "Sorry, but that's just how it is."
    [  90] show monika at t32 zorder 2
    [  91] show natsuki at f31 zorder 3
    [  92] n 1f "Like hell it is!"
    [  93] n "What are you trying to pull?"
    [  94] show natsuki at t31 zorder 2
    [  95] show yuri at f33 zorder 3
    [  96] y 3h "I-I agree with Natsuki!"
    [  97] y "Not only is your work already most suitable for one person..."
    [  98] y 3l "But my task is laborious enough to benefit from an extra pair of hands."
    [  99] show yuri at t33 zorder 2
    [ 100] show natsuki at f31 zorder 3
    [ 101] n 4c "Mine too!"
    [ 102] show natsuki at t31 zorder 2
    [ 103] show yuri at f33 zorder 3
    [ 104] y 1h "What, your cupcakes?"
    [ 105] y "Please."
    [ 106] show yuri at t33 zorder 2
    [ 107] show natsuki at f31 zorder 3
    [ 108] n 1o "Like <i>you</i> would fucking know!"
    [ 109] n 1x "All you care about now is dragging [player] around with you and your stupid books."
    [ 110] n 1f "You <i>and</i> Monika!"
    [ 111] show natsuki at t31 zorder 2
    [ 112] show monika at f32 zorder 3
    [ 113] m 2g "Hey!"
    [ 114] m "I didn't even do anything!"
    [ 115] show monika at t32 zorder 2
    [ 116] show natsuki at f31 zorder 3
    [ 117] n 3e "Okay, then why not let [player] decide who to help instead of abusing your power?"
    [ 118] show natsuki at t31 zorder 2
    [ 119] show monika at f32 zorder 3
    [ 120] m 1p "I'm not...abusing my power."
    [ 121] show monika at t32 zorder 2
    [ 122] show yuri at f33 zorder 3
    [ 123] y 2h "Yes you are, Monika."
    [ 124] y "Just let [player] make the choice, okay?"
    [ 125] show yuri at t33 zorder 2
    [ 126] show monika at f32 zorder 3
    [ 127] m 1r "Okay, fine!"
    [ 128] m "Fine."
    [ 129] show monika 1h at t32 zorder 2
    [ 130] show natsuki at f31 zorder 3
    [ 131] n 3w "Jeez..."
    [ 132] n "[player], I know how fed up you are with these two by now."
    [ 133] n 3c "We can just--"
    [ 134] show natsuki at t31 zorder 2
    [ 135] show yuri at f33 zorder 3
    [ 136] y 2r "Natsuki, shut your fucking mouth and let him decide for himself."
    [ 137] show yuri at t33 zorder 2
    [ 138] show natsuki at f31 zorder 3
    [ 139] n 1o "<i>You</i> shut your mouth!"
    [ 140] show natsuki at t31 zorder 2
    [ 141] show monika at f32 zorder 3
    [ 142] m 1r "For god's sake..."
    [ 143] m 1i "This is never going to end. Just make the choice, okay?"
    [ 144] show monika at t32 zorder 2
    [ 145] 
    [ 146] unless madechoice != "monika" goto [189]
    [ 147] window hide(None)
    [ 148] 
    [ 149] stop music
    [ 150] scene white
    [ 151] show white
    [ 152] show yuripupils zorder 10
    [ 153] 
    [ 154] show bg club_day at a0ba11eb26eb0c04184834f49844a859
    [ 155] show noise at 7eb16c512e7623949ad35b3740e458d0
    [ 156] 
    [ 157] window auto
    [ 158] goto [179]
    [ 159] pass
    [ 160] goto [181]
    [ 161] pass
    [ 162] goto [181]
    [ 163] pass
    [ 164] goto [181]
    [ 165] pass
    [ 166] goto [181]
    [ 167] pass
    [ 168] goto [181]
    [ 169] pass
    [ 170] goto [181]
    [ 171] pass
    [ 172] goto [181]
    [ 173] pass
    [ 174] goto [181]
    [ 175] pass
    [ 176] goto [181]
    [ 177] pass
    [ 178] goto [181]
    [ 179] # RenpyDialogueLine: RenpyDialogueLine {  }
    [ 180] menu:    # caption above
                "Monika":  goto [159]
                "Monika":  goto [161]
                "Monika":  goto [163]
                "Monika":  goto [165]
                "Monika":  goto [167]
                "Monika":  goto [169]
                "Monika":  goto [171]
                "Monika":  goto [173]
                "Monika":  goto [175]
                "Monika":  goto [177]
    [ 181] pass
    [ 182] hide white
    [ 183] hide noise
    [ 184] scene bg club_day
    [ 185] 
    [ 186] play music "t3m"
    [ 187] show monika 5 at i11
    [ 188] goto [193]
    [ 189] show natsuki at thide zorder 1
    [ 190] show yuri at thide zorder 1
    [ 191] hide natsuki
    [ 192] hide yuri
    [ 193] pass
    [ 194] m 5a "Yay, you picked me!"
    [ 195] m "We can meet at your house this weekend."
    [ 196] m "I promise it'll be fun."
    [ 197] m "Is Sunday okay with you?"
    [ 198] show natsuki 1e at f31 zorder 3
    [ 199] n "Are you fucking kidding me?"
    [ 200] n "This isn't fair at all!"
    [ 201] show natsuki at t31 zorder 2
    [ 202] show monika at f32 zorder 3
    [ 203] m 2i "It is fair, Natsuki."
    [ 204] m "It's what he chose."
    [ 205] show monika at t32 zorder 2
    [ 206] show yuri 3r at f33 zorder 3
    [ 207] y "No, it's not fair!"
    [ 208] y "Giving us all this work and then taking [player] for yourself."
    [ 209] y "What a shameful thing to do!"
    [ 210] show yuri at t33 zorder 2
    [ 211] show monika at f32 zorder 3
    [ 212] m 2r "Yuri, I didn't even give you any work."
    [ 213] m 2i "You decided it for yourself."
    [ 214] m "You're being a little unreasonable here."
    [ 215] stop music
    [ 216] show monika at t32 zorder 2
    [ 217] show yuri at f33 zorder 3
    [ 218] y 2y4 "I'm being unreasonable?"
    [ 219] y 2y3 "Ahahaha!"
    [ 220] y "Monika, I can't believe how delusional and self-important you are!"
    [ 221] y "Pulling [player] away from me every single time you're not included in something."
    [ 222] y 1y1 "Are you jealous?"
    [ 223] y "Crazy?"
    [ 224] y 1y3 "Or maybe you just hate yourself so much that you take it out on others?"
    [ 225] y 1y4 "Here's a suggestion. Have you considered killing yourself?"
    [ 226] y "It would be beneficial to your mental health."
    [ 227] show yuri at t33 zorder 2
    [ 228] show natsuki at f31 zorder 3
    [ 229] n 5u "Yuri, you're scaring me a little..."
    [ 230] show natsuki at t31 zorder 2
    [ 231] show monika at f32 zorder 3
    [ 232] m 1r "Natsuki, let's just go."
    [ 233] m 1i "I don't think she wants us around right now."
    [ 234] show monika at t32 zorder 2
    [ 235] show yuri at f33 zorder 3
    [ 236] y 2y3 "See, that wasn't very hard."
    [ 237] y "All I want is to spend a little time with him."
    [ 238] y "Is that so much to ask?"
    [ 239] hide natsuki
    [ 240] hide monika
    [ 241] hide yuri
    [ 242] with wipeleft
    [ 243] "Yuri follows Monika and Natsuki to the door."
    [ 244] show monika 5a at t11 zorder 2
    [ 245] m "Hey, [player]..."
    [ 246] m "Yuri is really something, isn't she?"
    [ 247] show monika at thide zorder 1
    [ 248] hide monika
    [ 249] "Monika giggles as Yuri pushes her out the door."
    [ 250] unless persistent.content_warnings_enabled == True goto [253]
    [ 251] 
    [ 252] goto [253]
    [ 253] pass
    [ 254] python:    # runs C# ch23_end_inlinepythonblock_1223570274
                
    [ 255] play music "t10y"
    [ 256] show yuri 2m at t11 zorder 2
    [ 257] y "Finally."
    [ 258] y 2y1 "Finally!"
    [ 259] y 2s "This is really all I wanted."
    [ 260] y 1y6 "[player], there's no need to spend the weekend with Monika."
    [ 261] y "Don't listen to her."
    [ 262] y 1y5 "Just come to my house instead."
    [ 263] y 3y5 "The whole day, with just the two of us..."
    [ 264] y "Doesn't that sound wonderful?"
    [ 265] y 3y1 "Ahahaha!"
    [ 266] y 3y4 "Wow... There's really something wrong with me, isn't there?"
    [ 267] y "But you know what?"
    [ 268] y 1y3 "I don't care anymore."
    [ 269] y "I've never felt this good my whole life."
    [ 270] y 1y4 "Just being with you is a far greater pleasure than anything I could imagine."
    [ 271] y "I'm addicted to you."
    [ 272] y 3y4 "It feels like I'm going to die if I'm not breathing the same air as you."
    [ 273] y 4a "Doesn't it feel nice to have someone care about you so much?"
    [ 274] y "To have someone who wants to revolve their entire life around you?"
    [ 275] y 2y6 "But if it feels so good..."
    [ 276] y 2y4 "Then why does it feel more and more like something horrible is going to happen?"
    [ 277] y 2y6 "Maybe that's why I tried stopping myself at first..."
    [ 278] y "But the feeling is too strong now."
    [ 279] y 3y1 "I don't care anymore, [player]!"
    [ 280] y "I have to tell you!"
    [ 281] y 3y4 "I'm...I'm madly in love with you!"
    [ 282] y "It feels like every inch of my body...every drop of blood in me...is screaming your name."
    [ 283] y 3y3 "I don't care what the consequences are anymore!"
    [ 284] y "I don't care if Monika is listening!"
    [ 285] y 3w "Please, [player], just know how much I love you."
    [ 286] y 3m "I love you so much that I even touch myself with the pen I stole from you."
    [ 287] y 3y4 "I just want to pull your skin open and crawl inside of you."
    [ 288] y 3y6 "I want you all to myself."
    [ 289] y "And I will be only yours."
    [ 290] y "Doesn't that sound perfect?"
    [ 291] y 3s "Tell me, [player]."
    [ 292] y "Tell me you want to be my lover."
    [ 293] y "Do you accept my confession?"
    [ 294] 
    [ 295] 
    [ 296] goto [302]
    [ 297] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="yuri_confession_yes", UnlockId=3605648560 }
    [ 298] jump yuri_kill
    [ 299] goto [303]
    [ 300] jump yuri_kill
    [ 301] goto [303]
    [ 302] menu:
                "Yes.":  goto [297]
                "No.":  goto [300]
    [ 303] pass
