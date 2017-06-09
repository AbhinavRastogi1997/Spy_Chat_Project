from datetime import datetime

class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name=name
        self.salutation=salutation
        self.age=age
        self.rating=rating
        self.is_online=True
        self.chats=[]
        self.curr_status_mess=None

class Chat_Message:
    def __init__(self,message,sent_by_me):
        self.message=message
        self.time=datetime.now()
        self.sent_by_me=sent_by_me





spy = Spy('Bond',"Mr.",19,4.5)

friend_one=Spy("Ravi","Mr.",18,4.6)
friend_two=Spy("Monica","Mrs.",19,4.7)
friend_three=Spy("Raman","Mr.",20,4.8)
friend_four=Spy("Kavya","Mrs.",22,4.9)

friend = [friend_one,friend_two,friend_three,friend_four]