from customtkinter import filedialog
import customtkinter
import time
import subprocess
import pyautogui
import os
from PIL import Image



ImageName = "Checking"

settingsconfigured = False
usinglist = False


current_dir = os.path.dirname(os.path.abspath(__file__))
twitchfile_loc = os.path.join(current_dir, 'all-scripts', 'twitch.py')
instafile_loc = os.path.join(current_dir, 'all-scripts', 'insatgram.py')
twitterfile_loc = os.path.join(current_dir, 'all-scripts', 'twitter.py')
try:
    open("Config.txt", "r")
    settingsconfigured = not False
except:
    open("config.txt", "w").close()


def instagram():
    subprocess.run(['python', instafile_loc])
def twitch():
    #userprompt x=930, y=392
    #submitprompt x=952, y=805
    subprocess.run(['python', twitchfile_loc])
def twitter():
    subheader.run(['python', twitterfile_loc])

    

def savesettings():
    with open("Config.txt", "w") as f:
        # Handle username settings based on the selections
        if readinglist.get() == 1:
            f.write("4\n")
            print("error")
        elif NumonlyVar.get() == 1:
            f.write("1\n")
        elif Letonlyvar.get() == 1:
            f.write("2\n")
        else:
            f.write("3\n")

        # Check if the username length was provided, otherwise write default
        if Userlen.get() != "":
            f.write(Userlen.get() + "\n")
        else:
            f.write("Default\n")

        # Handle file location selection
        if readinglist.get() == 1:
            FileLocation = customtkinter.filedialog.askopenfilename()
            if not FileLocation.endswith(".txt"):
                errorlabel.configure(text="FILE MUST END WITH TXT", text_color="Red", font=("Arial", 20))
                return  # Stop execution if the file extension is invalid
            else:
                errorlabel.configure(text="File Saved", text_color="Green", font=("Arial", 20))
            f.write(FileLocation + "\n")

        # Write the claim setting to the file
        if ClaimVar.get() == 1:
            f.write("\n1")
        elif readinglist.get() == 0 and ClaimVar.get() == 1:
            f.write("\n1")
        elif readinglist.get() == 0 and ClaimVar.get() == 0:
            f.write("\n0")
        
        # Update UI with a success message
        anythinglabel.configure(text="Settings Saved!", text_color="Green", font=("Arial", 20))
        settingsGui.destroy()
    


def usernameSettings():
    global letonly
    global numsonly
    global Userlen
    global NumonlyVar
    global readinglist
    global readlistsettings
    global Letonlyvar
    global ClaimVar
    global InstaClaim
    if Username_Variable.get() == 1:
        Letonlyvar = customtkinter.IntVar()
        NumonlyVar = customtkinter.IntVar()
        readinglist = customtkinter.IntVar()
        ClaimVar = customtkinter.IntVar()
        Userlen = customtkinter.CTkEntry(settingsGui, width=165, height=30, placeholder_text="        Username Length")
        numsonly = customtkinter.CTkCheckBox(settingsGui, text="Only Numbers", font=("Arial", 20), variable=NumonlyVar)
        letonly = customtkinter.CTkCheckBox(settingsGui, text="Only Letters", font=("Arial", 20), variable=Letonlyvar)
        readlistsettings = customtkinter.CTkCheckBox(settingsGui, text="Read List", font=("Arial", 20), variable=readinglist)
        InstaClaim = customtkinter.CTkCheckBox(settingsGui, text="Insta Claim", font=("Arial", 20), variable=ClaimVar)
        InstaClaim.place(relx=.19, rely=.55, anchor="center")
        readlistsettings.place(relx=0.18, rely=0.49, anchor="center")
        letonly.place(relx=0.199, rely=0.42, anchor="center")
        numsonly.place(relx=0.21, rely=0.35, anchor="center")
        Userlen.place(relx=0.21, rely=0.28, anchor="center")
    else:
        Userlen.place_forget()
        letonly.place_forget()
        numsonly.place_forget()
        readlistsettings.place_forget()
        InstaClaim.place_forget()

def settings():
    global errorlabel
    global settingsGui
    global Username_Variable
    settingsGui = customtkinter.CTk()
    settingsGui.geometry("700x450")
    settingsGui.resizable(False, False)
    settingsGui.title("Settings")

    header = customtkinter.CTkLabel(settingsGui, text="Settings", font=("Arial", 32))
    header.place(relx=0.5, rely=0.05, anchor="center")

    Username_Variable = customtkinter.IntVar()
    Usersettings = customtkinter.CTkCheckBox(settingsGui, text="Username Settings", font=("Arial", 20), variable=Username_Variable, command=usernameSettings)
    Usersettings.place(relx=0.2, rely=0.2, anchor="center")

    errorlabel = customtkinter.CTkLabel(settingsGui, text=" ", font=("Arial", 20), fg_color="Green", text_color="Red")

    savebtn = customtkinter.CTkButton(settingsGui, text="Save", font=("Arial", 20), fg_color="Green", text_color="White", command=savesettings)
    savebtn.place(relx=0.5, rely=0.9, anchor="center")

    settingsGui.mainloop()

# Main Window
MainGui = customtkinter.CTk()
MainGui.geometry("700x450")
MainGui.resizable(False, False)
MainGui.title("HandleHunter - 80dropz")
MainGui.iconbitmap('HandleHunterLogo.jpg')

# Header and Subheader
header = customtkinter.CTkLabel(MainGui, text="HandleHunter", font=("Arial", 32))
header.place(relx=0.5, rely=0.05, anchor="center")
subheader = customtkinter.CTkLabel(MainGui, text="By: 80dropz", font=("Arial", 20))
subheader.place(relx=0.5, rely=0.12, anchor="center")

# Twitch Button
twitchbtn = customtkinter.CTkButton(MainGui, text="Twitch", font=("Arial", 20), fg_color="#6342a2", text_color="Black", command=twitch)
twitchbtn.place(relx=.2, rely=.3, anchor="center")

# Instagram Button
igbtn = customtkinter.CTkButton(MainGui, text="Instagram", font=("Arial", 20), fg_color="#fb23a8", text_color="Black", command=instagram)
igbtn.place(relx=.2, rely=.45, anchor="center")



#twitter button 
xbtn = customtkinter.CTkButton(MainGui, text="Twitter", font=("Arial", 20), fg_color="#088ccf", text_color="Black", command=twitter)
xbtn.place(relx=.2, rely=.60, anchor="center")

# Settings Button
settingsbtn = customtkinter.CTkButton(MainGui, text="Settings", font=("Arial", 20), fg_color="#545454", text_color="White", command=settings)
settingsbtn.place(relx=.12, rely=.05, anchor="center")

#will store anything that i need to randomly in here
anythinglabel = customtkinter.CTkLabel(MainGui, text=" ",)
anythinglabel.place(relx=.5, rely=.95, anchor="center")


#checks if there is a config file and if there is prints ("Settings Loaded!")
if settingsconfigured:
    anythinglabel.configure(text="Settings Loaded!", text_color="Green", font=("Arial", 20))
MainGui.mainloop()

