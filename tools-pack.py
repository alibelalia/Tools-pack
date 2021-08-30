import os
import sys
import datetime 
import time 
from pyfiglet import Figlet
os.system("clear")
f = Figlet(font='slant')
print(f.renderText('Ali-Belalia'))
print("[+__Created By: Ali Belalia+__]")
def main():
	print('''
	{1}-Text Editor
	{2}-Phishing Attack Tools
	{3}-Web application Scanner
	{4}-Dos Attack
	{5}-Other Penetration testing Tools
	{00}-Exit
	''')
	first = input("Enter a Number From The List: ")
	if first=='1' :
		print('''
			{1}-Nano
			{2}-Codiad
			{3}-Emacs
			{4}-Micro
			{5}-exit
				''')
		a = input("Enter number from the list: ")
		if a=='1' :
			os.system("pkg install nano -y")
			if __name__ == '__main__':
				main()
		elif a=='2' :
			os.system("wget https://gist.githubusercontent.com/rnauber/9f579d1480db4cc5a9a3c97c00c52fb9/raw/install_codiad.sh &&     bash install_codiad.sh")
			if __name__ == '__main__':
				main()
		elif a=='3' :
			os.system("pkg install emacs")
			if __name__ == '__main__':
				main()
		elif a=='4' :
			os.system("pkg install micro")
			if __name__ == '__main__':
				main()
		elif a=='5':
			if __name__ == '__main__':
				main()
		else:
			if __name__ == '__main__':
				main()
	elif first=='2' :
		print('''
			{1}-Zphisher
			{2}-nexphisher
			{3}-Exit
			''')
		b = input("Enter number from the list: ")
		if b=='1' :
			os.system("$ git clone git://github.com/htr-tech/zphisher.git && cd zphisher && bash zphisher.sh")
		elif b=='2' :
			os.system("git clone git://github.com/htr-tech/nexphisher.git && cd nexphisher && bash tmux_setup && bash nexphisher")

		elif b=='3' :
			if __name__ == '__main__':
				main()
		else:
			if __name__ == '__main__':
				main()
	elif first=='3' :
		print('''
			{1}-XAttacker
			{2}-Nikto
			{3}-Nmap(to scan open PORTs)
			{4}-Helios
			{5}-Exit
			''')
		aa = input("Enter number from the list: ")
		if aa=='1' :
			os.system("git clone https://github.com/Moham3dRiahi/XAttacker.git && cd XAttacker && perl XAttacker.pl")
			if __name__ == '__main__':
						main()		
		elif aa=='2' :
			os.system("git clone https://github.com/sullo/nikto && cd nikto/program && perl nikto.pl")
			if __name__ == '__main__':
				main()
		elif aa=='3' :
			os.system("pkg install nmap")
			if __name__ == '__main__':
				main()
		elif aa=='4' :
			os.system("git clone https://github.com/stefan2200/Helios.git && cd Helios && pip setup.py install && helios-update-db && helios -h")
			if __name__ == '__main__':
				main()
		elif aa=='5' :
			if __name__ == '__main__':
				main()
		else:
			if __name__ == '__main__':
				main()
	elif first=='4' :
		print('''
			{1}-torshammer
			{2}-slowloris
			{3}-hammer
			{4}-Exit
			''')
		cc = input("Enter number from the list: ")
		if cc=='1' :
			os.system("git clone https://github.com/dotfighter/torshammer.git && cd torshammer && python2 torshammer.py")
			if __name__ == '__main__':
				main()
		elif cc=='2' :
			os.system("git clone https://github.com/gkbrk/slowloris.git && cd qlowloris && python3 slowloris.py")
			if __name__ == '__main__':
			 	main() 
		elif cc=='3' :
			os.system("git clone https://github.com/cyweb/hammer.git && cd hammer && python3 ahhmer.py")
			if __name__ == '__main__':
				main()
		elif cc=='4' :
			if __name__ == '__main__':
				main()
		else:
			if __name__ == '__main__':
				main()
	elif first=='5' :
		print('''
			{1}Hydra(for password cracking)
			{2}-Sqlmap(to performe an sql injection)
			{3}-install termux requirements
			{4}Exit
			''')
		bb = input("Enter number from the list: ")
		if bb=='1' :
			os.system("pkg install hydra")
			print('-'*60)
			pass
			pass
			pass
			print("type hydra to use the tool...")
			pass
			pass
			pass
			print('-'*60)
			time.sleep(3)
			if __name__ == '__main__':
				main()
		elif bb=='2' :
			os.system("git clone https://github.com/sqlmapproject/sqlmap.git && cd sqlmap && python2 sqlmap.py")
			if __name__ == '__main__':
				main()
		elif bb=='3' :
			os.system("pkg update -y && pkg upgrade -y && pkg install git -y && pkg install python -y && pkg install python2 -y && pkg install perl -y && pkg install php -y && pkg install wget -y && pkg install curl -y && pkg install java -y")
			if __name__ == '__main__':
				main()
	elif a=='00' :
		if __name__ == '__main__':
			main()
	else:
		if __name__ == '__main__':
			main()
if __name__ == '__main__':
	main()
