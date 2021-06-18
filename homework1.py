#clear the screen
import os
os.system('cls' if os.name == 'nt' else 'clear')
#getdata function used to get inpur form user
def getdata():
    str
username = input("enter the user name: ")
age = input("enter the age :")
Education =input("qualification:")
hobby = input("what is your hobby:")
# calldata function used to show user result
def calldata():
    print("user name is :-", username)
    print ("your are :-",age + " year Old")
    print("your qualification is:-",Education)
    print ("and you like :-",hobby)  
#the method user to get input form user
getdata()
#clear the screen
import os
os.system('cls' if os.name == 'nt' else 'clear')
#the method used to display data 
calldata()


