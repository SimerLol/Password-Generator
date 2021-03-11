import os
import sys
import time
import random
import lolcat
from pyfiglet import Figlet

#defining colors for a user friendly environment
RED =   '\033[31;2m' # red color
BLUE =   '\033[34;2m' # blue color
GREEN =   '\033[32;1m' # green color
YELLOW =   '\033[93m' # yellow color
PINK =   '\033[95m' # ping color
PURPLE =   '\033[35m' # green color
GREY =   '\033[90;1m' # grey color
WHITE =   '\033[37;1m' # white color
END =   '\033[m' # reset to the default

#banners
header = 'lolcat -a -d 3 -p 2 "./banners/header.txt"'
yourpass = 'lolcat -a -d 25 -p 2 "./banners/yourpass.txt"'
footer = 'lolcat -a -d 3 -p 2 "./banners/footer.txt"'
os.system(header)
print()

#clear command
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

# automated typing thing 
def typing(words):
  words
  for char in words:
    time.sleep(random.choice([0.04, 0.04,0.05, 0.05, 0.04, 0.038, 0.05]))
    sys.stdout.write(char)
    sys.stdout.flush()

#password requirements
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/._-"
all = lower + upper + numbers + symbols
length = 16

#password generation
password = "".join(random.sample(all,length))

#Generating Script
animation = "|/-\\"
for i in range(25):
  time.sleep(0.1)
  sys.stdout.write(WHITE + "\rGenerating" + animation[i % len(animation)])
  sys.stdout.flush()
sys.stdout.write(GREEN + "\rGenerated!\n")
time.sleep(1.5)
clear()

#password printing
os.system(footer)
print()
print()
os.system(yourpass)
print(password)
time.sleep(3.5)
print(PURPLE)
typing("This is a very simple script, feel free to improve on it!\n               My socials are - Simer00               \n")