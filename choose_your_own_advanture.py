name = input("type your name : ")
print("welcome", name, 'to this adventure!')

answer = input("you are on a dirt, it has come to an end to and you can go (left or right). which highway would you like to go?").lower()
#________________________________________________________________________________________________________________________________________
#you choose left side
if answer == 'left' :
    answer = input("you come to a river, you can walk around it or swim accross(swim/walk) :")

#swim or walk
    if answer == "swim":
        print("you swim acrross and were eaten by an alligater.")
    elif answer == "walk":
        print("you walk many mails, run out of water and you lost the game")
    else:
        print("not a vailed option. you lose")
 #________________________________________________________________________________________________________________________________________
 #you choose right side   
elif answer == 'right':
    answer = input("you come to a  bridge, it looks wobbly, do you want to cross it or head back(cross/back)?")

    #back or cross    
    if answer == "back":
        print("you go back and  lose.")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger. do you talk to them (yes/no)?")

        #yes or no
        if answer == "yes":
            print("you talk to the stanger and they give you gold. you Win!")
        elif answer == "no":
            print("you ignore the stranger and they are offended and you lose.")
            
        else:
             print("not a valid option. you lose. ")
    else:
        print("not a valid option. you lose.")
else : 
    print("not a valid option, you lose")

print("Thank you for trying", name)
 
  