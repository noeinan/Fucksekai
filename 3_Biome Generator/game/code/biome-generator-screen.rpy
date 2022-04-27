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

    #add "gui/Arctic_vs_Alpine_Tundra_Placement_Aid.png"

    hbox xalign 0.1 yalign 0.5:
        
        imagebutton auto "gui/button/biome/Terrestrial_Biome_Placeholder_Button_%s.png" focus_mask True action Show("terrestrial_generator")

    hbox xalign 0.9 yalign 0.5:

        imagebutton auto "gui/button/biome/Aquatic_Biome_Placeholder_Button_%s.png" focus_mask True action Show("aquatic_generator")

screen terrestrial_generator():
    tag generator

    add "#ffffff"

    #add "gui/Arid_vs_Semi-Arid_vs_Coastal_vs_Cold_Deserts_Placement_Aid.png"

    hbox xalign 0.05 yalign 0.1:
        
        imagebutton auto "gui/button/biome/Desert_Biome_Placeholder_Button_%s.png" focus_mask True action Show("desert_generator")

    hbox xalign 0.28 yalign 0.82:
        
        imagebutton auto "gui/button/biome/Forest_Biome_Placeholder_Button_%s.png" focus_mask True action Show("forest_generator")

    hbox xalign 0.95 yalign 0.1:
        
        imagebutton auto "gui/button/biome/Grassland_Biome_Placeholder_Button_%s.png" focus_mask True action Show("grassland_generator")

    hbox xalign 0.72 yalign 0.82:
        
        imagebutton auto "gui/button/biome/Tundra_Biome_Placeholder_Button_%s.png" focus_mask True action Show("tundra_generator")

screen desert_generator():
    tag generator

    add "#ffffff"

    #add "gui/Arid_vs_Semi-Arid_vs_Coastal_vs_Cold_Deserts_Placement_Aid.png"

    hbox xalign 0.05 yalign 0.1:
        
        imagebutton auto "gui/button/biome/Arid_Desert_Placeholder_Button_%s.png" focus_mask True action Jump("environment")

    hbox xalign 0.28 yalign 0.82:
        
        imagebutton auto "gui/button/biome/Coastal_Desert_Placeholder_Button_%s.png" focus_mask True action Jump("environment")

    hbox xalign 0.95 yalign 0.1:
        
        imagebutton auto "gui/button/biome/Cold_Desert_Placeholder_Button_%s.png" focus_mask True action Jump("environment")

    hbox xalign 0.72 yalign 0.82:
        
        imagebutton auto "gui/button/biome/Semi-Arid_Desert_Placeholder_Button_%s.png" focus_mask True action Jump("environment")

screen forest_generator():
    tag generator

    add "#ffffff"

    #add "gui/Temperate_vs_Tropical_vs_Steppe_Grassland_Placement_Aid.png"

    hbox xalign 0.05 yalign 0.1:
        
        imagebutton auto "gui/button/biome/Boreal_Forest_Placeholder_Button_%s.png" focus_mask True action Jump("environment")

    hbox xalign 0.5 yalign 0.85:
        
        imagebutton auto "gui/button/biome/Temperate_Forest_Placeholder_Button_%s.png" focus_mask True action Jump("environment")

    hbox xalign 0.95 yalign 0.1:
        
        imagebutton auto "gui/button/biome/Tropical_Forest_Placeholder_Button_%s.png" focus_mask True action Jump("environment")

screen grassland_generator():
    tag generator

    add "#ffffff"

    #add "gui/Temperate_vs_Tropical_vs_Steppe_Grassland_Placement_Aid.png"

    hbox xalign 0.05 yalign 0.1:
        
        imagebutton auto "gui/button/biome/Steppe_Grassland_Placeholder_Button_%s.png" focus_mask True action Jump("environment")

    hbox xalign 0.5 yalign 0.85:
        
        imagebutton auto "gui/button/biome/Temperate_Grassland_Placeholder_Button_%s.png" focus_mask True action Jump("environment")

    hbox xalign 0.95 yalign 0.1:
        
        imagebutton auto "gui/button/biome/Tropical_Grassland_Placeholder_Button_%s.png" focus_mask True action Jump("environment")

screen tundra_generator():
    tag generator

    add "#ffffff"

    #add "gui/Arctic_vs_Alpine_Tundra_Placement_Aid.png"

    hbox xalign 0.1 yalign 0.5:
        
        imagebutton auto "gui/button/biome/Alpine_Tundra_Placeholder_Button_%s.png" focus_mask True action Jump("environment")

    hbox xalign 0.9 yalign 0.5:

        imagebutton auto "gui/button/biome/Arctic_Tundra_Placeholder_Button_%s.png" focus_mask True action Jump("environment")

screen aquatic_generator():
    tag generator

    add "#ffffff"

    #add "gui/Arctic_vs_Alpine_Tundra_Placement_Aid.png"

    hbox xalign 0.1 yalign 0.5:
        
        imagebutton auto "gui/button/biome/Freshwater_Aquatic_Placeholder_Button_%s.png" focus_mask True action Jump("environment")

    hbox xalign 0.9 yalign 0.5:

        imagebutton auto "gui/button/biome/Marine_Aquatic_Placeholder_Button_%s.png" focus_mask True action Jump("environment")