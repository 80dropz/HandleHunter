import pyautogui
import keyboard
import customtkinter
import time
import random
import threading
try:
    open("Twitter.txt", "r")
except:
    open("Twitter.txt", "w").close()

letlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numlist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
bothlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]

lineon = 0

InstaClaim = False
running = False  
numonly = False
letonly = False
bothallowed = False

with open("config.txt", "r") as f:
    lines = f.readlines()
    l1 = lines[0].strip()
    l2 = lines[1].strip()
    l3 = lines[2].strip()
    l4 = lines[3].strip()
    
    if l1 == "1":
        numonly = not False
    elif l1 == "2":
        letonly = not False
    elif l1 == "3":
        bothallowed = not False
    elif l1 == "4":
        usinglist = not False
        l3 = lines[2].strip()
        FileLocation = l3
        print(f"using custom list at {FileLocation}")
    if l4 == "0":
        pass
    elif l4 == "1":
        InstaClaim = not False
    
    try:
        charlength = int(l2)
    except:
        charlength = 4

        

def get_user(length):
    global lineon
    if usinglist:
        with open(FileLocation, "r") as f:
            lineon += 1
            lines = f.readlines()
            userinlist = lines[lineon]
            return userinlist
        p
    elif numonly:
        return ''.join(random.choice(numlist) for i in range(length))
    elif letonly:
        return ''.join(random.choice(bothlist) for i in range(length))
    else:
        return ''.join(random.choice(numlist + bothlist) for i in range(length))



def p_clicked():
    global running 
    if not running: 
        running = True 
        prompt.configure(text="Press 'p' to stop", font=("Arial", 16))
        
        # Start a new thread for the clicking operation
        threading.Thread(target=perform_clicks).start()
    else:  # If running is True
        running = False  # Set running to False
        prompt.configure(text=" ", font=("Arial", 20))
        prompt.configure(text="Fill out all prompts on signup then click 'p' to start", font=("Arial", 16))

def perform_clicks():
    while running:  # While running is True
        pyautogui.click(1079, 201)
        time.sleep(0.3)
        pyautogui.click(1079, 201)
        pyautogui.click(1079, 201)
        time.sleep(0.2)
        keyboard.write(get_user(charlength))
        pyautogui.click(1468, 357)
        time.sleep(0.5)
        pyautogui.click(1472, 509)
        time.sleep(.5)
        pyautogui.click(1466, 473)

def twitter():
    prompt.configure(text="Fill out all prompts on signup then click 'p' to start", font=("Arial", 16))
    


main = customtkinter.CTk()
main.title("Twitter Handle Hunter")
main.geometry("400x350")
main.resizable(False, False)



header = customtkinter.CTkLabel(main, text="Twitter Handle Hunter", font=("Arial", 32), text_color="#088ccf")
header.place(relx=0.5, rely=0.05, anchor="center")

subheader = customtkinter.CTkLabel(main, text="By: 80dropz", font=("Arial", 20))
subheader.place(relx=0.5, rely=0.12, anchor="center")

prompt = customtkinter.CTkLabel(main, text=" ", font=("Arial", 20))
prompt.place(relx=0.5, rely=0.5, anchor="center")

startbtn = customtkinter.CTkButton(main, text="Start", font=("Arial", 20), text_color="White", fg_color="#088ccf", command=twitter)
startbtn.place(relx=0.5, rely=0.3, anchor="center")




keyboard.add_hotkey("p", p_clicked)
main.mainloop()
