
import sys

sys.path.append(r"c:\Users\BUYER CT\AppData\Local\Programs\Python\Python312\Lib\site-packages")
import msoffcrypto

encrypted = open(r"e:\odoo.xlsx", "rb")
file = msoffcrypto.OfficeFile(encrypted)

file.load_key(password="IPACRCI")  # Use password

with open("e:\final.xlsx", "wb") as f:
    openFile = file.decrypt(f)




    
    




