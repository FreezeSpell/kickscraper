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