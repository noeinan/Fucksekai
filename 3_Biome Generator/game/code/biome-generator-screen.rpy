init:
    transform customzoom:
        zoom 0.6

label biome_loop:
    $ renpy.pause()
    jump biome_loop

label biome:

    python:
        # updating global variables
        current_loc = "biome void"

    show screen biome_generator()

    jump biome_loop

screen biome_generator():
    tag generator

    add "#ffffff"

    hbox xalign 0.1 yalign 0.5:
        
        imagebutton auto "gui/button/Terrestrial_Biome_Placeholder_Button_%s.png" focus_mask True action MainMenu() at customzoom

    hbox xalign 0.9 yalign 0.5:

        imagebutton auto "gui/button/Aquatic_Biome_Placeholder_Button_%s.png" focus_mask True action MainMenu() at customzoom