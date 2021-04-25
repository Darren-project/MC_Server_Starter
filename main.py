import os
import shutil


fol = os.getcwd()


def ask():
    opt = input("Enter your option: ")
    if "s" in opt:
        shutil.move(fol + '/server/Spigot world/world', fol + '/server/spigot/world')
        os.system('cd server/spigot && java -jar -Dlog4j.skipJansi=true server.jar nogui')
        shutil.move(fol + '/server/spigot/world', fol + '/server/Spigot world/world')
    elif "b" in opt:
        os.system('cd server/buildtool && java -jar BuildTools.jar')
        print("rename the final jar file to server.jar and move to spigot folder.")
        print("P.S Remember to clean up the folder.")
    elif "e" in opt:
        exit()
    else:
        print('invalid option.')
        ask()


print('----------------')
print("Darren's server starter")
print('----------------')
print('s:spigot')
print('e:exit')
print('b:BuildTools')
print('----------------')
ask()
