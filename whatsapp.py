import csv
import pywhatkit as whats
import datetime
import pyautogui

# Ensure the file encoding is specified, often needed for CSV files to be read correctly
'''with open('dummyData.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == 'Action':
            continue
        elif row[0] == 'Whatsapp':
            name = row[7]
            number = row[17]
            cleannumber = number.strip(" +-(abcdefghijklmnopqrstuvwxyz)")
            country = row[16]
            message = f"Dear {name}, DFC is currently updating our database, and we need your assistance to ensure the accuracy of your information. To complete this update, we kindly request that you provide us with a copy of your Social Security card to verify your account with DFC. Your cooperation is highly appreciated. As a token of our gratitude, you will be entered into a raffle to win $250 towards your DFC account. Please send the requested information at your earliest convenience. Thank you for your prompt attention to this matter. Best regards, DFC Team"
            
            try:
                if country == "Belize" and cleannumber[:3] == "501":
                    whats.sendwhatmsg(f"+{cleannumber}", message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1, 10, True, 3)
                elif country == "Belize":
                    whats.sendwhatmsg(f"+501{cleannumber}", message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1, 10, True, 3)
                elif country == "United States" and cleannumber[:1] == "1":
                    whats.sendwhatmsg(f"+{cleannumber}", message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1, 10, True, 3)
                elif country == "United States":
                    whats.sendwhatmsg(f"+1{cleannumber}", message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1, 10, True, 3) 
            except:
                print("Error with number: ", cleannumber)'''
            

with open('Test1.csv', 'r', encoding='utf-8') as file: #opens the excel file (csv)
    reader = csv.reader(file)
    internExt = {"Roberto":"619", "Zoe": "618", "Nia": "617", "Daniel":"620", "Naisha":"621" } #dictionary to save the different extensions
    notReached = []

    for row in reader:
        if row[0] == 'Status':
            continue
        elif row[0] == 'Whatsapp' or row[0] == "Pending": #checks if the action is 'whatsapp' or 'pending'
            name = row[1]
            number = row[2]
            seminumber = number.strip(" +-()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") #removes any additional symbol added to the number
            seminumber = seminumber.lstrip("501")

            if seminumber[3] == " " or seminumber[3] == "-": #remove the dash and rebuilds the number
                firstpart = seminumber[:3]
                secondpart = seminumber[4:]
                cleannumber = firstpart + secondpart
            else:
                cleannumber = seminumber


            country = row[4]

            if row[5] in internExt.keys(): #checks if the intern exists in the dictionary established
                ext = internExt[row[5]] #selects the intern assigned to current client
                message = f"Dear {name}, \nThis is just a friendly reminder from DFC about the details mentioned in the previous message to finalize your update. \n\nFor additional information or assistance, please contact us at (501) 822-2575 Ext: {ext} or via WhatsApp at 6705310.\nYour prompt response would be greatly valued.\nThank you in advance for your attention to this matter.\nBest regards, \nDFC"
            
            try: #checks if the current number is from Belize or US
                if country == "Belize" and len(cleannumber) == 7:
                    whats.sendwhatmsg(f"+{cleannumber}", message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1, 10, True, 5)
                    pyautogui.press("enter")
                elif country == "United States":
                    whats.sendwhatmsg(f"+1{cleannumber}", message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1, 10, True, 5)
                    pyautogui.press("enter")
                else:
                    print("Customer not reached: ", name, "Number: ", cleannumber)
                    notReached.append(row[6]) #add id of client not reached

            except:
                print("Error with number: ", cleannumber)
    
    f = open("ClientsNotReached.txt", 'w') #file to write the client's ID who wasn't contacted
    for client in notReached:
        f.write(client + "\n")
    f.close
