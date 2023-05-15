import requests
import datetime
import time

# set up the MongoDB client
#client = pymongo.MongoClient('mongodb://mongo:27017/')
#db = client['gw2_trading']

# set up the base URL for the GW2 API
base_url = 'https://api.guildwars2.com/v2/commerce/prices/'

# define a function to get the current prices for an item and insert them into the database
def get_item_prices(item_id):
    # make the API request
    response = requests.get(base_url + str(item_id))

    # parse the response JSON
    response_json = response.json()

    # extract the buy and sell prices
    buy_price = response_json['buys']['unit_price']
    sell_price = response_json['sells']['unit_price']

    # convert the prices to gold, silver, and copper
    buy_gold = buy_price // 10000
    buy_silver = (buy_price // 100) % 100
    buy_copper = buy_price % 100
    sell_gold = sell_price // 10000
    sell_silver = (sell_price // 100) % 100
    sell_copper = sell_price % 100

    # get the item name from the API
    item_response = requests.get('https://api.guildwars2.com/v2/items/' + str(item_id))
    item_name = item_response.json()['name']

    # insert the prices into the database
#    db[str(item_id)].insert_one({
#        'item_name': item_name,
#        'buy_gold': buy_gold,
#        'buy_silver': buy_silver,
#        'buy_copper': buy_copper,
#        'sell_gold': sell_gold,
#        'sell_silver': sell_silver,
#        'sell_copper': sell_copper,
#        'timestamp': datetime.datetime.utcnow()
#    })

    print(f"{item_name}\t{item_name}\t{buy_gold}g {buy_silver}s {buy_copper}c\t{sell_gold}g {sell_silver}s {sell_copper}c")

# define a list of item IDs to scrape
item_ids = [19684, 19685, 19686]

# loop through the item IDs and scrape their prices every 5 minutes
while True:
    for item_id in item_ids:
        get_item_prices(item_id)
    time.sleep(300)
