label ch2_s_med:
    # nested label ch2_s_med_shared starts at [9]
    [   0] unless s_poemappeal[0] < 0 goto [19]
    [   1] s "..."
    [   2] s 4x "Ooh!"
    [   3] s "I like this one, [player]!"
    [   4] s "It has some nice feelings in it~"
    [   5] mc "Ah, I'm glad."
    [   6] mc "So it's at least better than yesterday's."
    [   7] s 1q "Uh-huh!"
    [   8] mc "Maybe I'm getting better at this, then."
    [   9] label label ch2_s_med_shared:    # nested entry point
    [  10] s 1a "Well, I'm not very good at figuring out if poems are good or bad..."
    [  11] s "But that's why I just go by my heart~"
    [  12] s "If it makes me feel things, then it must be a good poem!"
    [  13] "I'm not sure that's exactly how it works..."
    [  14] "...Then again, I guess conveying feelings is a pretty important part of this whole thing."
    [  15] mc "Yeah, maybe..."
    [  16] mc "Honestly, I don't even know what kind of writing you like in the first place."
    [  17] jump ch2_s_shared
    [  18] goto [52]
    [  19] unless s_poemappeal[0] == 0 goto [33]
    [  20] s "..."
    [  21] s 4x "Ooh!"
    [  22] s "I like this one, [player]!"
    [  23] s "It has some nice feelings in it~"
    [  24] mc "Ah, I'm glad."
    [  25] mc "Does that mean it's better than yesterday's?"
    [  26] s 4b "Mmm, lemme think..."
    [  27] s 1q "I dunno!"
    [  28] s "I guess I like them both!"
    [  29] s "Ehehe~"
    [  30] mc "That's not very helpful, you know..."
    [  31] jump ch2_s_med_shared
    [  32] goto [52]
    [  33] s "..."
    [  34] s 4x "Ooh!"
    [  35] s "I like this one, [player]!"
    [  36] s "It has some nice feelings in it~"
    [  37] mc "Ah, I'm glad."
    [  38] mc "Still, though..."
    [  39] mc "Your tone makes it sound like you liked yesterday's poem better."
    [  40] s 2l "Ehehe, I guess you caught me..."
    [  41] s "Sometimes you know me a little too well for my own good!"
    [  42] mc "Well, don't just try to be nice about it."
    [  43] mc "If I'm doing a bad job then I'd rather just hear it."
    [  44] s 1c "No, no!"
    [  45] s "I still liked this one! I promise!"
    [  46] s 1h "You know I wouldn't lie to you, [player]...!"
    [  47] s "Never ever!"
    [  48] mc "Yeah, I guess so..."
    [  49] mc "What made yesterday's poem so great compared to this one, then?"
    [  50] s 1b "Umm....."
    [  51] jump ch2_s_med_shared
    [  52] pass
