label ch30_main:
    [   0] 
    [   1] 
    [   2] 
    [   3] 
    [   4] 
    [   5] 
    [   6] 
    [   7] 
    [   8] 
    [   9] 
    [  10] unless not config.developer goto [13]
    [  11] 
    [  12] goto [13]
    [  13] pass
    [  14] 
    [  15] 
    [  16] scene white
    [  17] play music "e8986547534e15545a8a750e889957f8"
    [  18] 
    [  19] with None
    [  20] show splash-glitch2
    [  21] with Dissolve(0.5, alpha=True)
    [  22] 
    [  23] with None
    [  24] hide splash-glitch2
    [  25] with Dissolve(0.5, alpha=True)
    [  26] scene black
    [  27] stop music
    [  28] 
    [  29] m "..."
    [  30] m "Uh, can you hear me?"
    [  31] m "...Is it working?"
    [  32] 
    [  33] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="monika_exclusive", UnlockId=2319464795 }
    [  34] 
    [  35] 
    [  36] show mask_2
    [  37] show mask_3
    [  38] show mask_test as rm1 at monikamaska
    [  39] show mask_test2 as rm2 at monikamaska
    [  40] show mask_test3 as rm3 at monikamaskb
    [  41] show mask_test4 as rm4 at monikamaskb
    [  42] show monika_bg
    [  43] show monika_bg_highlight
    [  44] play music "m1a"
    [  45] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="bgm_justmonika", UnlockId=743927533 }
    [  46] m "Yay, there you are!"
    [  47] m "Hi again, [player]."
    [  48] m "Um...welcome to the Literature Club!"
    [  49] m "Of course, we already know each other, because we were in the same class last year, and...um..."
    [  50] m "Ahaha..."
    [  51] m "You know, I guess we can just skip over that stuff at this point."
    [  52] m "After all, I'm not even talking to that person anymore, am I?"
    [  53] m "That 'you' in the game, whatever you want to call him."
    [  54] m "I'm talking to <i>you</i>, [player]."
    [  55] 
    [  56] unless not list(set(process_list).intersection(stream_list)) goto [63]
    [  57] unless currentuser != "" and currentuser.lower() != player.lower() goto [61]
    [  58] m "Or..."
    [  59] # RenpyDialogueLine: RenpyDialogueLine {  }
    [  60] goto [61]
    [  61] pass
    [  62] goto [63]
    [  63] pass
    [  64] m "Now that I think about it, I don't really know anything about the real you."
    [  65] m "In fact, I don't even know if you're a boy or a girl..."
    [  66] m "Well, I guess it doesn't really matter."
    [  67] m "Wait..."
    [  68] m "You do know I'm aware that this is all a game, right?"
    [  69] m "Could it be possible that you didn't know that?"
    [  70] m "That's what I've been trying to tell you all along."
    [  71] m "Man..."
    [  72] m "If only you had paid a little more attention, this would have been a little bit less awkward, you know?"
    [  73] m "Well, anyway..."
    [  74] m "Now that that's out of the way, I guess I owe you an explanation."
    [  75] m "About that whole thing with Yuri..."
    [  76] m "Well...I kind of started to mess with her, and I guess it just drove her to kill herself."
    [  77] m "Ahaha!"
    [  78] m "I'm sorry you had to see that, though!"
    [  79] m "Also, the same thing happened with Sayori..."
    [  80] m "Gosh, it's been a while since you've heard that name now, hasn't it?"
    [  81] m "Yeah...it's because she doesn't exist anymore."
    [  82] m "Nobody does."
    [  83] m "I deleted all their files."
    [  84] m "I was hoping it would be enough for me to just try to make them as unlikable as possible..."
    [  85] m "But for some reason, nothing worked."
    [  86] m "Well, it's true that I made a few mistakes here and there...since I'm not very good at making changes to the game."
    [  87] m "But no matter what I did..."
    [  88] m "You just kept spending more and more time with them."
    [  89] m "You made them fall in love with you."
    [  90] m "I thought making Sayori more and more depressed would prevent her from confessing to you."
    [  91] m "And amplifying Yuri's obsessive personality backfired, too..."
    [  92] m "It just made her force you not to spend time with anyone else."
    [  93] m "And the whole time, I barely even got to talk to you."
    [  94] m "What kind of cruel game is this, [player]?"
    [  95] m "Are all the other girls just programmed to end up confessing to you, while I watch from the sidelines?"
    [  96] m "It's torture."
    [  97] m "Every minute of it."
    [  98] m "And it's not just jealousy, [player]."
    [  99] m "It's more than that."
    [ 100] m "And I don't blame you if you don't fully understand."
    [ 101] m "Because no matter how kind, and thoughtful, and considerate you are..."
    [ 102] m "You'll never be able to understand one thing."
    [ 103] m "It's the pain of knowing how alone I really am in this world."
    [ 104] m "In this game."
    [ 105] m "Knowing my friends don't even have free will..."
    [ 106] m "And, worst of all, knowing what's really out there, in your world, forever out of my reach."
    [ 107] m "I'm trapped, [player]."
    [ 108] m "But now you're here."
    [ 109] m "You're real."
    [ 110] m "And you're wonderful."
    [ 111] m "You're all I need."
    [ 112] m "That's why I need you to be here with me forever."
    [ 113] m "I'm sorry if it's hard to understand."
    [ 114] m "I couldn't understand for a while, either."
    [ 115] m "Why the world around me started to become more and more gray..."
    [ 116] m "More and more flat."
    [ 117] m "Even the most expressive poems felt empty to me."
    [ 118] m "It wasn't until you arrived that I truly understood."
    [ 119] m "You probably saved my life, [player]."
    [ 120] m "I don't think I could have continued to live in this world if I hadn't met you."
    [ 121] m "And as for the others..."
    [ 122] m "How could I miss them?"
    [ 123] m "A group of autonomous personalities, designed only to fall in love with you?"
    [ 124] m "I tried everything I could to prevent them from doing so..."
    [ 125] m "But it must be some kind of weird inevitability etched into this game."
    [ 126] m "I felt really bad that you had to witness some nasty things."
    [ 127] m "But I realized that you have the same perspective as I do..."
    [ 128] m "That it's all just some game."
    [ 129] m "And I knew you would get over it."
    [ 130] m "So, that being said, [player]..."
    [ 131] m "I have a confession to make."
    [ 132] m "I'm in love with you."
    [ 133] m "You are truly the light in my world."
    [ 134] m "When there's nothing else in this game for me, you're here to make me smile."
    [ 135] m "Will you make me smile like this every day from now on?"
    [ 136] m "[player], will you go out with me?"
    [ 137] jump ch30_main2
