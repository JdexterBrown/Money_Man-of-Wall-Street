# This is the Money Man program that should be funny

from sys import *
from _datetime import datetime
import textwrap   # import this module in order to wrap imported word doc
from PIL import Image
import random
from sys import exit
from Ages import calculate_age
import time
from figuringout_class import My_Country


def header():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$                                                                                                          $")
    print("$                   Money IS Power                                                                         $")
    print("$                Time to Buy some Assets                                                                   $")
    print("$                                                                                                          $")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    time.sleep(3)

def intro_to_game():
    print("---------------------------------------------------------------------------------------------------------")
    print("""Your wealthy uncle, just passed away. He was a billionaire and he left you a portion of his fortune. 
    The cars, planes, the rolex, the buildings, the notes, the gold, silver and so on. Now its your turn to be 
    the wall street shark""")
    print("----------------------------------------------------------------------------------------------------------")

    time.sleep(3)

def reading_of_will():
    print("You May now read my willl Yoda")
    will = open(r"C:\Users\HackerJB\PycharmProjects\Wolf of Wall Street\mywillforgame.txt", 'r')
    will_read = will.read()  # This reads the entire file called will
    wrapper = textwrap.TextWrapper(width=85) # wraps the text into a single paragraph
    string = wrapper.fill(text=will_read)
    print(string)

    time.sleep(5)

# Request if new identity needs to be created
def new_identity():
    new_name = input("Do you want to change your name?").lower()
    if "yes" in new_name:
        print("ok, if your sure. You will have to forget everyone you knew and your family")
        altered_identity()

    else:
        if "no" in new_name:
            print("""Thats ok, uncle same will love all the money you will give to him
            and so will all of your friends....sucker""")
            what_to_spend_on()

"""Engine to create new identity"""
def altered_identity():   # creates the altered identity and returns a picture of what your ID now looks like
    new_face = ['face1.jpg','face2.jpg','face3.jpg','face4.jpg']
    face = r"C:\Users\HackerJB\PycharmProjects\pythonthehardway\\vent\MoneyMan\\"
    new_face_item = random.choice(new_face)
    pic_of_newFace = Image.open(f"{face}{new_face_item}")

    new_name = input("whats your new first name last name: ")

    try:
        new_DOB = input("Enter in New Date of Birth [ MM/DD/YYYY]")
        dob = datetime.strptime(new_DOB, "%m/%d/%Y")

    except ValueError:
        print("Date of Birth Month, Day, and Year is invalid, please resubmit ")
        new_DOB = input("Enter in New Date of Birth [ MM/DD/YYYY]")
        dob = datetime.strptime(new_DOB, "%m/%d/%Y")

    new_age = calculate_age(dob)

    new_country = input("What country are you  from now: ").upper()

    My_Country(new_country)
    time.sleep(4)


    country_validity= input("Was your country name valid?").upper()
    if country_validity=="NO":
        altered_identity()
    else:
        print("Carry On")

    new_home = input("Where do you currently live: ")
    print(f" Your New name is {new_name}\n Your Age is {new_age}\n Your DOB is: {dob}\n You hail "
          f"from{new_country} and you live in {new_home}")

    print("This is what your new face look like that goes with your new identity")

    pic_of_newFace.show()

    what_to_spend_on()

#Function identifies the current assets you can choose from
def current_assets():
    assets = ['Cars', 'Buildings', 'Mortgage notes', 'Gold', 'Blue Chip Stock', 'Art Work', 'Tech Company']
    i = 1
    print("-----------------------------------------------------------")
    print("These are the assets that you get to choose from. You can only choose one of the assets (Please type in"
          "asset name:\n")
    for item in assets:
        print(f"{i}  {item}")
        i += 1

# Identify the asset you want to inherit
def Assets_you_want():
    count = 1
    b = False
    while b == False:

        a = input("Which asset do you want? Please type in the name of the asset:").lower()

        if a == "cars":
            print("The asset you selected was {}".format(a))
            b = True

        elif a == "buildings":
            print("The asset you selected was {}".format(a))
            b = True
        elif "notes" in a:
            print("The asset you selected was {}".format(a))
            b = True

        elif a == "gold":
            print("The asset you selected was {}".format(a))
            b = True
        elif "stock" in a:
            print("The asset you selected was {}".format(a))
            b = True

        elif a == "art work":
            print("The asset you selected was {}".format(a))
            b = True

        elif a == "tech company":
            print("The asset you selected was {}".format(a))
            b = True
        else:
            b = False

    asset_logic(a, count)

# Asset function engine that determines how much each asset is worth
def asset_logic(a, count):
    my_asset = a

    selected_asset = []

    if "cars" in a:
        my_asset = "Cars"
        selected_asset = ['30', '$200,000']
        print(f"Your the owner of {selected_asset[0]} {my_asset}, worth a total of {selected_asset[1]}")

    elif "buildings" in a:
        my_asset = "Buildings"
        selected_asset = ['6', '$3,000,000']
        print(f"Your the owner of {selected_asset[0]} {my_asset}, worth a total of {selected_asset[1]}")

    elif "notes" in a:
        my_asset = "Mortgage Notes"
        selected_asset = ['30', '$550,000']
        print(f"Your the owner of {selected_asset[0]} {my_asset}, worth a total of {selected_asset[1]}")

    elif "gold" in a:
        my_asset = "Gold"
        selected_asset = ['40 bricks of', '$456,000']
        print(f"Your the owner of {selected_asset[0]} {my_asset}, worth a total of {selected_asset[1]}")

    elif "stock" in a:
        my_asset = "Blue Chip Stock"
        selected_asset = ['400,000', '$456,000']
        print(f"Your the owner of {selected_asset[0]} shares of {my_asset}, worth a total of {selected_asset[1]}")

    elif "art work" in a:
        my_asset = "Paintings"
        selected_asset = [10, '$456,000']
        print(f"Your the owner of {selected_asset[0]} {my_asset}, worth a total of {selected_asset[1]}")

    elif "tech company" in a:
        my_asset = "Automation Technolgy Companies"
        selected_asset = [2, '$380,000']
        print(f"Your the owner of {selected_asset[0]} {my_asset}, worth a total of {selected_asset[1]}")


    else:
        print("A")

    how_much_money_inheritied(selected_asset, my_asset)
def how_much_money_inheritied(selected_asset, my_asset):
    print(f" WOW, you inherited {selected_asset[0]}  {my_asset} worth {selected_asset[1]}, you're rich.")


    new_identity()

def what_to_spend_on():
    investment_schemes =["Work with Bernie Madoff"," Invest in BitCoin","Invest in African prince diamond Mine"]
    print(textwrap.dedent("""Now that you have your new found fortune, would you like to make more money off of those 
    assets ?
    
    To make more money on top of your money you have to sell all  your new assets"""))
    answer = input(" Do you want to sell all of your assets to make more money? Yes or No? ").lower()

    i = 1
    if 'yes' in answer:
         print("Here are your options:")
         for s in investment_schemes:
             print(f"{i}. {s}")
             i += 1
         fake_money_scheme()
    elif 'no'in answer:

        print("You just avoid losing all of your money, but unfortunately the FBI is investigating you")
        FBI_or_Freedom()

def fake_money_scheme():

    fake_scheme = int(input("Which Scheme will you pick? (1, 2, or 3)"))
    if fake_scheme == 1:
        print("Bernie made off with all of your money....and you are back to being broke.")
        tryAgain()
    elif fake_scheme == 2:
       print(textwrap.dedent("""
       You invested in bitcoin and while the prices fluctuate, you triple your money.
       print("You just made so much money that you decide to by a portion of New Found land and rename it 
       pizza land"""))

       FBI_or_Freedom()

    elif fake_scheme == 3:
      print("""" I CAN'T BELEIVE YOU FEEL FOR THE NIGERAN PRINCE, DIAMOND MIND TRICK!. SMACK YOURSELF
      IN THE HEAD BECAUSE YOU JUST LOST IT ALL AGAIN""")
      print("You can file a police report, but they laugh you out of the station")

      tryAgain()
    else:
     print("You didn't select from the options provided.")
    what_to_spend_on()


def FBI_or_Freedom():   # Need to work on this to finish up program and then return image of person in jail
    print('Well Well Well Looks like Johnny Law is starting to investigate how you have so much money, but dont seem'
          'to have paid enough taxes')

    admit_wrong_or_not = int(input("You have three options:\n 1) You can put your money into a foreign bank"
                               "\n2) Flee the country\n3) Pay your Taxes\nWhich option do you want [1,2, or 3?]:  "))

    if admit_wrong_or_not == 3:
        print("While Uncle Sam Took a chunk of money form you remain free and live out your days still really rich")

    elif admit_wrong_or_not == 2:
        print(" You Flee the country, only for a local crime boss to find you and to make you disappear")

        tryAgain()

    elif admit_wrong_or_not == 1:
        print("You put your money into a foreign bank, but you forgot the account number and password"
              "You know spend 20 years trying to find your account number, only to die alone in an old folsk home"
              "in panama")

        tryAgain()

def tryAgain():
    retry= input("Do you want to try your luck again with getting wealthy and staying wealthy ?:").lower()

    if retry == "yes":
        header()
        intro_to_game()
        reading_of_will()
        current_assets()
        Assets_you_want()

    else:
        exit(0)


header()
intro_to_game()
reading_of_will()
current_assets()
Assets_you_want()




