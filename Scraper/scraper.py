import json
import datetime as dt

file = open("test_entry.json")
data = json.load(file)
time_run = dt.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
json_file = f"output_{time_run}.json"
outfile = open(json_file, "a+")

def getData(entry: dict) -> tuple:
    id = entry['data']['id']
    slug = entry['data']['slug']
    blurb = entry['data']['blurb']
    category = entry['data']['category']['slug']
    goal = entry['data']['goal']
    pledged = entry['data']['pledged']
    currency = entry['data']['currency']
    url = entry['data']['urls']['web']['project']
    return id, slug, blurb, category, goal, pledged, currency, url

def main(outfile = outfile, data: dict = data, startEntry: int = 0, finalEntry: int = 1):
    for i in range(startEntry, finalEntry):
        if i < len(data):
            id, slug, blurb, category, goal, pledged, currency, url = getData(data[i])
            blurbLength = len(blurb.split( ))
            slugLength = len(slug.split( ))
            cleanEntry = {
                "ID": id,
                "Slug": slug,
                "Slug Length": slugLength,
                "Blurb": blurb,
                "Blurb Length": blurbLength,
                "Category": category,
                "Goal": goal,
                "Pledged": pledged,
                "Currency": currency,
                "URL": url
            }
        json_object = json.dumps(cleanEntry)
        outfile.write(json_object)
        
if __name__ == "__main__":
    main()

        
    

# What do I want this to do?
# Take dataset, print every entry in a range in the dataset, but only
# specific parts of the entry.

# What I need to print:
# slug, blurb, goal, pledged, currency, kickstarter ID, kickstarter URL