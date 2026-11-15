label ch3_y_med:
    [   0] unless y_poemappeal[0] < 0 and y_poemappeal[1] < 0 goto [3]
    [   1] jump ch3_y_bad12_shared
    [   2] goto [37]
    [   3] unless y_poemappeal[0] < 1 or y_poemappeal[1] < 1 goto [28]
    [   4] y "..."
    [   5] y 1a "Well done, [player]."
    [   6] y "You've definitely improved your writing over the course of these few days."
    [   7] y "Has my advice been helpful to you?"
    [   8] mc "Yeah... Definitely."
    [   9] y 2m "I'm glad..."
    [  10] y "Sharing our writing like this..."
    [  11] y 2a "It's a lot more fun and rewarding than I anticipated."
    [  12] y "I need to remember to thank Monika..."
    [  13] y "I think we all felt a little awkward at first."
    [  14] y 1a "But now it seems like everyone is enjoying sharing their writing and seeing what others think."
    [  15] mc "I guess I can't really disagree."
    [  16] mc "I was afraid this whole thing would be a chore..."
    [  17] "But it's a great way for me to spend some personal time with all the girls in the club."
    [  18] mc "But it's been fun getting to know everyone and their writing."
    [  19] mc "And I guess doing some writing myself..."
    [  20] y 2a "Well..."
    [  21] y "Have you learned anything about yourself, [player]?"
    [  22] mc "Eh?"
    [  23] y 2i "Well, you know how I like to say that writing is a very personal way to get in touch with yourself..."
    [  24] y 1a "In the end, it doesn't matter if you're a good writer, or a bad writer."
    [  25] y "And even my opinions are just opinions...you know?"
    [  26] jump ch3_y_shared
    [  27] goto [37]
    [  28] y 1e "..."
    [  29] y "...Ah."
    [  30] y "Decided to try something different today?"
    [  31] mc "I guess so."
    [  32] mc "Is that good, or bad?"
    [  33] y 2i "Well, neither."
    [  34] y "I have my preferences."
    [  35] y "But it would be unfair of me to call something good or bad based on that."
    [  36] jump ch3_y_shared
    [  37] pass
