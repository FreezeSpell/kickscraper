###A program that runs main.py and outputs the name, blurb, funded amount and requested amount into a document in /Scraper/outputs.

from main import dataSet
import os   

fileNumber = max(os.listdir("Academics-Antics/Python/Outreaching CB/Scraper/outputs"))
fileNumber = int(fileNumber)
fileNumber += 1

outputLocation = (f"Academics-Antics/Python/Outreaching CB/Scraper/outputs/{fileNumber}")


file = open(outputLocation, "w")

for i in dataSet:
    file.writelines(str(i))
    file.write("\n")

print("Success!")