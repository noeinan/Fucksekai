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

    hbox:
            
        for n in range(0, 8):
            python:
                x = 0.125 * n
                y = 0
            for i in range (0, 3):
                python:
                    env_tile_pick(i)
                imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator") xalign x yalign y