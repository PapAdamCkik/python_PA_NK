import time
import os
menu = 0
while menu!=5:
# tomb = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if menu== 0:
        print("  _  _    _     _   ")                                                 
        print(" (_)(_)__| |_ _| |")                                                   
        print(" | || / _` \ V /_|")                                                   
        print("  \_,_\__,_|\_/(_)")                                                                                                                
        print(" __   __ __ _                  __     _         _      _       _   _") 
        print(" \ \ / //_/| |__ _ _________  / _|___| |__ _ __| |__ _| |_ ___| |_(_)")
        print("  \ V / _` | / _` (_-<_-<_ / |  _/ -_) / _` / _` / _` |  _/ _ \  _|_ ")
        print("   \_/\__,_|_\__,_/__/__/__| |_| \___|_\__,_\__,_\__,_|\__\___/\__(_) ")                                                     
        print("1) 3a feladat")
        print("2) 3b feladat")
        print("3) 3c feladat")
        print("4) 3d feladat")
        print("5) Kilépés")
        menu = int(input())
    
    if menu == 1:
        print("3a feladat")
        menu = 0
    elif menu == 2:
        print("3b feladat")
        menu = 0
    elif menu == 3:
        print("3c feladat")
        menu = 0
    elif menu == 4:
        print("3d feladat")
        menu = 0
    elif menu == 5:
        print('')
    else:
        
        print("Jó számot adj meg!")
        

    # for i in range(len(tomb)):
    #     ujszam = input()
    #     tomb[i] = ujszam
            
        # print(tomb)
    #else:
    # itt fog futni a kód    
print("viszlát!")
time.sleep(3)   
