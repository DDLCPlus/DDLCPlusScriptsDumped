label ch3_n_end:
    [   0] 
    [   1] unless n_appeal >= 3 goto [4]
    [   2] jump ch3_n_end_special
    [   3] goto [4]
    [   4] pass
    [   5] # RenpyUnlock: Unlock { UnlockType=Normal, UnlockName="ill_be_your_beach", UnlockId=3786085010 }
    [   6] call showpoem(<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["poem_n3"], constantObjects=[] }>)
    [   7] n 2a "Yeah..."
    [   8] n "I felt like I kept writing about negative things, so I wanted to write something with a nice message for once."
    [   9] n 2z "Besides...the beach is awesome!"
    [  10] n 2j "Kinda hard to write anything negative about the beach."
    [  11] unless not y_read3 or y_appeal >= 3 goto [29]
    [  12] mc "So you decided to write about the beach first, and then came up with the message later?"
    [  13] n 2c "Yeah, well..."
    [  14] n "It's only because of what happened yesterday."
    [  15] n 5q "I mean, after Yuri and I realized we kind of wrote about the same thing..."
    [  16] n "She wanted to pick a topic and have us both write about it, or whatever."
    [  17] unless y_readpoem goto [27]
    [  18] unless not y_read3 goto [22]
    [  19] mc "I see..."
    [  20] "I don't really have much to contribute here, since I didn't actually read Yuri's poem..."
    [  21] goto [25]
    [  22] mc "I see..."
    [  23] "Something tells me the poem Yuri showed me isn't the one she plans on sharing with everyone else..."
    [  24] "Of course, I choose not to mention that to Natsuki."
    [  25] pass
    [  26] goto [27]
    [  27] pass
    [  28] goto [33]
    [  29] mc "Well, Yuri's take on it was a little more solemn."
    [  30] n 5h "Well, that's--"
    [  31] n 42c "Jeez...she better not have said anything bad about mine!"
    [  32] n "After all, she was the one who wanted us to write about the same topic."
    [  33] pass
    [  34] n 1s "Ugh...you can really see her doing that, too."
    [  35] n "Making us write about a simple topic, then trying to impress me by coming up with something all fancy."
    [  36] n 1w "Well, it's not like I care."
    [  37] n "I just did it anyway."
    [  38] n 1q "I mean, I guess mine ended up being kind of metaphorical too..."
    [  39] n "...But there's nothing wrong with doing that once in a while!"
    [  40] n "At the very least, it was good practice."
    [  41] return
