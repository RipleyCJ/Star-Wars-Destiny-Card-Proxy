from requests import get
import json
import urllib.request
import os
import re

deck_list = 35187 # enter a deck list number here to download this deck

base_folder = "change to base of where ever you placed the DestinyDiceProject Folder" #example: /users/ripleycj/documents/destinydiceproject/
card_path = f"{base_folder}cards/"
dice_path = f"{base_folder}dice/"
create_die = True # True if you want the .scad files for 3d printing dice.

os.chdir(base_folder)#changes the directory to the base of the project






"""This pulls the deck from SW destiny db"""
def get_deck():
    response = get(f'http://swdestinydb.com/api/public/decklist/{deck_list}')
    deck =  json.loads(response.content.decode('utf-8'))
    return deck

"""Checks if their is a die for the provided card"""

def check_die(card_num):
    if card_num == True:
    	return True
    else:
        return False

"""Downloads the card to the /cards/ folder"""
def download_card(card, item):
	url = card['imagesrc']
	urllib.request.urlretrieve(url, f'{card_path}{item}.jpg')


"""returns the cards die"""
def get_die(die):
    return die

"""Writes to the beggining part of the scad file"""
def write_beg_file(card):
    with open("beg_die.txt") as f:
        beg_file = (card["code"])
        with open(f"{dice_path}{beg_file}.scad", "x") as f1:
            for line in f:
                f1.write(line)
            f1.write(f'DIE_NUMBER = "{beg_file[2:]}";\n')

            f1.write('FACES = [\n')

"""Writes the end of the scad file"""
def write_end_file(card):
    with open("end_die.txt") as f:
        beg_file = card["code"]
        with open(f"{dice_path}{beg_file}.scad", "a") as f1:
            for line in f:
                f1.write(line)

"""Checks for blanks and special attack on die"""
def check_special(num, card):
    with open(f"{dice_path}{card}.scad", "a") as f:
        if "-" in num:
            f.write(f'         ["blank"]\n')
        if "Sp" == num:
            f.write(f'         ["special"]')


"""checks for all non special results, aka regular results"""
def check_not_special(num, card):

        # no special results on die
    die_num = num[0]
    die_str = num.replace(die_num[0], '')

    with open(f"{dice_path}{card}.scad", "a") as f:
        if "R" == die_str:  # resource card
            f.write(f'         ["resource", "{die_num}"]')
        elif "RD" == die_str:  # range damage
            f.write(f'         ["ranged", "{die_num}"]')
        elif "F" == die_str:  # Focus
            f.write(f'         ["focus", "{die_num}"]')
        elif "Dc" == die_str:  # discard
            f.write(f'         ["discard", "{die_num}"]')
        elif "MD" == die_str:  # Melee
            f.write(f'         ["melee", "{die_num}"]')
        elif "Sh" == die_str:  # shield
            f.write(f'         ["shield", "{die_num}"]')
        elif "ID" == die_str:  # indirect damage
            f.write(f'         ["indirect", "{die_num}"]')
        elif "Dr" == die_str:
            f.write(f'         ["disrupt", "{die_num}"]')


"""Checks for sides that cost a resource"""

def check_resource_cost(num, card):
    if any(char.isdigit() for char in num) and len(num) > 3 and num[0].isdigit():
        first_num = num[0]
        last_num = num[3]
        pattern = pattern = '[0-9]'
        die_str = re.sub(pattern,'', num)
        with open(f"{dice_path}{card}.scad", "a") as f:

            if "R" == die_str:  # resource card
                f.write(f'         ["resource", "{first_num}", "resource", "{last_num}"]')
            elif "RD" == die_str:  # range damage
                f.write(f'         ["ranged", "{first_num}", "resource", "{last_num}"]')
            elif "F" == die_str:  # Focus
                f.write(f'         ["focus", "{first_num}", "resource", "{last_num}"]')
            elif "Dc" == die_str:  # discard
                f.write(f'         ["discard", "{first_num}", "resource", "{last_num}"]')
            elif "MD" == die_str:  # Melee
                f.write(f'         ["melee", "{first_num}", "resource", "{last_num}"]')
            elif "Sh" == die_str:  # shield
                f.write(f'         ["shield", "{first_num}", "resource", "{last_num}"]')
            elif "ID" == die_str:  # indirect damage
                f.write(f'         ["indirect", "{first_num}", "resource", "{last_num}"]')
            elif "Dr" == die_str:
                f.write(f'         ["disrupt", "{first_num}", "resource", {last_num}"]')


"""Checks for plus type cards"""
def check_plus(num, card):
    if num[0] == "+":
        plus = num[0]
        die_num = int(re.search(r'\d+', num).group())
        die_str = num[2:]
        with open(f"{dice_path}{card}.scad", "a") as f:
            if "R" == die_str:  # resource card
                f.write(f'         ["resource", "{plus}{die_num}"]')
            elif "RD" == die_str:  # range damage
                f.write(f'         ["ranged", "{plus}{die_num}"]')
            elif "F" == die_str:  # Focus
                f.write(f'         ["focus", "{plus}{die_num}"]')
            elif "Dc" == die_str:  # discard
                f.write(f'         ["discard", "{plus}{die_num}"]')
            elif "MD" == die_str:  # Melee
                f.write(f'         ["melee", "{plus}{die_num}"]')
            elif "Sh" == die_str:  # shield
                f.write(f'         ["shield", "{plus}{die_num}"]')
            elif "ID" == die_str:  # indirect damage
                f.write(f'         ["indirect", "{plus}{die_num}"]')
            elif "Dr" == die_str:
                f.write(f'         ["disrupt", "{plus}{die_num}"]')



def get_cards():
#print (type(deck))
    for item in get_deck()["slots"]:
        #gets each card in decklist from swdestinydb
        get_card = get(f'http://swdestinydb.com/api/public/card/{item}')

        #removes file if it already exists - mainly used for testing purposes, but also helps if you are accidentally creating a duplicate
        if os.path.exists(f"{card_path}{item}.scad"):
            os.remove(f"{card_path}{item}.scad")

        if os.path.exists(f"{dice_path}{item}.scad"):
            os.remove(f"{dice_path}{item}.scad")

        card = json.loads(get_card.content.decode('utf-8'))

        die_count = 1
        if create_die == True: #change to false if you just want to download cards.
            if check_die(card["has_die"]):
                die = get_die(card["sides"])

                write_beg_file(card)

                for i in die:  # iterates over all 6 sides
                    check_special(i, item)  # checks for blank side, or special ability side
                    check_not_special(i, item)  # All regular die are checked for here
                    check_resource_cost(i, item)  # die with resource cost
                    check_plus(i, item)  # die with + character

                    if die_count < 6:
                        with open(f"{dice_path}{item}.scad", "a") as f:
                            f.write(",\n")

                        die_count += 1
                    else:
                        with open(f"{dice_path}{item}.scad", "a") as f:
                            f.write("\n         ];\n")

                write_end_file(card)

        download_card(card, item)  # downloads the card from swdestinydb


get_cards()
