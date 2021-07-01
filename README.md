# twithandle

The workflow I used : export xls file to CSV, extract the contents of the ?3rd? column into `data.txt` using the awk command and `sort | uniq` remove duplicate entries.

```bash
  awk -F '\t' 'NR>1 {print $4;}' 41586_2021_3677_MOESM3_ESM.csv | sort | uniq > data.txt
```
I may try different google search patterns (e.g. site:twitter.com).
