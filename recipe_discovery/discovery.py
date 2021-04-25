from recipe_discovery.config import ALBION_ONLINE_DATA_API_URI, CITY_LIST, QUALITY_DICT
from recipe_discovery.recipes import RECIPIES
import requests
import pandas as pd
import datetime
from tqdm import tqdm
from collections import namedtuple
import itertools

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

Node = namedtuple("Node", "item_id, price, quantity, city")


class ProfitDiscover:
    def __init__(self):
        self.__recipes = {
            k: None for k in itertools.product(CITY_LIST, list(QUALITY_DICT.keys()))
        }
        logger.info("ProfitDiscover object created")

    def request_prices(self, city, quality):
        """Request prices from Albion Online Data project API

        Returns:
            pd.DataFrame: Dataframe with price information for each item
        """

        logger.info("Requesting prices data ...")

        item_set_response = []
        recipies_item_name = list(RECIPIES.keys())
        r = requests.get(
            ALBION_ONLINE_DATA_API_URI.format(
                item=",".join(recipies_item_name),
                cities=city.replace(" ", "%20"),
                quality=QUALITY_DICT[quality],
            )
        )

        logger.info("Request OK!")

        for item in r.json():
            item_set_response.append(item)

        curr_date = datetime.datetime.now() - datetime.timedelta(hours=12)
        item_set_df = pd.DataFrame(item_set_response)
        item_set_df = item_set_df[item_set_df["sell_price_min"] > 0]
        item_set_df["sell_price_max_date"] = pd.to_datetime(
            item_set_df["sell_price_max_date"]
        )
        item_set_df = item_set_df[item_set_df["sell_price_max_date"] >= curr_date]

        return item_set_df

    def get_recipe_price(self, recipe):
        """Calculate recipe price

        Args:
            recipe ([list of Node]): Recipe as a list of Nodes

        Returns:
            double: price of a recipe
        """
        _recipe_price = 0
        if recipe is None:
            return None
        for item in recipe:
            _recipe_price += item.price * item.quantity
        return _recipe_price

    def get_cheapest_recipe(self, item_name, recipies, price_hist):

        if sum(price_hist["item_id"].str.contains(item_name)) == 0:
            return None

        def _next_best_item(_item_name, _quantity):
            _item = recipies[_item_name]
            _children_list = []

            _best_price = price_hist[price_hist["item_id"] == _item_name]

            if len(_best_price) == 0:
                return None

            _best_price = _best_price[
                _best_price["sell_price_min"] == _best_price["sell_price_min"].min()
            ].to_dict(orient="list")
            _node = Node(
                _best_price["item_id"][0],
                _best_price["sell_price_min"][0],
                _quantity,
                _best_price["city"][0],
            )

            if _item is None:
                return [_node]
            else:
                for _child in _item:
                    _child_item_name, _child_item_quantity = _child
                    _next_child = _next_best_item(
                        _child_item_name, _quantity * _child_item_quantity
                    )
                    if _next_child is None:
                        _children_list = None
                        break
                    _children_list.extend(_next_child)

                if _children_list is not None:
                    _children_price = self.get_recipe_price(_children_list)
                    _item_price = _node.price * _node.quantity

                    if _children_price < _item_price:
                        return _children_list
                    else:
                        return [_node]
                else:
                    return [_node]

        return _next_best_item(item_name, 1)

    def get_highest_price(self, item, price_hist):
        _x = price_hist[price_hist["item_id"] == item]
        if len(_x) == 0:
            return None
        highest_price = _x[_x["sell_price_min"] == _x["sell_price_min"].max()].to_dict(
            orient="list"
        )
        return (
            highest_price["item_id"][0],
            highest_price["city"][0],
            highest_price["sell_price_min"][0],
        )

    def scan(self, city=None, quality=None, use_buffer=True):

        if city is None or quality is None:
            return None

        logger.info(
            f"Scanning recipies for {city} at quality {quality}. Use buffer: {use_buffer}"
        )

        if use_buffer == True and self.recipies[(city, quality)] is not None:
            logger.info(f"Prices for {city} on buffer!")
            return self.recipies[(city, quality)]

        recipies_buffer = {
            "item_name": [],
            "profitability": [],
            "profit": [],
            "recipe_price": [],
            "sell_price": [],
            "sell_city": [],
            "recipe": [],
        }

        item_set_df = self.request_prices(city, quality)

        for item_name in tqdm(RECIPIES):

            cheapest_recipe = self.get_cheapest_recipe(item_name, RECIPIES, item_set_df)

            if cheapest_recipe is None:
                continue

            recipe_price = self.get_recipe_price(cheapest_recipe)

            _, sell_city, sell_price = self.get_highest_price(item_name, item_set_df)
            profit = sell_price - recipe_price
            profitability = round((profit / recipe_price) * 100, 2)

            recipies_buffer["item_name"].append(item_name)
            recipies_buffer["profitability"].append(profitability)
            recipies_buffer["profit"].append(profit)
            recipies_buffer["recipe_price"].append(recipe_price)
            recipies_buffer["sell_price"].append(sell_price)
            recipies_buffer["sell_city"].append(sell_city)
            recipies_buffer["recipe"].append(cheapest_recipe)

            recipies_stats = pd.DataFrame(recipies_buffer)
            recipies_stats.sort_values("profitability", ascending=False, inplace=True)

        self.recipies[(city, quality)] = recipies_stats

        return recipies_stats

    @property
    def recipies(self):
        return self.__recipes

    @recipies.setter
    def recipies(self, val):
        self.__recipies = val
