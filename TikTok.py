import requests,os,time,sys
from bs4 import BeautifulSoup
from colorama import Fore,Style,init

init(convert=True)
blue,white = Fore.BLUE,Fore.WHITE
logo = f"""{blue}
████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗    ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗███████╗██████╗ 
╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
   ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝     ███████╗█████╗  ███████║██████╔╝██║     ███████║█████╗  ██████╔╝
   ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗     ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  ██╔══██╗
   ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗    ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║
   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{white}"""

def main():
	os.system('cls')
	print(logo+"\n\n[1]-TikTok searcher\n[2]-Credits\n[3]-Exit")
	choice = int(input(">> "))
	if choice == 1:
		tiktok()
	elif choice == 2:
		credits()
	elif choice == 3:
		print("GoodBye fellow friendio\n")
		time.sleep(0.5)
		sys.exit()
	else:
		print("Invalid Input")
		time.sleep(0.5)
		main()

def tiktok():
	os.system('cls')
	red = Fore.RED
	blue = Fore.BLUE
	white = Fore.WHITE
	green = Fore.GREEN
	purple = Fore.MAGENTA
	yellow = Fore.YELLOW
	print(logo)
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
	username = input("\n\nInput A username: ")
	data = requests.get(f"https://www.tiktok.com/@{username}",headers=headers)
	soup = BeautifulSoup(data.text, 'html.parser')
	t=time.localtime()
	current_time = time.strftime("%H:%M:%S",t)
	print(current_time)
	for h1 in soup.find_all('h1', {'class':'share-sub-title'}):
		print(f"{red}Nickname{white} = "+h1.text)
	for strong in soup.find_all('strong', {'title':'Followers'}):
		print(f"{blue}Followers{white} = " + strong.text)
	for strong1 in soup.find_all('strong', {'title':'Following'}):
		print(f"{green}Following{white} = "+strong1.text)
	for strong2 in soup.find_all('strong',{'title':'Likes'}):
		print(f"{purple}Likes{white} = "+strong2.text)
	for h2 in soup.find_all('h2',{'class':'share-desc mt10'}):
		print(f"{yellow}Bio{white} = "+h2.text)
	time.sleep(3)
	main()

def credits():
	os.system('cls')
	print(logo)
	print("\n\nMade by Mr dolphin#0777\nI made because i was bored :/")
	time.sleep(2)
	main()

main()