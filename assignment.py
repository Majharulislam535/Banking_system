
class Bank:

   accounts=[]

   total_balance=0

   total_loan_am =0

   def __init__(self,name,email,address,types):
       self.name = name
       self.email = email
       self.address = address

       self.type = types

       self.accountNum = len(Bank.accounts)+1
       self.balance =0
       self.transaction_history=[]
       self.loan = 0
       self.loan_status=True

       Bank.accounts.append(self)

   def deposit(self,amount):
       if amount > 0:
          self.balance += amount
          Bank.total_balance += amount
          self.transaction_history.append(f"Deposited {amount}")
          print(f"\nDeposited {amount} successfully\n")
       else:
         print("\nInvalid amount !\n")
    
   def withdraw(self,amount):
       if self.balance > amount  and amount > 0:
          self.balance -= amount
          Bank.total_balance -= amount
          self.transaction_history.append(f"WithDraw {amount}")
          print(f"\nWithDraw {amount} successfully\n")
       else:
         print("\n Withdrawal amount exceeded \n")
    
   def check_balance(self):
       print(f"\nTotal Balance: {self.balance}\n")


   def trans_history(self):
      print("\n ------Transaction history-------\n")

      for tr in self.transaction_history:
        print(tr)
        print("\n")
    
   def take_loan(self,amount):
        if self.loan_status and self.loan <= 2:
            self.loan +=1
            self.balance += amount
            Bank.total_balance += amount
            Bank.total_loan_am += amount
            self.transaction_history.append(f"Take a loan of {amount}")
            print(f'\n Successfully take a loan {amount}\n')
        elif self.loan_status==False:
            print("\n Loan Feature currently Disable \n")
        else:
            print("\n You Have already take the maximum Loan \n")
    
  
   def transfer_balance(self,accountNo,amount):
            
           find_account = None
           for account in Bank.accounts:
               if account.accountNum == accountNo:
                 find_account=account
                 break

           if find_account:
                if amount> self.balance:
                   print("\n Insufficient Balance \n")
                
                else:
                  self.balance -= amount
                  find_account.balance += amount
                  find_account.transaction_history.append(f"\n   Received amount {amount} \n")
                  self.transaction_history.append(f"\n Transfer   balance {amount} to {find_account.name}")
                  
           else:
              print("\n account does not exist \n")

        

   def bank_status():
        print(f"\n Total Balance : {Bank.total_balance} \n")
        print(f"\n Total Loan Balance : {Bank.total_loan_am} \n")
        print(f"\n Loan Status : {Bank.loan_status} \n")

   
   def loan__status(self):
       print(f"\n Loan status {self.loan_status} \n")




class Create_account(Bank):
    def __init__(self,name,email,address,types):
        super(). __init__(name,email,address,types)
    
   

class Admin:
     
     def create_account_ad(name,email,address,types):
        user=Bank(name,email,address,types)
     
     def delete_account(account):

        for user in Bank.accounts:
            if user.accountNum==account:
             Bank.accounts.remove(user)
             print("\n Account deleted Successfully \n")
             break
            else:
              print("\n User account not found \n")

     def view_all_accounts():
        print("\n ------ All Accounts ------\n")
        for user in Bank.accounts:
            print(f"\n Account Name {user.name} : account num: {user.accountNum} ")
    
     def bank_status():
        Bank.bank_status()

     def bank_loan_feature(status):
         Bank.bank_loan_status(status)
         print(f"\n currently Bank loan status {Bank.loan_status}\n")

     def bank_loan_status(status,accountNo):
           
           find_account = None
           for account in Bank.accounts:
               if account.accountNum == accountNo:
                 find_account=account
                 break

            
           if status == 1:
                 find_account.loan_status=True
           elif status == 0:
               find_account.loan_status = False
            
           if find_account == None :
             print("\n User Not Found \n")
           else:
            print(f"\nLoan Feature is {find_account.loan_status}\n")


currentUser = None

while(True):
    if currentUser==None:
        print("\n No user Login \n")

        ch=input("\n Login admin or Normal User (a/n) \n ")
        # a- admin user 
        # n- Normal user
        
        if ch=='n':
            
            user = input("\nLogin or Registration (L/R)\n")

            if user=='R':
                name = input("Enter Your Name : ")
                email = input("Enter Your Email : ")
                address = input("Enter Your Address : ")
                types = input("Account types : ")
                currentUser= Create_account(name,email,address,types)

            elif user=='L':

                account_number = int(input("Your Account Number : "))
                for account in Bank.accounts:
                    if account.accountNum ==account_number:
                        currentUser=account
                        break
            else:
                print("\n Invalid command \n")


        elif ch=='a':
            # admin password == 1234
            
            password = int(input("admin Password: "))
            
            if password==1234:
                currentUser= Admin
                while(True):
                    print("1. Create an Account :")
                    print("2. Delete Account :")
                    print("3. All User account list :")
                    print("4. Bank Loan Status :")
                    print("5. Bank Status :")
                    print("6. LogOut")


                    op=int(input("option: "))

                    if op==1:
                        name = input("Enter Your Name : ")
                        email = input("Enter Your Email : ")
                        address = input("Enter Your Address : ")
                        types = input("Account types : ")
                        Admin.create_account_ad(name,email,address,types)

                    elif op==2:
                        account_number=int(input("Account Number :"))
                        Admin.delete_account(account_number)
                    
                    elif op==3:
                        Admin.view_all_accounts()
                    
                    elif op==4:
                          status = int(input("on==1/off==0 :"))
                          account_number=int(input("Account_Num:"))
                          Admin.bank_loan_status(status,account_number)

                    elif op==5:
                        Admin.bank_status()

                    elif op==6:
                        currentUser=None
                        break

            else:
                print("\n Invalid password\n")
    

    else:
         
        print("1. Check balance : ")
        print("2. Transaction History : ")
        print("3. Deposit : ")
        print("4. withdraw : ")
        print("5. Take a loan : ")
        print("6. Transfer amount : ")
        print("7. Loan status :")
        print("8. LogOut : ")

        op = int(input("Option : "))

        if op==1:
            currentUser.check_balance()
        elif op==2:
            currentUser.trans_history()
        elif op==3:
            amount = int(input("Amount : "))
            currentUser.deposit(amount)
        elif op==4:
            amount = int(input("Amount : "))
            currentUser.withdraw(amount)
        elif op==5:
            amount = int(input("Amount : "))
            currentUser.take_loan(amount)

        elif op==6:
             amount = int(input("Amount : "))
             account_number=int(input("Account Number :"))
             currentUser.transfer_balance(account_number,amount)
        
        elif op==7:
            currentUser.loan__status()
        elif op==8:
             currentUser=None



   

  

