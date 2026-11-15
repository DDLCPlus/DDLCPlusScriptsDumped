label bg club_day2:
    [   0] $ randrangevalue = renpy.random.randint(0, 5)    # choice:
    [   1] unless randrangevalue == 0 goto [3]
    [   2] call bg club_day
    [   3] pass
    [   4] unless randrangevalue == 1 goto [6]
    [   5] call bg club_day
    [   6] pass
    [   7] unless randrangevalue == 2 goto [9]
    [   8] call bg club_day
    [   9] pass
    [  10] unless randrangevalue == 3 goto [12]
    [  11] call bg club_day
    [  12] pass
    [  13] unless randrangevalue == 4 goto [15]
    [  14] call bg club_day
    [  15] pass
    [  16] unless randrangevalue == 5 goto [18]
    [  17] call bg club_skill
    [  18] pass
