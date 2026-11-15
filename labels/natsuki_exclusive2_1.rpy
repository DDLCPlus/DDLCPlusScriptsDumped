label natsuki_exclusive2_1:
    [   0] scene bg club_day
    [   1] with wipeleft_scene
    [   2] n "Ugh...!"
    [   3] "I hear Natsuki utter an exasperated sigh from within the closet."
    [   4] "She seems to be annoyed by something."
    [   5] "I approach her, in case she needs a hand."
    [   6] play music "t6" fadeout 1
    [   7] scene bg closet
    [   8] unless persistent.content_warnings_enabled == True goto [11]
    [   9] 
    [  10] goto [11]
    [  11] pass
    [  12] show natsuki 4r at t11 zorder 2
    [  13] with wipeleft_scene
    [  14] 
    [  15] mc "You looking for something in there?"
    [  16] 
    [  17] n 4x "fucking monikammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
    [  18] 
    [  19] 
    [  20] n "She never puts my stuff back in the right spot!"
    [  21] n "What's the point in keeping your collection organized if someone else is just gonna mess it up?"
    [  22] "Natsuki slides a bunch of stacked books and boxes across the shelf."
    [  23] mc "Manga..."
    [  24] n 2c "You read manga, right?"
    [  25] mc "Ah--"
    [  26] mc "...Sometimes..."
    [  27] "Manga is one of those things where you can't admit you're really into it until you figure out where the other person stands."
    [  28] mc "...How did you know, anyway?"
    [  29] n 2k "I heard you bring it up at some point."
    [  30] n "Besides, it's kind of written on your face."
    [  31] "What's that supposed to mean...?"
    [  32] mc "I-I see..."
    [  33] "There's a lone volume of manga amidst a stack of various books on the side of one of the shelves."
    [  34] "Curious, I pull it out of the stack."
    [  35] n 1b "<i>There</i> it is!"
    [  36] "Natsuki snatches it out of my hand."
    [  37] "She then turns to a box of manga and slips the volume right into the middle of the rest."
    [  38] n 4d "Aah, much better!"
    [  39] n "Seeing a box set with one book missing is probably the most irritating sight in the world."
    [  40] mc "I know that feel..."
    [  41] "I get a closer look at the box set she's admiring."
    [  42] mc "Parfait Girls...?"
    [  43] "It's a series I've never heard of in my life."
    [  44] "That probably means it's either way out of my demographic, or it's simply terrible."
    [  45] n 5g "If you're gonna judge, you can go do it through the glass on that door."
    [  46] "She points to the classroom door."
    [  47] mc "H-Hey, I wasn't judging anything...!"
    [  48] mc "I didn't even say anything."
    [  49] n 5c "It was the tone of your voice."
    [  50] 
    [  51] n "But I'll tell you one thing, [player]."
    [  52] n 4l "Consider this a lesson straight from the Literature Club:{nw}"
    [  53] 
    [  54] 
    [  55] n "don't judge a bookkkkkkkkkkkkkkkkk kkkkk kk k  k      k        k          k"
    [  56] 
    [  57] 
    [  58] n "In fact--"
    [  59] "Natsuki pulls out the first volume of Parfait Girls from the box."
    [  60] n "I'm gonna show you exactly why!"
    [  61] "She shoves the book right into my hands."
    [  62] mc "Ah..."
    [  63] "I stare at the cover."
    [  64] "It features four girls in colorful attire striking animated feminine poses."
    [  65] "It's...exceedingly \"moe\"."
    [  66] n 4b "Don't just stand there!"
    [  67] mc "Uwa--"
    [  68] show natsuki at thide zorder 1
    [  69] hide natsuki
    [  70] "Natsuki grabs my arm and pulls me out of the closet."
    [  71] "She then takes a seat against the wall, beneath the windowsills."
    [  72] "She pats on the ground next to her, signaling me to sit there."
    [  73] show bg club_day
    [  74] show natsuki 2a at t11 zorder 2
    [  75] with wipeleft
    [  76] mc "Wouldn't chairs be more comfortable...?"
    [  77] "I take my seat."
    [  78] n 2k "Chairs wouldn't work."
    [  79] n "We can't read at the same time like that."
    [  80] mc "Eh? Why's that?"
    [  81] mc "Ah...I guess it's easier to be close together like this..."
    [  82] n 2o "--!"
    [  83] n 5r "D-Don't just say that!"
    [  84] n "You'll make me feel weird about it!"
    [  85] "Natsuki crosses her arms and scootches an inch away from me."
    [  86] mc "Sorry..."
    [  87] show natsuki 5g
    [  88] "I didn't exactly expect to be sitting this close to her, either..."
    [  89] "Not that I can say it's a particularly bad thing."
    [  90] "I open the book."
    [  91] "It's only a few seconds before Natsuki once again inches closer, reclaiming the additional space while she hopes I won't notice."
    [  92] "I can feel her peering over my shoulder, much more eager to begin reading than I am."
    [  93] n 1k "Wow, how long has it been since I read the beginning...?"
    [  94] mc "Hm?"
    [  95] mc "You don't go back and flip through the older volumes every now and then?"
    [  96] n 2k "Not really."
    [  97] n "Maybe sometimes after I've already finished the series."
    [  98] n 2c "Hey, are you paying attention?"
    [  99] mc "Uh..."
    [ 100] "I am, but nothing's really happened yet, so I can talk at the same time."
    [ 101] "It looks like it's about a bunch of friends in high school."
    [ 102] "Typical slice-of-life affair."
    [ 103] "I kind of grew out of these, since it's rare for the writing to be entertaining enough to make up for the lack of plot."
    [ 104] 
    [ 105] 
    [ 106] scene n_cg1_bg
    [ 107] show n_cg1_base
    [ 108] with dissolve_cg
    [ 109] mc "...Are you sure this isn't boring for you?"
    [ 110] n "It's not!"
    [ 111] mc "Even though you're just watching me read?"
    [ 112] n "Well...!"
    [ 113] n "I'm...fine with that."
    [ 114] mc "If you say so..."
    [ 115] mc "...I guess it's fun sharing something you like with someone else."
    [ 116] mc "I always get excited when I convince any of my friends to pick up a series I enjoy."
    [ 117] mc "You know what I mean?"
    [ 118] n "...?"
    [ 119] mc "Hm?"
    [ 120] mc "You don't?"
    [ 121] show n_cg1_exp2 at cgfade
    [ 122] n "Um..."
    [ 123] n "That's not..."
    [ 124] n "Well, I wouldn't really know."
    [ 125] mc "...What do you mean?"
    [ 126] mc "Don't you share your manga with your friends?"
    [ 127] hide n_cg1_exp2
    [ 128] show n_cg1_exp3 at cgfade
    [ 129] n "Could you not rub it in?"
    [ 130] n "Jeez..."
    [ 131] mc "Ah... Sorry..."
    [ 132] n "Hmph."
    [ 133] n "Like I could ever get my friends to read this..."
    [ 134] n "They just think manga is for kids."
    [ 135] n "I can't even bring it up without them being all like..."
    [ 136] n "'Eh? You still haven't grown out of that yet?'"
    [ 137] n "Makes me want to punch them in the face..."
    [ 138] mc "Urgh, I know those kinds of people..."
    [ 139] mc "Honestly, it takes a lot of effort to find friends who don't judge, much less friends who are also into it..."
    [ 140] mc "I'm already kind of a loser, so I guess I gravitated toward the other losers over time."
    [ 141] mc "But it's probably harder for someone like you..."
    [ 142] hide n_cg1_exp3
    [ 143] n "Hm."
    [ 144] n "Yeah, that's pretty accurate."
    [ 145] "<i>...Wait, which part??</i>"
    [ 146] 
    [ 147] n "I mean, I feel like I can't even keep it in my own room..."
    [ 148] 
    [ 149] n "My dad would beat the shit out of me if he found this."
    [ 150] 
    [ 151] 
    [ 152] n "At least it's safe here in the clubroom."
    [ 153] show n_cg1_exp3 at cgfade
    [ 154] n "'Cept Monika's kind of a jerk about it..."
    [ 155] n "Ugh! I just can't win, can I?"
    [ 156] mc "Well, it paid off in the end, didn't it?"
    [ 157] mc "I mean, here I am, reading it."
    [ 158] n "Well, it's not like that solves any of my problems."
    [ 159] mc "Maybe..."
    [ 160] mc "But at least you're enjoying yourself, right?"
    [ 161] hide n_cg1_exp3
    [ 162] show n_cg1_exp2 at cgfade
    [ 163] n "--"
    [ 164] n "..."
    [ 165] n "...So?"
    [ 166] mc "Ahaha."
    [ 167] hide n_cg1_exp2
    [ 168] show n_cg1_exp3 at cgfade
    [ 169] n "Jeez, that's enough!"
    [ 170] n "Are you gonna keep reading, or what?"
    [ 171] mc "Yeah, yeah..."
    [ 172] "I flip the page."
    [ 173] with None
    [ 174] show black zorder 5
    [ 175] with dissolve_cg
    [ 176] "..."
    [ 177] "..."
    [ 178] "....."
    [ 179] "......."
    [ 180] "........."
    [ 181] "Time passes."
    [ 182] hide n_cg1_exp3
    [ 183] show n_cg1_exp4 at cgfade zorder 4
    [ 184] "Natsuki is strangely quiet now."
    [ 185] "I glance over at her."
    [ 186] with None
    [ 187] hide black
    [ 188] with dissolve_cg
    [ 189] "It looks like she's started to fall asleep."
    [ 190] mc "Hey, Natsuki..."
    [ 191] hide n_cg1_exp4
    [ 192] show n_cg1_exp5 at cgfade
    [ 193] n "Y-Yeah...?"
    [ 194] "Suddenly, Natsuki collapses straight into me."
    [ 195] play sound "fall"
    [ 196] 
    [ 197] mc "H-Hey--"
    [ 198] 
    [ 199] show n_cg1b at n_cg1b_t
    [ 200] show n_cg1_exp5
    [ 201] 0.01
    [ 202] hide n_cg1_exp5
    [ 203] hide n_cg1_base
    [ 204] 
    [ 205] 
    [ 206] play music "t6g"
    [ 207] 
    [ 208] 
    [ 209] # RenpyDialogueLine: RenpyDialogueLine {  }
    [ 210] 
    [ 211] # RenpyDialogueLine: RenpyDialogueLine {  }
    [ 212] 
    [ 213] 
    [ 214] stop music
    [ 215] window hide(None)
    [ 216] window auto
    [ 217] scene bg club_day
    [ 218] show monika 1r at t11 zorder 2
    [ 219] m "Oh jeez..."
    [ 220] m 1d "Natsuki, are you okay?"
    [ 221] show monika at t21 zorder 2
    [ 222] show natsuki 12b at f22 zorder 3
    [ 223] n "..."
    [ 224] show natsuki at t22 zorder 2
    [ 225] show monika at f21 zorder 3
    [ 226] m 1a "Here..."
    [ 227] show monika at t21 zorder 2
    [ 228] "Monika reaches into her bag and pulls out some kind of protein bar."
    [ 229] "She throws it in Natsuki's direction."
    [ 230] "Natsuki's eyes suddenly light up again."
    [ 231] "She snatches the bar from the floor and immediately tears off the wrapper."
    [ 232] show natsuki at f22 zorder 3
    [ 233] n 1s "I told you not to give mmph..."
    [ 234] show natsuki at t22 zorder 2
    [ 235] "She doesn't even finish her sentence before stuffing it into her mouth."
    [ 236] show natsuki at thide zorder 1
    [ 237] hide natsuki
    [ 238] show monika 3b at t11 zorder 2
    [ 239] m "Don't worry, [player]."
    [ 240] m "She's fine."
    [ 241] m "It just happens every now and then."
    [ 242] m 1a "That's why I always keep a snack in my bag for her."
    [ 243] m 5a "Anyway...!"
    [ 244] m "Why don't we all share poems now?"
    [ 245] return
