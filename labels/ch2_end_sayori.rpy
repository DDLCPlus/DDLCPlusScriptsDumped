label ch2_end_sayori:
    [   0] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="walk_with_sayori", UnlockId=1685960407 }
    [   1] mc "Sayori..."
    [   2] # RenpyDialogueLine: RenpyDialogueLine {  }
    [   3] s 1e "Eh?!"
    [   4] s "B-But..."
    [   5] unless ch2_winner == "Natsuki" goto [8]
    [   6] s "She's so cute and fun to be around..."
    [   7] goto [9]
    [   8] s "She's so beautiful and smart..."
    [   9] pass
    [  10] mc "Jeez..."
    [  11] mc "I already see her in the club every day."
    [  12] mc "Besides, you always seem to really like going home together..."
    [  13] mc "I wouldn't just ruin that for you."
    [  14] s 1y "You're so silly, [player]..."
    [  15] s "You think about me too much sometimes."
    [  16] # RenpyDialogueLine: RenpyDialogueLine {  }
    [  17] mc "Sayori, I've already made up my mind."
    [  18] mc "I really can't figure you out sometimes..."
    [  19] s "Sorry..."
    [  20] mc "Besides, what's the point in speculating something that's never going to happen?"
    [  21] s 1k "Hm..."
    [  22] show sayori at thide
    [  23] hide sayori
    [  24] "The conversation trails off."
    [  25] "It's kind of a weird thing for Sayori to care so much about..."
    [  26] "But I want to respect her and keep her happy, too."
    [  27] return
