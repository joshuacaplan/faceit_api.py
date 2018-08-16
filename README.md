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

## Usage
---

### "It outputted an object inside of an object, how do I access it?"

`faceit_data.all_faceit_games()` will return something like this:

```json
{
    "items": [
        {
            "assets": {
                "cover": "string",
                "featured_img_l": "string",
                "featured_img_m": "string",
                "featured_img_s": "string",
                "flag_img_icon": "string",
                "flag_img_l": "string",
                "flag_img_m": "string",
                "flag_img_s": "string",
                "landing_page": "string"
            },
            "game_id": "string",
            "long_label": "string",
            "order": 0,
            "parent_game_id": "string",
            "platforms": [
                "string"
            ],
            "regions": [
                "string"
            ],
            "short_label": "string"
        }
    ],
}
```

```python
# This will return an item called items which the value is an array with even more objects in it
all_games = faceit.data.all_faceit_games()

# In order to access the first game inside of the items array: "tf2" we need to do something like this:

print(all_games['items'][0]['game_id'])

# The above code will access the items array, then acess the first object in the array, and then access the first value inside of the object which is inside the first position of the array.
```