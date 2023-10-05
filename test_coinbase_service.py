import unittest

import stubbed_data
from mock.mock import patch, Mock
import json

from coinbase_service import CoinbaseService


class TestCoinbaseService(unittest.TestCase):

    @patch.object(CoinbaseService, "make_signed_request")
    def test_list_accounts(self, mock_make_signed_request):
        mock_make_signed_request.return_value = stubbed_data.list_accounts
        self.assertEqual(json.loads(stubbed_data.list_accounts), CoinbaseService().list_accounts())
        mock_make_signed_request.assert_called_once_with("GET", 'accounts', '')

    @patch.object(CoinbaseService, "make_signed_request")
    def test_list_orders(self, mock_make_signed_request):
        mock_make_signed_request.return_value = stubbed_data.orders
        self.assertEqual(json.loads(stubbed_data.orders), CoinbaseService().list_orders())
        mock_make_signed_request.assert_called_once_with("GET", 'orders/historical/batch', '')

    @patch("uuid.uuid4")
    @patch.object(CoinbaseService, "make_signed_request")
    def test_sell_btc_for_gbp(self, mock_make_signed_request, mock_uuid4):
        mock_uuid4.return_value = Mock(hex='123')
        mock_make_signed_request.return_value = '{"test":"test"}'
        payload = json.dumps({
            "side": "SELL",
            "product_id": "BTC-GBP",
            "client_order_id": "123",
            "order_configuration": {
                "market_market_ioc": {
                    "base_size": "1"
                }
            }
        })
        self.assertEqual('{"test":"test"}', CoinbaseService().sell_btc_for_gbp(1))
        mock_make_signed_request.assert_called_once_with("POST", 'orders', payload)

    @patch("uuid.uuid4")
    @patch.object(CoinbaseService, "make_signed_request")
    def test_buy_btc_for_gbp(self, mock_make_signed_request, mock_uuid4):
        mock_uuid4.return_value = Mock(hex='123')
        mock_make_signed_request.return_value = '{"test":"test"}'
        payload = json.dumps({
            "side": "BUY",
            "product_id": "BTC-GBP",
            "client_order_id": "123",
            "order_configuration": {
                "market_market_ioc": {
                    "quote_size": "1"
                }
            }
        })
        self.assertEqual('{"test":"test"}', CoinbaseService().buy_btc_for_gbp(1))
        mock_make_signed_request.assert_called_once_with("POST", 'orders', payload)

    @patch("uuid.uuid4")
    @patch.object(CoinbaseService, "make_signed_request")
    def test_sell_eth_for_gbp(self, mock_make_signed_request, mock_uuid4):
        mock_uuid4.return_value = Mock(hex='123')
        mock_make_signed_request.return_value = '{"test":"test"}'
        payload = json.dumps({
            "side": "SELL",
            "product_id": "ETH-GBP",
            "client_order_id": "123",
            "order_configuration": {
                "market_market_ioc": {
                    "base_size": "1"
                }
            }
        })
        self.assertEqual('{"test":"test"}', CoinbaseService().sell_eth_for_gbp(1))
        mock_make_signed_request.assert_called_once_with("POST", 'orders', payload)

    @patch("uuid.uuid4")
    @patch.object(CoinbaseService, "make_signed_request")
    def test_buy_eth_for_gbp(self, mock_make_signed_request, mock_uuid4):
        mock_uuid4.return_value = Mock(hex='123')
        mock_make_signed_request.return_value = '{"test":"test"}'
        payload = json.dumps({
            "side": "BUY",
            "product_id": "ETH-GBP",
            "client_order_id": "123",
            "order_configuration": {
                "market_market_ioc": {
                    "quote_size": "1"
                }
            }
        })
        self.assertEqual('{"test":"test"}', CoinbaseService().buy_eth_for_gbp(1))
        mock_make_signed_request.assert_called_once_with("POST", 'orders', payload)

    @patch("uuid.uuid4")
    @patch.object(CoinbaseService, "make_signed_request")
    def test_sell_ada_for_gbp(self, mock_make_signed_request, mock_uuid4):
        mock_uuid4.return_value = Mock(hex='123')
        mock_make_signed_request.return_value = '{"test":"test"}'
        payload = json.dumps({
            "side": "SELL",
            "product_id": "ADA-GBP",
            "client_order_id": "123",
            "order_configuration": {
                "market_market_ioc": {
                    "base_size": "1"
                }
            }
        })
        self.assertEqual('{"test":"test"}', CoinbaseService().sell_ada_for_gbp(1))
        mock_make_signed_request.assert_called_once_with("POST", 'orders', payload)

    @patch("uuid.uuid4")
    @patch.object(CoinbaseService, "make_signed_request")
    def test_buy_ada_for_gbp(self, mock_make_signed_request, mock_uuid4):
        mock_uuid4.return_value = Mock(hex='123')
        mock_make_signed_request.return_value = '{"test":"test"}'
        payload = json.dumps({
            "side": "BUY",
            "product_id": "ADA-GBP",
            "client_order_id": "123",
            "order_configuration": {
                "market_market_ioc": {
                    "quote_size": "1"
                }
            }
        })
        self.assertEqual('{"test":"test"}', CoinbaseService().buy_ada_for_gbp(1))
        mock_make_signed_request.assert_called_once_with("POST", 'orders', payload)
