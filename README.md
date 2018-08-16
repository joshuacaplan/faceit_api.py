# Faceit_API.py
### A Faceit API wrapper for Python
Currently I only made a wrapper for the Faceit Data API, however I will continue to add more Faceit APIs

## Requirements
--------

`requests` - A python pacakge to handle API requests

`pip install -U requests`

-------------

`python 3.x` - You need to have Python 3 installed in order to use this


## Install

----

1. Clone the repo into the directory you want to use the class
2. Import the class like this:

```python
from faceit_api.faceit_data import FaceitData
```

3. Then use the class like this:

```python
# Auths with API key
faceit_data = FaceitData("API_KEY")

# Gets match details from Faceit API
match_details = faceit_data.match_details("match_id")

# Prints JSON data
for k, v in match_details.items():
    print("{}: {}".format(k, v))
```