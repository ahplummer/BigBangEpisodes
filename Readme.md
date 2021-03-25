# The Big Bang Theory Episodes


### What this is
* [JSON Entry](./episodes.json) for all episodes, scraped from [here](https://bigbangtheory.fandom.com/wiki/List_of_The_Big_Bang_Theory_episodes).

### To run
* Create a Virtualenv
```
python3 -m venv .venv
```
* Source it 
```
source .venv/bin/activate
```
* Install requirements via pip
```
pip install -r requirements.txt
```
* Run it, show to screen
```
python driver.py 
```
* Run it, save to file
```
python driver.py > episodes.json
```