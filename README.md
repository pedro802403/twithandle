# twithandle

The code uses the [google search module](https://pypi.org/project/googlesearch-python/). May be wise to use a virtual environment.

```bash
  python3 -m pip install googlesearch-python
```

The workflow I used : export xls file to CSV, extract the contents of the ?3rd? column into `data.txt` using the awk command and `sort | uniq` remove duplicate entries.

```bash
  awk -F '\t' 'NR>1 {print $4;}' 41586_2021_3677_MOESM3_ESM.csv | sort | uniq > data.txt
```
I may try different google search patterns (e.g. site:twitter.com).

The code is rather crude, I didn't test it on the whole set, and it may be necessarry to split the execution or use "adequate" sleep times to keep Google "calm" 😅.  
