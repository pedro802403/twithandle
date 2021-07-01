#  awk -F '\t' 'NR>1 {print $4;}' 41586_2021_3677_MOESM3_ESM.csv | sort | uniq > data.txt
 
from googlesearch import search
import re
import time

with open("data.txt") as f:

    for elt in f:
        request = '"{}" twitter'.format(elt)
        results = search(request, num_results=20)
        regex = re.compile("^https://twitter.com/(\w+).*$") # retrieve twitter urls  
        candidateUrls = set() # set to avoid duplicates
        for result in results:
            match = regex.match(result)
            if match:
                candidateUrls.add("@{}".format(match.group(1))) # group 1 should have handle in it
        print(elt)
        print(candidateUrls)
        print("---------------------")
        time.sleep(1)


