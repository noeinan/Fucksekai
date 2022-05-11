label environment_loop:
    $ renpy.pause()
    jump environment_loop

label environment:

    python:
        # updating global variables
        current_loc = "environment void"

        def env_tile_pick(tile_dir):
            global idlei, hoveri
            selected_path = base_path.split("game\\")[1] + renpy.random.choice(env_tiles[tile_dir])
            selected_path = selected_path.replace("\\", "/")
            idlei = selected_path + "_idle.png"
            hoveri = selected_path + "_hover.png"

    show screen environment_generator()

    jump environment_loop

screen environment_generator():
    tag generator

    add "#ffffff"

    #add "gui/button/environment_screen/soil_map_placeholder.png"

    #for l in range(0, 7):
    #    $ y = (1 / 7) * l
    #    for n in range(0, 8):
    #        $ x = (1 / 8) * n
    #        for i in range (0, 4):
    #            python:
    #                env_tile_pick(i)
    #            imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign x yalign y

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0 yalign 0

    
    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.145 yalign 0
    
    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.29 yalign 0

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.435 yalign 0

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.58 yalign 0

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.725 yalign 0

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.87 yalign 0

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 1.015 yalign 0

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0 yalign 0.1685

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.145 yalign 0.1685
    
    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.29 yalign 0.1685

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.435 yalign 0.1685

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.58 yalign 0.1685

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.725 yalign 0.1685

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.87 yalign 0.1685

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 1.015 yalign 0.1685

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0 yalign 0.337

    
    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.145 yalign 0.337
    
    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.29 yalign 0.337

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.435 yalign 0.337

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.58 yalign 0.337

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.725 yalign 0.337

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.87 yalign 0.337

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 1.015 yalign 0.337  

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0 yalign 0.5055
    
    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.145 yalign 0.5055
    
    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.29 yalign 0.5055

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.435 yalign 0.5055

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.58 yalign 0.5055

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.725 yalign 0.5055

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.87 yalign 0.5055

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 1.015 yalign 0.5055

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0 yalign 0.674
    
    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.145 yalign 0.674
    
    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.29 yalign 0.674

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.435 yalign 0.674

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.58 yalign 0.674

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.725 yalign 0.674

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.87 yalign 0.674

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 1.015 yalign 0.674

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0 yalign 0.8425
    
    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.145 yalign 0.8425
    
    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.29 yalign 0.8425

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.435 yalign 0.8425

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.58 yalign 0.8425

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.725 yalign 0.8425

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.87 yalign 0.8425

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 1.015 yalign 0.8425

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0 yalign 1.011
    
    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.145 yalign 1.011
    
    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.29 yalign 1.011

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.435 yalign 1.011

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.58 yalign 1.011

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.725 yalign 1.011

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 0.87 yalign 1.011

    for i in range (0, 4):
        $ env_tile_pick(i)
        imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign 1.015 yalign 1.011