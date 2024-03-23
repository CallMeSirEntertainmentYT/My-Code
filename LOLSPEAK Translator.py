import random
import time as tiem
def katify_text(text):
    text = text.upper()
    text = text.replace("HI", "HOI")
    text = text.replace("CHEESE", "CHEEZ")
    text = text.replace("HAVE", "HAS")
    text = text.replace("HELLO", "HEWWO")
    text = text.replace("YOU", "U")
    text = text.replace("ZE", "Z")
    text = text.replace("CAN I", "I CAN")
    text = text.replace("KITTY", "KITTEH")
    text = text.replace("CAT", "KAT")
    text = text.replace("ARE", "R")
    text = text.replace("GOOD", "GUD")
    text = text.replace("DUMB", "DUM")
    text = text.replace("DOCTOR", "DOCTA")
    text = text.replace("HEART", "HART")
    text = text.replace("AM", "IZ")
    text = text.replace("IS", "IZ")
    text = text.replace("THE", "DA")
    text = text.replace("ING", "IN")
    text = text.replace("SYSTEM", "SISTAM")
    text = text.replace("LIKE", "LIEK")
    text = text.replace("MIGHT", "MITE")
    text = text.replace("TO", "2")
    text = text.replace("FOR", "4")
    text = text.replace("SOME", "SUM")
    text = text.replace("TIME", "TIEM")
    text = text.replace("LAUGHS", "LOLZ")
    text = text.replace("LAUGH", "LAFF")
    text = text.replace("IMPROVE", "IMPROOV")
    return text
tranzlate = True
furst_tiem = True
while tranzlate == True:
    if furst_tiem == True:
        furst_tiem = False
        input_text = input("ENTR SUM TEXT:\n")
    else:
        input_text = input("\nENTR SUM TEXT:\n")
    output_text = katify_text(input_text)
    loadin_tiem = random.randint(1,5)
    print("\nTRANZLATIN...")
    tiem.sleep(loadin_tiem)
    print("\nTRANZLASHUN:", output_text)
    confirmashun = input("\nDO U WANTS 2 DO ANOTHR TRANZLASHUN? (y/n)\n")
    if confirmashun == "y":
        tranzlate = True
    else:
        tranzlate = False
        print("\nTANKS 4 USIN!")
        break
