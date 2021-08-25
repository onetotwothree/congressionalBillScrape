import requests
import time
from bs4 import BeautifulSoup
import re
MOST_RECENT_BILL = 2712
LAST_BILL_TO_COLLECT = MOST_RECENT_BILL - 10
BILL_CHECK = ["A", "BILL"]
START_OF_NAME = "Sen."
resultsPages = "" 
start_time = time.time()

for i in range(LAST_BILL_TO_COLLECT, MOST_RECENT_BILL):
    URL = "https://www.congress.gov/bill/117th-congress/senate-bill/" + str(i) + "/text?r=1&s=9&format=txt"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    authordiv = soup.find("div", {"class": "overview"})
    authordiv = str(authordiv)
    authorIndex = authordiv.find(START_OF_NAME)
    authorEnd = authordiv.find("]", authorIndex)
    author = str(authordiv)[authorIndex:authorEnd + 1]
    results = soup.find(id="billTextContainer") #Find bill text and clean
    results = results.get_text()
    results = results.split()
    results.remove("<all>")
    results = " ".join(results)
    index = results.find("_______________________________________________________________________ A BILL")    
    results = results[index:]
    results = results.replace("_______________________________________________________________________ A BILL ", "")
    """results = results.lower()
    results = re.sub(r"[^A-Za-z0-9^,!?.\/'+]", " ", results)
    results = re.sub(r"\+", " plus ", results)
    results = re.sub(r",", " ", results)
    results = re.sub(r"\.", " ", results)
    results = re.sub(r"!", " ! ", results)
    results = re.sub(r"\?", " ? ", results)
    results = re.sub(r"'", " ", results)
    results = re.sub(r":", " : ", results)
    results = re.sub(r"\s{2,}", " ", results)
    results = results.split()"""
    print("Got item: " + str(i) + "\n")
    resultsPages += "Sponsor: " + author + "\n" + str(str(i) + ". " + results + "\n\n") #Store all cleaned info in this variable

print(resultsPages)
print("--- %s seconds ---" % (time.time() - start_time))