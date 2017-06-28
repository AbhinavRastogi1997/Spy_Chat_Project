                                                             #The Spy Chat Application

from spy_details import spy,Spy,friend,Chat_Message  #importing various spy details from the file spy_details
from steganography.steganography import Steganography #importing the Steganography module
from colorama import init
init()
from colorama import Fore, Back, Style   #importing Fore from Coloroma





print"Hello!" #This is how we use the print function to print something......

print"Let's get Started!!" #Another print Statement.We can enclose the statement in both single and double quotes.
#If the above statement was enclosed with single quotes then we write it as 'Let\'s get Started'....
#This is basically referred to as escaping in python ..........


q="Do you want to continue as"+" "+ spy.salutation + " " + spy.name+ "(y/n?)"
ans = raw_input(q) # We use raw_input to take input from the user.
status_messages=["I am busy","I am in Office","I'll call you later","Dream Big"]#A python list showing different status messages


def add_status(): #Defining a function to add the status
    updated_status_message = None

# Using the if-else statement to check whether the current status is none or not.
    if spy.curr_status_mess != None:
        print"Your current status message is %s" % (spy.curr_status_mess)
    else:
        print"You dont have any status at the moment."

    choice = (raw_input("Do you want to chose from older status messages (Y/N)?"))#Asking the user if he wants to choose from older status mesages

    if choice.upper() == 'Y':
        item = 1                                       #If the user wnats to select a status from the older status messages
        print"Choose from the statuses given below:"   #for this we use the for loop
        for messages in status_messages:               #We iterate through various messages and then print each message through every iteration
            print(str(item) + "." + " " + messages)
            item = item + 1

        status_select = int(raw_input("Which status do you want to select"))      #Asking the user about the status he wants to select

        if status_select <= len(status_messages):
            updated_status_message = status_messages[status_select - 1]       #Storing the status message in updated_status_message

        else:
            print"Select a valid status message"

    elif choice.upper() == 'N':
        new_status_message = raw_input("Write your new status message")   #If the user wants to write a status of his own ,then asking him to write his status

        if len(new_status_message) > 0:
            status_messages.append(new_status_message)
            updated_status_message = new_status_message             #Storing the status message in updated_status_message

        else:
            print"Add a valid status message"

    else:
        print"Enter either Y/N"

    if updated_status_message:
        print"The updated status message is %s" % (updated_status_message) #Printing the following statement if the updated status message is not none
    else:
        print"You dont have a status update" #Printing the following statement if the updated status message is none

    return updated_status_message   #returning the updated status message to the calling function

def add_friend():    # Defining a function to add a friend
    new_friend=Spy("","",0,0.0)     #Using a constructor to initialize various variables of object new_friend of the spy class
    new_friend.name=raw_input("Please add the name of your friend.") #Taking input for new friend's name
    new_friend.salutation=raw_input("What salutation would you like to give to your friend Mr./Mrs.?") #Taking input for new friend's salutation
    new_friend.age=int(raw_input("What is your friend's age?")) #Taking input for new friend's age
    new_friend.rating=float(raw_input("Give your friend a rating")) #Taking input for new friend's rating

    if new_friend.name>0 and new_friend.age>12 and new_friend.rating>=spy.rating:
        friend.append(new_friend)                                            #Adding the new friend to the friend list if the conditions in the if statement are met.
        print"Your new friend has been added!"

    else:
        print"Enter valid friend details"      #Printing the following statement if the if condition is not met




    return len(friend)         #Returning the number of friends of the user

def select_a_friend():  #Defining a function to select a friend
    temp=1
    for friends in friend:   #Printing out the details of various friends of the user using the for loop
        print("%d. Name:%s %s , Age:%s , Rating:%.2f"%(temp,friends.salutation,friends.name,friends.age,friends.rating))
        temp=temp+1

    friend_choice=int(raw_input("Choose from the above friends"))

    pos_of_friend= friend_choice-1

    return pos_of_friend   #Returning the index position of the friend in the friend list.

def send_a_message():   #Defining a function to send the secret message to a friend
    friend_choice=select_a_friend()  #Calling the select a friend function to get the index position of the friend to whom we want to send the secret message

    original_img=raw_input("Enter the image path that you want to encode:")#Asking the user to input the image path of the text in the image to be encoded
    output_path='output.jpg' #path of the outfut file that will contain the encoded image
    text=raw_input("Enter the text that you want to hide:")
    Steganography.encode(original_img,output_path,text)  #Using Steganography to encode the text within the original_image
                                                         #The encoded image is output.jpg
    chat=Chat_Message(text,True)  #Using constructor to initialize various variables of the object chat of the Chat_Message class

    friend[friend_choice].chats.append(chat)  #Appending the chat to the "chats" list of the selected friend

    print"The secret message is ready"

def read_message():  #Defining a function to read a message sent by the sender
    sender = select_a_friend()  #Calling the select a friend function to get the index position of the sender

    output_path = raw_input("What is the path of the image to be decoded?") #Asking the user to input the output path of the image to be decoded

    secret_text = Steganography.decode(output_path) #Using Steganography to decode the secret text in the image and the storing the secret message
                                                    # in the secret_text variable

    if len(secret_text)>0:


        if len(secret_text.split())<=100:
            chat = Chat_Message(secret_text,False) #Using the constructor to initialize various variables of chat object of Chat_Message class.
            friend[sender].chats.append(chat)   #Appending the chat to the "chats" list of the sender
            print("Your secret message is %s !!"%(secret_text))     #printing out the secret message

            if secret_text=='SOS' or secret_text=="SAVE ME":          #If the sender(spy friend) sends "SOS" / "SAVE ME" as secret text
                print("Go!!Help your friend.He is in Danger!!!")      #Then the following statement is printed out.

        else:
            friend.remove(friend[sender])                     #Removing the sender(spy friend) from the friend list if he is speaking more than 100 words
            print("Your friend has been removed from the friends list as he is speaking too much")
            print("You now have %d friends"%(len(friend)))


    else:
        print("No secret message found!")

def read_chat_history():   #Defining a function to read the chat history
    chat_with=select_a_friend()  #Calling the select a friend function to get the index position of the friend to read the chat history

    for chat in friend[chat_with].chats:
        if chat.sent_by_me:
            print (Fore.BLUE+'[%s]'+Fore.RED+' %s:'+Fore.BLACK+' %s') % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print (Fore.BLUE+'[%s]'+Fore.RED+ '%s said:'+Fore.BLACK+' %s') % (chat.time.strftime("%d %B %Y"), friend[chat_with].name, chat.message)


def start_chat(spy):  #Defining a function to start the spy chat


    spy.name = spy.salutation+" "+spy.name

    if spy.age>12 and spy.age<50:
        print"Authentication complete."+"Welcome %s , age: %d ,of Rating %.2f"%(spy.name,spy.age,spy.rating)
        print"Nice to have you here."                      #Writing a welcome message for the spy if the "if" statement condition is met

        show_menu=True

        while show_menu:

            menu_choice = int(raw_input("What do u want to do?\n 1) Add a status update 2) Add a friend 3) Send a secret message 4) Read a secret message 5) Read chats from a user 6) Close application "))
            #Asking the user about what he wants to do
            if menu_choice>=1 and menu_choice<=6:

                if menu_choice == 1:
                    print"You chose to update the status"
                    spy.curr_status_mess = add_status() #Calling the add status function if the user wishes to update his/her status

                if menu_choice == 2:
                    print"Oh! So you want to add a friend!"
                    Num_Of_Friends=add_friend()   #Calling the add friend function if the user wants to add a friend
                    print"You have %d friends"%(Num_Of_Friends)


                if menu_choice == 3:
                    print"Let's send the secret message!!"
                    send_a_message() #Calling the send a message function if the user wishes to send a secret message


                if menu_choice == 4:
                    print"Lets read the secret message!!"
                    read_message()#Calling the read a message function if the user wishes to read the secret message sent by his/her friend


                if menu_choice == 5:
                    print"Let's read chats from the user"
                    read_chat_history()#Calling the read chat history function if the user wishes to read the chat history of his chat with a particular friend

                if menu_choice == 6:
                    print"You chose to close the application."
                    show_menu=False #Using the exit function to close the application
            else:
                print"Choose a valid menu."




    else:
        print"This is not a valid spy-age."




if ans.upper()=='Y':  #If the user wishes to continue as default user
    start_chat(spy)    #Calling the start chat function to start the chat

elif ans.upper()=='N':

    spy=Spy("","",0,0.0) #Using the constructor to initialize various variables of the object spy of Spy class

    spy.name=raw_input("What is your name?") #Taking input of the spy name

    if len(spy.name)>0:
        spy.salutation=raw_input("What would you like to be called Mr./Mrs ?")#Taking input of the spy salutation
        spy.age=raw_input("What is your age ?")#Taking input of the spy age
        spy.age=int(spy.age)
        spy.rating=raw_input("What is your rating?")#Taking input of spy rating
        spy.rating=float(spy.rating)
        spy_is_online=True
        start_chat(spy)#Calling the start chat function to start the chat

    else:
         print"The name entered by you is not a valid spy-name" #Printing out the following statement in the the user enters an invalid spy name

else:
    print"Enter either Y/N" #Printing out the following statement if the user enters something other than Y/N















