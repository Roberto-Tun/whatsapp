import csv
with open('Test1.csv', 'r', encoding='utf-8') as file: #opens the excel file (csv)
    reader = csv.reader(file)
    notReached = []
    rowCounter = 0
    for row in reader:
        if rowCounter == 0:
            row.append("tester")
        elif rowCounter > 0:
            number = row[2]
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

            row[2] = cleannumber
            nextKinName = row[7]
            nextKinName = nextKinName.strip("1234567890/.()-| ")

            nextKinNumber = row[7]
            nextKinNumber = nextKinNumber.strip(" .+-()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

            row[7] = nextKinName
            row.append(nextKinNumber)
        rowCounter += 1
    

        notReached.append(row)
    
    with open('results.csv', 'w', encoding='utf-8') as newfile: #opens the excel file (csv)
        writer = csv.writer(newfile, lineterminator='\n')
        for cust in notReached:
            writer.writerow(cust)
            #newreader.writerow(row+["TEST"])

