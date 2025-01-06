#951, y=442 userprompt
import pyautogui
import keyboard
import customtkinter
import time
import random
import threading
try:
    open("Instauser.txt", "r")
except:
    open("Instauser.txt", "w").close()

letlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numlist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
bothlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]



running = False  
numonly = False
letonly = False
bothallowed = False

with open("config.txt", "r") as f:
    lines = f.readlines()
    l1 = lines[0].strip()
    l2 = lines[1].strip()
    if l1 == "1":
        numonly = not False
    elif l1 == "2":
        letonly = not False
    elif l1 == "3":
        bothallowed = not False
    try:
        charlength = int(l2)
    except:
        charlength = 4
        

def get_user(length):
    with open("instauser.txt", "r") as f:
            existing_users = f.read().strip().splitlines()  # Read existing usernames into a list

        # Generate a new username based on the conditions
    while True:
        if numonly:  # Generate only numbers
            new_user = ''.join(random.choice(numlist) for _ in range(length))
        elif letonly:  # Generate only letters
            new_user = ''.join(random.choice(bothlist) for _ in range(length))
        else:  # Generate both numbers and letters
            new_user = ''.join(random.choice(numlist + bothlist) for _ in range(length))

            # Check if the generated username is unique
        if new_user not in existing_users:
            with open("instauser.txt", "a") as f:  # Open in append mode
                f.write(new_user + '\n')  # Write the new unique username
            return new_user  # Return the unique username




def p_clicked():
    global running  # Declare running as global
    if not running:  # If running is False
        running = True  # Set running to True
        prompt.configure(text="Press 'p' to stop", font=("Arial", 16))
        
        # Start a new thread for the clicking operation
        threading.Thread(target=perform_clicks).start()
    else:  # If running is True
        running = False  # Set running to False
        prompt.configure(text=" ", font=("Arial", 20))
        prompt.configure(text="Fill out all prompts on signup then click 'p' to start", font=("Arial", 16))

def perform_clicks():
    while running:  # While running is True
        pyautogui.click(951, 442)
        time.sleep(0.3)
        pyautogui.click(951, 442)
        pyautogui.click(951, 442)
        time.sleep(0.2)
        keyboard.write(get_user(charlength))
        pyautogui.click(947, 700)
        time.sleep(0.5)
        pyautogui.click(947, 665)
        pyautogui.click(948, 638)
        with open("Instauser.txt", "a") as f:
            f.write(get_user(charlength) + "\n")
def twitch():
    prompt.configure(text="Fill out all prompts on signup then click 'p' to start", font=("Arial", 16))
    
main = customtkinter.CTk()
main.title("Insta Handle Hunter")
main.geometry("400x350")
main.resizable(False, False)



header = customtkinter.CTkLabel(main, text="Insta Handle Hunter", font=("Arial", 32), text_color="#fb23a8")
header.place(relx=0.5, rely=0.05, anchor="center")
subheader = customtkinter.CTkLabel(main, text="By: 80dropz", font=("Arial", 20))
subheader.place(relx=0.5, rely=0.12, anchor="center")

prompt = customtkinter.CTkLabel(main, text=" ", font=("Arial", 20))
prompt.place(relx=0.5, rely=0.5, anchor="center")

startbtn = customtkinter.CTkButton(main, text="Start", font=("Arial", 20), text_color="White", fg_color="#fb23a8", command=twitch)
startbtn.place(relx=0.5, rely=0.3, anchor="center")




keyboard.add_hotkey("p", p_clicked)
main.mainloop()
