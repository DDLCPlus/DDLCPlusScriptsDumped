label ch22_end:
    [   0] stop music fadeout 1
    [   1] scene black
    [   2] with wipeleft_scene
    [   3] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=False }
    [   4] # WindowAuto: WindowAuto { show=False, command="call screen" }
    [   5] # WaitForScreen: WaitForScreen { screen="confirm" }
    [   6] unless _return goto [12]
    [   7] call expression <compiled: CompiledExpression { instructions=[CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction, CompiledInstruction], constantFloats=[1, 0], constantStrings=["poem_special_", "persistent", "special_poems", "str"], constantObjects=[] }>
    [   8] with None
    [   9] scene black
    [  10] with Dissolve(1.0)
    [  11] goto [13]
    [  12] pass
    [  13] pass
    [  14] unless not faint_effect and renpy.random.randint(0,2) == 0 goto [17]
    [  15] 
    [  16] goto [18]
    [  17] 
    [  18] pass
    [  19] scene bg club_day2
    [  20] show monika 4b at t32 zorder 2
    [  21] unless faint_effect goto [28]
    [  22] show layer master at dizzy_faint_effect
    [  23] show layer screens at dizzy_faint_effect
    [  24] show 3855ef53c1a67144598c9ef7f850ee03 as i1 at 7aa8fd77211ef8c45a5c1479bc60f33f onlayer front
    [  25] show 729effe14b3ef354685ce0161a5758ab as i2 at b3d5d67804285f74d8c4829a75567fb5 onlayer front
    [  26] show veins onlayer front
    [  27] goto [28]
    [  28] pass
    [  29] with wipeleft_scene
    [  30] unless faint_effect goto [33]
    [  31] play music "t3g3"
    [  32] goto [34]
    [  33] play music "t3"
    [  34] pass
    [  35] unless renpy.random.randint(0,2) == 0 goto [38]
    [  36] 
    [  37] goto [38]
    [  38] pass
    [  39] m "Okay, everyone!"
    [  40] m "We're all done reading each other's poems, right?"
    [  41] 
    [  42] m "We have something we need to go over today, so if everyone could come sit at the front of the room..."
    [  43] show natsuki 3c at f31 zorder 3
    [  44] n "Is this about the festival?"
    [  45] show natsuki at t31 zorder 2
    [  46] show monika 1j at f32 zorder 3
    [  47] m "Well, sort of~"
    [  48] show monika 1a at t32 zorder 2
    [  49] show natsuki 1m at f31 zorder 3
    [  50] n "Ugh. Do we really have to do something for the festival?"
    [  51] n "It's not like we can put together anything good in just a few days."
    [  52] n "We'll just end up embarrassing ourselves instead of getting any new members."
    [  53] unless faint_effect goto [58]
    [  54] 
    [  55] stop music fadeout 2
    [  56] show black at ea4654c2cbddbe24e90d31fda6431cfe onlayer front
    [  57] goto [58]
    [  58] pass
    [  59] show natsuki at t31 zorder 2
    [  60] show yuri 2g at f33 zorder 3
    [  61] y "That's a concern of mine as well."
    [  62] unless faint_effect goto [71]
    [  63] hide black
    [  64] hide veins
    [  65] hide i1
    [  66] hide i2
    [  67] show layer master
    [  68] show layer screens
    [  69] play music "c9a75e43842f07040a04ec28cb94e739"
    [  70] goto [71]
    [  71] pass
    [  72] y "I don't really do well with last-minute preparations..."
    [  73] show yuri at t33 zorder 2
    [  74] show monika at f32 zorder 3
    [  75] m 1b "Don't worry so much!"
    [  76] m "We're going to keep it simple, okay?"
    [  77] m 2a "Look..."
    [  78] m 2m "I know everyone's been a little more...lively...ever since [player] joined and we've started with some club activities."
    [  79] m 2d "But this isn't the time for us to become complacent."
    [  80] m "We still only have four members..."
    [  81] m 2a "And the festival is our only real chance to find more, you know?"
    [  82] show monika at t32 zorder 2
    [  83] show natsuki at f31 zorder 3
    [  84] n 5g "What's so great about getting new members, anyway?"
    [  85] n "We already have enough to be considered an official club."
    [  86] n "More members will just mean everything gets noisier and more difficult to manage."
    [  87] show natsuki at t31 zorder 2
    [  88] show monika at f32 zorder 3
    [  89] m 1g "Natsuki..."
    [  90] m "I don't think you're looking at it the right way at all."
    [  91] m "Don't you want to share your passion with as many people as you can?"
    [  92] m 3e "To inspire them to find the same feelings that brought you here in the first place?"
    [  93] m "The Literature Club should be a place where people can express themselves like they can't do anywhere else."
    [  94] m "It should be a place so intimate that you never want to leave."
    [  95] m 2e "I know you feel that way, too."
    [  96] m 2b "I know we all do!"
    [  97] m "So that's why we should work hard and put something together for the festival...even if it's something small!"
    [  98] m "Right, [player]?"
    [  99] show monika 2a at t32 zorder 2
    [ 100] mc "Ah..."
    [ 101] show natsuki at f31 zorder 3
    [ 102] n 42c "Oh, come on!"
    [ 103] n "You can't take advantage of [player] to agree with you just because he doesn't know how to say no to anything."
    [ 104] stop music fadeout 1
    [ 105] n 1c "Look, Monika."
    [ 106] n "Do you really think any of us here joined the club with other people in mind?"
    [ 107] n "Yuri never even talked until [player] joined."
    [ 108] n 2b "As for me, I just like it better here than I do at home."
    [ 109] n "And [player] isn't even passionate about literature in the first place."
    [ 110] n "And that's everyone."
    [ 111] n 4w "Sorry, but you're really the only one who's so interested in finding new members."
    [ 112] n "The rest of us are fine like this."
    [ 113] n 4q "I know you're President and all, but you should really consider our opinions for once."
    [ 114] show natsuki at t31 zorder 2
    [ 115] show monika at f32 zorder 3
    [ 116] m 1g "..."
    [ 117] "Monika is clearly taken aback by Natsuki's words."
    [ 118] play music "t9"
    [ 119] m 1m "That's...not true at all."
    [ 120] m 2m "I'm sure Yuri and [player] want to get more members too..."
    [ 121] m 2p "...Right?"
    [ 122] show monika at t32 zorder 2
    [ 123] show yuri at f33 zorder 3
    [ 124] y 4b "..."
    [ 125] show yuri at t33 zorder 2
    [ 126] mc "..."
    [ 127] "I don't know about Yuri, but I'm kind of indifferent."
    [ 128] "If I showed as much enthusiasm as Monika wanted, then I would probably be lying."
    [ 129] "Still, if it's up to me to rescue this situation..."
    [ 130] mc "Um--"
    [ 131] show monika at f32 zorder 3
    [ 132] m 1i "No."
    [ 133] m "Natsuki's right, isn't she?"
    [ 134] m 1g "This club..."
    [ 135] m "It's nothing more than a place for a few people to hang out."
    [ 136] m 1r "Why did I think that everyone here saw it the same way as I did?"
    [ 137] show monika at t32 zorder 2
    [ 138] mc "But that doesn't mean that we're against getting new members or anything..."
    [ 139] show monika at f32 zorder 3
    [ 140] m 1i "[player], why did you even join this club?"
    [ 141] m "What were you hoping to get out of it?"
    [ 142] show monika at t32 zorder 2
    [ 143] mc "Well--"
    [ 144] "That's not really something I can be honest about, is it?"
    [ 145] show monika at f32 zorder 3
    [ 146] m 1p "In fact..."
    [ 147] m "If I remember, you weren't even given a choice not to join."
    [ 148] show monika at thide zorder 1
    [ 149] hide monika
    [ 150] "Monika sits down and stares at her desk."
    [ 151] m "What's the point of all this, anyway?"
    [ 152] m "What if starting this club was a mistake?"
    [ 153] mc "..."
    [ 154] show yuri at f33 zorder 3
    [ 155] y 2g "Now you've done it, Natsuki..."
    [ 156] show yuri at t33 zorder 2
    [ 157] show natsuki at f31 zorder 3
    [ 158] n 1p "What, me?"
    [ 159] n 1s "I just spoke my mind..."
    [ 160] n "Is it a crime to be honest?"
    [ 161] show natsuki at t31 zorder 2
    [ 162] show yuri at f33 zorder 3
    [ 163] y 2l "It's not about being honest."
    [ 164] y "It's about word choice."
    [ 165] y 2h "Besides, you have no right to speak for everyone else in the club like that..."
    [ 166] show yuri at t33 zorder 2
    [ 167] show natsuki at f31 zorder 3
    [ 168] n 1e "You don't understand at all!"
    [ 169] n 5s "I just..."
    [ 170] n "I just want a place that feels nice to hang out with a few friends."
    [ 171] n 5u "Is there a problem with the club being that for me?"
    [ 172] n "There aren't...there aren't many other places like that for me..."
    [ 173] n 5x "And now Monika wants to take it away from me!"
    [ 174] show natsuki at t31 zorder 2
    [ 175] mc "She's not taking anything away--"
    [ 176] show natsuki at f31 zorder 3
    [ 177] n 1g "No, [player]."
    [ 178] n "It's not the same."
    [ 179] n 1q "It won't be the same with the direction she wants to take it."
    [ 180] n "If I wanted that, then I could have just joined any other stupid club."
    [ 181] n 12d "But this one..."
    [ 182] n "I mean..."
    [ 183] n 12e "At least for a little bit of time..."
    [ 184] n "Things were nice."
    [ 185] "Natsuki starts packing up her things."
    [ 186] n 12d "I'm going home."
    [ 187] n "I feel like...I don't belong here right now."
    [ 188] show natsuki at t31 zorder 2
    [ 189] show yuri at f33 zorder 3
    [ 190] y 3t "Natsuki..."
    [ 191] show natsuki at thide zorder 1
    [ 192] hide natsuki
    [ 193] "Natsuki ignores Yuri and walks right out of the classroom."
    [ 194] show yuri at t11 zorder 2
    [ 195] y 3v "..."
    [ 196] y "This is bad..."
    [ 197] y "I don't know what to do..."
    [ 198] mc "Well..."
    [ 199] mc "Do you have an opinion on the festival?"
    [ 200] y 4b "I-I don't know..."
    [ 201] 
    [ 202] y "I'm kind of indifferent, I guess..."
    [ 203] 
    [ 204] show black zorder 3
    [ 205] show y_glitch_head at 466eb4f7700b99848b6c4223add3e419 zorder 4
    [ 206] 
    [ 207] 
    [ 208] play music "7e479bbabc162c2488504750637ff7fd"
    [ 209] y "Who cares about that obnoxious brat?"
    [ 210] 
    [ 211] 
    [ 212] play music "56dde94a702372440973101515b0b303"
    [ 213] hide black
    [ 214] hide y_glitch_head
    [ 215] 
    [ 216] y "I mean, I like how nice and quiet the club is right now..."
    [ 217] y "And I'm just...happy with you here..."
    [ 218] y 2t "But still!"
    [ 219] y "I'm the Vice President..."
    [ 220] y "It's not right for me to ignore my responsibilities like that..."
    [ 221] 
    [ 222] show black zorder 3
    [ 223] show y_glitch_head at 325439f72db347945be64c914e8575d2 zorder 4
    [ 224] 
    [ 225] 
    [ 226] play music "8d645a6c559a042428d1dbcc2c84ea6a"
    [ 227] y "Nobody would cry if she killed herself."
    [ 228] 
    [ 229] 
    [ 230] stop music
    [ 231] 
    [ 232] play sound "51474a0977eb51f44afeb4d70c36f87a"
    [ 233] show blood_eye at e4262b7ec05d1f54e95c4ed5d0133203 zorder 5
    [ 234] 
    [ 235] stop sound
    [ 236] play music "3d5fe99b941bba3429f7012e91406cf0"
    [ 237] hide black
    [ 238] hide y_glitch_head
    [ 239] hide blood_eye
    [ 240] 
    [ 241] y 2l "I should do my best to consider everyone's perspective and make the decision that's right for the club."
    [ 242] y 1t "But what about you, [player]?"
    [ 243] y "What do you want to get out of this club?"
    [ 244] "Yuri repeats the same question as Monika."
    [ 245] "I decide giving an indirect answer is better than nothing."
    [ 246] mc "...I think the most important thing is for everyone to get along..."
    [ 247] mc "...And for the club to provide something that you can't get anywhere else."
    [ 248] mc "I don't think it's about how many members, but rather the quality of each member."
    [ 249] mc "That's what will end up making the Literature Club a special place."
    [ 250] y 1u "I see..."
    [ 251] y "I really agree with you."
    [ 252] show blood_eye2 at d694a9e9596653944a904a63b1397d5e zorder 3
    [ 253] y 1f "Each member contributes their own qualities in a special way."
    [ 254] y "With each change in members, the identity of the club as a whole will change, too."
    [ 255] y 1h "I don't think that's necessarily a bad thing."
    [ 256] y "Stepping out of your comfort zone once in a while..."
    [ 257] y 1a "So if you would like to help Monika with the festival, then I'm on your side as well."
    [ 258] hide blood_eye2
    [ 259] mc "Alright."
    [ 260] mc "Well, maybe we can all talk to Natsuki tomorrow..."
    [ 261] "Yuri nods."
    [ 262] show monika 1g at f21 zorder 3
    [ 263] show yuri at t22 zorder 2
    [ 264] m "Hey, Yuri..."
    [ 265] show monika at t21 zorder 2
    [ 266] show yuri at f22 zorder 3
    [ 267] y 1t "Eh?"
    [ 268] show yuri at t22 zorder 2
    [ 269] show monika at f21 zorder 3
    [ 270] m 1p "Um, I know things were a little awkward yesterday..."
    [ 271] m "But I feel like you deserve to know that I still think you're a wonderful vice president."
    [ 272] m 1e "And also, a wonderful friend."
    [ 273] show monika at t21 zorder 2
    [ 274] show yuri at f22 zorder 3
    [ 275] y 3s "M-Monika..."
    [ 276] show yuri at t22 zorder 2
    [ 277] show monika at f21 zorder 3
    [ 278] m 2e "I want to do everything I can to make this the best club ever."
    [ 279] m "Okay?"
    [ 280] show monika at t21 zorder 2
    [ 281] show yuri at f22 zorder 3
    [ 282] y "...Me too."
    [ 283] show yuri at t22 zorder 2
    [ 284] show monika at f21 zorder 3
    [ 285] m 1a "Yeah..."
    [ 286] m "Let's all go home for today."
    [ 287] m "We'll talk about the festival tomorrow."
    [ 288] show monika at t21 zorder 2
    [ 289] show yuri at f22 zorder 3
    [ 290] y 1m "Okay."
    [ 291] y "I look forward to it."
    [ 292] y 1a "Shall we go, [player]?"
    [ 293] show yuri at t22 zorder 2
    [ 294] show monika at f21 zorder 3
    [ 295] m 1d "Um--"
    [ 296] m 1p "Please don't take this the wrong way, but..."
    [ 297] m "I'm going to chat a little bit with [player] before we leave."
    [ 298] m 1d "Just to see what he thinks of his time here and all that..."
    [ 299] m "It's important to me, as President."
    [ 300] show monika at t21 zorder 2
    [ 301] show yuri at f22 zorder 3
    [ 302] y 2v "..."
    [ 303] "Yuri looks a little troubled, but she doesn't protest."
    [ 304] y 2t "Okay."
    [ 305] y 2s "I trust your judgment, Monika."
    [ 306] y "In that case, I'll see the two of you tomorrow."
    [ 307] show yuri at t22 zorder 2
    [ 308] show monika at f21 zorder 3
    [ 309] m 1j "See you tomorrow~"
    [ 310] show yuri at thide zorder 1
    [ 311] hide yuri
    [ 312] "Monika waves as Yuri exits the classroom."
    [ 313] show monika 2a at t11 zorder 2
    [ 314] m "Phew..."
    [ 315] m 2e "Things have been a bit hectic lately, haven't they?"
    [ 316] show darkred at 817e2ea1ead663e429ecdbee72733242
    [ 317] show noise at dabcfe8fd5416ed49aa4c52dc909dba8
    [ 318] m "[player], I just wanted to make sure you're enjoying your time at this club."
    [ 319] m "I would really hate to see you unhappy."
    [ 320] m 2m "I feel kind of like I'm responsible for that, as President..."
    [ 321] stop music
    [ 322] m 4e "And I really do care about you...you know?"
    [ 323] m "I don't like seeing the other girls give you a hard time."
    [ 324] m 4r "With how mean Natsuki is and everything..."
    [ 325] m 4m "And Yuri being a little bit...you know."
    [ 326] m 5a "Ahaha..."
    [ 327] m "Sometimes it feels like you and I are the only real people here."
    [ 328] m "You know what I mean?"
    [ 329] m 1g "But it's weird, because in all the time you've been here, we've hardly gotten to spend any time together."
    [ 330] m 1n "Ah...I mean..."
    [ 331] m "I guess it's technically only been a couple days..."
    [ 332] m 1l "Sorry, I didn't mean to say something weird!"
    [ 333] m 1e "There are just some things I've been hoping to talk about with you..."
    [ 334] m "Things I know only you could understand."
    [ 335] stop music fadeout 3
    [ 336] show black at 09f4733a5eff2944087135fd8046a427 onlayer front
    [ 337] m "So that's why--{w=0.75}{nw}"
    [ 338] m 1g "Wait, not yet!{w=0.5}{nw}"
    [ 339] m "No!{w=0.5}{nw}"
    [ 340] m "Stop it!{w=1}{nw}"
    [ 341] hide noise
    [ 342] window auto
    [ 343] return
