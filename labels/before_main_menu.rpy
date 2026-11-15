label before_main_menu:
    [   0] 
    [   1] unless not renpy.music.get_playing(channel='music') == config.main_menu_music goto [4]
    [   2] 
    [   3] goto [4]
    [   4] pass
    [   5] return
