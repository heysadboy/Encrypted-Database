from cryptography.fernet import Fernet
import getpass
import mysql.connector

def enc(str):
    cipher_suite = Fernet(key)
    hash = cipher_suite.encrypt(str.encode())
    #print (hash)
    return hash

def dec(str,enkey):
    cipher_suite = Fernet(enkey)
    hash = cipher_suite.decrypt(str.encode())
    #print (hash)
    ans = hash.decode();
    return ans

def operate_database():
    cnx=mysql.connector.connect(user='root',password='sakura',host='localhost',database='test')
    cursor=cnx.cursor() 
    try:
        cursor.execute("SELECT * FROM usr;")
        myresult = cursor.fetchall()
        
        print("Enter account number to search: ")
        qu = input(">>")

        print("The matching values are: ")
        for x in myresult:
          if dec(x[2],x[4]) == qu:
          	print(x[0])

        
    except Exception as e:
        print(e) 

def con_database():
    cnx=mysql.connector.connect(user='root',password='sakura',host='localhost',database='test')
    cursor=cnx.cursor() 
    try:
        query=("INSERT INTO usr VALUES(%s,%s,%s,%s,%s);")
        data=(us,enc(pwd),enc(acc_num),salary,key)
        cursor.execute(query,data)
        cnx.commit()
        print("User Recorded")
        
    except Exception as e:
        print(e)
  
def user_data():
    global us
    global acc_num
    global salary
    global pwd
    global key
    
    print("Enter username: ")
    us=input(">>")
    print("Enter password: ")
    pwd=getpass.getpass(">>")
    print("Enter account number: ")
    acc_num=input(">>")
    print("Enter salary: ")
    salary=input(">>")

    key = Fernet.generate_key() 

    con_database()

    operate_database()


if __name__=="__main__":
    user_data()
