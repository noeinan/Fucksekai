# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    python:
        import os

        env_tiles = [[],[],[],[]]
        base_path = "\\game\\gui\\button\\environment_screen\\"
        path = sys.path[0] + base_path

        for files in os.listdir(path):
            files = files.replace("_hover.png", "")
            files = files.replace("_idle.png", "")
            if "north" in files and files not in env_tiles[0]:
                env_tiles[0].append(files)
            elif "east" in files and files not in env_tiles[1]:
                env_tiles[1].append(files)
            elif "south" in files and files not in env_tiles[2]:
                env_tiles[2].append(files)
            elif "west" in files and files not in env_tiles[3]:
                env_tiles[3].append(files)

    jump biome

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
