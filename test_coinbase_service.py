import unittest

import stubbed_data
from mock.mock import patch, Mock
import json

from coinbase_service import CoinbaseService


class TestCoinbaseService(unittest.TestCase):

    @patch.object(CoinbaseService, "_make_signed_request")
    def test_list_accounts(self, mock__make_signed_request):
        mock__make_signed_request.return_value = stubbed_data.list_accounts
        self.assertEqual(stubbed_data.list_accounts, CoinbaseService().list_accounts())
        mock__make_signed_request.assert_called_once_with("GET", 'accounts', '')

    @patch.object(CoinbaseService, "_make_signed_request")
    def test_list_orders(self, mock__make_signed_request):
        mock__make_signed_request.return_value = stubbed_data.orders
        self.assertEqual(stubbed_data.orders, CoinbaseService().list_orders())
        mock__make_signed_request.assert_called_once_with("GET", 'orders/historical/batch', '')

    @patch("uuid.uuid4")
    @patch.object(CoinbaseService, "_make_signed_request")
    def test_sell_btc_for_gbp(self, mock__make_signed_request, mock_uuid4):
        mock_uuid4.return_value = Mock(hex='123')
        mock__make_signed_request.return_value = stubbed_data.buy_success_response
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
        self.assertEqual(stubbed_data.buy_success_response, CoinbaseService().sell_btc_for_gbp(1))
        mock__make_signed_request.assert_called_once_with("POST", 'orders', payload)

    @patch("uuid.uuid4")
    @patch.object(CoinbaseService, "_make_signed_request")
    def test_buy_btc_for_gbp(self, mock__make_signed_request, mock_uuid4):
        mock_uuid4.return_value = Mock(hex='123')
        mock__make_signed_request.return_value = stubbed_data.buy_success_response
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
        self.assertEqual(stubbed_data.buy_success_response, CoinbaseService().buy_btc_for_gbp(1))
        mock__make_signed_request.assert_called_once_with("POST", 'orders', payload)

    @patch("uuid.uuid4")
    @patch.object(CoinbaseService, "_make_signed_request")
    def test_sell_eth_for_gbp(self, mock__make_signed_request, mock_uuid4):
        mock_uuid4.return_value = Mock(hex='123')
        mock__make_signed_request.return_value = stubbed_data.buy_success_response
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
        self.assertEqual(stubbed_data.buy_success_response, CoinbaseService().sell_eth_for_gbp(1))
        mock__make_signed_request.assert_called_once_with("POST", 'orders', payload)

    @patch("uuid.uuid4")
    @patch.object(CoinbaseService, "_make_signed_request")
    def test_buy_eth_for_gbp(self, mock__make_signed_request, mock_uuid4):
        mock_uuid4.return_value = Mock(hex='123')
        mock__make_signed_request.return_value = stubbed_data.buy_success_response
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
        self.assertEqual(stubbed_data.buy_success_response, CoinbaseService().buy_eth_for_gbp(1))
        mock__make_signed_request.assert_called_once_with("POST", 'orders', payload)

    @patch("uuid.uuid4")
    @patch.object(CoinbaseService, "_make_signed_request")
    def test_sell_ada_for_gbp(self, mock__make_signed_request, mock_uuid4):
        mock_uuid4.return_value = Mock(hex='123')
        mock__make_signed_request.return_value = stubbed_data.buy_success_response
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
        self.assertEqual(stubbed_data.buy_success_response, CoinbaseService().sell_ada_for_gbp(1))
        mock__make_signed_request.assert_called_once_with("POST", 'orders', payload)

    @patch("uuid.uuid4")
    @patch.object(CoinbaseService, "_make_signed_request")
    def test_buy_ada_for_gbp(self, mock__make_signed_request, mock_uuid4):
        mock_uuid4.return_value = Mock(hex='123')
        mock__make_signed_request.return_value = stubbed_data.buy_success_response
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
        self.assertEqual(stubbed_data.buy_success_response, CoinbaseService().buy_ada_for_gbp(1))
        mock__make_signed_request.assert_called_once_with("POST", 'orders', payload)

    @patch("uuid.uuid4")
    @patch.object(CoinbaseService, "_make_signed_request")
    def test_buy_btc_for_gbp_raises_when_failed_response(self, mock__make_signed_request, mock_uuid4):
        mock_uuid4.return_value = Mock(hex='123')
        mock__make_signed_request.return_value = stubbed_data.buy_failure_response
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
        with self.assertRaises(Exception) as exc:
            self.assertEqual(stubbed_data.buy_success_response, CoinbaseService().buy_btc_for_gbp(10))
        self.assertEqual("('Purchase unsuccessful: Insufficient balance in source account', {'success': False, "
                         "'failure_reason': 'UNKNOWN_FAILURE_REASON', 'order_id': '', 'error_response': {'error': "
                         "'INSUFFICIENT_FUND', 'message': 'Insufficient balance in source account', 'error_details': "
                         "'', 'preview_failure_reason': 'PREVIEW_INSUFFICIENT_FUND'}, 'order_configuration': {"
                         "'market_market_ioc': {'quote_size': '100'}}})", str(exc.exception))
        mock__make_signed_request.assert_called_once_with("POST", 'orders', payload)

