

playersPath = "I:/FM/Football Manager 2023/graphics/1999/" #input("Please enter the path to the folder where the images are located: ")
shortlist = "I:/FM/Football Manager 2023/Shortlist.html" #input("Please enter the path to the shortlist file you exported: ")
valid = False
while not valid:
    inputText = input("Do you want the script to rename all the files to playerIDs? Y/N: ")
    if inputText =="Y":
        rename = True
        valid = True
    elif inputText == "N":
        rename = False
        valid = True
    else:
        print("Please enter a valid input")



import os, os.path, pathlib


from lxml import etree as ET


import pandas as pd


newgens = pd.read_html(shortlist,encoding="UTF-8")[0]


newgens = newgens.drop(["Rec","Inf"], axis=1)






newgens["Deaccented"] = newgens["Name"].str.normalize("NFKD").str.encode("ascii",errors="ignore").str.decode("utf-8")


duplicates = newgens[newgens["Name"].duplicated(keep=False)]
noDuplicates = newgens[~newgens["Name"].duplicated(keep=False)]






files = list(pathlib.Path(playersPath).glob("*.[pj][np][g]"))



fileData = pd.DataFrame({"FilePath":files})


fileData["FileName"] = fileData["FilePath"].apply(lambda file: os.path.splitext(os.path.basename(file))[0] )



if(fileData["FileName"].str.contains("_").any()):
    fileData[["Identifier", "Team"]] = fileData["FileName"].str.split(pat="_",expand=True)
else:
    fileData["Identifier"] = fileData["FileName"]
    fileData["Team"] = None
config = ET.Element("record")
preload = ET.SubElement(config,"boolean", id="preload", value="false")
amap = ET.SubElement(config,"boolean", id="amap", value="false")
playerList = ET.SubElement(config, "list", id="maps")


for index,fileRow in fileData.iterrows():
    record = {"from":None, "to":None}
    identifier = str(fileRow["Identifier"])
    fileName = fileRow["FileName"]
    if(fileRow["Team"]):
        player = newgens.loc[((newgens["Name"] == identifier)|(newgens["Deaccented"] == identifier)) & (newgens["Club"] == fileRow["Team"])]
        
    else:
        
        player = noDuplicates.loc[(noDuplicates["Name"] == identifier)|(noDuplicates["Deaccented"] == identifier)|(noDuplicates["UID"].astype(str) == identifier)]
        
    if(len(player) == 1 ):
        
        if(rename and fileName != str(player["UID"].values[0]) ):
            path, name = os.path.split(fileRow["FilePath"])
            extension = os.path.splitext(name)[1]
            newFile = str(player["UID"].values[0]) + extension
            newPath = os.path.join(path,newFile)
            fileName = str(player["UID"].values[0])
            os.rename(fileRow["FilePath"], newPath)
        
        record = {"from":fileName,"to":str(player["UID"].values[0])}
    else:
        comment = ET.Comment(f'{fileName} not found')
        playerList.insert(0, comment)
    if record["from"] and record["to"]:
        recordXML = ET.SubElement(playerList, "record")
        recordXML.set("from", str(record["from"]))
        recordXML.set("to",f'graphics/pictures/person/{record["to"]}/portrait')
 

configTree = config.getroottree()
configTree.write(f"{playersPath}/config.xml", encoding="utf-8", pretty_print=True)





