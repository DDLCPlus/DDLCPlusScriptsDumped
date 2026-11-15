label monika g2:
    # nested label 6356b40d72adb87408eb27ad5758b608 starts at [0]
    # nested label b86b1a88c4fee254084bf6d1e2e9b300 starts at [11]
    [   0] label block 6356b40d72adb87408eb27ad5758b608    # nested entry point
    [   1] $ randrangevalue = renpy.random.randint(0, 2)    # choice:
    [   2] unless randrangevalue == 0 goto [4]
    [   3] "monika/g2.png"    # image key g2
    [   4] pass
    [   5] unless randrangevalue == 1 goto [7]
    [   6] "monika/g3.png"    # image key g3
    [   7] pass
    [   8] unless randrangevalue == 2 goto [10]
    [   9] "monika/g4.png"    # image key g4
    [  10] pass
    [  11] label block b86b1a88c4fee254084bf6d1e2e9b300    # nested entry point
    [  12] $ randrangevalue = renpy.random.randint(0, 3)    # choice:
    [  13] unless randrangevalue == 0 goto [15]
    [  14] 0.05
    [  15] pass
    [  16] unless randrangevalue == 1 goto [18]
    [  17] 0.1
    [  18] pass
    [  19] unless randrangevalue == 2 goto [21]
    [  20] 0.15
    [  21] pass
    [  22] unless randrangevalue == 3 goto [24]
    [  23] 0.2
    [  24] pass
    [  25] goto [0]
