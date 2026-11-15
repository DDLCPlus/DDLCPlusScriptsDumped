label sayori_exclusive_2:
    [   0] unless not renpy.music.get_playing(channel='music') == audio.t2 goto [3]
    [   1] stop music fadeout 1
    [   2] goto [3]
    [   3] pass
    [   4] scene bg club_day
    [   5] with wipeleft_scene
    [   6] unless not renpy.music.get_playing(channel='music') == audio.t2 goto [9]
    [   7] play music "t2"
    [   8] goto [9]
    [   9] pass
    [  10] s "[player], [player]!"
    [  11] "Sayori suddenly comes up to me."
    [  12] show sayori 1x at t11 zorder 2
    [  13] s "I'm gonna go get some supplies from another classroom."
    [  14] s "Want to come with me?"
    [  15] mc "Supplies?"
    [  16] mc "What for?"
    [  17] s 2a "Well, you know how the festival is coming up?"
    [  18] s "Me and Monika were gonna make some posters and stuff."
    [  19] s "So I need to go find some crayons, and markers, and glue sticks..."
    [  20] mc "Ah, I see."
    [  21] mc "Sure, I'll go with you."
    [  22] s 4q "Yaay~"
    [  23] s 4x "Okay Monika, we'll be back soon!"
    [  24] show sayori at t22 zorder 2
    [  25] show monika 1a at f21 zorder 3
    [  26] m "Ah, are you going with [player] to get the supplies?"
    [  27] m "There's no need to trouble yourself."
    [  28] m "I'd be happy to go with him."
    [  29] show monika at t21 zorder 2
    [  30] show sayori 1h at s22
    [  31] s "Aw, but I wanted to go!"
    [  32] s "It's so much fun exploring empty classrooms and stuff!"
    [  33] show monika at f21 zorder 3
    [  34] m 2j "Hehe, okay, okay."
    [  35] m 2a "It was just a suggestion."
    [  36] m "See if you can find poster paper too, okay?"
    [  37] show monika at t21 zorder 2
    [  38] show sayori at f22 zorder 3
    [  39] s 1r "Okaay~!"
    [  40] s 1a "Ready, [player]?"
    [  41] mc "Yep, let's go."
    [  42] scene bg corridor
    [  43] show sayori 4a at t11 zorder 2
    [  44] with wipeleft_scene
    [  45] "Sayori and I exit the clubroom."
    [  46] "I follow behind as Sayori hums and skips around the hallway."
    [  47] "Honestly..."
    [  48] "It feels like I'm taking a kid to the mall or something."
    [  49] "Sayori finds pleasure in the simplest things sometimes."
    [  50] mc "Hey, Sayori..."
    [  51] mc "What exactly are we doing for the festival, anyway?"
    [  52] mc "I'm not sure how you would make an event out of literature..."
    [  53] s 1q "Ehehe!"
    [  54] s 1x "Me and Monika have it all planned out!"
    [  55] s "Don't you worry~"
    [  56] mc "Is that so...?"
    [  57] s "Yup!"
    [  58] s "We're gonna do a poetry performance!"
    [  59] mc "A performance...?"
    [  60] mc "Of what kind?"
    [  61] s 1c "Well..."
    [  62] s "Everyone is gonna take turns on stage..."
    [  63] s 1x "And recite their favorite poems!"
    [  64] mc "Ah..."
    [  65] mc "That sounds..."
    [  66] "...Kind of dull?"
    [  67] s 1h "[player]!"
    [  68] s "You're not thinking about it the right way at all!"
    [  69] s "It's not just about reading poems..."
    [  70] s 1x "It's about performing them!"
    [  71] s "Like, you say the lines of the poem like..."
    [  72] s 2j "<i>Between my feet...</i>"
    [  73] s "<i>The last remaining flower beckons to me.</i>"
    [  74] s 1c "<i>I twist the stem, freeing it from its clinging roots...</i>"
    [  75] s "<i>Caressing the final joyous moment between my fingers.</i>"
    [  76] s 3g "<i>But to what ends have I summoned this joy?</i>"
    [  77] s "<i>For now when I look in every direction...</i>"
    [  78] s 1j "<i>The once-prosperous field before me...</i>"
    [  79] show sayori at h11
    [  80] s 4m "<i>Is but a barren wasteland!</i>"
    [  81] s "..."
    [  82] s 1r "Like that!!"
    [  83] mc "Sayori..."
    [  84] "How do I put this..."
    [  85] mc "I'm sure it's just me, but it's impossible for me to take you seriously when you talk like that..."
    [  86] show sayori 5c at s11
    [  87] s "Ehhh?"
    [  88] s "You meanie!"
    [  89] s "I'm working super hard on this, you know!"
    [  90] mc "Ah, I know, I know!"
    [  91] mc "I just meant that it's a pretty unordinary contrast to your cute self."
    [  92] show sayori 4s at t11 zorder 2
    [  93] s "Ahaha! Don't say that, it's embarrassing!"
    [  94] s 4y "But I guess that means I'm doing a good job~"
    [  95] mc "Yeah, I guess so..."
    [  96] show sayori at h11
    [  97] s 4r "Aaah, I'm so excited!"
    [  98] s "The festival is going to be so much fun~"
    [  99] "Sayori spins herself around in the hallway again."
    [ 100] s 1x "Hey, [player], this classroom over here is empty!"
    [ 101] s "Let's begin the mission!"
    [ 102] show sayori at thide zorder 1
    [ 103] hide sayori
    [ 104] mc "The mission, eh...?"
    [ 105] "It's been a long time since I've spent time with Sayori like this."
    [ 106] "But in the end, she hasn't changed one bit."
    [ 107] "She's nothing but a ball of sunshine, drawing happy vibes from the world around her."
    [ 108] "It's a pretty nostalgic feeling for me."
    [ 109] "As the years went by, I began to hole myself up in my room more and more."
    [ 110] "So going adventuring with Sayori brings about a special sort of feeling I forgot I had in me."
    [ 111] scene bg class_day
    [ 112] with wipeleft_scene
    [ 113] "The two of us enter the classroom."
    [ 114] "Sayori heads straight to the closet, and I follow."
    [ 115] show sayori 1b at t11 zorder 2
    [ 116] s "Let's see what we have in here..."
    [ 117] s 4x "...Crayons!!"
    [ 118] "Sayori pulls a box full of crayons off the shelf."
    [ 119] s "They're the best brand, too!"
    [ 120] s 1b "They're kind of dirty, though..."
    [ 121] "Sayori starts pulling various crayons out of the box, reading the color names."
    [ 122] mc "Alright, that's one down."
    [ 123] mc "Don't get distracted, we still need to find--"
    [ 124] s 1a "Wait, I'm looking for my favorite color..."
    [ 125] mc "Fine, fine..."
    [ 126] mc "Then at least move aside so I can look for the poster paper."
    [ 127] s 1b "Ah, I dropped one by accident--"
    [ 128] play sound "a27391741102e6e4f82a015c5a8a8a12"
    [ 129] show white at dac37b34d287d8c418cf131b2ba55f15 zorder 4
    [ 130] show sayori 2p at h11
    [ 131] "<i>Smack!</i>"
    [ 132] hide white
    [ 133] s "Kya--!"
    [ 134] "Sayori bends over and smacks her forehead right into the shelf."
    [ 135] "She falls to the floor, and the crayons spill all over her lap."
    [ 136] show sayori 4p at s11
    [ 137] s "Owowowowow..."
    [ 138] mc "You okay?"
    [ 139] s "My forehead..."
    [ 140] "Sayori clutches her forehead."
    [ 141] mc "Jeez, Sayori..."
    [ 142] mc "That's just like you, isn't it?"
    [ 143] mc "C'mon, let me see."
    [ 144] "Since Sayori is sitting on the floor, I grab her by the waist and pull her out of the closet."
    [ 145] mc "You have to move your hands, Sayori..."
    [ 146] s 4g "But it hurts..."
    [ 147] mc "Just do it for a second."
    [ 148] 
    [ 149] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="sayori_exclusive2", UnlockId=1131709031 }
    [ 150] 
    [ 151] scene s_cg2_base1
    [ 152] show s_cg2_exp2
    [ 153] with dissolve_cg
    [ 154] "Sayori slowly releases her hands from her forehead."
    [ 155] "I gently brush her bangs to the side."
    [ 156] show s_cg2_exp1 at cgfade
    [ 157] show s_cg2_exp3 at cgfade
    [ 158] s "Ow--!"
    [ 159] mc "Sorry..."
    [ 160] "There's a huge red mark on the center of her forehead."
    [ 161] "A bump is starting to form, as well."
    [ 162] mc "Man, that's gonna swell up."
    [ 163] mc "I should find you some ice..."
    [ 164] hide s_cg2_exp3
    [ 165] hide s_cg2_exp1
    [ 166] s "[player]..."
    [ 167] mc "Where would I even find ice around this time...?"
    [ 168] mc "Ah, I guess a cold drink would do..."
    [ 169] s "You don't have to--!"
    [ 170] show s_cg2_exp2 at cgfade
    [ 171] hide s_cg2_exp2
    [ 172] s "I'm fine with--looking like a unicorn--"
    [ 173] "Even wincing from the pain, Sayori makes a silly joke."
    [ 174] mc "Ahaha, what are you saying?"
    [ 175] mc "I'll be right back, okay?"
    [ 176] s "O-Okay..."
    [ 177] stop music fadeout 1
    [ 178] with None
    [ 179] scene bg corridor
    [ 180] with wipeleft_scene
    [ 181] "I pat Sayori on the shoulder and run out into the hallway."
    [ 182] "I locate the nearest vending machine."
    [ 183] mc "What should I get...?"
    [ 184] "It doesn't really matter, since it will be used as an ice pack, rather than to drink."
    [ 185] "But I know Sayori likes apple juice, so I purchase that one."
    [ 186] "In just a moment, I'm already returning to the classroom where I left Sayori."
    [ 187] scene s_cg2_base1
    [ 188] show s_cg2_exp2
    [ 189] with wipeleft_scene
    [ 190] play music "t9"
    [ 191] "She has one palm on her forehead and is using the other hand to clumsily scoop crayons back into the box."
    [ 192] s "At least they were already in the wrong spots before I spilled them..."
    [ 193] mc "Sayori, here."
    [ 194] show s_cg2_base2 at cgfade behind s_cg2_exp2
    [ 195] "I hand Sayori the bottle of apple juice."
    [ 196] show s_cg2_exp2 at cgfade
    [ 197] hide s_cg2_exp2
    [ 198] s "It's nice and cold..."
    [ 199] "Sayori opens the cap and starts drinking from it."
    [ 200] mc "Sayori, what are you doing?!"
    [ 201] mc "It's for your forehead, idiot!"
    [ 202] show s_cg2_exp3 at cgfade
    [ 203] s "Ah--"
    [ 204] s "Sorry, I forgot~"
    [ 205] s "Ahahaha!"
    [ 206] mc "How hard did you hit your head...?"
    [ 207] "Sayori places the bottle against the bump on her head."
    [ 208] show s_cg2_exp1 at cgfade
    [ 209] s "It stings..."
    [ 210] mc "Just bear with it, it'll feel better soon."
    [ 211] mc "Looks like you cleaned up most of the crayons, so that's good."
    [ 212] hide s_cg2_exp1
    [ 213] hide s_cg2_exp3
    [ 214] s "Hey, [player]..."
    [ 215] s "This kind of reminds you of growing up, doesn't it...?"
    [ 216] mc "Eh? What do you mean?"
    [ 217] s "You know how we used to play outside all the time..."
    [ 218] s "I would always try to keep up with you."
    [ 219] s "You were kind of oblivious in some ways..."
    [ 220] s "Like I usually fell behind or had trouble climbing on the things you did..."
    [ 221] s "But sometimes when I tried to do things I couldn't, I would get myself hurt."
    [ 222] s "I'd fall and scrape myself, or get a bump..."
    [ 223] s "And I would start crying really hard."
    [ 224] show s_cg2_exp3 at cgfade
    [ 225] s "Ahaha!"
    [ 226] s "And you would rush over as quick as you could."
    [ 227] hide s_cg2_exp3
    [ 228] s "You would try really hard to get me to stop crying."
    [ 229] s "It was almost like you blamed yourself and were afraid of getting in trouble if someone found out..."
    [ 230] s "Even though it really wasn't your fault at all, you know?"
    [ 231] mc "Did I really do that...?"
    [ 232] s "Yeah...you don't remember?"
    [ 233] mc "Come to think of it, maybe I do remember a bit..."
    [ 234] mc "I guess I was always so focused on my games that I didn't pay enough attention to you."
    [ 235] mc "So in a way, it was my fault."
    [ 236] mc "Kind of like this time, too..."
    [ 237] mc "If I wasn't rushing you out of the closet, you probably wouldn't have hit your head."
    [ 238] s "[player]..."
    [ 239] s "I don't think you realize it, but you're always thinking about other people."
    [ 240] s "Even after all these years..."
    [ 241] s "You're rushing to help me, even though I'm just being clumsy."
    [ 242] show s_cg2_exp3 at cgfade
    [ 243] s "You're really a sweetheart..."
    [ 244] mc "D-Don't call me that!"
    [ 245] mc "And I don't really do this kind of thing all the time..."
    [ 246] mc "I guess when it comes to you, it just feels natural."
    [ 247] mc "Before I even know it, I'm treating you like that."
    [ 248] mc "I guess that's what happens when you've been friends for so long."
    [ 249] hide s_cg2_exp3
    [ 250] s "Really...?"
    [ 251] s "Maybe you're right..."
    [ 252] s "[player]..."
    [ 253] s "I'm so glad that nothing's changed between us."
    [ 254] s "Do you think it'll be like this forever?"
    [ 255] mc "Forever...?"
    [ 256] "If I'm honest to myself..."
    [ 257] "There's no telling where we'll each end up for college, or after that."
    [ 258] "So it wouldn't be fair for me to make any promises."
    [ 259] "But..."
    [ 260] mc "Well, I hope so."
    [ 261] mc "It's been this long already, right?"
    [ 262] mc "I can't imagine you ever changing, so my hopes are up."
    [ 263] s "I'm so happy..."
    [ 264] "Sayori has a whimsical expression in her eyes."
    [ 265] "We remain silent for a moment."
    [ 266] "She's so silly and clumsy on the outside that when I see her deep in thought like this..."
    [ 267] "It makes me not want to disturb her."
    [ 268] s "I guess we should go back..."
    [ 269] s "I don't want to worry Monika, you know?"
    [ 270] mc "Good luck with that."
    [ 271] mc "She's gonna see your forehead either way."
    [ 272] s "Not if I hide it under my bangs~"
    [ 273] play music "t8" fadeout 1
    [ 274] scene bg class_day
    [ 275] show sayori 1a at i11 zorder 2
    [ 276] with dissolve_cg
    [ 277] "Sayori hops to her feet."
    [ 278] show sayori 4p at s11
    [ 279] s "A-Aaahh--!"
    [ 280] "She clutches her forehead again."
    [ 281] mc "Don't stand up so fast after hurting yourself!"
    [ 282] s "Uuuu..."
    [ 283] mc "Well, I guess it's too late now..."
    [ 284] mc "Anyway, let's go."
    [ 285] scene bg corridor
    [ 286] with wipeleft_scene
    [ 287] "I follow Sayori out of the classroom."
    [ 288] "Sayori plays with her bangs to try to hide the bump, but without much success."
    [ 289] "In a moment, we make it back to the clubroom."
    [ 290] scene bg club_day
    [ 291] show sayori 1a at t21 zorder 2
    [ 292] show monika 1b at t22 zorder 2
    [ 293] with wipeleft_scene
    [ 294] show monika at f22 zorder 3
    [ 295] m "Ah, you're back!"
    [ 296] m "Good timing, I was just about ready to start with sharing our poems."
    [ 297] m 1d "Eh? Sayori, your forehead..."
    [ 298] show monika at t22 zorder 2
    [ 299] mc "She's fine, don't worry about--"
    [ 300] show sayori 4r at f21 zorder 3
    [ 301] s "I was playing with the crayons and smacked my forehead into the shelf!"
    [ 302] show sayori at t21 zorder 2
    [ 303] mc "..."
    [ 304] show monika 3m at f22 zorder 3
    [ 305] m "..."
    [ 306] m 3l "...Well, anyway!"
    [ 307] m 1a "Were you able to find everything we needed?"
    [ 308] show monika at t22 zorder 2
    [ 309] show sayori 1x at f21 zorder 3
    [ 310] s "Uh-huh! I have it right--"
    [ 311] s 1n "...Eh?"
    [ 312] "Sayori frantically glances around herself."
    [ 313] show sayori 4m at hf21 zorder 3
    [ 314] s "I...forgot all of the stuff!!"
    [ 315] show sayori at t21 zorder 2
    [ 316] mc "Calm down, Sayori."
    [ 317] mc "I have it all right here."
    [ 318] mc "I found the poster paper, too."
    [ 319] show sayori 4b
    [ 320] show monika 5a at f22 zorder 3
    [ 321] m "Ahaha!"
    [ 322] m "Sounds like you ended up doing all the work, [player]."
    [ 323] show monika at t22 zorder 2
    [ 324] mc "Ah, well, Sayori--"
    [ 325] "I fail to come up with an excuse for Sayori."
    [ 326] show sayori 1q at f21 zorder 3
    [ 327] s "I made it an adventure!"
    [ 328] show sayori 1a at t21 zorder 2
    [ 329] mc "...Yeah, that."
    [ 330] show monika 1j at f22 zorder 3
    [ 331] m "Ahaha, okay, okay."
    [ 332] m 1a "In any case, good work!"
    [ 333] m "I'll start working on the posters tonight."
    [ 334] show monika at t22 zorder 2
    [ 335] show sayori 4x at f21 zorder 3
    [ 336] s "Me too!"
    [ 337] show monika at t11 zorder 2
    [ 338] show sayori at thide behind monika
    [ 339] hide sayori
    [ 340] m 4b "...Okay, everyone!"
    [ 341] m "Are you ready to share your poems?"
    [ 342] mc "Guess I should grab mine..."
    [ 343] "After making sure the crayon box is closed tightly, I return to my seat."
    [ 344] return
