list_of_names=[]
list_of_DOB=[]
list_of_contact_num=[]
list_of_email=[]
list_of_password=[]
users_list=[list_of_names,list_of_DOB,list_of_contact_num,list_of_email,list_of_password]
list_of_food=[ "tandoori chicken (4 pieces) [INR 240]","vegan burger (1piece)[INR 320]","traffle cake (500gm)[INR 900]"]
food_info={"101":{"Name":"tandoori chicken","Quantity": " 4 pieces","Price":240,"Discount":0,"stock left":0},
            "102":{"Name":"vegan burger","Quantity":"1 piece","Price":320,"Discount":0,"stock left":0},
             "103":{"Name":"traffle cake","Quantity":"500 gram","Price":900,"Discount":0,"stock left":0}}

pos=0
class user:
    def __init__(self):
        pass

    def  register(self):
        name=self.NAME()
        dob=self.DOB()
        contact=self.contact_num()
        email_id=self.email()
        Password=self.password()
    
   
    def NAME(self):
        print("enter name")
        name=input()
        self.name=name
        list_of_names.append(name)
    def DOB(self):

        print("enter your date of birth in format dd-mm-yyyy")
        DOB=input().split("-")
        self.dob=DOB
        list_of_DOB.append(DOB)
    def contact_num(self):
        print("enter contact number")
        num=input()
        import re
        if (re.search("[0-9]{10}",num)):
            self.contact=num
            list_of_contact_num.append(num)
            return
        else:
            print("contact number is 10 digits number ,fill it again")
            contact_num()
    def email(self):
        print("enter email address")
        email_add=input()
        import re
        if email_add in list_of_email:
            print("this email id is already registered ,please login")
            list_of_names.pop(len(list_of_names)-1)
            list_of_DOB.pop(len(list_of_DOB)-1)
            list_of_contact_num.pop(len(list_of_contact_num)-1)
        else:
            if( re.search("^[a-zA-Z]+[0-9]+.*@gmail.com$",email_add)):
                list_of_email.append(email_add)
                self.email=email_add
                #self.password()
            else:
                print("email_address must start with an alphabet ,then it shoulh have one or more digit and  should have a domain @gmail.com")
                email()
    def password(self):
        print("enter your password")
        word=input()
        import re
        if(re.search("[a-zA-Z]+[0-9]+.",word)):
            self.password=word
            list_of_password.append(word)
        else:
            print("password must begin with an alphabet ,must contain one or more digit and a special character")
            password()

           
    def order(self):
        self.list_of_order=[]
        for i in range(len(list_of_food)):
            print("enter",i+1,"for",list_of_food[i])
        z=list(map(int,input().split(" ")))
        for i in z:
            print("You have selected ",list_of_food[i-1])
        print("Do you want to place your order? enter OK to place your order")
        if(input()=="OK"):
            for i in z:
                self.list_of_order.append(list_of_food[i-1])
            print("Your order has been placed,Enjoy your meal")
        else:
            return
    def login_user(self):
        print("enter your email address")
        x=input()
        if x in list_of_email:
            print("enter password")
            y=input()
            if y==list_of_password[list_of_email.index(x)]:
                print("enter 1 for placing an order \nenter 2 for checking order history \nenter 3 to update profile")
                z=int(input())
                if z==1:
                    print(list_of_food)
                    if input("want to order something,press Yes or No")=="Yes":
                        self.order()
                    else:
                        pass
                elif z==2:
                    self.show_order()
                elif z==3:
                    self.update_profile()
            else:
                print("password does not match with the email id")
        else:
            print("the email id is not registered")
    def show_order(self):
        print(self.list_of_order)
    def update_profile(self):
        print("NAME",self.name)
        print("DOB",self.dob)
        print("contact",self.contact)
        print("Email id",self.email)
        print("Password",self.password)
        x=input("what do you want to update")
        if(x=="NAME"):
            name= self.NAME()
            print("profile updated")
        elif(x=="DOB"):
            dob= self.DOB()
            print("profile updated")
        elif(x=="contact number"):
            contact=self.contact_num()
            print("profile updated")
        elif(x=="email Id"):
            email= self.email()
            print("profile updated")
        elif(x=="password"):
            Password=self.password()
            print("profile updated")
        else:
            print('You have not selected anythng to be updated')
class admin:
    def __init__(self):
        pass
    def admin_functions(self):
        print("enter 1to view  the food item and related info\n enter 2 to add more food items\n enter 3 to edit information of food items")
        y=int(input())
        if y==1:
            self.show_food_list()
        elif y==2:
            self.add_more_food()
        elif y==3:
            self.edit_food_info()
        print("Do you want to be here more?Enter yes")
        x=input()
        if x=="yes":
            self.admin_functions()
        else:
            return
    def login_admin(self):
        print("enter your email id")
        x=input()
        if x=="admin@gmail.com":
            print("enter password")
            if input()=="admin":
                self.admin_functions()
    
    def show_food_list(self):
                   print(food_info)
    def add_more_food(self):
                   a={}
                   food_info[input("enter food id")]=a
                   a["Name"]=input("enter name of food item")
                   a["Quantity"]=input("enter quantity per serving")
                   a["price"]=int(input("enter price per serve"))
                   a["discount"]=int(input("offer customer some discount"))
                   a["stocK_left"]=int(input("enter stocks left"))
    def edit_food_info(self):
        print("enter id of food item you want to make changes on ")
        x=input()
        if x not in food_info:
            print("There is no food item with this id")
        else:
            print(food_info[x])
            print("enter 1 to change the name \n enter 2 to change the quantity \n enter 3 to change the price \n enter 4 to change discount \n enter 5 to change the stock left \n enter 6 to delete the fod item from the menu")
            y=int(input())
            if y==1:
                food_info[x]["Name"]=input("enter new name")
            elif y==2:
                food_info[x]["Quantity"]=input("enter new quantity")
            elif y==3:
                food_info[x]["Pice"]=int(input("enter new price"))
            elif y==4:
                food_info[x]["Discount"]=int(input("enter new discount"))
            elif y==5:
                food_info[x]["stock left"]=int(input("enter new stock left"))
            elif y==6:
                del food_info[x]
            else:
                print("Data has been updated")
                return
                
                
                   
                  
        
        

