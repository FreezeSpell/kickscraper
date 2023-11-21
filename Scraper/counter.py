###A very simple script that counts the number of entries in the databse.

fileLocation = "Python/Outreaching CB/Scraper/Kickstarter Oct 23.json"
# Test
search_word = 'blurb'
with open(fileLocation, "r") as f:
    data = f.read()
    total = data.count(search_word)

print(total)
