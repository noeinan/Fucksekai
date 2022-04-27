# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 23:58:55 2022

@author: ASUS
"""
import os, sys, random
base_path = "\\Documents\\GitHub\\Fucksekai\\3_Biome Generator\\game\\gui\\button\\environment_screen\\"
path = sys.path[0] + base_path
files = os.listdir(path)
selected_path = base_path + random.choice(files)
formatted_path = selected_path.split("game\\")[1]
formatted_path = formatted_path.replace("idle.png", "%s.png")

print(formatted_path)