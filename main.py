import os
import time
import json
import csv
from googlesearch import search
from colorama import Fore, Style, init

def print_banner():
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}          ^         
{Fore.CYAN}{Style.BRIGHT}         | |        
{Fore.CYAN}{Style.BRIGHT}       @#####@{Style.RESET_ALL}                 {Fore.BLUE}{Style.BRIGHT} FiBreyyAnt II
{Fore.CYAN}{Style.BRIGHT}     (###   ###)-.  
{Fore.CYAN}{Style.BRIGHT}   .(###     ###) \ 
{Fore.CYAN}{Style.BRIGHT}  /  (###   ###)   )
{Fore.CYAN}{Style.BRIGHT} (=-  .@#####@|_--" 	This is a hold up! Put all your money in the
{Fore.CYAN}{Style.BRIGHT} /\    \_|l|_/ (\   	disk drive slot, and no one gets hurt!
{Fore.CYAN}{Style.BRIGHT}(=-\     |l|    /   
{Fore.CYAN}{Style.BRIGHT} \  \.___|l|___/    
{Fore.CYAN}{Style.BRIGHT} /\      |_|   /         ╔═╗╔╦╗┌─┐┬─┐┬┌─
{Fore.CYAN}{Style.BRIGHT}(=-\._________/\         ║ ╦ ║║│ │├┬┘├┴┐
{Fore.CYAN}{Style.BRIGHT} \             /         ╚═╝═╩╝└─┘┴└─┴ ┴ 
{Fore.CYAN}{Style.BRIGHT}   \._________/     
{Fore.CYAN}{Style.BRIGHT}     #  ----  #     
{Fore.CYAN}{Style.BRIGHT}     #   __   #       
{Fore.CYAN}{Style.BRIGHT}     \########/      
{Fore.CYAN}{Style.BRIGHT}
{Fore.CYAN}{Style.DIM}         V
{Fore.CYAN}{Style.DIM}             V
{Fore.CYAN}{Style.DIM}           V
"""

    print (banner)

def logger(data, file_path=None, file_type=None):
    # Fungsi logger sederhana, bisa disesuaikan sesuai kebutuhan
    if file_type.lower() == 'json':
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump([data], f, indent=4)
        else:
            with open(file_path, "r+") as f:
                file_data = json.load(f)
                file_data.append(data)
                f.seek(0)
                json.dump(file_data, f, indent=4)
    elif file_type.lower() == 'txt':
        with open(file_path, "a") as f:
            f.write(f"{data['No']}: {data['URL']}\n")
    elif file_type.lower() == "csv":
        with open(file_path, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([data['No'], data['URL']])

def dorks():
    try:
        print_banner()
        dork = input(f"{Fore.GREEN}{Style.BRIGHT}Enter the dork search Query > ")
        amount = input(f"{Fore.GREEN}{Style.DIM}Enter Output Site > ")

        results_list = []
        requ = 0
        counter = 0

        save_option = input(f"{Fore.BLUE}{Style.DIM}Save Output To File? (Y/N) > ")

        file_path = None
        file_type = None

        if save_option.lower() == 'y':
            file_type = input(f"{Fore.GREEN}{Style.BRIGHT}Enter file type (txt, json, csv) > ")
            if file_type.lower() not in ['txt', 'json', 'csv']:
                print(f"\n\n{Fore.YELLOW}{Style.BRIGHT}[!] {Fore.RED}{Style.BRIGHT}Invalid file type. Skipping file output.\n")
            else:
                file_name = input("Enter File Name! > ")
                file_path = f"{file_name}.{file_type}"

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter += 1

            # Print [+] in green and URL in purple
            print(Fore.GREEN + "[+]", counter, Fore.MAGENTA + results)

            time.sleep(0.1)

            requ += 1
            if requ >= int(amount):
                break

            data = {"No": counter, "URL": results}
            results_list.append(data)

            if file_path and file_type:
                logger(data, file_path, file_type)

    except Exception as e:
        print(Fore.RED + f"Terjadi Kesalahan: {e}")

def main():
    init(autoreset=True)
    os.system("clear")
    dorks()

if __name__ == "__main__":
    main()
