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
        bottom_artificial_dimensions_number = 0
        bottom_divine_dimensions_number = 0
        bottom_spiritual_dimensions_number = 0
        terrestrial_dimensions_number = 0
        top_spiritual_dimensions_number = 0
        top_divine_dimensions_number = 0
        top_artificial_dimensions_number = 0
        i = 0

        # How common low-energy artificial dimensions are:
        # In the future, maybe add a mod so players can affect this.
        n = WeightedRandom( [(0, 50), (1,25), (2,10), (3,8), (4,6), (5,1)] )

        # Now generate a random item from the list
        bottom_artificial_dimensions_number = n.pick()

        # How common low-energy divine dimensions (cthonic) are:
        # In the future, maybe add a mod so players can affect this.
        n = WeightedRandom( [(0, 75), (1,10), (2,8), (3,1), (4,1), (5,1), (6,1), (7,1), (8,1), (9,1)] )

        # Now generate a random item from the list
        bottom_divine_dimensions_number = n.pick()

        # How common low-energy spiritual dimensions are:
        # In the future, maybe add a mod so players can affect this.
        n = WeightedRandom( [(0, 25), (1,1), (2,2), (3,2), (4,3), (5,3), (6,4), (7,5), (8,10), (9,30), (10,10), (11,5)] )

        # Now generate a random item from the list
        bottom_spiritual_dimensions_number = n.pick()

        # How common Terrestrial dimensions are:
        # In the future, maybe add a mod so players can affect this.
        n = WeightedRandom( [(0, 1), (1,2), (2,2), (3,2), (4,3), (5,3), (6,3), (7,4), (8,5), (9,5), (10,30), (11,40)] )

        # Now generate a random item from the list
        terrestrial_dimensions_number = n.pick()

        # How common high-energy spiritual dimensions are:
        # In the future, maybe add a mod so players can affect this.
        n = WeightedRandom( [(0, 25), (1,1), (2,2), (3,2), (4,3), (5,3), (6,4), (7,5), (8,10), (9,30), (10,10), (11,5)] )

        # Now generate a random item from the list
        top_spiritual_dimensions_number = n.pick()

        # How common high-energy divine dimensions (celestial) are:
        # In the future, maybe add a mod so players can affect this.
        n = WeightedRandom( [(0, 75), (1,10), (2,8), (3,1), (4,1), (5,1), (6,1), (7,1), (8,1), (9,1)] )

        # Now generate a random item from the list
        top_divine_dimensions_number = n.pick()

        # How common high-energy artificial dimensions are:
        # In the future, maybe add a mod so players can affect this.
        n = WeightedRandom( [(0, 50), (1,25), (2,10), (3,8), (4,6), (5,1)] )

        # Now generate a random item from the list
        top_artificial_dimensions_number = n.pick()

    show screen multiverse_generator()

    jump multiverse_loop

label multiverse_reroll:

    python:

        # Terrestrial and Spiritual Patterns

        # Common to have many planes, very rare to have few or none:
        #n = WeightedRandom( [(0, 2), (1,2), (2,3), (3,3), (4,3), (5,3), (6,4), (7,5), (8,5), (9,30), (10,40)] )

        # Common to have many planes, common to have no planes, rare to have few planes:
        #n = WeightedRandom( [(0, 25), (1,1), (2,2), (3,3), (4,4), (5,4), (6,5), (7,10), (8,30), (9,10), (10,5)] )


        # Divine and Artificial Patterns

        # Very Common to have no planes, uncommon to have few planes, very rare to have many planes.
        #n = WeightedRandom( [(0, 75), (1,10), (2,8), (3,1), (4,1), (5,1)] )

        # Common to have no planes, common to have few planes, rare to have many planes.
        #n = WeightedRandom( [(0, 50), (1,25), (2,10), (3,8), (4,6), (5,1)] )

        # How common low-energy artificial dimensions are:
        # In the future, maybe add a mod so players can affect this.
        n = WeightedRandom( [(0, 50), (1,25), (2,10), (3,8), (4,6), (5,1)] )

        # Now generate a random item from the list
        bottom_artificial_dimensions_number = n.pick()
        bottom_artificial_dimensions_number = int(bottom_artificial_dimensions_number)

        # How common low-energy divine dimensions (cthonic) are:
        # In the future, maybe add a mod so players can affect this.
        n = WeightedRandom( [(0, 75), (1,10), (2,8), (3,1), (4,1), (5,1)] )

        # Now generate a random item from the list
        bottom_divine_dimensions_number = n.pick()
        bottom_divine_dimensions_number = int(bottom_divine_dimensions_number)

        # How common low-energy spiritual dimensions are:
        # In the future, maybe add a mod so players can affect this.
        n = WeightedRandom( [(0, 25), (1,1), (2,2), (3,3), (4,4), (5,4), (6,5), (7,10), (8,30), (9,10), (10,5)] )

        # Now generate a random item from the list
        bottom_spiritual_dimensions_number = n.pick()
        bottom_spiritual_dimensions_number = int(bottom_spiritual_dimensions_number)

        # How common Terrestrial dimensions are:
        # In the future, maybe add a mod so players can affect this.
        n = WeightedRandom( [(0, 2), (1,2), (2,3), (3,3), (4,3), (5,3), (6,4), (7,5), (8,5), (9,30), (10,40)] )

        # Now generate a random item from the list
        terrestrial_dimensions_number = n.pick()
        terrestrial_dimensions_number = int(terrestrial_dimensions_number)

        # How common high-energy spiritual dimensions are:
        # In the future, maybe add a mod so players can affect this.
        n = WeightedRandom( [(0, 25), (1,1), (2,2), (3,2), (4,3), (5,3), (6,4), (7,5), (8,10), (9,30), (10,10), (11,5)] )

        # Now generate a random item from the list
        top_spiritual_dimensions_number = n.pick()
        top_spiritual_dimensions_number = int(top_spiritual_dimensions_number)

        # How common high-energy divine dimensions (celestial) are:
        # In the future, maybe add a mod so players can affect this.
        n = WeightedRandom( [(0, 75), (1,10), (2,8), (3,1), (4,1), (5,1)] )

        # Now generate a random item from the list
        top_divine_dimensions_number = n.pick()
        top_divine_dimensions_number = int(top_divine_dimensions_number)

        # How common high-energy artificial dimensions are:
        # In the future, maybe add a mod so players can affect this.
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

        for i in range (bottom_artificial_dimensions_number):
            imagebutton auto "gui/multiverse/dimension_bottom_artificial_base_%s.png" focus_mask True action MainMenu()

    hbox:
        xalign 0.52 yalign 0.75
        spacing -50

        for i in range (bottom_divine_dimensions_number):
            imagebutton auto "gui/multiverse/dimension_bottom_divine_base_%s.png" focus_mask True action MainMenu()

    hbox:
        xalign 0.5 yalign 0.6
        spacing -250

        for i in range (bottom_spiritual_dimensions_number):
            imagebutton auto "gui/multiverse/dimension_bottom_spiritual_base_%s.png" focus_mask True action MainMenu()

    hbox:
        xalign 0.5 yalign 0.5
        spacing -50

        for i in range (terrestrial_dimensions_number):
            imagebutton auto "gui/multiverse/dimension_terrestrial_base_%s.png" focus_mask True action MainMenu()

    hbox:
        xalign 0.5 yalign 0.4
        spacing -250

        for i in range (top_spiritual_dimensions_number):
            imagebutton auto "gui/multiverse/dimension_top_spiritual_base_%s.png" focus_mask True action MainMenu()

    hbox:
        xalign 0.48 yalign 0.25
        spacing -50

        for i in range (top_divine_dimensions_number):
            imagebutton auto "gui/multiverse/dimension_top_divine_base_%s.png" focus_mask True action MainMenu()

    hbox:
        xalign 0.46 yalign 0.0
        spacing -250

        for i in range (top_artificial_dimensions_number):
            imagebutton auto "gui/multiverse/dimension_top_artificial_base_%s.png" focus_mask True action MainMenu()

    imagebutton auto "gui/multiverse/button_reroll_%s.png" xalign 1.0 yalign 0.0 focus_mask True action Jump("multiverse_reroll")
