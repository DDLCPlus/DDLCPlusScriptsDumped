label ch2_y_med:
    [   0] unless y_poemappeal[0] <= 0 goto [15]
    [   1] y 1a "Let's see what you've written for today."
    [   2] y "..."
    [   3] y "Mm..."
    [   4] y 1c "Well done, [player]."
    [   5] y "Your skills are already improving."
    [   6] mc "Really?"
    [   7] mc "Thanks, Yuri."
    [   8] mc "Coming from you, that means a lot."
    [   9] y 3f "Eh?"
    [  10] y 3v "I-It's nothing!"
    [  11] y "I'm just happy to help inspire fellow writers..."
    [  12] y "I know you're new to this, so don't worry so much if it seems like you can't get your poem to feel perfect."
    [  13] jump ch2_y_shared
    [  14] goto [24]
    [  15] y 1a "Let's see what you've written for today."
    [  16] y "..."
    [  17] y "Mm..."
    [  18] y "This is pretty good, [player]."
    [  19] y "Were you influenced by seeing everyone's writing styles yesterday?"
    [  20] mc "I guess you could say that..."
    [  21] y 1m "I was also a bit surprised by how differently everyone writes."
    [  22] y "So I respect you for trying new things."
    [  23] jump ch2_y_shared
    [  24] pass
