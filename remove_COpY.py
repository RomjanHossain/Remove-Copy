# importing some modules
import os
from collections import Counter
from ctypes import *


# change directory
drive = input(
    "Enter which drive you want to search :\n[C, D, E, F or G]\nDrive: ")
ndrive = drive+":\\"
os.chdir(ndrive)
print("Your'r current directory is", os.getcwd())       # "F:\\"
specific_folder = input("Any specific_folder :\n")
if specific_folder in ['no', "NO", "No"]:
        drive = ndrive
else:
        drive = f"{drive}:\{specific_folder}\\"

print(drive)
# defining some global variables
save = []
copyed = []
removed_from = []
count = 0
counter = []

# getting all the files
for path, folder, files in os.walk(drive):
    # print("current path: "+ path)
    # spl = path.split('\\',',')
    # print('current folders: ' , folder)
    save += files


# counting all the duplicate files

jack = Counter(save)
# print(jack.values())


def if_in_dup():
    global jack
    for a, b in jack.items():
        # print(a,b)
        if b == 2:
            copyed.append(a)
            # print(copyed)

# printing coped items


def count_copy():
    global count
    global counter
    global copyed
    if copyed == []:
        print("You've no duplicate files in you dirs")
    else:
        for i in copyed:
            count += 1
            counter.append(f"{count}.{i}")
        # print("=========================")

# messagebox.showinfo("Information","Informative message")


def show_copy():
    global count
    global counter
    if windll.user32.MessageBoxW(0, f"You've {count} copyed files!", "Copyed Files", 1) == 1:
        for i in counter:
            windll.user32.MessageBoxW(0, f"{i}", "Files", 1)
    else:
        windll.user32.MessageBoxW(0, "Thank You", "Thanks", 1)
# final part


def removing():
    global drive
    global copyed
    global removed_from
    permission = input(
        "If you want to delete those files\nType 'Yes'\nelse Type 'No'\nType Here :")
    if permission in ["Yes", "yes", "YES"]:

            # if_in_dup()
        for path, folder, files in os.walk(drive):
            for i in files:
                if i in copyed:
                    removed_from.append(path+'\\'+i)
                    os.chdir(path)
                    os.remove(i)
                    copyed.remove(i)
        print("Task complete")
    elif permission in ["No", "no", "NO"]:
        print("Thank you. \nWe didn't remove anything from this path!")
    else:
        print("try again")
        permission = input("Write Yes or No\n")


'''def duplicate_or_not():
        if copyed == []:
                print("You've no duplicate files in you dirs")
        else:
                print(f"You have some Duplicate files in this dir--> {copyed}")

duplicate_or_not()'''


def run():
    if_in_dup()
    count_copy()
    show_copy()
    removing()


if __name__ == "__main__":
    run()
