#Main file that takes bash arguments

import os,sys
from frombash import frombash
from listinstalled import listinstalled

if os.path.exists(os.path.expanduser("~") + "/.config/legendary/installed.json") == True:

    #If len of arguments is 1 (no extra arguements), then proceed to create launch files for all games
    #   else, update parameters of a game through launch file

    if len(sys.argv) == 1: #Only name of file as default argument
    
        listinstalled()
        print("Launch files stored in GameFiles folder.\n\nHave fun gaming!")
    else:
        frombash(sys.argv[1], sys.argv[2], sys.argv[3])
else:

    print("Looks like you have not installed Heroic Games Launcher or installed any game\n\nPlease consider doing so and try again.")
