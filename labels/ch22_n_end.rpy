label ch22_n_end:
    [   0] unless n_appeal >= 2 goto [3]
    [   1] jump ch22_n_end2
    [   2] goto [27]
    [   3] call showpoem(<compiled: CompiledExpression { instructions=[CompiledInstruction], constantFloats=[], constantStrings=["poem_n2"], constantObjects=[] }>)
    [   4] n 2a "Not bad, right?"
    [   5] mc "It's quite a bit longer than yesterday's."
    [   6] n 2w "Yesterday's was way too short..."
    [   7] n "I was just warming up!"
    [   8] n 2c "I hope you didn't think that was the best I could do."
    [   9] mc "No, of course not..."
    [  10] n 2a "Anyway, the message is pretty straightforward in this poem."
    [  11] n "I doubt I have to explain it."
    [  12] n 2g "Like, anyone would agree that the subject of this poem is an ignorant jerk..."
    [  13] n "Everyone has some kind of weird hobby, or a guilty pleasure."
    [  14] n 5q "Something that you're afraid if people find out, they'd make fun of you or think less of you."
    [  15] n 1e "...But that just makes people stupid!"
    [  16] n "Who cares what someone likes, as long as they're not hurting anyone, and it makes them happy?"
    [  17] n 1q "I think people really need to learn to respect others for liking weird things..."
    [  18] n 1x "...Such as two of the girls in this very club, whom I respectfully won't name."
    [  19] n 1s "Kind of ironic that even in my one place of comfort, I can't even have people respect me..."
    [  20] n 1u "...Jeez, now you're making me complain too much!"
    [  21] "<i>(...What did I do?)</i>"
    [  22] mc "For what it's worth, I respect you..."
    [  23] n 1h "Well--"
    [  24] n "I guess thanks..."
    [  25] n 1s "...But it's kind of obvious that you 'respect' Yuri more, so..."
    [  26] n 42c "Whatever... We're done sharing, so you can leave now."
    [  27] pass
    [  28] return
