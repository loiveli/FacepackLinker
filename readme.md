# FaceLinker

## What is FaceLinker?

Facelinker is a program that links pictures to players in Football Manager 23

## How to use it?

### Prerequisites
1. Python
2. Football manager 23

#### Download
Download the 0.1 release [here](https://github.com/loiveli/FacepackLinker/releases/tag/0.1)
Unzip it anywhere on your machine, it contains two files and a folder called "Views". Copy the contents of the view folder to your Football manager views folder

#### Install required packages
Open the folder you unzipped the files in the command line, and run this command: `pip install -r requirements.txt`, this will install all the required python packages.

#### Create and export the shortlist
Now you need to create a shortlist of all the players you want to link the pictures to. 
If you are using the 1998/1999 DB and the regen mod, here is how to link the facepacks to the regens from the regen mod:
1. Create a new shortlist for the regens
2. search "faceinthegame" on the search bar
3. Change to the "People" tab
4. Select a chunk of the players, as long as you select under 500 you are fine
5. Right click and select "Add to shortlist" and add them to the shortlist you created
6. Repeat 4 and 5 until all players from the search are shortlisted
7. Open the shortlist you created
8. Import the view you copied to the views folder and activate it
9. Select all the players with ctrl+A
10. Press ctrl+P, select "Web page" and press OK
11. Choose where you want to export the shortlist to

#### Prepare the pictures you want to link
You need to make sure the pictures you want to link are all in the same folder, and that they follow a few naming rules:
1. They need to all be either .png or .jpg files
2. They need to be named either according to the UID of the player, Exact name of the player inside FM or they need to be named in the format: "Name_Team"

### Using the Script
Once you have completed all the prerequisite steps, you can now actually use the script to link the pictures to the players.
Run the script by opening the folder you unzipped the files to in the command prompt, and running the command `python FaceLinker.py`
The script will first ask you for the path to the folder where the pictures are, this should be somewhere inside the Football Manager 23/graphics folder
Second thing it will ask is the path to the shortlist file you exported, you can get this by opening the file with a web browser and copying what is in the address bar
Then it will ask if you want to rename the files according to the player UID:s, you can answer Y for Yes or N for No.
Once that is done, it will start processing the files and linking them to players it finds inside the shortlist file, and once its done it will create a config.xml file in the folder where the pictures are.
After its done you need to refresh the skin inside FM and the pictures should be linked to the correct players
