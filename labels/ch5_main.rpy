label ch5_main:
    [   0] stop music fadeout 2
    [   1] scene bg residential_day
    [   2] with dissolve_scene_full
    [   3] unless persistent.content_warnings_enabled == True goto [6]
    [   4] 
    [   5] goto [6]
    [   6] pass
    [   7] dc "Don't Skip Previous Line on AutoSave"    # say, developer commentary
    [   8] 
    [   9] "It's the day of the festival."
    [  10] "Of all days, I expected this to be the one where I'd be walking to school with Sayori."
    [  11] "But Sayori isn't answering her phone."
    [  12] "I considered going to her house to wake her up, but decided that's a little too much."
    [  13] "Meanwhile, the preparations for the event should be nearly complete."
    [  14] unless ch4_scene == "natsuki" goto [18]
    [  15] "I managed to carry all the cupcakes myself by carefully stacking two trays."
    [  16] "Natsuki is already texting up a storm, but I can't respond, thanks to my hands being full."
    [  17] goto [20]
    [  18] "The banner Yuri and I painted is dry, and I gently rolled it up to take with me."
    [  19] "She sent me a pleasant text reminding me not to forget anything, and I reassured her."
    [  20] pass
    [  21] "Funnily enough, I probably feel the same way as Natsuki about the event."
    [  22] "I'm more excited for it to be over so I can spend time with Sayori and [ch4_name] at the festival."
    [  23] "But knowing Monika, I'm sure the event will be great, too."
    [  24] with None
    [  25] scene bg club_day
    [  26] with wipeleft_scene
    [  27] show monika 5 at t11 zorder 2
    [  28] m "[player]!"
    [  29] m "You're the first one here."
    [  30] m "Thanks for being early!"
    [  31] mc "That's funny, I thought at least Yuri would be here by now."
    [  32] "Monika is placing little booklets on each of the desks in the classroom."
    [  33] "They must be the ones she prepared that have all the poems we're performing."
    [  34] "In the end, I found a random poem online that I thought Monika would like, and submitted it."
    [  35] "So, that's the one I'll be performing."
    [  36] m 1d "I'm surprised you didn't bring Sayori with you."
    [  37] mc "Yeah, she overslept again..."
    [  38] mc "That dummy."
    [  39] mc "You'd think that on days this important, she'd try a little harder..."
    [  40] "I say that, but I suddenly remember what Sayori told me yesterday..."
    [  41] "And I suddenly feel awful, knowing it's not nearly that simple for her."
    [  42] "I only said it because it's the way I'm used to thinking."
    [  43] "But..."
    [  44] "Maybe I should have gone to wake her up after all?"
    [  45] m 1k "Ahaha."
    [  46] m 4b "You should take a little responsibility for her, [player]!"
    [  47] m "I mean, especially after your exchange with her yesterday..."
    [  48] m "You kind of left her hanging this morning, you know?"
    [  49] show monika 4a
    [  50] mc "Exchange...?"
    [  51] mc "Monika-- You know about that??"
    [  52] m 2a "Of course I do."
    [  53] m "I'm the club president, after all."
    [  54] mc "But--!"
    [  55] "I stammer, embarrassed."
    [  56] "Did Sayori really tell her about it that quickly?"
    [  57] unless sayori_confess goto [61]
    [  58] "That we're...a couple now?"
    [  59] "I didn't really plan on bringing it up with anyone yet..."
    [  60] goto [64]
    [  61] "About how I basically turned down her confession?"
    [  62] "That makes me really seem like the bad guy here..."
    [  63] "But I'm the one who knows what's best for her, right?"
    [  64] pass
    [  65] mc "Jeez..."
    [  66] mc "You don't know the full story at all, so..."
    [  67] m 2j "Don't worry."
    [  68] m "I probably know a lot more than you think."
    [  69] mc "Eh...?"
    [  70] "Monika is being as friendly as usual, but for some reason I felt a chill down my spine after hearing that."
    [  71] m 5 "Hey, do you want to check out the pamphlets?"
    [  72] m "They came out really nice!"
    [  73] mc "Yeah, sure."
    [  74] "I grab one of the pamphlets laid out on the desks."
    [  75] mc "Oh yeah, they really did."
    [  76] mc "Something like this will definitely help people take the club more seriously."
    [  77] m "Yeah, I thought so too!"
    [  78] show monika at thide zorder 1
    [  79] hide monika
    [  80] "I flip through the pages."
    [  81] "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    [  82] "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."
    [  83] mc "What's this...?"
    [  84] "I flip to Sayori's poem."
    [  85] "It's different from the one she practiced."
    [  86] "It's one that I haven't read before..."
    [  87] call showpoem(<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["poem_s3"], constantObjects=[] }>, music=<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[0], constantStrings=[], constantObjects=[] }>)
    [  88] mc "Ah--"
    [  89] "What is this...?"
    [  90] "Reading the poem, I get a pit in my stomach."
    [  91] show monika 1d at t11 zorder 2
    [  92] m "[player]?"
    [  93] m "What's wrong?"
    [  94] mc "Ah, nothing..."
    [  95] "This poem feels completely different from everything else Sayori's written."
    [  96] "But more than that..."
    [  97] mc "I-I changed my mind!"
    [  98] mc "I'm going to go get Sayori, so..."
    [  99] m "Ah--"
    [ 100] m 1b "Well, alright!"
    [ 101] m "Try not to take too long, okay?"
    [ 102] with None
    [ 103] scene bg corridor
    [ 104] with wipeleft
    [ 105] "I quickly leave the classroom."
    [ 106] m "Don't strain yourself~"
    [ 107] "Monika calls that out after me."
    [ 108] "I quicken my pace."
    [ 109] with None
    [ 110] scene bg residential_day
    [ 111] with wipeleft_scene
    [ 112] "What was I thinking?"
    [ 113] "I should have tried a little bit harder for Sayori."
    [ 114] "It's not a big deal to at least wait for her, or help her wake up."
    [ 115] "Even the simple gesture of walking her to school makes her really happy."
    [ 116] "Besides..."
    [ 117] "I told her yesterday that things will be the same as they always have been."
    [ 118] "That's all she needs, and what I want to give her."
    [ 119] with None
    [ 120] scene bg house
    [ 121] with wipeleft
    [ 122] "I reach Sayori's house and knock on the door."
    [ 123] "I don't expect an answer, since she's not picking up her phone, either."
    [ 124] "Like yesterday, I open the door and let myself in."
    [ 125] with None
    [ 126] scene black
    [ 127] with wipeleft
    [ 128] mc "Sayori?"
    [ 129] "She really is a heavy sleeper..."
    [ 130] "I swallow."
    [ 131] "I can't believe I ended up doing this after all."
    [ 132] "Waking her up in her own house..."
    [ 133] unless sayori_confess goto [136]
    [ 134] "That really is something that a boyfriend would do, isn't it?"
    [ 135] goto [137]
    [ 136] "Isn't that more like something a boyfriend would do?"
    [ 137] pass
    [ 138] "In any case..."
    [ 139] "It just feels right."
    [ 140] "Outside Sayori's room, I knock on her door."
    [ 141] mc "Sayori?"
    [ 142] mc "Wake up, dummy..."
    [ 143] "There's no response."
    [ 144] "I really didn't want to have to enter her room like this..."
    [ 145] "Isn't it kind of a breach of privacy?"
    [ 146] "But she really leaves me no choice."
    [ 147] "I gently open the door."
    [ 148] mc ".{cps=30}......Sayo--{/cps}{nw}"
    [ 149] 
    [ 150] 
    [ 151] 
    [ 152] 
    [ 153] 
    [ 154] 
    [ 155] 
    [ 156] window hide(None)
    [ 157] window auto
    [ 158] play music "td"
    [ 159] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="bgm_sayonara", UnlockId=1610925366 }
    [ 160] show s_kill_bg2
    [ 161] show s_kill2
    [ 162] show s_kill_bg as s_kill_bg at s_kill_bg_start
    [ 163] show s_kill as s_kill at s_kill_start
    [ 164] 
    [ 165] show s_kill_bg2 as s_kill_bg
    [ 166] show s_kill2 as s_kill
    [ 167] 
    [ 168] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [ 169] play sound "096731335a0022b45a416ca418260076"
    [ 170] 
    [ 171] stop sound
    [ 172] hide screen tear
    [ 173] call screen_tear_hide
    [ 174] hide s_kill_bg
    [ 175] hide s_kill
    [ 176] show s_kill_bg_zoom zorder 1
    [ 177] show s_kill_bg2_zoom zorder 1
    [ 178] show s_kill_zoom zorder 3
    [ 179] show s_kill2_zoom zorder 3
    [ 180] show s_kill as s_kill at 71eac053a44d90243bfbabdebf67561a zorder 3
    [ 181] 
    [ 182] show noise at e2de5fcd185a9b0459c867f39cc2f034 zorder 3
    [ 183] show vignette at 0c95f36aa99e45044a1ee2a3001c8829 zorder 3
    [ 184] 
    [ 185] show white zorder 2
    [ 186] show splash_glitch zorder 2
    [ 187] 
    [ 188] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [ 189] play sound "05d33f5be3cc6cd46992577e1f23471d"
    [ 190] 
    [ 191] stop sound
    [ 192] hide screen tear
    [ 193] call screen_tear_hide
    [ 194] 
    [ 195] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [ 196] play sound "0206aac56c8b2ec4eb3f83be6da00d57"
    [ 197] 
    [ 198] stop sound
    [ 199] hide screen tear
    [ 200] call screen_tear_hide
    [ 201] hide splash_glitch
    [ 202] hide sf_splash_glitch
    [ 203] show splash_glitch2 zorder 2
    [ 204] show splash_glitch_m zorder 2
    [ 205] show splash_glitch_n zorder 2
    [ 206] show splash_glitch_y zorder 2
    [ 207] 
    [ 208] hide white
    [ 209] hide splash_glitch2
    [ 210] hide splash_glitch_m
    [ 211] hide splash_glitch_n
    [ 212] hide splash_glitch_y
    [ 213] show exception_bg zorder 2
    [ 214] show fake_exception at 04d05703cdf20db42831d0611dab87c8 zorder 2
    [ 215] show fake_exception2 at 87deb25309bd34040971ede33c1e4e3d zorder 2
    [ 216] python:    # runs C# ch5_main_inlinepythonblock_253810834
                
    [ 217] 
    [ 218] 
    [ 219] "..."
    [ 220] hide fake_exception
    [ 221] hide fake_exception2
    [ 222] hide exception_bg
    [ 223] "What the hell...?"
    [ 224] "<i>What the hell??</i>"
    [ 225] "Is this a nightmare?"
    [ 226] "It...has to be."
    [ 227] "This isn't real."
    [ 228] "There's no way this can be real."
    [ 229] "Sayori wouldn't do this."
    [ 230] "Everything was normal up until a few days ago."
    [ 231] "That's why I can't believe what my eyes are showing me...!"
    [ 232] with None
    [ 233] scene black
    [ 234] with dissolve_cg
    [ 235] "I suppress the urge to vomit."
    [ 236] "Just yesterday..."
    [ 237] "I told Sayori I would be there for her."
    [ 238] "I told her I know what's best, and that everything will be okay."
    [ 239] "Then why...?"
    [ 240] "Why would she do this...?"
    [ 241] "How could I be so helpless?"
    [ 242] "What did I do wrong?"
    [ 243] unless sayori_confess goto [250]
    [ 244] "Confessing to her..."
    [ 245] "I shouldn't have confessed to her."
    [ 246] "That's not what Sayori needed at all."
    [ 247] "She even told me how painful it is for others to care about her."
    [ 248] "Then why did I confess to her, and make her feel even worse?"
    [ 249] goto [254]
    [ 250] "Turning down her confession..."
    [ 251] "That has to have been what pushed her over the edge."
    [ 252] "Her agonized scream still echoes in my ears."
    [ 253] "Why did I do that to her when she needed me the most?"
    [ 254] pass
    [ 255] "Why was I so selfish?"
    [ 256] "This is my fault--!"
    [ 257] "My swarming thoughts keep telling me everything I could have done to prevent this."
    [ 258] "If I just spent more time with her."
    [ 259] "Walked her to school."
    [ 260] unless sayori_confess goto [263]
    [ 261] "And remained friends with her, like it always has been..."
    [ 262] goto [264]
    [ 263] "And gave her what I know she wanted out of our relationship..."
    [ 264] pass
    [ 265] "...Then I could have prevented this."
    [ 266] "I know I could have prevented this!"
    [ 267] "Screw the Literature Club."
    [ 268] "Screw the festival."
    [ 269] "I just...lost my best friend."
    [ 270] "Someone I grew up with."
    [ 271] "She's gone forever now."
    [ 272] "Nothing I do can bring her back."
    [ 273] "This isn't some game where I can reset and try something different."
    [ 274] "I had only one chance, and I wasn't careful enough."
    [ 275] "And now I'll carry this guilt with me until I die."
    [ 276] "Nothing in my life is worth more than hers..."
    [ 277] "But I still couldn't do what she needed from me."
    [ 278] "And now..."
    [ 279] "I can never take it back."
    [ 280] "Never."
    [ 281] "Never."
    [ 282] "Never."
    [ 283] "Never."
    [ 284] "Never..."
    [ 285] 
    [ 286] 
    [ 287] return
