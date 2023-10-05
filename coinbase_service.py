import http.client
import hmac
import hashlib
import json
import time
import os
from enum import Enum
import uuid


class Sides(Enum):
    SELL = 'SELL'
    BUY = 'BUY'


class GBPProducts(Enum):
    BTC = 'BTC-GBP'
    ETH = 'ETH-GBP'
    ADA = 'ADA-GBP'


class APICategories(Enum):
    ACCOUNTS = "accounts"
    PRODUCTS = "products"
    ORDERS = "orders"


class Methods(Enum):
    GET = "GET"
    POST = "POST"


class CoinbaseService:

    def __init__(self):
        self.base_path = "/api/v3/brokerage/"

    def make_signed_request(self, method, category, body):
        path = self.base_path + category
        unix_timestamp = str(int(time.time()))
        message = str(unix_timestamp) + method + path.split('?')[0] + str(body)
        signature = hmac.new(os.environ['COINBASE_API_SECRET'].encode(
            'utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()
        conn = http.client.HTTPSConnection("api.coinbase.com")
        headers = {
            'Content-Type': 'application/json',
            'CB-ACCESS-KEY': os.environ['COINBASE_API_KEY'],
            'CB-ACCESS-SIGN': signature.hex(),
            'CB-ACCESS-TIMESTAMP': unix_timestamp,
        }
        conn.request(method, path, body, headers)
        print('made request')
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

    def list_accounts(self):
        account_data = self.make_signed_request(Methods.GET.value, APICategories.ACCOUNTS.value, '')
        return json.loads(account_data)

    def list_accounts_by_product_quantity(self):
        return sorted(self.list_accounts().get('accounts'), key=lambda x: x['available_balance']["value"], reverse=True)

    def list_orders(self):
        order_data = self.make_signed_request(Methods.GET.value, APICategories.ORDERS.value + '/historical/batch', '')
        return json.loads(order_data)

    def _create_buy_market_order_gbp(self, product, amount):
        assert type(product) == GBPProducts
        payload = json.dumps({
            "side": Sides.BUY.name,
            "product_id": product.value,
            "client_order_id": uuid.uuid4().hex,
            "order_configuration": {
                "market_market_ioc": {
                    "quote_size": str(amount)
                }
            }
        })
        return self.make_signed_request(Methods.POST.value, APICategories.ORDERS.value, payload)

    def _create_sell_market_order_gbp(self, product, amount):
        assert type(product) == GBPProducts
        payload = json.dumps({
            "side": Sides.SELL.name,
            "product_id": product.value,
            "client_order_id": uuid.uuid4().hex,
            "order_configuration": {
                "market_market_ioc": {
                    "base_size": str(amount)
                }
            }
        })
        return self.make_signed_request(Methods.POST.value, APICategories.ORDERS.value, payload)

    def sell_btc_for_gbp(self, amount):
        """
        Sell amount of BTC for GBP at current market value
        :param amount: in BTC
        :return: response from Coinbase API
        """
        return self._create_sell_market_order_gbp(GBPProducts.BTC, amount)

    def buy_btc_for_gbp(self, amount):
        """
        Buy amount of BTC for GBP at current market value
        :param amount: in GBP
        :return: response from Coinbase API
        """
        return self._create_buy_market_order_gbp(GBPProducts.BTC, amount)

    def sell_eth_for_gbp(self, amount):
        """
       Sell amount of ETH for GBP at current market value
       :param amount: in ETH
       :return: response from Coinbase API
       """
        return self._create_sell_market_order_gbp(GBPProducts.ETH, amount)

    def buy_eth_for_gbp(self, amount):
        """
        Buy amount of ETH for GBP at current market value
        :param amount: in GBP
        :return: response from Coinbase API
        """
        return self._create_buy_market_order_gbp(GBPProducts.ETH, amount)

    def sell_ada_for_gbp(self, amount):
        """
       Sell amount of ADA for GBP at current market value
       :param amount: in ADA
       :return: response from Coinbase
       """
        return self._create_sell_market_order_gbp(GBPProducts.ADA, amount)

    def buy_ada_for_gbp(self, amount):
        """
        Buy amount of ADA for GBP at current market value
        :param amount: in GBP
        :return: response from Coinbase API
        """
        return self._create_buy_market_order_gbp(GBPProducts.ADA, amount)
