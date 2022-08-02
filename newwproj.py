import matplotlib.pyplot as plt
import numpy as np
# import mysql.connector
def final_bill() : #USER INFO + INVOICE
    global F_Total
    while True :
        name1 = input("Owner's Name (only First Name) : ")
        if name1.isalpha() == False :
            print("Name should not have digits in them....!")
        else :
            break
    address1 = input("Owner's Address : ")
    while True :
        phone1 = input("Owner's Phone Number : ")
        if phone1.isdigit() and len(phone1) == 10 :
            break
        else :
            print("Invalid Phone Number....!")
    while True :
        pincode1 = input("Owner's Address Pincode : ")
        if pincode1.isdigit() and len(pincode1) == 6 :
            break
        else :
            print("Invalid Pincode....!")
    print(format("","=^78"))
    print(format("FINAL-BILL","-^78"))
    print(format("","=^78"),"\n")
    print(format("","-^78"))
    print("|"+format("NAME","^25")+"|"+format(name1,"^50")+"|")
    print("|"+format("ADDRESS","^25")+"|"+format(address1,"^50")+"|")
    print("|"+format("PHONE","^25")+"|"+format(phone1,"^50")+"|")
    print("|"+format("PINCODE","^25")+"|"+format(pincode1,"^50")+"|")
    print(format("","-^78"))
    print("|"+format("PAYABLE AMOUNT","^25")+"|"+format(str(F_Total),"^50")+"|")
    print(format("","-^78"))
def confirm_order() : #CHANGE MODES OR CHECKOUT
    while True : 
        print("Do you want to go back to CUSTOM store or reselect packs again or checkout ? ")
        print("1. CUSTOM STORE : ")
        print("2. PRE-MADE PACKS : ")
        print("3. CHECKOUT ")
        s1 = input(" : ")
        if s1 == "1" :
            print("Directing Towards the Custom Store now.....")
            shopping()
        elif s1 == "2" :
            print("U can reselect Packs again")
            packs()
        elif s1 == "3" :
            break
        else :
            print("Invalid Input....!")
    final_bill()
    print("Thanks for shopping....!")
def error_check(check1) : #DIGIT CHECKER
    if check1.isdigit() :
        check1 = int(check1)
        if check1 != 1 and check1 != 2 and check1 != 3 and check1 != 4 :
            check1 = ""
        else :
            pass
    else :
        check1 = ""
    return check1
def Invoice(dict1,tot) : #INVOICE PRINTER
    print(format("","=^78"))
    print(format("INVOICE","-^78"))
    print(format("","=^78"),"\n")
    print(format("","-^78"))
    print("|"+format("SR.NO","^12")+"|"+format("COMPUTER PART","^27")+"|"+format("ITEM","^17")+"|"+format("COST","^17")+"|")
    print(format("","-^78"))
    sr_no = 1
    comp_parts = ["PROCESSOR","GRAPHICS CARD","DISPLAY","RAM"]
    for part,costs in dict1.items() :
        print("|"+format(str(sr_no),"^12")+"|"+format(comp_parts[(sr_no)-1],"^27")+"|"+format(part,"^17")+"|"+format(str(costs),"^17")+"|")
        sr_no += 1
    print(format("","-^78"))
    print("|"+format("SUB TOTAL","^15"),format("|",">43")+format(str(tot),"^17")+"|")
    print(format("","-^78"))
    CGST = int(0.09*tot)
    SGST = int(0.09*tot)
    global F_Total
    F_Total = tot + CGST + SGST
    print("|"+format("CGST","^15"),format("|",">43")+format(str(CGST),"^17")+"|")
    print("|"+format("SGST","^15"),format("|",">43")+format(str(SGST),"^17")+"|")
    print(format("","-^78"))
    print("|"+format("TOTAL","^15"),format("|",">43")+format(str(F_Total),"^17")+"|")
    print(format("","-^78"))
def packs() : #PACKS SELECTION :
    print(format("","-^78"))
    print(format("PREDEFINED PACKS","-^78"))
    print(format("","-^78"))
    print("Here are the packs : \n")
    print("1.School : ")
    print("Processor : i3 - 6000")
    print("RAM : 4GB - 6000")
    print("Display : LG - 3000")
    print("Graphics Card : 1GB - 5000\n")
    print("2.Company : ")
    print("Processor : i5 - 10000")
    print("RAM : 8GB - 10000")
    print("Display : ASUS - 4000")
    print("Graphics Card : 2GB - 7000\n")
    print("3.Gaming : ")
    print("Processor : i7 - 14000")
    print("RAM : 8GB - 10000")
    print("Display : SAMSUNG - 4500")
    print("Graphics Card : 4GB - 10000\n")
    print("4.Graphics Rendering : ")
    print("Processor : i9 - 18000")
    print("RAM : 16GB - 14000")
    print("Display : HP - 5000")
    print("Graphics Card : 8GB - 16000\n")
    ans2 = input("Enter your pack number : ")
    while True :
        if error_check(ans2) == "" :
            print("Invalid input....!")
            ans2 = input("Enter your pack number : ")
        else :
            ans2 = int(ans2)
            break
    SHOP_F = {}
    if ans2 == 1 :
        print("You have selected school pack :")
        SHOP_F["i3"] = 6000
        SHOP_F["1GB"] = 5000
        SHOP_F["LG"] = 3000
        SHOP_F["4GB"] = 6000   
        T1 = 20000
        Invoice(SHOP_F,T1)
    elif ans2 == 2 :
        print("You have selected Company pack :")    
        SHOP_F["i5"] = 10000
        SHOP_F["2GB"] = 7000
        SHOP_F["ASUS"] = 4000
        SHOP_F["8GB"] = 10000  
        T1 = 31000        
        Invoice(SHOP_F,T1) 
    elif ans2 == 3 :
        print("You have selected Gaming pack :")  
        SHOP_F["i7"] = 14000
        SHOP_F["4GB"] = 10000
        SHOP_F["SAMSUNG"] = 4500
        SHOP_F["8GB"] = 10000    
        T1 = 38500
        Invoice(SHOP_F,T1) 
    elif ans2 == 4 :
        print("You have selected Graphics Rendering pack :")
        SHOP_F["i9"] = 18000
        SHOP_F["8GB"] = 16000
        SHOP_F["HP"] = 5000
        SHOP_F["16GB"] = 14000    
        T1 = 53000
        Invoice(SHOP_F,T1) 
def shopping() : #CUSTOM SELECTION :
    print(format("","-^78"))
    print(format("CUSTOM STORE","-^78"))
    print(format("","-^78"))
    print("Choose your products by writing the number besides them : ")
    T1_p , shop_p = processors()
    T1_g , shop_g = graphics_card()
    T1_d , shop_d = displays()
    T1_r , shop_r = rams()
    T1 = T1_p + T1_g + T1_d + T1_r
    SHOP_F={}
    SHOP_F[shop_p[0]] = T1_p
    SHOP_F[shop_g[0]] = T1_g
    SHOP_F[shop_d[0]] = T1_d
    SHOP_F[shop_r[0]] = T1_r    
    Invoice(SHOP_F,T1)
def processors() : #PROCESSORS
    shop = []
    print("Processor : ")
    print("1. i3")
    print("2. i5")
    print("3. i7")
    print("4. i9")
    x = np.arange(2012,2020,1)
    y1 = [5,4.5,3.7,3,3.8,5,4,3]
    y2 = [3,4.6,5.5,5.8,6,6.3,5.7,5]
    y3 = [2.2,3,4.5,4,5.2,6.3,7,7.7]
    y4 = [1,1.2,1.8,2.5,3.9,4.6,5,4.3]
    plt.plot(x,y1,color = 'red',marker = 'o',label = 'i3')
    plt.plot(x,y2,color = 'blue',marker = 'o',label = 'i5')
    plt.plot(x,y3,color = 'green',marker = 'o',label = 'i7')
    plt.plot(x,y4,color = 'cyan',marker = 'o',label = 'i9')
    plt.title("#Annual Sales#")
    plt.xlabel('Year ->',fontsize = 14)
    plt.ylabel('Sales in Million ->',fontsize = 15)
    plt.grid(True)
    plt.legend()
    plt.show()
    C1 = input("Enter the product number : ")
    while True :
        if error_check(C1) == "" :
            print("Invalid input....!")
            C1 = input("Enter your pack number : ")
        else :
            C1 = int(C1)
            break
    if C1 == 1 :
        T1 = 6000
        shop.append("i3")
    elif C1 == 2 :
        T1 = 10000
        shop.append("i5")
    elif C1 == 3 :
        T1 = 14000
        shop.append("i7")
    elif C1 == 4 :
        T1 = 18000
        shop.append("i9")
    return T1 , shop
def graphics_card() : #GRAPHICS CARD
    shop = []
    print("Graphics Card : ")
    print("1. 1GB")
    print("2. 2GB")
    print("3. 4GB")
    print("4. 8GB")
    x = np.arange(2014,2020,1)
    y1 = [3,4.3,5.5,6,5.8,5]
    y2 = [2,2.5,3.1,4,4.8,5.7]
    y3 = [1.7,2.5,3.3,4.4,5.3,6.1]
    y4 = [1,1.4,2.3,3,3.3,4]
    plt.plot(x,y1,color = 'red',marker = 'o',label = '1GB')
    plt.plot(x,y2,color = 'blue',marker = 'o',label = '2GB')
    plt.plot(x,y3,color = 'green',marker = 'o',label = '4GB')
    plt.plot(x,y4,color = 'cyan',marker = 'o',label = '8GB')
    plt.title("#Annual Sales#")
    plt.xlabel('Year ->',fontsize = 14)
    plt.ylabel('Sales in Million ->',fontsize = 15)
    plt.grid(True)
    plt.legend()
    plt.show()
    C2 = input("Enter the product number : ")
    while True :
        if error_check(C2) == "" :
            print("Invalid input....!")
            C2 = input("Enter your pack number : ")
        else :
            C2 = int(C2)
            break
    if C2 == 1 :
        T1 = 5000
        shop.append("1GB")
    elif C2 == 2 :
        T1 = 7000
        shop.append("2GB")
    elif C2 == 3 :
        T1 = 10000
        shop.append("4GB")
    elif C2 == 4 :
        T1 = 16000
        shop.append("8GB")
    return T1 , shop
def displays() : #DISPLAY
    shop = []
    print("Display : ")
    print("1. SAMSUNG")
    print("2. ASUS")
    print("3. LG")
    print("4. HP")
    x = np.arange(2014,2020,1)
    y1 = [4,4.5,5,4.8,4.7,5.5]
    y2 = [3,3.7,4.6,5.8,5.6,5.3]
    y3 = [5,5.3,5.5,6.2,6,6.4]
    y4 = [4,4.3,4.9,5.2,5.8,5.5]
    plt.plot(x,y1,color = 'red',marker = 'o',label = 'SAMSUNG')
    plt.plot(x,y2,color = 'blue',marker = 'o',label = 'ASUS')
    plt.plot(x,y3,color = 'green',marker = 'o',label = 'LG')
    plt.plot(x,y4,color = 'cyan',marker = 'o',label = 'HP')
    plt.title("#Annual Sales#")
    plt.xlabel('Year ->',fontsize = 14)
    plt.ylabel('Sales in Million ->',fontsize = 15)
    plt.grid(True)
    plt.legend()
    plt.show()
    C3 = input("Enter the product number : ")
    while True :
        if error_check(C3) == "" :
            print("Invalid input....!")
            C3 = input("Enter your pack number : ")
        else :
            C3 = int(C3)
            break
    if C3 == 1 :
        T1 = 4500
        shop.append("SAMSUNG")
    elif C3 == 2 :
        T1 = 4000
        shop.append("ASUS")
    elif C3 == 3 :
        T1 = 3500
        shop.append("LG")
    elif C3 == 4 :
        T1 = 5000
        shop.append("HP")
    return T1 , shop
def rams() : #RAM
    shop = []
    print("RAM : ")
    print("1. 4GB")
    print("2. 6GB")
    print("3. 8GB")
    print("4. 16GB")
    x = np.arange(2014,2020,1)
    y1 = [5,5.8,6.3,6.5,6,6.2]
    y2 = [4,4.9,5.5,6.9,7.5,7]
    y3 = [3,4,4.8,5.5,6.1,6.6]
    y4 = [1,1.5,2.3,2.8,3.9,3.6]
    plt.plot(x,y1,color = 'red',marker = 'o',label = '4GB')
    plt.plot(x,y2,color = 'blue',marker = 'o',label = '6GB')
    plt.plot(x,y3,color = 'green',marker = 'o',label = '8GB')
    plt.plot(x,y4,color = 'cyan',marker = 'o',label = '16GB')
    plt.title("#Annual Sales#")
    plt.xlabel('Year ->',fontsize = 14)
    plt.ylabel('Sales in Million ->',fontsize = 15)
    plt.grid(True)
    plt.legend()
    plt.show()
    C4 = input("Enter the product number : ")
    while True :
        if error_check(C4) == "" :
            print("Invalid input....!")
            C4 = input("Enter your pack number : ")
        else :
            C4 = int(C4)
            break
    if C4 == 1 :
        T1 = 6000
        shop.append("4GB")
    elif C4 == 2 :
        T1 = 8000
        shop.append("6GB")
    elif C4 == 3 :
        T1 = 10000
        shop.append("8GB")
    elif C4 == 4 :
        T1 = 14000
        shop.append("16GB")
    return T1 , shop
print(format("","-^78"))
print(format("WELCOME TO ONLINE STORE","-^78"))
print(format("","-^78"))
while True : #PROGRAM STARTS HERE 
    ans1 = input("Do u want to see some pre-made packs ? (Y/N) : ") #SWITCHING BETWEEN PACKS AND CUSTOM :
    if ans1 == "Y" or ans1 == "y" : #PACKS :
        packs()
        break
    elif ans1 == "N" or ans1 == "n" : #CUSTOM :
        print("Directing Towards the Custom Store now.....")
        shopping()
        break
    else :
        print("Invalid Input....!")
confirm_order()


#cur.excecute 

