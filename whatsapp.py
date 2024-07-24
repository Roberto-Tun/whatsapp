import csv
import pywhatkit as whats
import datetime

# Ensure the file encoding is specified, often needed for CSV files to be read correctly
with open('dummyData.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == 'Status':
            continue
        elif row[0] == 'Whatsapp':
            number = row[2]
            name = row[1]
            message = f"Dear {name}, DFC is currently updating our database, and we need your assistance to ensure the accuracy of your information. To complete this update, we kindly request that you provide us with a copy of your Social Security card to verify your account with DFC. Your cooperation is highly appreciated. As a token of our gratitude, you will be entered into a raffle to win $250 towards your DFC account. Please send the requested information at your earliest convenience. Thank you for your prompt attention to this matter. Best regards, DFC Team"
            whats.sendwhatmsg(f"+501{number}", message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1, 10, True, 3)

