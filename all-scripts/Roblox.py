import pyautogui
import keyboard
import customtkinter
import time
import random
import threading
from PIL import ImageGrab

try:
    open("Robloxuser.txt", "r")
except:
    open("Robloxuser.txt", "w").close()
try:
    open("RobloxUnclaimed.txt", "r")
except:
    open("RobloxUnclaimed.txt", "w").close()

letlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numlist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
bothlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]


        

#ALL CORDS
#First Click
FirstClickX = 965
FirstClickY = 242

UserNamePromptX = 937
UsernamePromptY = 455

UsernamePromptSuccessX = 929
UsernamePromptSuccessY = 472

UsernameSuccessX = 815
UsernameSuccessY = 784

UsernameFailX = 807
UsernameFailY = 812

firstclick = False
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
    else:
        InstaClaim = not False

    try:
        charlength = int(l2)
    except:
        charlength = 4

        

def get_user(length):
    try:
        if usinglist:
            lineon = 0
            with open(FileLocation, "r") as f:
                lineon += 1
                lines = f.readlines()
                userinlist = lines[lineon]
                return userinlist
    except:
        pass
    if numonly:
        return ''.join(random.choice(numlist) for i in range(length))
    elif letonly:
        return ''.join(random.choice(bothlist) for i in range(length))
    else:
        return ''.join(random.choice(numlist + bothlist) for i in range(length))



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
    global firstclick
    while running:  # While running is True
        tempname = get_user(charlength)
        with open("RobloxUser.txt", "r") as tur:
            if tempname in tur.read():
                perform_clicks()
            else:
                with open("RobloxUser.txt", "a") as tua:
                    tua.write(f"\n{tempname}")


        if firstclick == False:
            pyautogui.click(FirstClickX, FirstClickY)
            firstclick = not False
        else:
            pass


        time.sleep(.3)
        print("Username Prompt")
        pyautogui.click(UserNamePromptX, UsernamePromptY)
        pyautogui.click(UserNamePromptX, UsernamePromptY)
        time.sleep(0.5)

        tempname = get_user(charlength)
        keyboard.write(tempname)

        if InstaClaim == True:
            pyautogui.click(UsernameSuccessX, UsernameSuccessY)
        else:
            print("Username Success")
            pyautogui.moveTo(UsernameSuccessX, UsernameSuccessY)
            time.sleep(.5)
            screenshot = ImageGrab.grab()
            
            color = screenshot.getpixel((UsernameSuccessX, UsernameSuccessY))
            print(color)
            if color == (255, 255, 255):
                with open("RobloxUnclaimed.txt", "a") as fa:
                    fa.write(f"\n{tempname}")
            del screenshot
            
        

        time.sleep(0.5)

def Roblox():
    prompt.configure(text="Fill out all prompts on signup then click 'p' to start", font=("Arial", 16))
    


main = customtkinter.CTk()
main.title("Roblox Handle Hunter")
main.geometry("400x350")
main.resizable(False, False)



header = customtkinter.CTkLabel(main, text="Roblox Handle Hunter", font=("Arial", 32), text_color="#ffffff")
header.place(relx=0.5, rely=0.05, anchor="center")

subheader = customtkinter.CTkLabel(main, text="By: 80dropz", font=("Arial", 20))
subheader.place(relx=0.5, rely=0.12, anchor="center")

prompt = customtkinter.CTkLabel(main, text=" ", font=("Arial", 20))
prompt.place(relx=0.5, rely=0.5, anchor="center")

startbtn = customtkinter.CTkButton(main, text="Start", font=("Arial", 20), text_color="Black", fg_color="#ffffff", command=Roblox)
startbtn.place(relx=0.5, rely=0.3, anchor="center")




keyboard.add_hotkey("p", p_clicked)
main.mainloop()
