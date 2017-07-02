# Warframe Drop Chance Calculator

## Usage
To query the percentage drop chance of an item:
```bash
$ python3 query.py
> Rage
Interpreting as "Rage"
 Infested Mesa       : 0.6%
 Chroma              : 0.6%
 Tenno Specter       : 0.6%
 Napalm              : 0.0603%
 Kuva Napalm         : 0.0603%
```
### Updating Database
To update the database of (currently only mods) from [the official Warframe drop table list](http://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html):
```bash
$ python3 update.py
Downloading page...    done.
Parsing...             done.
Extracting mod info... done.
Writing to file...     done.
finished.
```
