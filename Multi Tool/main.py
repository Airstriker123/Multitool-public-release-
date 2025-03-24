from colorama import Fore, init
import sys
import time
import socket
import os
import random
from datetime import datetime
import webbrowser
import platform
import requests
import json

init(autoreset=True)

#get keys at https://aimlapi.com/app/keys
api_keys = {
    "INSERT_KEY_HERE",
    "",
    "",
    "",
    "", 
}
api_url = "https://api.aimlapi.com/v1/chat/completions"
current_date = datetime.now().strftime("%d-%m-%Y")
pc_name = socket.gethostname()
try:
    user_name = os.getlogin()
except OSError:
    user_name = "Unknown User"  # Fallback if os.getlogin() fails


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_gui():
    clear_screen()
    current_time = datetime.now().strftime("%I:%M:%S %p")
    print(Fore.RED + """
_____________________________________________________________________________________________________________
███╗██╗███╗    ███╗   ███╗██╗   ██╗██╗  ████████╗██╗    ████████╗ ██████╗  ██████╗ ██╗     ██╗    ███╗██╗███╗
██╔╝██║╚██║    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██║    ██╔╝██║╚██║
██║ ██║ ██║    ██╔████╔██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     ██║    ██║ ██║ ██║
██║ ╚═╝ ██║    ██║╚██╔╝██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     ╚═╝    ██║ ╚═╝ ██║
███╗██╗███║    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║       ██║   ╚██████╔╝╚██████╔╝███████╗██╗    ███╗██╗███║
╚══╝╚═╝╚══╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝    ╚══╝╚═╝╚══╝
_____________________________________________________________________________________________________________                                                                              
""")
    print(Fore.MAGENTA + " │date: " + Fore.YELLOW + f"{current_date}")
    print(Fore.MAGENTA + " │time: " + Fore.YELLOW + f"{current_time}")
    print(Fore.MAGENTA + " ├─────────────────────────────")
    print(Fore.MAGENTA + " │Running on: ")
    print(Fore.MAGENTA + " │device name: " + Fore.BLUE + f"{pc_name}")
    print(Fore.MAGENTA + " │User:  " + Fore.LIGHTRED_EX + f"{user_name}")
    print(Fore.MAGENTA + " ├─────────────────────────────")
    print(Fore.MAGENTA + " │Project by: Airstriker")
    print(Fore.MAGENTA + " │Link: https://github.com/Airstriker123/Multitool-public-release-")
    print(Fore.MAGENTA + " ├─────────────────────────────")
    print(
        Fore.CYAN + "Enter the number given next to an option to execute command (e.g., entering 1 will execute game)")
    print(
        Fore.CYAN + "_____________________________________________________________________________________________________________ ")


def display_menu():
    print(Fore.YELLOW + """
  ╔═══                              ═══╗                    ╔═══                              ═══╗    
    [!] 1: Play number guessing game                            [!] 2 : Exit App (or type exit)

    [!] 3: Refresh gui(updates gui/time)                        [!] 4: Current Date

    [!] 5: Show a Random Quote                                  [!] 6: Show System Information

    [!] 7: open google classroom                                [!] 8: Sand Monkey (A.i)  
  ╚═══                              ═══╝                    ╚═══                              ═══╝""")
    print(
        Fore.CYAN + "_____________________________________________________________________________________________________________ ")


def execute_command(command):
    if command == '1':
        number_guessing_game()
    elif command == '2':
        print(Fore.GREEN + "Exiting APP!")
        sys.exit()
    elif command == '3':
        gui_update()
    elif command == '4':
        print(Fore.GREEN + f"Current Date: {current_date}")
    elif command == '5':
        random_quote()
    elif command == '6':
        show_system_info()
    elif command == '7':
        webbrowser.open('https://classroom.google.com')
    elif command == '8':
        Sand_Monkey_AI()
    else:
        print(Fore.RED + 'Invalid option! Please choose the correct one.')


def send_message(user_message):
    if not user_message:
        print("Error: No message entered.")
        return

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    for api_key in api_keys:
        try:
            response = requests.post(api_url, headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }, data=json.dumps(payload))

            #error handle
            data = response.json()

            if data and "choices" in data:
                ai_message = data["choices"][0]["message"]["content"]
                print(Fore.LIGHTCYAN_EX + f"🐒Sand Monkey🤖:", Fore.WHITE + f"{ai_message}")
                break  # Exit loop if the request is successful
            else:
                print("Error: Unable to retrieve response. Trying next API key.")
                print(Fore.LIGHTRED_EX + "Switching to the next API key, please wait...")

        except requests.exceptions.RequestException as error:
            print(f"Error: Unable to connect with API key {api_key}. {error}")
            print(Fore.LIGHTRED_EX + "Attempting to use the next available API key...")


# rest

def Sand_Monkey_AI():
    print(
        Fore.LIGHTGREEN_EX + 'Remember to type ' + Fore.RED + 'exit' + Fore.LIGHTGREEN_EX + ' once you have completed your prompts')
    while True:
        user_input = input(Fore.YELLOW + "\b👨‍💻You: ")
        if user_input.lower() == "exit":
            print(Fore.RED + 'Exiting program.')
            break
        send_message(user_input)

def number_guessing_game():
    private_number = random.randint(1, 100)
    attempts = 0
    player = input(Fore.LIGHTMAGENTA_EX + "What is your chosen player name? ")
    while True:
        guess = input(Fore.CYAN + "Guess a number between 1 and 100: ")
        try:
            guess = int(guess)
            attempts += 1
            if guess < private_number:
                print(Fore.YELLOW + "Too low!")
            elif guess > private_number:
                print(Fore.YELLOW + "Too high!")
            else:
                current_time = datetime.now().strftime("%I:%M:%S %p")
                print(Fore.LIGHTRED_EX + f"{player}", Fore.GREEN + f"has guessed the number in",
                      Fore.LIGHTCYAN_EX + f"{attempts}", Fore.GREEN + f"attempts! on",
                      Fore.LIGHTYELLOW_EX + f"{current_date}", Fore.GREEN + "at",
                      Fore.LIGHTMAGENTA_EX + f"{current_time}!")
                with open("results.txt", "a") as file:
                    file.write(
                        f"{player} has guessed the number in {attempts} attempts! on {current_date} at {current_time}!\n")
                print("Game results have also been saved as a txt file in the current folder!")
                break
        except ValueError:
            print(Fore.RED + "Please enter a valid number")


def random_quote():
    quotes = [
        "Believe you can and you're halfway there.",
        "Keep going. Everything you need will come to you at the perfect time.",
        "The purpose of our lives is to be happy.",
        "In the end, we only regret the chances we didn't take."
    ]
    print(Fore.GREEN + random.choice(quotes))


def show_system_info():
    os_info = platform.system() + " " + platform.release()
    processor = platform.processor()
    print(Fore.GREEN + f"Operating System: {os_info}")
    print(Fore.GREEN + f"Processor: {processor}")


def gui_update():
    while True:
        print_gui()
        display_menu()
        command = input(Fore.LIGHTCYAN_EX + '> ')
        if command.lower() == 'exit':
            print(Fore.GREEN + "Exiting APP!")
            sys.exit()
        execute_command(command)


def main_loop():
    while True:
        print_gui()
        display_menu()
        command = input(Fore.LIGHTCYAN_EX + '> ')
        if command.lower() == 'exit':
            print(Fore.GREEN + "Exiting APP!")
            sys.exit()
        execute_command(command)

        final_print = "Choose another option!"
        print(Fore.BLUE + final_print)
        z = Fore.BLUE
        input(f"{x}PRESS ENTER TO CONTINUE: ")

main_loop()
