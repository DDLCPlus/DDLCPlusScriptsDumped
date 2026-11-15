label blood_particle_censor:
    [   0] pass
    [   1] "stab_censor/blood_drop_censor.png"    # image key blood_drop_censor
    [   2] zoom 0.75
    [   3] alpha 0.75
    [   4] $ randrangevalue = renpy.random.randint(0, 3)    # choice:
    [   5] unless randrangevalue == 0 goto [7]
    [   6] linear 0.25 zoom 0
    [   7] pass
    [   8] unless randrangevalue == 1 goto [10]
    [   9] linear 0.35 zoom 0
    [  10] pass
    [  11] unless randrangevalue == 2 goto [13]
    [  12] linear 0.35 zoom 0
    [  13] pass
    [  14] unless randrangevalue == 3 goto [16]
    [  15] linear 0.55 zoom 0
    [  16] pass
