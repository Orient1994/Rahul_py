def mail(email_add):
    import smtplib
    from email.message import EmailMessage


    smtp = smtplib.SMTP("smtp.gmail.com",587)

    smtp.starttls()
    smtp.login("gsrahul86@gmail.com","Amdocs123")

    message = EmailMessage()

    message['Subject'] = 'Testimg sendmail via python'
    message['From'] = 'gsrahul86@gmail.com'
    message['To']  = 'gsrahul86@gmail.com'
    message.set_content("""
        <!DOCTYPE html>
            <html>
            <body>
                  <h2>Welcome</h2>
                  Testing
            </body>
            </html>
             """,subtype='html')

    
def DB_connection():
    import mysql.connector
    from mysql.connector import Error
    from mysql.connector import errorcode
    conn = mysql.connector.connect(host="localhost",user="root",password="root",database="IRCTC")
    MYCURSOR = conn.cursor()




def pnr_db_insertion(pnr,flag):
    DB_connection()
    
    mySql_insert_query = "insert into pnr_status values(%s,%s)"

    cursor = connection.cursor()
    result = cursor.execute(mySql_insert_query,(pnr,flag))
    connection.commit()

def ticket_cancellation(pnr_value):
    DB_connection()
    Pnr_tup=(pnr_value,)
    #mySql_insert_query = "update pnr_status set pnr_number='N' where pnr_number = %s"

    cursor = conn.cursor()
    #result = cursor.execute(mySql_insert_query,(pnr_value))
    cursor.execute("update pnr_status set flag='N' where pnr_number = %s",(Pnr_tup))
    conn.commit()
    
    
    

    

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
conn = mysql.connector.connect(host="localhost",user="root",password="root",database="IRCTC")
MYCURSOR = conn.cursor()
    

MYCURSOR.execute("Select  city_name as city from city;")

ALL_RECORDS = MYCURSOR.fetchall()
print(list(ALL_RECORDS))
MYCURSOR.execute("select fname as first_name from cust_info;")
CUST_REC=MYCURSOR.fetchall()

#print(list(CUST_REC))


print("\n Welcome !! To IRCTC booking system")
user_name=input("Please enter the username :- ")

cursor = conn.cursor(buffered=True)
cursor.execute("select * from user_auth where user_name =%s",(user_name,))
record = cursor.fetchall()
        

for row in record:
    
    print("cust_name = ", row[0] )
    cust_name=row[0]
    print("email_id = ", row[1])
    email_id=row[1]

if cust_name==user_name:
    print("Successfully login")
    restart = ("Y")

    while restart != ("N","No","n","no"):
        print("1.cancel the ticket ")
        print("2.Ticket booking")
        
    
        option = int(input("Enter you option : "))

        if option == 1:
            PNR_value=input("Please enter the PNR number")
            ticket_cancellation(PNR_value)
            print("Ticket has been successfully cancelled ")
            
        elif option == 2:
            count= int(input("Enter the number of ticket you want to book: "))
            name_1=list()
            age_1=list()
            sex_1=list()
            location_list = ("Y")
        #while location_list != ("N","No","no","NO"):
            
            
            print("select your source and destination location from below list: ")
            out = [ item for t in ALL_RECORDS for item in t ]
        
            print(out)
            for i in out:
                print(i,"\n")
            
            
            
            source_location= input("Source location from above list :- ")
            destination_location=input("destination location :- ")
        #location=["Pune","Mumbai","Goa","Kokan","Nagpur","Satara"]

            if source_location in out:
                print("You have selected the souce location as : ",source_location,"\nDestination location as :-",destination_location)
            else:
                print("Oops please select the source location from above list")
                slocation_list= input("Press Y/Yes for re-selection of location")
                #if location_list in ("Y","Yes"):
                    #location_list("Y")

            for i in range(count):
                name = input("\n Name: ")
                name_1.append(name)
                age = int(input("\n Age: "))
                age_1.append(age)
                sex = input("Male or female : ")
                sex_1.append(sex)
                restart = input("\n Oops !!! forgot someone : ")
                if restart in ("y","Yes","yes","yes"):
                    restart("Y")
                try:
                    connection = mysql.connector.connect(host="localhost",user="root",password="root",database="IRCTC")

                    mySql_insert_query = "insert into users_info values(%s,%s,%s)"

                    cursor = connection.cursor()
                    result = cursor.execute(mySql_insert_query,(name,age,sex))
                    connection.commit()
                    print("Ticket booking has been completed successfully\n!!!Happy Journey!!!")
                
                    cursor.close()

                except mysql.connector.Error as error:
                    print("Failed to insert record into Laptop table {}".format(error))
            

        
        
            if restart in ("y","Yes","yes","yes"):
                restart("Y")
            else:
                x=0
                print("\n Total Ticket :",count)
                for p in range(1,count + 1):
                    print("Ticket :",p)
                    print("Name :", name_1[x])
                    print("Age :",age_1[x])
                    print("Sex : ", sex_1[x])
                    x += 1
                import random
                PNR_number=random.randint(0,9999)
                flag='Y'
                print("Your PNR number is :- ",PNR_number)
                pnr_db_insertion(PNR_number,flag)
                print("Sending mail to your register email id")
                mail(email_id)
            
            
            
        

else:
    print("Login failed, Incorrect username provided ")
    

        
            


     

