import json
import requests

class FaceitData:
    """The Data API for Faceit"""
    def __init__(self, api_token):
        self.api_token = api_token 
        self.base_url = "https://open.faceit.com/data/v4"

        self.headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer {}'.format(self.api_token)
        }
    
    # Championships

    def championship_details(self, championship_id, game=None, organizer=None):
        """Retrieve championship details

        championship_id -- The ID of the championship
        game -- An entity name to expand in request (default is None, either is True or False)
        organizer -- An entity name to expand in request (default is None, either is True or False)
        """
        api_url = "{}/championships/{}".format(self.base_url, championship_id)

        if game is not None:
            if game is True:
                api_url += "?expanded=game"
        if organizer is not None:
            if game is None:
                if organizer is True:
                    api_url += "?expanded=organizer"

        res = requests.get(api_url, headers=self.headers)

        if res.status_code is 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            return None
    
    def championship_matches(self, championship_id, type_of_match="all", starting_item_position=0, return_items=20):
        """Championship match details

        Keyword arguments:
        championship_id -- The championship ID
        type_of_match -- Kind of matches to return. Can be all(default), upcoming, ongoing or past
        starting_item_position -- The starting item position (default 0)
        return_items -- The number of items to return (default 20)
        """
        api_url = "{}/championships/{}/matches?type={}&offset={}&limit={}".format(self.base_url, championship_id, type_of_match, starting_item_position, return_items)

        res = requests.get(api_url, headers=self.headers)
        if res.status_code is 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            return None

    def championship_subscriptions(self, championship_id, starting_item_position=0, return_items=10):
        """Retrieve all subscriptions of a championship

        Keyword arguments:
        championship_id -- The championship ID
        starting_item_position -- The starting item position (default 0)
        return_items -- The number of items to return (default 10)
        """

        api_url = "{}/championships/{}/subscriptions?offset={}&limit={}".format(self.base_url, championship_id, starting_item_position, return_items)

        res = requests.get(api_url, headers=self.headers)
        if res.status_code is 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            return None

    # Games

    def all_faceit_games(self, starting_item_position=0, return_items=20):
        """Retrieve details of all games on FACEIT

        Keyword arguments:
        starting_item_position -- The starting item position (default 0)
        return_items -- The number of items to return (default 20)
        """

        api_url = "{}/games?offset={}&limit={}".format(self.base_url, starting_item_position, return_items)

        res = requests.get(api_url, headers=self.headers)
        if res.status_code is 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            return None
    
    def game_details(self, game_id=None):
        """Retrieve game details

        Keyword arguments:
        game_id -- The id of the game
        """

        if game_id is None:
            print("You need to specify a game_id!")
        else:
            api_url = "{}/games/{}".format(self.base_url, game_id)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code is 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None
    
    def game_details_parent(self, game_id=None):
        """Retrieve the details of the parent game, if the game is region-specific.

        Keyword arguments:
        game_id -- The id of the game
        """
        
        if game_id is None:
            print("You need to specify a game_id!")
        else:
            api_url = "{}/games/{}/parent".format(self.base_url, game_id)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code is 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None
    
    # Hubs

    def hub_details(self, hub_id=None, game=None, organizer=None):
        """Retrieve hub details

        Keyword arguments:
        hub_id -- The id of the hub
        game -- An entity to expand in request (default is None, but can be True)
        organizer -- An entity to expand in request (default is None, but can be True)
        """

        if hub_id is None:
            print("You need to specify a hub ID!")
        else:
            api_url = "{}/hubs/{}".format(self.base_url, hub_id)
            if game is not None:
                if game is True:
                    api_url += "?expanded=game"
            if organizer is not None:
                if game is None:
                    if organizer is True:
                        api_url += "?expanded=organizer"
            
            res = requests.get(api_url, headers=self.headers)
            if res.status_code is 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None
    
    def hub_matches(self, hub_id, type_of_match="all", starting_item_position=0, return_items=20):
        """Retrieve all matches of a hub

        Keyword arguments:
        hub_id -- The ID of the hub
        type_of_match -- Kind of matches to return. Default is all, can be upcoming, ongoing, or past
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        api_url = "{}/hubs/{}/matches?type={}&offset={}&limit={}".format(self.base_url, hub_id, type_of_match, starting_item_position, return_items)

        res = requests.get(api_url, headers=self.headers)
        if res.status_code is 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            return None

    def hub_members(self, hub_id, starting_item_position=0, return_items=20):
        """Retrieve all members of a hub

        Keyword arguments:
        hub_id -- The ID of the hub
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        api_url = "{}/hubs/{}/members?offset={}&limit={}".format(self.base_url, hub_id, starting_item_position, return_items)

        res = requests.get(api_url, headers=self.headers)
        if res.status_code is 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            return None
    
    def hub_roles(self, hub_id, starting_item_position=0, return_items=20):
        """Retrieve all roles members can have in a hub

        Keyword arguments:
        hub_id -- The ID of the hub
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        api_url = "{}/hubs/{}/roles?offset={}&limit={}".format(self.base_url, hub_id, starting_item_position, return_items)

        res = requests.get(api_url, headers=self.headers)
        if res.status_code is 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            return None

    def hub_statistics(self, hub_id, starting_item_position=0, return_items=20):
        """Retrieves statistics of a hub

        Keyword arguments:
        hub_id -- The ID of the hub
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        api_url = "{}/hubs/{}/stats?offset={}&limit={}".format(self.base_url, hub_id, starting_item_position, return_items)


        res = requests.get(api_url, headers=self.headers)
        if res.status_code is 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            return None

    # Leaderboards

    def championship_leaderboards(self, championship_id=None, starting_item_position=0, return_items=20):
        """Retrieves all leaderboards of a championship

        Keyword arguments:
        championship_id -- The ID of a championship
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        if championship_id is None:
            print("The championship ID cannot be nothing!")
        else:
            api_url = "{}/leaderboards/championships/{}?offset={}&limit={}".format(self.base_url, championship_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code is 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None
    
    def championship_group_ranking(self, championship_id=None, group=None, starting_item_position=0, return_items=20):
        """Retrieve group ranking of a championship

        Keyword arguments:
        championship_id -- The ID of a championship
        group -- A group of the championship
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        if championship_id is None:
            print("The championship ID cannot be nothing!")
        else:
            if group is None:
                print("The group cannot be nothing!")
            else:
                api_url = "{}/leaderboards/championships/{}/groups/{}?offset={}&limit={}".format(self.base_url, championship_id, group, starting_item_position, return_items)

                res = requests.get(api_url, headers=self.headers)
                if res.status_code is 200:
                    return json.loads(res.content.decode('utf-8'))
                else:
                    return None
    
    def hub_leaderboards(self, hub_id=None, starting_item_position=0, return_items=20):
        """Retrieve all leaderboards of a hub

        Keyword arguments:
        hub_id -- The ID of the hub
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        if hub_id is None:
            print("The hub_id cannot be nothing!")
        else:
            api_url = "{}/leaderboards/hubs/{}?offset={}&limit={}".format(self.base_url, hub_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code is 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def hub_ranking(self, hub_id=None, starting_item_position=0, return_items=20):
        """Retrieve all time ranking of a hub

        Keyword arguments:
        hub_id -- The ID of the hub
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        if hub_id is None:
            print("The hub_id cannot be nothing!")
        else:
            api_url = "{}/leaderboards/hubs/{}/general?offset={}&limit={}".format(self.base_url, hub_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code is 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None
    
    def hub_season_ranking(self, hub_id=None, season=None, starting_item_position=0, return_items=20):
        """Retrieve seasonal ranking of a hub

        Keyword arguments:
        hub_id -- The ID of the hub
        season -- A season of the hub
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        if hub_id is None:
            print("The hub_id cannot be nothing!")
        else:
            if season is None:
                print("The season cannot be nothing!")
            else:
                api_url = "{}/leaderboards/hubs/{}/seasons/{}?offset={}&limit={}".format(self.base_url, hub_id, season, starting_item_position, return_items)

                res = requests.get(api_url, headers=self.headers)
                if res.status_code is 200:
                    return json.loads(res.content.decode('utf-8'))
                else:
                    return None

    def leaderboard_ranking(self, leaderboard_id=None, starting_item_position=0, return_items=20):
        """Retrieve ranking from a leaderboard id

        Keyword arguments:
        leaderboard_id -- The ID of the leaderboard
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        if leaderboard_id is None:
            print("The leaderboard_id cannot be nothing!")
        else:
            api_url = "{}/leaderboards/{}?offset={}&limit={}".format(self.base_url, leaderboard_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code is 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None
    
    # Matches

    def match_details(self, match_id=None):
        """Retrieve match details

        Keyword arguments:
        match_id -- The ID of the match
        """

        if match_id is None:
            print("match_id cannot be nothing")
        else:
            api_url = "{}/matches/{}".format(self.base_url, match_id)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code is 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def match_stats(self, match_id=None):
        """Retrieve match details

        Keyword arguments:
        match_id -- The ID of the match
        """

        if match_id is None:
            print("match_id cannot be nothing")
        else:
            api_url = "{}/matches/{}/stats".format(self.base_url, match_id)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code is 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None
    
    # Organizers

    def organizer_details(self, name_of_organizer=None, organizer_id=None):
        """Retrieve organizer details

        Keyword arguments:
        name_of_organizer -- The name of organizer (use either this or the the organizer_id)
        organizer_id -- The ID of the organizer (use either this or the name_of_organizer)
        """

        if name_of_organizer is None:
            if organizer_id is None:
                print("You cannot have the name_of_organizer or the organizer_id set to None! Please choose one!")
            else:
                api_url = "{}/organizers"

                if name_of_organizer is not None:
                    api_url += "?name={}".format(name_of_organizer)
                else:
                    if organizer_id is not None:
                        api_url +="/{}".format(organizer_id)
                res = requests.get(api_url, headers=self.headers)
                if res.status_code is 200:
                    return json.loads(res.content.decode('utf-8'))
                else:
                    return None
    
    def organizer_championships(self, organizer_id=None, starting_item_position=0, return_items=20):
        """Retrieve all championships of an organizer

        Keyword arguments:
        organizer_id -- The ID of the organizer
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        if organizer_id is None:
            print("You cannot have organizer_id set to nothing!")
        else:
            api_url = "{}/organizers/{}/championships?offset={}&limit={}".format(self.base_url, organizer_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code is 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None
    
    def organizer_games(self, organizer_id=None):
        """Retrieve all games an organizer is involved with.

        Keyword arguments:
        organizer_id -- The ID of the organizer
        """

        if organizer_id is None:
            print("You cannot have organizer_id set to nothing!")
        else:
            api_url = "{}/organizers/{}/games".format(self.base_url, organizer_id)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code is 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None
    
    def organizer_hubs(self, organizer_id=None, starting_item_position=0, return_items=20):
        """Retrieve all hubs of an organizer

        Keyword arguments:
        organizer_id -- The ID of the organizer
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        if organizer_id is None:
            print("You cannot have the organizer_id set to nothing!")
        else:
            api_url = "{}/organizers/{}/hubs?offset={}&limit={}".format(self.base_url, organizer_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code is 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None
    
    def organizer_tournaments(self, organizer_id=None, type_of_tournament="upcoming", starting_item_position=0, return_items=20):
        """Retrieve all tournaments of an organizer

        Keyword arguments:
        organizer_id -- The ID of the organizer
        type_of_tournament -- Kind of tournament. Can be upcoming(default) or past
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        if organizer_id is None:
            print("You cannot have the organizer_id set to nothing!")
        else:
            api_url = "{}/organizers/{}/tournaments?type={}&offset={}&limit={}".format(self.base_url, organizer_id, type_of_tournament, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code is 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None
    
    # Players

    def player_details(self, nickname=None, game=None, game_player_id=None):
        """Retrieve player details

        Keyword arguments:
        nickname -- The nickname of the player of Faceit
        game -- A game on Faceit
        game_player_id -- The ID of a player on a game's platform
        """

        api_url = "{}/players".format(self.base_url)
        if nickname is not None:
            api_url += "?nickname={}".format(nickname)
        if game_player_id is not None:
            if nickname is not None:
                api_url += "&game_player_id={}".format(game_player_id)
            else:
                api_url += "?game_player_id={}".format(game_player_id)
        if game is not None:
            api_url += "&game={}".format(game)
        
        print(api_url)
        res = requests.get(api_url, headers=self.headers)
        if res.status_code is 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            return None

    # TODO: The rest of Players category, Rankings category, Search category, Teams category, and Tournaments category