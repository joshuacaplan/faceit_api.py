import json
import requests

import urllib.parse


class FaceitData:
    """The Data API for Faceit"""

    def __init__(self, api_token):
        """Contructor
        Keyword arguments:
        api_token -- The api token used for the Faceit API (either client or server API types)
        """

        self.api_token = api_token
        self.base_url = 'https://open.faceit.com/data/v4'

        self.headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer {}'.format(self.api_token)
        }

    # Championships

    def championship_details(self, championship_id=None, expanded=None):
        """Retrieve championship details
        championship_id -- The ID of the championship
        expanded -- List of entity names to expand in request, either "organizer" or "game"
        """

        if championship_id is None:
            print("The championship_id of championship_details() cannot be nothing!")
        else:
            api_url = "{}/championships/{}".format(self.base_url, championship_id)

            if expanded is not None:
                if expanded.lower() == 'game':
                    api_url += '?expanded=game'
                elif expanded.lower() == 'organizer':
                    api_url += '?expanded=organizer'

            res = requests.get(api_url, headers=self.headers)

            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def championship_matches(self, championship_id=None, type_of_match="all", starting_item_position=0,
                             return_items=20):
        """Championship match details
        Keyword arguments:
        championship_id -- The championship ID
        type_of_match -- Kind of matches to return. Can be all(default), upcoming, ongoing or past
        starting_item_position -- The starting item position (default 0)
        return_items -- The number of items to return (default 20)
        """

        if championship_id is None:
            print("The championship_id of championship_matches() cannot be nothing!")
        else:
            api_url = "{}/championships/{}/matches?type={}&offset={}&limit={}".format(
                self.base_url, championship_id, type_of_match, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def championship_subscriptions(self, championship_id=None, starting_item_position=0, return_items=10):
        """Retrieve all subscriptions of a championship
        Keyword arguments:
        championship_id -- The championship ID
        starting_item_position -- The starting item position (default 0)
        return_items -- The number of items to return (default 10)
        """

        if championship_id is None:
            print("The championship_id of championship_subscriptions() cannot be nothing!")
        else:
            api_url = "{}/championships/{}/subscriptions?offset={}&limit={}".format(
                self.base_url, championship_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
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

        api_url = "{}/games?offset={}&limit={}".format(
            self.base_url, starting_item_position, return_items)

        res = requests.get(api_url, headers=self.headers)
        if res.status_code == 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            return None

    def game_details(self, game_id=None):
        """Retrieve game details
        Keyword arguments:
        game_id -- The id of the game
        """

        if game_id is None:
            print("You need to specify a game_id in game_details()!")
        else:
            api_url = "{}/games/{}".format(self.base_url, game_id)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def game_details_parent(self, game_id=None):
        """Retrieve the details of the parent game, if the game is region-specific.
        Keyword arguments:
        game_id -- The id of the game
        """

        if game_id is None:
            print("You need to specify a game_id in game_details_parent!")
        else:
            api_url = "{}/games/{}/parent".format(self.base_url, game_id)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
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
            print("You need to specify a hub ID in hub_details()!")
        else:
            api_url = "{}/hubs/{}".format(self.base_url, hub_id)
            if game is not None:
                if game is True:
                    api_url += "?expanded=game"
            if organizer != None:
                if game == None:
                    if organizer == True:
                        api_url += "?expanded=organizer"

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def hub_matches(self, hub_id=None, type_of_match="all", starting_item_position=0, return_items=20):
        """Retrieve all matches of a hub
        Keyword arguments:
        hub_id -- The ID of the hub (required)
        type_of_match -- Kind of matches to return. Default is all, can be upcoming, ongoing, or past
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        if hub_id == None:
            print("The hub_id of hub_matches() cannot be nothing!")
        else:
            api_url = "{}/hubs/{}/matches?type={}&offset={}&limit={}".format(
                self.base_url, hub_id, type_of_match, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def hub_members(self, hub_id=None, starting_item_position=0, return_items=20):
        """Retrieve all members of a hub
        Keyword arguments:
        hub_id -- The ID of the hub (required)
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        if hub_id == None:
            print("The hub_id of hub_members() cannot be nothing!")
        else:
            api_url = "{}/hubs/{}/members?offset={}&limit={}".format(
                self.base_url, hub_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def hub_roles(self, hub_id=None, starting_item_position=0, return_items=20):
        """Retrieve all roles members can have in a hub
        Keyword arguments:
        hub_id -- The ID of the hub
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        if hub_id is None:
            print("The hub_id of hub_roles() cannot be nothing!")
        else:
            api_url = "{}/hubs/{}/roles?offset={}&limit={}".format(
                self.base_url, hub_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def hub_statistics(self, hub_id=None, starting_item_position=0, return_items=20):
        """Retrieves statistics of a hub
        Keyword arguments:
        hub_id -- The ID of the hub
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        if hub_id is None:
            print("The hub_id of hub_statistics() cannot be nothing!")
        else:
            api_url = "{}/hubs/{}/stats?offset={}&limit={}".format(
                self.base_url, hub_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
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

        if championship_id == None:
            print("The championship ID cannot be nothing!")
        else:
            api_url = "{}/leaderboards/championships/{}?offset={}&limit={}".format(
                self.base_url, championship_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
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

        if championship_id == None:
            print("The championship ID cannot be nothing!")
        else:
            if group == None:
                print("The group cannot be nothing!")
            else:
                api_url = "{}/leaderboards/championships/{}/groups/{}?offset={}&limit={}".format(
                    self.base_url, championship_id, group, starting_item_position, return_items)

                res = requests.get(api_url, headers=self.headers)
                if res.status_code == 200:
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

        if hub_id == None:
            print("The hub_id cannot be nothing!")
        else:
            api_url = "{}/leaderboards/hubs/{}?offset={}&limit={}".format(
                self.base_url, hub_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
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

        if hub_id == None:
            print("The hub_id cannot be nothing!")
        else:
            api_url = "{}/leaderboards/hubs/{}/general?offset={}&limit={}".format(
                self.base_url, hub_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
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

        if hub_id == None:
            print("The hub_id cannot be nothing!")
        else:
            if season == None:
                print("The season cannot be nothing!")
            else:
                api_url = "{}/leaderboards/hubs/{}/seasons/{}?offset={}&limit={}".format(
                    self.base_url, hub_id, season, starting_item_position, return_items)

                res = requests.get(api_url, headers=self.headers)
                if res.status_code == 200:
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

        if leaderboard_id == None:
            print("The leaderboard_id cannot be nothing!")
        else:
            api_url = "{}/leaderboards/{}?offset={}&limit={}".format(
                self.base_url, leaderboard_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    # Matches

    def match_details(self, match_id=None):
        """Retrieve match details
        Keyword arguments:
        match_id -- The ID of the match
        """

        if match_id == None:
            print("match_id cannot be nothing")
        else:
            api_url = "{}/matches/{}".format(self.base_url, match_id)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def match_stats(self, match_id=None):
        """Retrieve match details
        Keyword arguments:
        match_id -- The ID of the match
        """

        if match_id == None:
            print("match_id cannot be nothing")
        else:
            api_url = "{}/matches/{}/stats".format(self.base_url, match_id)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
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

        if name_of_organizer == None:
            if organizer_id == None:
                print(
                    "You cannot have the name_of_organizer or the organizer_id set to None! Please choose one!")
            else:
                api_url = "{}/organizers"

                if name_of_organizer != None:
                    api_url += "?name={}".format(name_of_organizer)
                else:
                    if organizer_id != None:
                        api_url += "/{}".format(organizer_id)
                res = requests.get(api_url, headers=self.headers)
                if res.status_code == 200:
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

        if organizer_id == None:
            print("You cannot have organizer_id set to nothing!")
        else:
            api_url = "{}/organizers/{}/championships?offset={}&limit={}".format(
                self.base_url, organizer_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def organizer_games(self, organizer_id=None):
        """Retrieve all games an organizer is involved with.
        Keyword arguments:
        organizer_id -- The ID of the organizer
        """

        if organizer_id == None:
            print("You cannot have organizer_id set to nothing!")
        else:
            api_url = "{}/organizers/{}/games".format(
                self.base_url, organizer_id)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
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

        if organizer_id == None:
            print("You cannot have the organizer_id set to nothing!")
        else:
            api_url = "{}/organizers/{}/hubs?offset={}&limit={}".format(
                self.base_url, organizer_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def organizer_tournaments(self, organizer_id=None, type_of_tournament="upcoming", starting_item_position=0,
                              return_items=20):
        """Retrieve all tournaments of an organizer
        Keyword arguments:
        organizer_id -- The ID of the organizer
        type_of_tournament -- Kind of tournament. Can be upcoming(default) or past
        starting_item_position -- The starting item position. Default is 0
        return_items -- The number of items to return. Default is 20
        """

        if organizer_id == None:
            print("You cannot have the organizer_id set to nothing!")
        else:
            api_url = "{}/organizers/{}/tournaments?type={}&offset={}&limit={}".format(
                self.base_url, organizer_id, type_of_tournament, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
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
        if nickname != None:
            api_url += "?nickname={}".format(nickname)
        if game_player_id != None:
            if nickname != None:
                api_url += "&game_player_id={}".format(game_player_id)
            else:
                api_url += "?game_player_id={}".format(game_player_id)
        if game != None:
            api_url += "&game={}".format(game)

        # print(api_url)
        res = requests.get(api_url, headers=self.headers)
        if res.status_code == 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            return None

    def player_id_details(self, player_id=None):
        """Retrieve player details
        Keyword arguments:
        player_id -- The ID of the player
        """

        if player_id == None:
            print("The player_id cannot be nothing!")
        else:
            api_url = "{}/players/{}".format(self.base_url, player_id)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def player_matches(self, player_id=None, game=None, from_timestamp=None, to_timestamp=None,
                       starting_item_position=0, return_items=20):
        """Retrieve all matches of a player
        Keyword arguments:
        player_id -- The ID of a player
        game -- A game on Faceit
        from_timestamp -- The timestamp (UNIX time) as a lower bound of the query. 1 month ago if not specified
        to_timestamp -- The timestamp (UNIX time) as a higher bound of the query. Current timestamp if not specified
        starting_item_position -- The starting item position (Default is 0)
        return_items -- The number of items to return (Default is 20)
        """

        if player_id == None:
            print("The player_id cannot be nothing!")
        else:
            if game == None:
                print("The game cannot be nothing!")
            else:
                api_url = "{}/players/{}/history".format(self.base_url, player_id)
                if from_timestamp == None:
                    if to_timestamp == None:
                        api_url += "?game={}&offset={}&limit={}".format(
                            game, starting_item_position, return_items)
                    else:
                        api_url += "?to={}".format(to_timestamp)
                else:
                    api_url += "?from={}".format(from_timestamp)

                res = requests.get(api_url, headers=self.headers)
                if res.status_code == 200:
                    return json.loads(res.content.decode('utf-8'))
                else:
                    return None

    def player_hubs(self, player_id=None, starting_item_position=0, return_items=20):
        """Retrieve all hubs of a player
        Keyword arguments:
        player_id -- The ID of a player
        starting_item_position -- The starting item position (Default is 0)
        return_items -- The number of items to return (Default is 20)
        """

        if player_id == None:
            print("The player_id cannot be nothing!")
        else:
            api_url = "{}/players/{}/hubs?offset={}&limit={}".format(
                self.base_url, player_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def player_stats(self, player_id=None, game_id=None):
        """Retrieve the statistics of a player
        Keyword arguments:
        player_id -- The ID of a player
        game_id -- A game on Faceit
        """

        if player_id == None:
            print("The player_id cannot be nothing!")
        else:
            if game_id == None:
                print("The game_id cannot be nothing!")
            else:
                api_url = "{}/players/{}/stats/{}".format(
                    self.base_url, player_id, game_id)

                res = requests.get(api_url, headers=self.headers)
                if res.status_code == 200:
                    return json.loads(res.content.decode('utf-8'))
                else:
                    return None

    def player_tournaments(self, player_id=None, starting_item_position=0, return_items=20):
        """Retrieve all hubs of a player
        Keyword arguments:
        player_id -- The ID of a player
        starting_item_position -- The starting item position (Default is 0)
        return_items -- The number of items to return (Default is 20)
        """

        if player_id == None:
            print("The player_id cannot be nothing!")
        else:
            api_url = "{}/players/{}/tournaments?offset={}&limit={}".format(
                self.base_url, player_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    # Rankings

    def game_global_ranking(self, game_id=None, region=None, country=None, starting_item_position=0, return_items=20):
        """Retrieve global ranking of a game
        Keyword arguments:
        game_id -- The ID of a game (Required)
        region -- A region of a game (Required)
        country -- A country code (ISO 3166-1)
        starting_item_position -- The starting item position (Default is 0)
        return_items -- The number of items to return (Default is 20)
        """

        if game_id == None:
            print("The game_id cannot be nothing!")
        else:
            if region == None:
                print("The region cannot be nothing!")
            else:
                api_url = "{}/rankings/games/{}/regions/{}".format(
                    self.base_url, game_id, region)
                if country != None:
                    api_url += "?country={}&offset={}&limit={}".format(
                        country, starting_item_position, return_items)
                else:
                    api_url += "?offset={}&limit={}".format(
                        starting_item_position, return_items)

                res = requests.get(api_url, headers=self.headers)
                if res.status_code == 200:
                    return json.loads(res.content.decode('utf-8'))
                else:
                    return None

    def player_ranking_of_game(self, game_id=None, region=None, player_id=None, country=None, return_items=20):
        """Retrieve user position in the global ranking of a game
        Keyword arguments:
        game_id -- The ID of a game (required)
        region -- A region of a game (required)
        player_id -- The ID of a player (required)
        country -- A country code (ISO 3166-1)
        return_items -- The number of items to return (default is 20)
        """

        if game_id == None:
            print("The game_id cannot be nothing!")
        else:
            if region == None:
                print("The region cannot be nothing!")
            else:
                if player_id == None:
                    print("The player_id cannot be nothing!")
                else:
                    api_url = "{}/rankings/games/{}/regions/{}/players/{}".format(
                        self.base_url, game_id, region, player_id)

                    if country != None:
                        api_url += "?country={}&limit={}".format(
                            country, return_items)
                    else:
                        api_url += "?limit={}".format(return_items)

                    res = requests.get(api_url, headers=self.headers)
                    if res.status_code == 200:
                        return json.loads(res.content.decode('utf-8'))
                    else:
                        return None

    # Search

    def search_championships(self, name_of_championship=None, game=None, region=None, type_of_competition="all",
                             starting_item_position=0, return_items=20):
        """Search for championships
        Keyword arguments:
        name_of_championship -- The name of a championship on Faceit (required)
        game -- A game on Faceit
        region -- A region of the game
        type_of_competition -- Kind of competitions to return (default is all, can be upcoming, ongoing, or past)
        starting_item_position -- The starting item position (Default is 0)
        return_items -- The number of items to return (Default is 20)
        """
        if name_of_championship == None:
            print("The name of the championship cannot be nothing!")
        else:
            api_url = "{}/search/championships?name={}&type={}&offset={}&limit={}".format(self.base_url,
                                                                                          urllib.parse.quote_plus(
                                                                                              name_of_championship),
                                                                                          type_of_competition,
                                                                                          starting_item_position,
                                                                                          return_items)

            if game != None:
                api_url += "&game={}".format(game)
            elif region != None:
                api_url += "&region={}".format(region)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def search_hubs(self, name_of_hub=None, game=None, region=None, starting_item_position=0, return_items=20):
        """Search for hubs
        Keyword arguments:
        name_of_hub -- The name of a hub on Faceit (required)
        game -- A game on Faceit
        region -- A region of the game
        starting_item_position -- The starting item position (Default is 0)
        return_items -- The number of items to return (Default is 20)
        """

        if name_of_hub == None:
            print("The name_of_hub cannot be nothing!")
        else:
            api_url = "{}/search/hubs?name={}&offset={}&limit={}".format(
                self.base_url, urllib.parse.quote_plus(name_of_hub), starting_item_position, return_items)

            if game != None:
                api_url += "&game={}".format(game)
            elif region != None:
                api_url += "&region={}".format(region)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def search_organizers(self, name_of_organizer=None, starting_item_position=0, return_items=20):
        """Search for organizers
        Keyword arguments:
        name_of_organizer -- The name of an organizer on Faceit
        starting_item_position -- The starting item position (Default is 0)
        return_items -- The number of items to return (Default is 20)
        """

        if name_of_organizer == None:
            print("The name of the organizer cannot be nothing!")
        else:
            api_url = "{}/search/organizers?name={}&offset={}&limit={}".format(
                self.base_url, urllib.parse.quote_plus(name_of_organizer), starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def search_players(self, nickname=None, game=None, country_code=None, starting_item_position=0, return_items=20):
        """Search for players
        Keyword arguments:
        nickname -- The nickname of a player on Faceit (required)
        game -- A game on Faceit
        country_code -- A country code (ISO 3166-1)
        starting_item_position -- The starting item position (Default is 0)
        return_items -- The number of items to return (Default is 20)
        """

        if nickname == None:
            print("The nickname cannot be nothing!")
        else:
            api_url = "{}/search/players?nickname={}&offset={}&limit={}".format(
                self.base_url, urllib.parse.quote_plus(nickname), starting_item_position, return_items)

            if game != None:
                api_url += "&game={}".format(urllib.parse.quote_plus(game))
            elif country_code != None:
                api_url += "&country={}".format(country_code)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def search_teams(self, nickname=None, game=None, starting_item_position=0, return_items=20):
        """Search for teams
        Keyword arguments:
        nickname -- The nickname of a team on Faceit (required)
        game -- A game on Faceit
        starting_item_position -- The starting item position (Default is 0)
        return_items -- The number of items to return (Default is 20)
        """

        if nickname == None:
            print("The nickname for search_teams() cannot be nothing!")
        else:
            api_url = "{}/search/teams?nickname={}&offset={}&limit={}".format(
                self.base_url, urllib.parse.quote_plus(nickname), starting_item_position, return_items)

            if game != None:
                api_url += "&game={}".format(urllib.parse.quote_plus(game))

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def search_tournaments(self, name_of_tournament=None, game=None, region=None, type_of_competition="all",
                           starting_item_position=0, return_items=20):
        """Search for tournaments
        Keyword arguments:
        name_of_tournament -- The name of a tournament on Faceit (required)
        game -- A game on Faceit
        region -- A region of the game
        type_of_competition -- Kind of competitions to return (default is all, can be upcoming, ongoing, or past)
        starting_item_position -- The starting item position (Default is 0)
        return_items -- The number of items to return (Default is 20)
        """

        if name_of_tournament == None:
            print("The name_of_tournament for search_tournaments() cannot be nothing!")
        else:
            api_url = "{}/search/tournaments?name={}&type={}&offset={}&limit={}".format(self.base_url,
                                                                                        urllib.parse.quote_plus(
                                                                                            name_of_tournament),
                                                                                        type_of_competition,
                                                                                        starting_item_position,
                                                                                        return_items)

            if game != None:
                api_url += "&game={}".format(urllib.parse.quote_plus(game))
            elif region != None:
                api_url += "&region={}".format(region)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    # Teams

    def team_details(self, team_id=None):
        """Retrieve team details
        Keyword arguments:
        team_id -- The ID of the team (required)
        """

        if team_id == None:
            print("The team_id of team_details() cannot be None!")
        else:
            api_url = "{}/teams/{}".format(self.base_url, team_id)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def team_stats(self, team_id=None, game_id=None):
        """Retrieve statistics of a team
        Keyword arguments:
        team_id -- The ID of a team (required)
        game_id -- A game on Faceit (required)
        """

        if team_id == None:
            print("The team_id of team_stats() cannot be nothing!")
        elif game_id == None:
            print("The game_id of team_stats() cannot be nothing")
        else:
            api_url = "{}/teams/{}/stats/{}".format(
                self.base_url, team_id, urllib.parse.quote_plus(game_id))

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def team_tournaments(self, team_id=None, starting_item_position=0, return_items=20):
        """Retrieve tournaments of a team
        Keyword arguments:
        team_id -- The ID of a team (required)
        starting_item_position -- The starting item position (Default is 0)
        return_items -- The number of items to return (Default is 20)
        """

        if team_id == None:
            print("The team_id of team_tournaments() cannot be nothing!")
        else:
            api_url = "{}/teams/{}/tournaments?offset={}&limit={}".format(
                self.base_url, team_id, starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    # Tournaments

    def all_tournaments(self, game=None, region=None, type_of_tournament="upcoming", starting_item_position=0,
                        return_items=20):
        """Retrieve all tournaments
        Keyword arguments:
        game -- A game on Faceit
        region -- A region of the game
        type_of_tournament -- Kind of tournament. Can be upcoming(default) or past
        starting_item_position -- The starting item position (Default is 0)
        return_items -- The number of items to return (Default is 20)
        """

        api_url = "{}/tournaments?type={}".format(
            self.base_url, type_of_tournament)

        if game != None:
            api_url += "&game={}".format(urllib.parse.quote_plus(game))
        elif region != None:
            api_url += "&region={}".format(region)

        res = requests.get(api_url, headers=self.headers)
        if res.status_code == 200:
            return json.loads(res.content.decode('utf-8'))
        else:
            return None

    def tournament_details(self, tournament_id=None, expanded=None):
        """Retrieve tournament details
        Keyword arguments:
        tournament_id -- The ID of the tournament (required)
        expanded -- List of entity names to expand in request, either "organizer" or "game"
        """

        if tournament_id == None:
            print("The tournament_id of tournament_details() cannot be nothing!")
        else:
            api_url = "{}/tournaments/{}".format(self.base_url, tournament_id)
            if expanded != None:
                if expanded.lower() == "organizer":
                    api_url += "?expanded=organizer"
                elif expanded.lower() == "game":
                    api_url += "?expanded=game"

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def tournament_brackets(self, tournament_id=None):
        """Retrieve brackets of a tournament

        Keyword arguments:
        tournament_id -- The ID of the tournament (required)
        """

        if tournament_id == None:
            print("The tournament_id of tournament_brackets() cannot be nothing!")
        else:
            api_url = "{}/tournaments/{}/brackets".format(self.base_url, tournament_id)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def tournament_matches(self, tournament_id=None, starting_item_position=0, return_items=20):
        """Retrieve all matches of a tournament
        Keyword arguments:
        tournament_id -- The ID of a tournament (required)
        starting_item_position -- The starting item position (Default is 0)
        return_items -- The number of items to return (Default is 20)
        """

        if tournament_id == None:
            print("The tournament_id of tournament_matches() cannot be nothing!")
        else:
            api_url = "{}/tournaments/{}/matches?offset={}&limit={}".format(self.base_url, tournament_id,
                                                                            starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None

    def tournament_teams(self, tournament_id=None, starting_item_position=0, return_items=20):
        """Retrieve all teams of a tournament
        Keyword arguments:
        tournament_id -- The ID of a tournament (required)
        starting_item_position -- The starting item position (Default is 0)
        return_items -- The number of items to return (Default is 20)
        """

        if tournament_id == None:
            print("The tournament_id of tournament_teams() cannot be nothing!")
        else:
            api_url = "{}/tournaments/{}/teams?offset={}&limit={}".format(self.base_url, tournament_id,
                                                                          starting_item_position, return_items)

            res = requests.get(api_url, headers=self.headers)
            if res.status_code == 200:
                return json.loads(res.content.decode('utf-8'))
            else:
                return None
