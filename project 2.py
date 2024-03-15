from tabulate import tabulate

import mysql.connector

con=mysql.connector.connect(host='localhost',password='Vikram',user='root',database='python')

'''if con:
    print("connected")
else:
    print("Not connected")'''


#DATA DEFINITION COMMAND:
#MULTILEVEL INHERITANCE:
class show_tables():
    def create_show_tables(self):
        res=con.cursor()
        sql="show tables"
        res.execute(sql)
        result=res.fetchall()
        print(result)
        print("Show Table Success")
        
class create_tables(show_tables):
    def creating_tables(self):
        print()
        res=con.cursor()
        print()
        print("create table 'This place you are creating that TableName Mention it'('key Name Mention it' 'value is only word keyword used a varchar(100) Mention it',('key Name Mention it' 'value is only integer keyword used a int Mention it' )")
        sql=input("Enter the sql query in create table :")
        create=sql
        patient=res.execute(create)
        print(patient)
        print()
        print("Create Table Sucess")
        print()

class add_tables(create_tables):
    def add_column_tables(self):
        print()
        res=con.cursor()
        print()
        print("Ex :Alter table 'This place you are creating that TableName' add  'This place you are which New column created that name Mention it ' ")
        sql=input("Enter the sql query in add column :")
        add_column_name=sql
        patient=res.execute(add_column_name)
        print(patient)
        print()
        print("Add Column Success")
        print()

class change_tables(add_tables):
    def change_column_tables(self):
        print()
        res=con.cursor()
        print()
        print("Ex :Alter table 'This place you are creating that TableName Mention it' change 'This place you are which table name changed that column name Mention it' 'This place you are New column name crated that name Mention it' ")
        sql=input("Enter the sql query in change column :")
        change_column_name=sql
        patient=res.execute(change_column_name)
        print(patient)
        print()
        print("Change Column Sucess")
        print()

class drop_tables(change_tables):
    def drop_full_tables(self):
        res=con.cursor()
        print()
        print("EX :Drop table 'This place you are creating that TableName Mention it'")
        sql=input("Enter the sql query in Drop table :")
        drop_table_name=sql
        patient=res.execute(drop_table_name)
        print(patient)
        print()
        print("Drop Table Success")
        print()



def insert(PATIENT_NAME,PATIENT_AGE,PATIENT_DETAILS,MEDICAL_REPORT,STAFF_NURSE_NAME,DISCHARGE_DETAILS,DEATH_CASES):
    res=con.cursor()
    sql="insert into patient(PATIENT_NAME,PATIENT_AGE,PATIENT_DETAILS,MEDICAL_REPORT,STAFF_NURSE_NAME,DISCHARGE_DETAILS,DEATH_CASES) values (%s,%s,%s,%s,%s,%s,%s)"    
    patient=(PATIENT_NAME,PATIENT_AGE,PATIENT_DETAILS,MEDICAL_REPORT,STAFF_NURSE_NAME,DISCHARGE_DETAILS,DEATH_CASES)
    res.execute(sql,patient)
    con.commit()
    print("Data Insert Success")


print()
#DATA MANIPULATION COMMAND:
#Multilevel Inheritance
class update_Alldata():
    def updating1(self,patient_name,patient_age,patient_details,medical_report,staff_nurse_name,discharge_details,death_cases,patient_id_no):
        print()
        print("1.FULL DATA")
        res=con.cursor()
        sql="update patient set patient_name=%s,patient_age=%s,patient_details=%s,medical_report=%s,staff_nurse_name=%s,discharge_details=%s,death_cases=%s where patient_id_no=%s"
        patient=(patient_name,patient_age,patient_details,medical_report,staff_nurse_name,discharge_details,death_cases,patient_id_no)
        res.execute(sql,patient)
        con.commit()
        print("Update Success")
        print()
class update_Namedata(update_Alldata):
    def updating2(self,patient_name,patient_id_no):
        print()
        print("2.PATIENT NAME DATA")
        res=con.cursor()
        sql="update patient set patient_name=%s where patient_id_no=%s"
        patient=(patient_name,patient_id_no)
        res.execute(sql,patient)
        con.commit()
        print("Update Success")
        print()
class update_Agedata(update_Namedata):
    def updating3(self,patient_age,patient_id_no):
        print()
        print("3.PATIENT AGE DATA")
        res=con.cursor()
        sql="update patient set patient_age=%s where patient_id_no=%s"
        patient=(patient_age,patient_id_no)
        res.execute(sql,patient)
        con.commit()
        print("Update Success")
        print()
class update_Detailsdata(update_Agedata):
    def updating4(self,patient_details,patient_id_no):
        print()
        print("4.PATIENT DETAILS DATA")
        res=con.cursor()
        sql="update patient set patient_details=%s where patient_id_no=%s"
        patient=(patient_details,patient_id_no)
        res.execute(sql,patient)
        con.commit()
        print("Update Success")
        print()
class update_Medicaldata(update_Detailsdata):
    def updating5(self,medical_report,patient_id_no):
        print()
        print("5.MEDICAL REPORT DATA")
        res=con.cursor()
        sql="update patient set medical_report=%s where patient_id_no=%s"
        patient=(medical_report,patient_id_no)
        res.execute(sql,patient)
        con.commit()
        print("Update Success")
        print()
class update_Staffdata(update_Medicaldata):
    def updating6(self,staff_nurse_name,patient_id_no):
        print()
        print("6.STAFF NURSE NAME DATA")
        res=con.cursor()
        sql="update patient set staff_nurse_name=%s where patient_id_no=%s"
        patient=(staff_nurse_name,patient_id_no)
        res.execute(sql,patient)
        con.commit()
        print("Update Success")
        print()
class update_Dischargedata(update_Staffdata):
    def updating7(self,discharge_details,patient_id_no):
        print()
        print("7.DISCHARGE DETAIL DATA")
        res=con.cursor()
        sql="update patient set discharge_details=%s where patient_id_no=%s"
        patient=(discharge_details,patient_id_no)
        res.execute(sql,patient)
        con.commit()
        print("Update Success")
        print()
class update_Deathdata(update_Dischargedata):
    def updating8(self,death_cases,patient_id_no):
        print()
        print("8.DEATH CASE DATA")
        res=con.cursor()
        sql="update patient set death_cases=%s where patient_id_no=%s"
        patient=(death_cases,patient_id_no)
        res.execute(sql,patient)
        con.commit()
        print("Update Success")
        print()
class update_phone_number(update_Deathdata):
    def updating9(self,patient_phone_number,patient_id_no):
        print()
        print("9.PATIENT PHONE NUMBER DATA")
        res=con.cursor()
        sql="update patient set Patient_Phone_Number=%s where patient_id_no=%s"
        patient=(patient_phone_number,patient_id_no)
        res.execute(sql,patient)
        con.commit()
        print("Update Success")
        print()
    
        

def select():
    print()
    print("1.PATIENT ALL MEDICAL CASE TYPE AND DETAILS")
    print("2.OPERATION PATIENT AND DETAILS")
    print("3.REGULAR CHECKUP PATIENT and DETAILS")
    print("4.NORMAL CHECKUP PATIENT and DETAILS")
    print("5.STAFF NURSE NAME AND PATIENT DETAILS")
    print("6.DISCHARGE PATIENT and DETAILS")
    print("7.DEATH PATIENT")
    print()
    patient_cases=int(input("which case you are find? :"))
    if patient_cases==1:
        print()
        print("1.PATIENT ALL MEDICAL CASE TYPE AND DETAILS:")
        print()
        res=con.cursor()
        sql="select PATIENT_ID_NO,PATIENT_NAME,PATIENT_AGE,PATIENT_DETAILS,MEDICAL_REPORT,STAFF_NURSE_NAME,DISCHARGE_DETAILS,DEATH_CASES from patient"
        res.execute(sql)
        #result=res.fetchone() to be printed in one record
        #result=res.fetchall()All record printed print it
        result=res.fetchall()
        print(tabulate(result,headers=["PATIENT_ID_NO","PATIENT_NAME","PATIENT_AGE","PATIENT_DETAILS","MEDICAL_REPORT","STAFF_NURSE_NAME","DISCHARGE_DETAILS","DEATH_CASES"]))
        print()
    elif patient_cases==2:
        print()
        print("2.OPERATION PATIENT AND DETAILS")
        print()
        res=con.cursor()
        sql="select * from patient where PATIENT_DETAILS='operation patient'"
        res.execute(sql)
        result=res.fetchall()
        print(tabulate(result,headers=["PATIENT_ID_NO","PATIENT_NAME","PATIENT_AGE","PATIENT_DETAILS","MEDICAL_REPORT","STAFF_NURSE_NAME","DISCHARGE_DETAILS","DEATH_CASES"]))
        print()
    elif patient_cases==3:
        print()
        print("3.REGULAR CHECKUP PATIENT AND DETAILS")
        print()
        res=con.cursor()
        sql="select * from patient where PATIENT_DETAILS='regular checkup patient'"
        res.execute(sql)
        result=res.fetchall()
        print(tabulate(result,headers=["PATIENT_ID_NO","PATIENT_NAME","PATIENT_AGE","PATIENT_DETAILS","MEDICAL_REPORT","STAFF_NURSE_NAME","DISCHARGE_DETAILS","DEATH_CASES"]))
        print()
    elif patient_cases==4:
        print()
        print("4.NORMAL CHECKUP PATIENT AND DETAILS")
        print()
        res=con.cursor()
        sql="select * from patient where PATIENT_DETAILS='normal checkup patient'"
        res.execute(sql)
        result=res.fetchall()
        print(tabulate(result,headers=["PATIENT_ID_NO","PATIENT_NAME","PATIENT_AGE","PATIENT_DETAILS","MEDICAL_REPORT","STAFF_NURSE_NAME","DISCHARGE_DETAILS","DEATH_CASES"]))
        print()
    elif patient_cases==5:
        print()
        print("5.STAFF NURSE NAME AND PATIENT DETAILS")
        print()
        res=con.cursor()
        sql="select PATIENT_NAME,PATIENT_DETAILS,STAFF_NURSE_NAME from patient"
        res.execute(sql)
        result=res.fetchall()
        print(tabulate(result,headers=["PATIENT_NAME","PATIENT_DETAILS","STAFF_NURSE_NAME"]))
        print()
    elif patient_cases==6:
        print()
        print("6.DISCHARGE PATIENT AND DETAILS")
        print()
        res=con.cursor()
        sql="select PATIENT_NAME,PATIENT_DETAILS,DISCHARGE_DETAILS from patient"
        res.execute(sql)
        result=res.fetchall()
        print(tabulate(result,headers=["PATIENT_NAME","PATIENT_DETAILS","DISCHARGE_DETAILS"]))
        print()
    elif patient_cases==7:
        print()
        print("7.DEATH CASES")
        print()
        res=con.cursor()
        sql="select PATIENT_NAME,DEATH_CASES from patient where DEATH_CASES='death'"
        res.execute(sql)
        result=res.fetchall()
        print(tabulate(result,headers=["PATIENT_NAME","DEATH_CASES"]))
        print()          
  
                    
    
def delete(PATIENT_ID_NO):
    res=con.cursor()
    sql="Delete from Patient Where Patient_ID_NO=%s"    
    patient=(PATIENT_ID_NO,)
    res.execute(sql,patient)
    con.commit()
    print("Data Delete Success")


while True:
    print("1.DATA DEFINITION COMMAND")
    print("2.DATA MANIPULATION COMMAND")
    print()
    command=input("Enter the Which Type Of Command use a Table? :")
    print()
    if command=="1":
        print("1.SHOW TABLES")
        print("2.CREATE TABLES")
        print("3.ADD TABLES")
        print("4.CHANGE TABLES")
        print("5.DROP TABLES")
        print()
        DDL=input("Enter the which type of Tables? :")
        #DATA DEFINITION COMMAND
        if DDL=="1":
            print()
            print("1.SHOW TABLES")
            obj=drop_tables()
            obj.create_show_tables()
        elif DDL=="2":
            print()
            print("2.CREATE TABLES")
            obj=drop_tables()
            obj.creating_tables()
        elif DDL=="3":
            print()
            print("3.ADD TABLES")
            obj=drop_tables()
            obj.add_column_tables()
        elif DDL=="4":
            print()
            print("4.CHANGE TABLES")
            obj=drop_tables()
            obj. change_column_tables()
        elif DDL=="5":
            print()
            print("5.DROP TABLES")
            obj=drop_tables()
            obj.drop_full_tables()
        else:
            print("You have wrong Data Passed.Try Again")
    elif command=="2":
        #DATA MANIPULATION COMMAND
        print("1.Insert Data")
        print("2.Update Data")
        print("3.Select Data")
        print("4.Delete Data")
        print("5.Exit")
        print()
        choice=input("Enter the Data No :")
        if choice=="1":
            print()
            print("INSERT DATA:")
            print()
            PATIENT_NAME=input("Enter the Patient Name :")
            PATIENT_AGE=int(input("Enter the Patient Age :"))
            PATIENT_DETAILS=input("Enter the Patient Checkup Details :")
            MEDICAL_REPORT=input("Enter the Medical report :")
            STAFF_NURSE_NAME=input("Enter the Staff Nurse Name :")
            DISCHARGE_DETAILS=input("Enter the Discharge Patient Details :")
            DEATH_CASES=input("Enter the Death Report :")
            PATIENT_PHONE_NUMBER=int(input("Enter the Patient Phone Number"))
            insert(PATIENT_NAME,PATIENT_AGE,PATIENT_DETAILS,MEDICAL_REPORT,STAFF_NURSE_NAME,DISCHARGE_DETAILS,DEATH_CASES,PATIENT_PHONE_NUMBER)
        elif choice=="2":
            print()
            print("1.FULL DATA UPDATE")
            print("2.PATIENT NAME UPDATE")
            print("3.PATIENT AGE UPDATE")
            print("4.PATIENT DETAILS UPDATE")
            print("5.MEDICAL REPORT UPDATE")
            print("6.STAFF NURSE NAME UPDATE")
            print("7.DISCHARGE DETAILS UPDATE")
            print("8.DEATH CASES UPDATE")
            print("9.PATIENT PHONE NUMBER")
            print()
            update=input("Which Enter a Data to be Update? :")
            print()
            print("UPDATE DATA:")
            print()
            if update=="1":
                print("1.FULL DATA UPDATE")
                print()
                PATIENT_ID_NO=input("Enter the Patient ID NO :")
                PATIENT_NAME=input("Enter the Patient Name :")
                PATIENT_AGE=int(input("Enter the Patient Age :"))
                PATIENT_DETAILS=input("Enter the Patient Checkup Details :")
                MEDICAL_REPORT=input("Enter the Medical report :")
                STAFF_NURSE_NAME=input("Enter the Staff Nurse Name :")
                DISCHARGE_DETAILS=input("Enter the Discharge Patient Details :")
                DEATH_CASES=input("Enter the Death Report :")
                PATIENT_PHONE_NUMBER=int(input("Enter the Patient Phone Number"))
                obj=update_Alldata()
                obj.updating1(PATIENT_NAME,PATIENT_AGE,PATIENT_DETAILS,MEDICAL_REPORT,STAFF_NURSE_NAME,DISCHARGE_DETAILS,DEATH_CASES,PATIENT_PHONE_NUMBER,PATIENT_ID_NO)
            elif update=="2":
                print("2.PATIENT NAME UPDATE")
                print()
                PATIENT_ID_NO=input("Enter the Patient ID NO :")
                PATIENT_NAME=input("Enter the Update Patient Name :")
                obj=update_Namedata()
                obj.updating2(PATIENT_NAME,PATIENT_ID_NO)
            elif update=="3":
                print("3.PATIENT AGE UPDATE")
                print()
                PATIENT_ID_NO=input("Enter the Patient ID NO :")
                PATIENT_AGE=input("Enter the Update Patient Age :")
                obj=update_Agedata()
                obj.updating3(PATIENT_AGE,PATIENT_ID_NO)
            elif update=="4":
                print("4.PATIENT DETAILS UPDATE")
                print()
                PATIENT_ID_NO=input("Enter the Patient ID NO :")
                PATIENT_DETAILS=input("Enter the Update Patient Details :")
                obj=update_Detailsdata()
                obj.updating4(PATIENT_DETAILS,PATIENT_ID_NO)
            elif update=="5":
                print("5.PATIENT MEDICAL REPORT UPDATE")
                print()
                PATIENT_ID_NO=input("Enter the Patient ID NO :")
                MEDICAL_REPORT=input("Enter the Update Patient Medical Report :")
                obj=update_Medicaldata()
                obj.updating5(MEDICAL_REPORT,PATIENT_ID_NO)
            elif update=="6":
                print("6.STAFF NURSE NAME UPDATE")
                print()
                PATIENT_ID_NO=input("Enter the Patient ID NO :")
                STAFF_NURSE_NAME=input("Enter the Update Staff Nurse Name :")
                obj=update_Staffdata()
                obj.updating6(STAFF_NURSE_NAME,PATIENT_ID_NO)
            elif update=="7":
                print("7.DISCHARGE DETAILS UPDATE")
                print()
                PATIENT_ID_NO=input("Enter the Patient ID NO :")
                DISCHARGE_DETAILS=input("Enter the Update Patient Discharge Details :")
                obj=update_Dischargedata()
                obj.updating7(DISCHARGE_DETAILS,PATIENT_ID_NO)
            elif update=="8":
                print("8.DEATH CASES UPDATE")
                print()
                PATIENT_ID_NO=int(input("Enter the Patient ID NO :"))
                DISCHARGE_CASES=input("Enter the Update Patient Death Cases :")
                obj=update_Deathdata()
                obj.updating8(DISCHARGE_CASES,PATIENT_ID_NO)
            elif update=="9":
                print("9.PATIENT PHONE NUMBER UPDATE")
                print()
                PATIENT_ID_NO=int(input("Enter the Patient ID NO :"))
                PATIENT_PHONE_NUMBER=int(input("Enter the Update Patient Phone Number :"))
                obj=update_phone_number()
                obj.updating9(PATIENT_PHONE_NUMBER,PATIENT_ID_NO)
                
            else:
                print("Exit UPDATE DATA")

        elif choice=="3":
            print()
            print("SELECT DATA:")
            select()

            
        elif choice=="4":
            print()
            print("DELETE DATA:")
            print()
            PATIENT_ID_NO=int(input("Enter the PATIENT_ID_NO Delete :"))
            delete(PATIENT_ID_NO)

        elif choice=="5":
            print("Exit")
            quit()
        
        else:
            print("You are Passed Invalid Data.Please Try again")
            print()











    
    
