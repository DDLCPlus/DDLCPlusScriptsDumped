label ch4_end:
    [   0] play music "t10" fadeout 2
    [   1] show sayori 1ba at t11 zorder 2
    [   2] mc "Sayori--"
    [   3] mc "I thought you didn't want to come over today!"
    [   4] s 2bl "Ahaha, well..."
    [   5] s "I tried staying in my room..."
    [   6] s "But my imagination was being really mean to me..."
    [   7] s 1by "So I had to come here and see it for myself."
    [   8] mc "See what?"
    [   9] mc "What are you talking about?"
    [  10] s "You know..."
    [  11] s "How much fun you were having with [ch4_name]."
    [  12] s "And how close you got to her."
    [  13] s 1bt "It makes me...really happy..."
    [  14] s "That you've made such good friends."
    [  15] s "That's all that matters to me."
    [  16] "Tears start to fall down Sayori's face."
    [  17] s 4bv "That's all that matters to me--!"
    [  18] s "Why am I feeling this way, [player]?"
    [  19] s "I'm supposed to be happy for you."
    [  20] s 4bw "Why does it feel like my heart is splitting in half?"
    [  21] s "It hurts so much..."
    [  22] s "Everything hurts so much..."
    [  23] s "This would be so much better if I could just disappear!"
    [  24] mc "Sayori, don't say that!"
    [  25] s 1bw "It's true, [player]!"
    [  26] s "If I wasn't here, then you wouldn't have to waste your sympathy on me!"
    [  27] s "You wouldn't have to put up with me being selfish!"
    [  28] s 1bv "Monika was right..."
    [  29] s "I should just..."
    [  30] mc "Monika...?"
    [  31] mc "Monika was right about what?"
    [  32] s "..."
    [  33] mc "Sayori..."
    [  34] mc "What I said before is true."
    [  35] mc "I'm not going to let this continue."
    [  36] mc "Caring about you like this isn't the burden your mind is making it out to be."
    [  37] mc "It's something that makes me happy."
    [  38] mc "It's something that I wouldn't trade for anything else."
    [  39] mc "So, even if it takes an entire lifetime..."
    [  40] mc "I'm going to be by your side until you don't feel any more pain."
    [  41] s 1bk "B-But..."
    [  42] "Sayori looks away."
    [  43] "I put a hand on her shoulder to reassure her."
    [  44] s "I'm scared, [player]..."
    [  45] s "I'm really scared..."
    [  46] mc "What are you scared of, Sayori?"
    [  47] s "I'm scared that..."
    [  48] s "That I might like you more than you like me..."
    [  49] mc "Sayori...?"
    [  50] s 1bu "It's true, isn't it?"
    [  51] s "I was weak and started to like you too much..."
    [  52] s "I did this to myself."
    [  53] s "[player]..."
    [  54] s 4bw "I like you so much that I want to die!"
    [  55] s "That's how I feel!"
    [  56] s 2bv "And...and..."
    [  57] mc "That's enough, Sayori..."
    [  58] mc "I don't want you to hurt anymore."
    [  59] "I slide my hand down Sayori's arm and squeeze her hand in my own."
    [  60] mc "Do you remember how I said I always know what's best for you?"
    [  61] mc "Do you still believe me?"
    [  62] "Wordlessly, Sayori nods."
    [  63] mc "Even if you don't understand all of your own feelings..."
    [  64] mc "I know what you need the most right now."
    [  65] mc "And that's what I'm going to give to you."
    [  66] with None
    [  67] show black zorder 4
    [  68] with dissolve_cg
    [  69] goto [82]
    [  70] 
    [  71] with None
    [  72] hide black
    [  73] with dissolve_cg
    [  74] call ch4_end_yes
    [  75] goto [84]
    [  76] 
    [  77] with None
    [  78] hide black
    [  79] with dissolve_cg
    [  80] call ch4_end_no
    [  81] goto [84]
    [  82] mc "Sayori...{nw}"    # menu-with-caption
    [  83] menu:    # caption above
                "I love you.":  goto [70]
                "You'll always be my dearest friend.":  goto [76]
    [  84] pass
    [  85] return
