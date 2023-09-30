import time
from colorama import init, Fore
import os
print("1(Hide File")
print("2(View File Data")
tool = input(Fore.CYAN + "Select:")
if tool == "1":
        name = input(Fore.CYAN + "Enter File Name:")
        if "." in name:
            path2 = ".password.txt"
            days2_file = open(path2,'r+')
            read = days2_file.read()
            print(Fore.RED + "Please Enter Password For All Files In .password.txt")
            password = input("Enter Password:")
            if password == read:
                print(Fore.RED + "Waiting To Find...")
                time.sleep(10)
                print(Fore.GREEN + "Reading Files...")
                time.sleep(10)
                print(Fore.CYAN + "Changing To Hide File")
                os.system(f"mv {name} .{name}")
                time.sleep(10)
                path = "." + name
                days_file = open(path,'r+')
                print(Fore.WHITE + days_file.read())
            else:
                print(Fore.RED + "Wrong Password")
elif tool == "2":
    filename = input(Fore.CYAN + "Enter File Name:")
    if "." in filename:
         path2 = ".password.txt"
         days2_file = open(path2,'r+')
         read = days2_file.read()
         password = input(Fore.RED + "Enter Password:")
         if password == read:
            print(Fore.RED + "Waiting To Find...")
            time.sleep(10)
            print(Fore.GREEN + "Reading Files...")
            time.sleep(10)
            path3 = filename
            days3_file = open(path3, 'r+')
            print(Fore.WHITE + days3_file.read())
         else:
              print(Fore.RED + "Wrong Password")