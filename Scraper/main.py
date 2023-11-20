###Settings
fileLocation = "Academics-Antics/Python/Outreaching CB/Scraper/Kickstarter Oct 23.json"
startEntry = 0 #The first entry in the list to start from
finalEntry = 100000 #The last entry in the list to finish
sleepTimer = 0.01 #The amount of time to sleep between each entry
printIndices = False #Print the blurb index and goal index for each entry
printMoneys = True #Print the goal money and funded amount for each entry
setFilter = True #Filter out entries that don't meet the requirements

###Filters
goalFunded = True #Only show entries that have their goal funded
goalNotFunded = False #Only show entries that don't have their goal funded
activeFailed = True #Count active entries not yet funded as failed

###Imports
import time

###Starting Commands
startTime = time.time()
dataSet = []

print("Initialising database...")
time.sleep(2)
data = open(fileLocation)
print("Database initialised.")
time.sleep(1)

print("Accessing database...")
listdata = data.readlines()
print("Database accessed.")

time.sleep(1)

print(f"[Starting Entry]: {startEntry}")
print(f"[Final Entry]: {finalEntry}")

time.sleep(2)

skippedEntriesNmbr = 0
skippedEntries = []
filteredEntriesNmbr = 0
filteredEntries = []

if goalFunded == True and goalNotFunded == True and setFilter == True:
    print("Too many filters active, no results will be printed.")

print(f"Commencing scraping of {finalEntry-startEntry} entries...")
time.sleep(5)

###Looping through the set of entries
for i in range(startEntry, finalEntry):
    entry = listdata[i]
    n = listdata[i].index("blurb")
    o = listdata[i].index("goal")
    p = listdata[i].index("name")
    q = listdata[i].index("pledged")
    r = listdata[i].index("state")
    s = listdata[i].index("currency")
    t = listdata[i].index("currency_symbol")
    u = listdata[i].index("state")
    v = listdata[i].index("slug")
    try:
        goalMoney = entry[o+6:q-2]
        fundedMoney = entry[q+9:r-2]
        goalMoney = int(round(float(goalMoney)))
        fundedMoney = int(round(float(fundedMoney)))
        currency = entry[s+11:t-3]
        projectStatus = entry[u+8:v-3]

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
        
        print(f"[Project name]: {entry[p+7:n-3]}")
        print(f"[Entry index]: {i+1} / {finalEntry}")
        print(f"[Project status]: {projectStatus.upper()}")
        print("\n")
        if printIndices == True:
            print(f"[Blurb index]: {n}")
            print(f"[Goal index]: {o}")
        if printMoneys == True:

            print(f"[Goal money]: {goalMoney} {currency}")
            print(f"[Funded amount]: {fundedMoney} {currency}")
            print(f"[Goal reached]: {goalReached}")
        blurb = entry[n+7:o-2]
        print(f"[Blurb]: \n{blurb}")
        print("-------------")
        print(f"Progress: {round((1+i)/finalEntry*100, 1)}%")
        print("\n")
        time.sleep(sleepTimer)
        dataSet.append([(entry[p+7:n-3]), blurb, goalMoney, fundedMoney])
    except:
        print(f"[Entry {i+1} could not be processed, skipping...]")
        print("\n")
        print("-------------")
        print("\n")
        skippedEntriesNmbr += 1
        skippedEntries.append(i)
        pass



###Ending Commands
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
