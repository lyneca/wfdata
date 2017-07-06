# Warframe Drop Chance Calculator

## Usage
To query the percentage drop chance of an item:
```bash
$ python3 query.py
> Tempo Ro 
Interpreting as "Tempo Royale"
Sedna/Vodyanoi (Arena)..................: 0.25%
Sedna/Yam (Arena).......................: 0.25%
Isolator Bursa..........................: 0.0603%
```
### Updating Database
To update the database of (currently only mods) from [the official Warframe drop table list](http://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html):
```bash
$ python3 update.py
Starting update. This might take a while; we're parsing a lot of HTML here.
Downloading page...    done.
Parsing...             done.
Extracting mods... done.
Writing to file...     done.
Extracting missions... done.
Writing to file...     done.
Finished.
```
`update.py` hashes and saves the data, and will only reparse and save if the data has changed.

More importantly, it will also save a dated backup whenever the site has changed since it was last run. I have mine set up on a cron job to check and backup every day, and I'll be committing changes whenever I see them.

### Requirements
- Python 3.6 or higher
- `fuzzywuzzy <https://github.com/seatgeek/fuzzywuzzy/>`_
- `beutifulsoup <https://pypi.python.org/pypi/beautifulsoup4https://pypi.python.org/pypi/beautifulsoup4/>`_
