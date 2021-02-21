Repo for scraping website bias information from https://www.allsides.com

To scrape:

1. Run the command 
   ```
   $ sh update_mirror.sh
   ```
   This will update the `www.allsides.com` folder with current website information.

2. Run the command
   ```
   $ python3 generate_csv.py
   ```
   This will parse the files in the mirrored `www.allsides.com` folder into the `allsides.csv` file.
