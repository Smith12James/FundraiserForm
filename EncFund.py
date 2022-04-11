from cryptography.fernet import Fernet
import csv
import os.path
import time

key = b'ocmOHTg-C56jK8_9EKImdo-KTMmWAn-WzP_yf2lewOI='
fernet = Fernet(key)

file = 'fundraiserForm.csv'
encFile = 'encFundraiserForm.csv'

rows = []


    #write to CSV or create CSV and add info from GUI
def WriteToCSV(fullName, phoneNum, emailAddr, donation):
    doesExist = os.path.isfile('fundraiserForm.csv')
    if doesExist == True:
        with open(file, 'a', newline='') as csvFile:
            infoArr = [fullName, phoneNum, emailAddr, donation]
            formWriter = csv.writer(csvFile)
            formWriter.writerow(infoArr)

            EncCSV()
            time.sleep(1)
            DecCSV()
            time.sleep(1)


    else:
        with open(file, 'w', newline='') as csvFile:
            infoArr = [fullName, phoneNum, emailAddr, donation]
            formWriter = csv.writer(csvFile)
            formWriter.writerow(infoArr)

            EncCSV()
            time.sleep(1)
            DecCSV()
            time.sleep(1)


#Encrypt CSV file
def EncCSV():
    doesExist = os.path.isfile('fundraiserForm.csv')

    if doesExist == True:
        with open('fundraiserForm.csv', 'rb') as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open('encFundraiserForm.csv', 'wb') as file:
            file.write(encrypted)

    else:
        with open('encFundraiserForm.csv', 'wb') as file:
            original = file.read()
            encrypted = fernet.encrypt(original)
            file.write(encrypted)


#Decrypt CSV file
def DecCSV():
    with open('encFundraiserForm.csv', 'rb') as file:
        encrypted = file.read()

    decrypted = fernet.decrypt(encrypted)

    with open('decFundraiserForm.csv', 'wb') as file:
        file.write(decrypted)