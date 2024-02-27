###Settings
fileLocation = "Kickstarter_2023-10-12T03_20_02_365Z 2.json"
startEntry = 0 #The first entry in the list to start from
finalEntry = 10 #The last entry in the list to finish
sleepTimer = 0 #The amount of time to sleep between each entry
printIndices = False #Print the blurb index and goal index for each entry
printMoneys = True #Print the goal money and funded amount for each entry
setFilter = True #Filter out entries that don't meet the requirements

###Filters
goalFunded = True #Only show entries that have their goal funded
goalNotFunded = False #Only show entries that don't have their goal funded
activeFailed = True #Count active entries not yet funded as failed

###Imports
import time
import os

###Starting Commands
startTime = time.time()
dataSet = []

print("Initialising database...")
data = open(fileLocation)
print("Database initialised.")

print("Accessing database...")
listdata = data.readlines()
print("Database accessed.")

print(f"[Starting Entry]: {startEntry}")
print(f"[Final Entry]: {finalEntry}")

skippedEntriesNmbr = 0
skippedEntries = []
filteredEntriesNmbr = 0
filteredEntries = []

if goalFunded == True and goalNotFunded == True and setFilter == True:
    print("Too many filters active, no results will be printed.")
    os.exit()

print(f"Commencing scraping of {finalEntry-startEntry} entries...")

def scrapeFile(skippedEntriesNmbr,
               skippedEntries,
               filteredEntriesNmbr,
               filteredEntries,
               startEntry: int = 0, 
               finalEntry: int = 1000, 
               sleepTimer: int = 0) -> tuple:
    """
    Scrapes data from a list of entries based on specified parameters.

    Args:
        skippedEntriesNmbr (int): The number of skipped entries, initialisation only.
        skippedEntries (list): The list of skipped entry indices, initialisation only.
        filteredEntriesNmbr (int): The number of filtered entries, initialisation only.
        filteredEntries (list): The list of filtered entry indices, initialisation only.
        startEntry (int, optional): The starting index of the entries to scrape. Defaults to 0.
        finalEntry (int, optional): The ending index of the entries to scrape. Defaults to 1000.
        sleepTimer (int, optional): The time to sleep between each scrape iteration. Defaults to 0.

    Returns:
        tuple: A tuple containing the updated skippedEntries, skippedEntriesNmbr, filteredEntries, and filteredEntriesNmbr.
    """
    ###Looping through the set of entries
    for i in range(startEntry, finalEntry):
        entry = listdata[i]
        blurbIndex = listdata[i].index("blurb")
        goalIndex = listdata[i].index("goal")
        nameIndex = listdata[i].index("name")
        pledgeIndex = listdata[i].index("pledged")
        stateIndex = listdata[i].index("state")
        currencyIndex = listdata[i].index("currency")
        symbolIndex = listdata[i].index("currency_symbol")
        slugIndex = listdata[i].index("slug")
        categoryIndex = listdata[i].index("analytics_name")
        try:
            goalMoney = entry[goalIndex+6:pledgeIndex-2]
            fundedMoney = entry[pledgeIndex+9:stateIndex-2]
            goalMoney = int(round(float(goalMoney)))
            fundedMoney = int(round(float(fundedMoney)))
            currency = entry[currencyIndex+11:symbolIndex-3]
            projectStatus = entry[stateIndex+8:slugIndex-3]
            

            if fundedMoney >= goalMoney:
                goalReached = True
            elif fundedMoney < goalMoney:
                goalReached = False
            
            if setFilter == True and goalNotFunded == True:
                if goalReached == True: ##Cuts out entries that have their goal funded
                    filteredEntriesNmbr += 1
                    continue
            
            if setFilter == True and goalNotFunded == False:
                if goalReached == False: ##Allows entries that don't have their goal funded
                    filteredEntriesNmbr += 1
                    continue
            
            if setFilter == True and goalFunded == True:
                if goalReached == False: ##Cuts out entries that don't have their goal funded
                    filteredEntriesNmbr += 1
                    continue
            
            if setFilter == True and goalFunded == False:
                if goalReached == True: ##Allows entries that have their goal funded
                    filteredEntriesNmbr += 1
                    continue
            
            if setFilter == True and goalNotFunded == True:
                if projectStatus == "live" and activeFailed == False: ##Cuts out entries that don't yet have their goal funded, but are still live
                    filteredEntriesNmbr += 1
                    continue
            
            print(f"[Project name]: {entry[nameIndex+7:blurbIndex-3]}")
            print(f"[Entry index]: {i+1} / {finalEntry}")
            print(f"[Project status]: {projectStatus.upper()}")
            print("\n")
            if printIndices == True:
                print(f"[Blurb index]: {blurbIndex}")
                print(f"[Goal index]: {goalIndex}")
            if printMoneys == True:

                print(f"[Goal money]: {goalMoney} {currency}")
                print(f"[Funded amount]: {fundedMoney} {currency}")
                print(f"[Goal reached]: {goalReached}")
            blurb = entry[blurbIndex+7:goalIndex-2]
            print(f"[Blurb]: \n{blurb}")
            print("-------------")
            print(f"Progress: {round((1+i)/finalEntry*100, 1)}%")
            print("\n")
            time.sleep(sleepTimer)
            dataSet.append([(entry[nameIndex+7:blurbIndex-3]), blurb, goalMoney, fundedMoney])
        except:
            print(f"[Entry {i+1} could not be processed, skipping...]")
            print("\n")
            print("-------------")
            print("\n")
            skippedEntriesNmbr += 1
            skippedEntries.append(i)
            pass
        
    return skippedEntries, skippedEntriesNmbr, filteredEntries, filteredEntriesNmbr

###Ending Commands
def endScrape(startTime: int, skippedEntries: list, skippedEntriesNmbr: int) -> int:
    """
    Prints the final status report of the scraping process, including the total time taken,
    the number of skipped entries, and the skipped entries themselves.

    Parameters:
    - startTime (int): The start time of the scraping process.
    - skippedEntries (list): A list of skipped entries.
    - skippedEntriesNmbr (int): The number of skipped entries.

    Returns:
    - int: Returns 1 if the function completes successfully.
    """
    endTime = time.time()
    totalTime = round(endTime - startTime, 2)
    print("Processing complete.")
    time.sleep(0.2)
    print("Printing final status report...")
    time.sleep(0.5)
    print(f"Total time taken:                  {totalTime} seconds")
    time.sleep(0.3)
    print(f"Skipped entries:                   {skippedEntries}")
    time.sleep(0.3)
    print(f"Number of skipped entries:         {skippedEntriesNmbr}")
    
    return 1


if __name__ == "__main__":
    scrapeFile(skippedEntriesNmbr, skippedEntries, filteredEntriesNmbr, filteredEntries, startEntry, finalEntry, sleepTimer)
    endScrape(startTime, skippedEntries, skippedEntriesNmbr)
    
##