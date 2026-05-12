#mw CP_2 saving and loading

import pandas as pd



def saveCurrentLevel(health, weapon, speed, level):
    df = pd.DataFrame(sendable_data = {"Level":str(level), "Health":str(health), "WeaponName":weapon.name, "WeaponDamage" : str(weapon.dmg), "WeaponRange": weapon.range, "Speed": speed})
    df.to_csv("michael/saved_character.csv", mode = 'a', index = False, header = False)
