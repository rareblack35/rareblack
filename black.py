#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import time
import sys

os.system('apt update')
os.system('apt upgrade -y')
os.system('pkg install figlet -y')
os.system('pkg install ncurses-utils -y') 
os.system('pkg install ruby -y')
os.system('gem install lolcat')

output = '/data/data/com.termux/files/usr/etc/'

print('')
name = raw_input('Input your Name : ')

wlc = '''
import os,sys,time,random
print("")
print("")
color = ["\\033[1;31m","\\033[1;32m"]
m = random.choice(color)+"Welcome {} \\n"
for msg in m:
    sys.stdout.write(msg)
    sys.stdout.flush()
    time.sleep(0.06)
print("")
'''.format(name)

h1 = open(output+'wlc.py', 'w')
h1.write(wlc)
h1.close()

bashrc1 = '''
clear
echo
echo "
   ★★★★★★★★ [★] 𝗪𝗲 𝗔𝗿𝗲 𝗔𝗻𝗢𝗻𝗬𝗺𝗢𝘂𝗦 [★] ★★★★★★★★  " |lolcat
echo
    echo " Ｑｕａｎｔｕｍ Ｃｙｂｅｒ Ｓｑｕａｄ " |lolcat
'''

bashrc2 = '''
echo "
               ★★★★★ 𝖂𝖊 𝖜𝖔𝖗𝖐 𝖋𝖔𝖗 𝕯𝖎𝖌𝖓𝖎𝖙𝖞 ★★★★★   
                   ★★★★ 𝓝𝓸𝓽 𝓕𝓸𝓻 𝓜𝓸𝓷𝓮𝔂 ★★★★
      ✵•.¸,✵°✵.｡. CrEaTeD BY ReAZ .｡.✵°✵,¸.•✵
      ★━━━━━━━━━━━[★] RaRe BlAcK [★]━━━━━━━━━━━★ " |lolcat

python /data/data/com.termux/files/usr/etc/wlc.py
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi

#PS1="\\033[1;31mTHBD~#"

PS1="\[\e[1;34m┌──\\a─T─I─M─E─\\a──┐\\033[1;34m\\a┌──\\a─D─A─T─E─\\a───>\\033[1;34m
\\a┌─[\\033[1;93m \@\\033[1;34m ]──[\\033[1;93m \d\\033[1;34m ]\\033[1;34m
\\a├─[\\033[1;32m\w\\033[1;34m]\\033[1;34m
'''

h2 = open(output+'bash.bashrc', 'w')
h2.write(bashrc1)
h2.write("\nfiglet    '    "+name+"' |lolcat\n")
h2.write(bashrc2)
h2.write('\[\e[34m\]└─>\[\e[35m\]'+name+'\[\e[34m\][~]:#\[\e[1;32m\] "\n')
h2.write('echo -e "\e[6 q"')
h2.close()
print('DONE')
