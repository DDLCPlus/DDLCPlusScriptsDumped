label ch3_y_end:
    [   0] 
    [   1] unless y_appeal >= 3 goto [4]
    [   2] jump ch3_y_end_special
    [   3] goto [4]
    [   4] pass
    [   5] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="beach", UnlockId=4105357384 }
    [   6] call showpoem(<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["poem_y3"], constantObjects=[] }>)
    [   7] y 2v "Um..."
    [   8] y "I'm aware that the beach is kind of an inane thing to write about."
    [   9] y "But I did my best to take a metaphorical approach to it."
    [  10] unless not n_read3 or n_appeal >= 3 goto [28]
    [  11] mc "You say that like you didn't even want to write about it..."
    [  12] y 2e "Oh, you haven't heard...?"
    [  13] y 2h "After yesterday, Natsuki and I...well..."
    [  14] y "It was...amusing that we wrote about something similar in such different ways."
    [  15] y "So, Natsuki wanted us to write about the same topic as each other again."
    [  16] unless n_readpoem goto [26]
    [  17] unless not n_read3 goto [21]
    [  18] mc "I see..."
    [  19] "Natsuki didn't even let me read her poem, so I don't have much to contribute."
    [  20] goto [24]
    [  21] mc "I see..."
    [  22] "Something tells me the poem Natsuki showed me isn't the one she plans on sharing with everyone else..."
    [  23] "Of course, I choose not to mention that to Yuri."
    [  24] pass
    [  25] goto [26]
    [  26] pass
    [  27] goto [32]
    [  28] mc "Yeah, Natsuki already told me about it."
    [  29] y 3t "S-She did...?"
    [  30] y "She didn't say anything weird, did she?"
    [  31] y "She just wanted us to write about the same topic again..."
    [  32] pass
    [  33] y 2f "I suppose to better compare the differences in our writing styles...or thought processes."
    [  34] y 2w "Anyway, it was her idea...!"
    [  35] y "Knowing her, it's no surprise that she'd want to do something like that."
    [  36] y "She probably just wants to show off."
    [  37] y 2v "It's not like I have a particular interest in her writing style..."
    [  38] y "I just went with her request."
    [  39] y "But..."
    [  40] y 1s "Well, I suppose it's not so bad to write about something simple on occasion."
    [  41] y 1m "It can be refreshing, you know?"
    [  42] y "It's good for me to calm my thoughts once in a while."
    [  43] mc "Yeah...I think I agree."
    [  44] mc "Thanks for sharing."
    [  45] return
