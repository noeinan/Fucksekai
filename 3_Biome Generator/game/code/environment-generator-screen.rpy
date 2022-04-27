label environment_loop:
    $ renpy.pause()
    jump environment_loop

label environment:

    python:
        import os

        base_path = "\\game\\gui\\button\\environment_screen\\"
        path = sys.path[0] + base_path
        files = os.listdir(path)
        selected_path = base_path + renpy.random.choice(files)
        formatted_path = selected_path.split("game\\")[1]
        formatted_path = formatted_path.replace("idle.png", "%s.png")

        #if d.endswith('fun'):
            

        # updating global variables
        current_loc = "environment void"

    show screen environment_generator()

    jump environment_loop

screen environment_generator():
    tag generator

    add "#ffffff"

    add "gui/button/environment_screen/soil_map_placeholder.png"

    python:
        x = 0
        y = 0

    #hbox xalign x yalign y:
        
        #imagebutton auto "gui/button/environment_screen/west_alfisol_%s.png" focus_mask True action Show("terrestrial_generator")

    hbox xalign x yalign y:
        
        imagebutton auto formatted_path focus_mask True action Show("terrestrial_generator")