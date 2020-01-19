# DestinyDiceProject

Today is Jan 14, 2019, which is also the day that FFG announce that they are bringing this game to a close. 

Well, this may be bad timing then - This project is for creating proxy dice and cards for Star Wars Destiny. 

This project utilizes decklists from swdestinydb.com and downloads the card faces, as well as creates a .scad file for making 3D printed dice with OpenScad.

How To Use:

Download the program.

Python3 needs to be installed your system
Also, need to have the requests module installed as well.

cmd: pip3 install requests

Open the "get_deck.py" file in your favorite text editor

There are a few things you will need to edit

Deck_list: enter a number for a decklist on swdestinydb.com - The decklist is the number listed in the url.
Example: https://swdestinydb.com/decklist/view/35305/oldmansolochewie-1.0 - Decklist is 35305 for this deck.


In base_folder, enter the path to wherever you downloaded this project.

Change create_dice to false if you only want cards, not scad files for 3d printing dice.

The beg_file.txt and end_file.txt need to be in the same directory as get_deck.py IF you are using this for dice.

Run the python file and you should have all the images downloaded for the cards and if create_dice is true, scad files
for 3d printing proxy dice.


Please let me know of any issues!

May The Force Be With You

Also, I would be happy for any help if anyone wants to add to this.


Credit for the .scad file format goes to:
https://www.thingiverse.com/thing:3296582
