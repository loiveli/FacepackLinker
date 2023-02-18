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
Few precautions when using the tool: 
Make sure you have a backup of the pictures with original names, if you choose to rename the files, those will be hardlinked and you cant really undo it
The tool will overwrite any existing config.xml file in the folder you have the pictures in, so make a backup of that too

### Using the Tool
Once you have completed all the prerequisite steps, you can now actually use the tool to link the pictures to the players.
Run the executable, and after a while a small box with a very simple UI should open.
In the first line, you have the shortlist, press the "Browse" button and select the shortlist file you exported
Second line is for the folder all the pictures are in, again press the "Browse" button and navigate to the correct folder
Third line has a checkbox. If that checkbox is checked, the tool will rename all the files with the corresponding player UIDs, if its not checked, it will keep the names as is.
Once you have filled the first and second lines, you can then press the "Link pictures" button, this will start the linking process. Once the linking process is done it will pop up saying its done.
After its done you need to refresh the skin inside FM and the pictures should be linked to the correct players
You can check the config.xml file for any players that were not found in the shortlist, they will be commented at the top
