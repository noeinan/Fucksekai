##### Multiverse Generator #####
#
### Description ###
#
# Generating the multiverse, made up of multiple dimensional planes.
#
### Preferences ###
#
# Weighted average of different dimension types is set in the preferences.
# This controls how violent vs peaceful the dimensions contained are.
#
### Notes ###
#

label multiverse_loop:
    $ renpy.pause()
    jump multiverse_loop

label multiverse:

    python:
        # updating global variables
        current_loc = "multiverse void"

        # defining local variables
        top_artificial_dimensions_number = 0
        i = 0

        # initialize our random picker with the options and their likelyhood of being selected:
        n = WeightedRandom( [(0, 50), (1,25), (2,10), (3,8), (4,6), (5,1)] )

        # Now generate a random item from the list
        top_artificial_dimensions_number = n.pick()

    show screen multiverse_generator()

    jump multiverse_loop

label multiverse_reroll:

    python:
        # initialize our random picker with the options and their likelyhood of being selected:
        n = WeightedRandom( [(0, 50), (1,25), (2,10), (3,8), (4,6), (5,1)] )

        # Now generate a random item from the list
        top_artificial_dimensions_number = n.pick()
        top_artificial_dimensions_number = int(top_artificial_dimensions_number)

    jump multiverse_loop

screen multiverse_generator():
    tag generator

    add "#ffffff"

    hbox:
        xalign 0.54 yalign 0.98
        spacing -250

        imagebutton auto "gui/multiverse/dimension_bottom_artificial_base_%s.png" xalign 0.5 yalign 1.0 focus_mask True action MainMenu()

    hbox:
        xalign 0.52 yalign 0.75
        spacing -250

        imagebutton auto "gui/multiverse/dimension_cthonic_base_%s.png" xalign 0.5 yalign 0.8 focus_mask True action MainMenu()

    hbox:
        xalign 0.5 yalign 0.6
        spacing -250

        imagebutton auto "gui/multiverse/dimension_bottom_spiritual_base_%s.png" xalign 0.5 yalign 0.6 focus_mask True action MainMenu()

    hbox:
        xalign 0.5 yalign 0.5
        spacing -250

        imagebutton auto "gui/multiverse/dimension_terrestrial_base_%s.png" xalign 0.5 yalign 0.5 focus_mask True action MainMenu()

    hbox:
        xalign 0.5 yalign 0.4
        spacing -250

        imagebutton auto "gui/multiverse/dimension_top_spiritual_base_%s.png" xalign 0.5 yalign 0.4 focus_mask True action MainMenu()

    hbox:
        xalign 0.48 yalign 0.25
        spacing -250

        imagebutton auto "gui/multiverse/dimension_celestial_base_%s.png" xalign 0.5 yalign 0.2 focus_mask True action MainMenu()

    hbox:
        xalign 0.46 yalign 0.0
        spacing -250

        for i in range (top_artificial_dimensions_number):
            imagebutton auto "gui/multiverse/dimension_top_artificial_base_%s.png" focus_mask True action MainMenu()

    imagebutton auto "gui/multiverse/button_reroll_%s.png" xalign 0.9 yalign 0.0 focus_mask True action Jump("multiverse_reroll")
