import pywhatkit
from My_packege import Hours_format

class Whatsapp:

# This is read the password 
    def password(self):
        with open("password.txt","r")as f:
            return(f.read())

# This is forget the password     
    def Forgetpassword(cls):
        New_password=int(input("Enter a new password: "))
        with open("password.txt","w")as f:
            f.write("")
        with open("password.txt","w")as a:
            a.write(str(New_password))

# Change the Second
    def Second(self):
        Second=input("Defualt Second is 25. If you want to Decriese or Increase the Second then Enter . if not then click Enter : ")
        if(Second == ""):
            return 25
        else:
            return int(Second)

# This send the message          
    def send_message(self, number, message, time_in_Hour, time_in_min, wait_time):
        pywhatkit.sendwhatmsg("+91"+(number), message, time_in_Hour, time_in_min,wait_time)

# This is send the message to group      
    def sendwhatmsg_to_group(self, Group_name, message, time_in_Hour, time_in_min):
        pywhatkit.sendwhatmsg_to_group(Group_name, message, time_in_Hour, time_in_min)
        
# This is send send the message and after 2 second it colose
    def message_and_close(self,number,message,time_in_Hour, time_in_min, wait_time, closing_time):
        pywhatkit.sendwhatmsg(number,message,time_in_Hour,time_in_min,wait_time,closing_time)
        
# This is send photo
    def send_photo(self,number,image):
        pywhatkit.sendwhats_image(number,image)
        
class User(Whatsapp):
    
# This is show the Number list
    def __init__(self,List_of_Number):
        self.List_of_Number=List_of_Number
    
# This is show contact lsit
    def show_contact_list(self):
        return(self.List_of_Number)
  
# This is adding a number to contact list  
    def adding_contact_list(self,name,number):
        self.name=name
        self.number=number
        self.List_of_Number[name]=number

# This is take a message from the user       
    def message(self):
        message=input("Enter the message: ")
        return(message)

# This is take a message to the send to the group   
    def message_to_Group(self):
        message_to_Group=input("Enter the message for group: ")
        return(message_to_Group)
 
# This is send the photo   
    def Phot_send(self):
        Path_of_photo=input("Enter the location of photo: ")
        return(Path_of_photo)
    
    
sibashis=Whatsapp()

Number_list={
    "bapi":"8280826602",
}
us=User(Number_list)
Welcome_message="""---------------------------------THIS whatsapp WAS MAKE BY SIBASHIS---------------------------------"""
Whatstapp_option="""\n1.Show contact list\n
2.Add number\n
3.Message send\n
4.Sendwhatmsg_to_group\n
5.message_and_close\n
6.send_photo"""

print(Welcome_message)
while(True):
    Your_password=input("Enter the password: ")
    if(Your_password != sibashis.password()):
        print("“Password incorrect”\n\nDo you want to forget password \n\nIf yes chose 1\nIf No chose 2\n")
        chose=int(input("Chose one of them: "))
        if(chose == 1):
            sibashis.Forgetpassword()
    else:
        print(Whatstapp_option)
        chose_function=int(input("Chose one of them: "))
        if(chose_function == 1):
            print(us.show_contact_list())
            
        elif(chose_function == 2):
            name=input("Enter the name: ")
            number=int(input("Enter the number"))
            us.adding_contact_list(name,number)
            print(us.show_contact_list())
            
        elif(chose_function == 3):
            print(us.show_contact_list())
            name=input("Enter the name: ")
            if(name in us.show_contact_list()):
                message=input(f"Enter the message for {name}: ")
                Hours=int(input("Enter the hourse: "))
                Minutes=int(input("Enter the minute: "))
                Second=us.Second()
                print(Second)
                format=input("PM or AM ?  (Notice- Please write in Capital letter)")
                sibashis.send_message(Number_list[name],message,Hours_format.Hoursformat(Hours,format),Minutes,Second)
                # sibashis.send_message(Number_list[name],message,23,18,25)
            else:
                number=input(f"Enter the number of {name}")
                us.adding_contact_list(name,number)
                print(us.show_contact_list())
                message=input(f"Enter the message for {name}: ")
                Hours=int(input("Enter the hourse: "))
                Minutes=int(input("Enter the minute: "))
                Second=us.Second()
                format=input("PM or AM ?  (Notice- Please write in Capital letter)")
                sibashis.send_message(Number_list[name],message,Hours_format.Hoursformat(Hours,format),Minutes,Second)

        elif(chose_function == 4):
            print(us.show_contact_list())
            Group_name=input("Enter the name: ")
            message=input(f"Enter the message for {Group_name}: ")
            Hours=int(input("Enter the hourse: "))
            Minutes=int(input("Enter the minute: "))
            format=input("PM or AM ?  (Notice- Please write in Capital letter)")
            sibashis.send_message(Group_name, message,Hours_format.Hoursformat(Hours,format),Minutes)
                
        elif(chose_function == 5):
            print(us.show_contact_list())
            name=input("Enter the name: ")
            if(name in us.show_contact_list()):
                message=input(f"Enter the message for {name}: ")
                Hours=int(input("Enter the hourse: "))
                Minutes=int(input("Enter the minute: "))
                format=input("PM or AM ?  (Notice- Please write in Capital letter)")
                sibashis.send_message(Number_list[name],message,Hours_format.Hoursformat(Hours,format),Minutes)
            else:
                number=input(f"Enter the number of {name}")
                us.adding_contact_list(name,number)
                print(us.show_contact_list())
                message=input(f"Enter the message for {name}: ")
                Hours=int(input("Enter the hourse: "))
                Minutes=int(input("Enter the minute: "))
                format=input("PM or AM ?  (Notice- Please write in Capital letter)")
                sibashis.send_message(Number_list[name],message,Hours_format.Hoursformat(Hours,format),Minutes)
                
        elif(chose_function==6):
            print(us.show_contact_list())
            name=input("Enter the name: ")
            if(name in us.show_contact_list()):
                image=input(f"Give the path of the photo for {name} : ")
                Hours=int(input("Enter the hourse: "))
                Minutes=int(input("Enter the minute: "))
                format=input("PM or AM ?  (Notice- Please write in Capital letter)")
                sibashis.send_message(Number_list[name],image,00,Minutes)
            else:
                number=input(f"Enter the number of {name}")
                us.adding_contact_list(name,number)
                print(us.show_contact_list())
                image=input(f"Give the path of the photo for {name} : ")
                Hours=int(input("Enter the hourse: "))
                Minutes=int(input("Enter the minute: "))
                format=input("PM or AM ?  (Notice- Please write in Capital letter)")
                sibashis.send_message(Number_list[name],image,Hours_format.Hoursformat(Hours,format),Minutes)
    print("Thanks for using whatsapp")