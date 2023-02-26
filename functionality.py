from lxml import etree as ET
import os, os.path, pathlib
import pandas as pd
import logging
import traceback
logging.basicConfig(filename='FaceLinker.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

def ingestShortlist(path):
    shortlist = pd.read_html(path,encoding="UTF-8")[0]
    shortlist[["UID","Name","Club"]]
    shortlist["Deaccented"] = shortlist["Name"].str.normalize("NFKD").str.encode("ascii",errors="ignore").str.decode("utf-8")
    return shortlist

def ingestFiles(folder):
    files = list(pathlib.Path(folder).glob("*.[pj][np][g]"))
    fileData = pd.DataFrame({"FilePath":files})
    fileData["FileName"] = fileData["FilePath"].apply(lambda file: os.path.splitext(os.path.basename(file))[0] )
    if(fileData["FileName"].str.contains("_").any()):
        fileData[["Identifier", "Team"]] = fileData["FileName"].str.split(pat="_",expand=True)
    else:
        fileData["Identifier"] = fileData["FileName"]
        fileData["Team"] = None
    return fileData

def linkPlayers(shortlistPath, playersPath, rename):
    try:
        newgens = ingestShortlist(shortlistPath)
        fileData = ingestFiles(playersPath)
        duplicates = newgens[newgens["Name"].duplicated(keep=False)]
        noDuplicates = newgens[~newgens["Name"].duplicated(keep=False)]

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
        return "Pictures were linked succesfully"
    except KeyError as keysmissing:
        logger.error(keysmissing)
        return"There was an error with the columns of your shortlist, please make sure you have the correct view active and your FM is set to english"

    except Exception as error:
        logger.error(traceback.format_exc())
        return "An unexpected error occured, check FaceLinker.log for more details"



