import csv
import pywhatkit as whats
import datetime
import pyautogui

with open('CustomerContact.csv', 'r', encoding='utf-8') as file: #opens the excel file (csv)
    reader = csv.reader(file)
    internExt = {"Kian":"622", "Marleni": "299", "Michael": "239", "Ravin":"244", "Vlademir":"253" } #dictionary to save the different extensions
    notReached = []

    for row in reader:
        if row[1] == 'Status':
            continue
        elif row[1] == 'Whatsapp' or row[1] == "Pending": #checks if the action is 'whatsapp' or 'pending'
            name = row[2]
            number = row[4]
            seminumber = number.strip(" .+-()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") #removes any additional symbol added to the number
            seminumber = seminumber.lstrip("501")

            if seminumber == " " or seminumber == "":
                cleannumber = ""
            elif (seminumber[3] == " " or seminumber[3] == "-") and len(seminumber) >= 7: #remove the dash and rebuilds the number
                firstpart = seminumber[:3]
                secondpart = seminumber[4:8]
                cleannumber = firstpart + secondpart
            else:
                cleannumber = seminumber

            if row[0] in internExt.keys(): #checks if the intern exists in the dictionary established
                ext = internExt[row[0]] #selects the intern assigned to current client
                message = f"Dear {name}, \nThis is just a friendly reminder from DFC about the details mentioned in the previous message to finalize your update. \n\nFor additional information or assistance, please contact us at (501) 822-2575 Ext: {ext} or via WhatsApp at 6705310.\nYour prompt response would be greatly valued.\nThank you in advance for your attention to this matter.\nBest regards, \nDFC"


            try: #checks if the current number is from Belize or US
                if cleannumber != "" or cleannumber != " ":
                    whats.sendwhatmsg(f"+{cleannumber}", message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1, 10, True, 12)
                    pyautogui.press("enter")
            except:
                print("Customer not reached: ", name, "Number: ", cleannumber)
                notReached.append(row[3]) #add id of client not reached
    
    f = open("ClientsNotReached.txt", 'w') #file to write the client's ID who wasn't contacted
    for client in notReached:
        f.write(client + "\n")
    f.close
