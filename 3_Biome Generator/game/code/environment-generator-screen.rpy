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

    add "gui/button/environment_screen/soil_map_placeholder.png"

    for n in range(1, 8):
        python:
            x = n / 8
            y = 0
            for i in range (0, 3):
                env_tile_pick(i)
        hbox xalign x yalign y:
            
                imagebutton idle idlei hover hoveri focus_mask True action Show("terrestrial_generator")