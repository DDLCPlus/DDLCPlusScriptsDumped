label ch10_main:
    [   0] 
    [   1] 
    [   2] 
    [   3] stop music
    [   4] 
    [   5] scene bg residential_day
    [   6] with dissolve_scene_half
    [   7] 
    [   8] play music "t2g"
    [   9] 
    [  10] # RenpyDialogueLine: RenpyDialogueLine {  }
    [  11] 
    [  12] "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    [  13] "That girl is [s_name], my neighbor and good friend since we were children."
    [  14] "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
    [  15] "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    [  16] "But if she's going to chase after me like this, I almost feel better off running away."
    [  17] "However, I just sigh and idle in front of the crosswalk and let [s_name] catch up to me."
    [  18] show sayori glitch at t11 zorder 2
    [  19] 
    [  20] 
    [  21] unless startpos < 0 goto [24]
    [  22] 
    [  23] goto [24]
    [  24] pass
    [  25] 
    [  26] 
    [  27] 
    [  28] 
    [  29] # RenpyDialogueLine: RenpyDialogueLine {  }
    [  30] 
    [  31] 
    [  32] # RenpyDialogueLine: RenpyDialogueLine {  }
    [  33] # Expression: Expression { Expr=CompiledExpression { instructions=List`1, constantFloats=List`1, constantStrings=List`1, constantObjects=List`1 }, WaitInteraction=True }
    [  34] 
    [  35] hide screen tear
    [  36] call screen_tear_hide
    [  37] window hide(None)
    [  38] window auto
    [  39] with None
    [  40] scene black
    [  41] with trueblack
    [  42] 
    [  43] 
    [  44] 
    [  45] 
    [  46] 
    [  47] jump ch20_from_ch10
