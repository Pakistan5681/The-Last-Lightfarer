#mw CP_2 saving and loading
from paxtons_helpers import Player, Weapon
import pandas as pd


#function to save the current level, this needs to take in the players HEALTH, WEAPON, SPEED, LEVEL, and then you will ned to insert a save file (either 1,2,or 3) Paxton will implement the menu functionality of this.
def saveCurrentLevel(health, weapon, speed, level, save_file):
    save_file -= 1
    try:
        #read the csv
        df = pd.read_csv("michael/saved_character.csv")
        #get the specific row, and then change it!
        df.loc[save_file] = [level,health, weapon.name, weapon.damage, weapon.type, weapon.range, speed]
        #saving!
        df.to_csv("michael/saved_character.csv",index = False)
    except:
        print("Error saving file")
    else:
        print("File saved successfully")


#this allows you to load, it will return 1 of two things, either a string "fail", in which case this save file has no usable data on it, OR it will return the player object, and the level they are on.
#save file NEEDS TO BE 1,2, or 3
def loadCurrentLevel(save_file):
    save_file -= 1
    try:
        #read csv
        df = pd.read_csv("michael\saved_character.csv")
        #get level
        level = df.loc[save_file, "Level"]
        #check if level 0, it is a placeholder save file.
        if level == 0:
            print("this save file is empty")
            #in the case of an empty file
            return "fail"
        #get health
        health = df.loc[save_file, "Health"]
        #get weapon name
        weapon_name = df.loc[save_file, "WeaponName"]
        #get weapon damage
        weapon_damage = df.loc[save_file, "WeaponDamage"]
        #get wewapon type
        weapon_type = df.loc[save_file, "WeaponType"]
        #get weapon range
        weapon_range = df.loc[save_file, "WeaponRange"]
        #get player speed
        speed = df.loc[save_file, "Speed"]
    except:
        print("Error loading file")
    else:
        print("File loaded successfully")
        #return the object for packston to use
        #index 0 is the player object, index 1 is the level
        return (Player(weapon=Weapon(name=weapon_name, damage=int(weapon_damage), type=weapon_type, range=int(weapon_range)), health=int(health), speed=int(speed)), level)

#save file needs to be a 1,2 or 3
def deleteSaveFile(save_file):
    save_file -= 1
    try:
        #read the csv
        df = pd.read_csv("michael/saved_character.csv")
        #change the row to be the default values, 0 makes the code fail when trying to load.
        df.loc[save_file] = [0,100,"sword",1,"sword",1,10]
        #saving!
        df.to_csv("michael/saved_character.csv",index = False)
    except:
        print("Error deleting file")
    else:
        print("File deleted successfully")

