# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 23:58:55 2022

@author: ASUS
"""
import os, sys, random
env_tiles = [[],[],[],[]]
base_path = "\\Documents\\GitHub\\FuckSekai\\3_Biome Generator\\game\\gui\\button\\environment_screen\\"
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

print(random.choice(env_tiles[3]))