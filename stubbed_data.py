import json

list_accounts = ('{"accounts":[{"uuid":"5c5b5e0a-ee7b-509a-903f-1ac438c4d9e6", "name":"AERGO Wallet", '
                 '"currency":"AERGO", "available_balance":{"value":"0", "currency":"AERGO"}, "default":true, '
                 '"active":true, "created_at":"2023-09-27T15:22:20.380Z", "updated_at":"2023-09-27T15:22:21.843Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"AERGO"}}, {"uuid":"60d9e127-6d26-5842-b4c6-55d37f3f8685", "name":"USDC Wallet", '
                 '"currency":"USDC", "available_balance":{"value":"0", "currency":"USDC"}, "default":true, '
                 '"active":true, "created_at":"2023-09-27T12:51:38.478Z", "updated_at":"2023-09-27T12:51:39.596Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"USDC"}}, {"uuid":"dff8bf08-83d2-5b36-8e06-98144b6d896c", "name":"ETH2 Wallet", '
                 '"currency":"ETH2", "available_balance":{"value":"0.01821349", "currency":"ETH2"}, "default":true, '
                 '"active":true, "created_at":"2023-07-20T14:12:30.307Z", "updated_at":"2023-10-02T06:37:17.594Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":false, "hold":{"value":"0", '
                 '"currency":"ETH2"}}, {"uuid":"94af0fbd-c03f-5646-8dbc-bd4ffdb5fa19", "name":"ADA Wallet", '
                 '"currency":"ADA", "available_balance":{"value":"0.039895", "currency":"ADA"}, "default":true, '
                 '"active":true, "created_at":"2021-09-26T17:07:27.638Z", "updated_at":"2023-09-27T15:57:14.286Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"ADA"}}, {"uuid":"e3ddf3e7-51b9-580d-9140-ef5ab533c394", "name":"AMP Wallet", '
                 '"currency":"AMP", "available_balance":{"value":"63.92045519", "currency":"AMP"}, "default":true, '
                 '"active":true, "created_at":"2021-09-26T12:06:12.609Z", "updated_at":"2023-09-27T12:52:14.705Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"AMP"}}, {"uuid":"6d14c76f-76d0-59b9-a35f-f67f38d48333", "name":"COMP Wallet", '
                 '"currency":"COMP", "available_balance":{"value":"0.00088035", "currency":"COMP"}, "default":true, '
                 '"active":true, "created_at":"2021-09-26T12:00:54.052Z", "updated_at":"2021-09-26T12:32:17.257Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"COMP"}}, {"uuid":"870c4699-0c8b-5e46-913c-599cf26807a5", "name":"GRT Wallet", '
                 '"currency":"GRT", "available_balance":{"value":"0.00672606", "currency":"GRT"}, "default":true, '
                 '"active":true, "created_at":"2021-09-26T11:55:58.080Z", "updated_at":"2021-09-26T12:22:06.942Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"GRT"}}, {"uuid":"16bb7f71-ce71-5945-9e8f-b043eaa778ad", "name":"XLM Wallet", '
                 '"currency":"XLM", "available_balance":{"value":"0.3754551", "currency":"XLM"}, "default":true, '
                 '"active":true, "created_at":"2021-09-26T11:45:42.745Z", "updated_at":"2023-09-27T12:52:14.739Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"XLM"}}, {"uuid":"7c2510da-10ff-5fdf-8d22-8cf0205932ba", "name":"CLV Wallet", '
                 '"currency":"CLV", "available_balance":{"value":"0.00461538", "currency":"CLV"}, "default":true, '
                 '"active":true, "created_at":"2021-09-26T11:42:01.064Z", "updated_at":"2021-09-26T12:22:30.201Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"CLV"}}, {"uuid":"f516276d-f365-5c2e-b013-68aaecdb6bbe", "name":"ETC Wallet", '
                 '"currency":"ETC", "available_balance":{"value":"0", "currency":"ETC"}, "default":true, '
                 '"active":true, "created_at":"2021-09-26T11:37:36.884Z", "updated_at":"2021-09-26T11:37:36.884Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"ETC"}}, {"uuid":"6afca941-4bea-53e0-af65-5ed6458eff30", "name":"FET Wallet", '
                 '"currency":"FET", "available_balance":{"value":"3.59655913", "currency":"FET"}, "default":true, '
                 '"active":true, "created_at":"2021-09-26T11:35:36.325Z", "updated_at":"2023-09-28T08:58:58.339Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"FET"}}, {"uuid":"7aa31306-1960-5477-980b-eae3609218fd", "name":"LINK Wallet", '
                 '"currency":"LINK", "available_balance":{"value":"0", "currency":"LINK"}, "default":true, '
                 '"active":true, "created_at":"2021-09-24T16:06:50.105Z", "updated_at":"2023-09-27T17:24:44.373Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"LINK"}}, {"uuid":"b11960a3-651c-500d-974b-8061d2f3aaf5", "name":"ETH Wallet", '
                 '"currency":"ETH", "available_balance":{"value":"0.0000000017876934", "currency":"ETH"}, '
                 '"default":true, "active":true, "created_at":"2021-09-24T15:33:58.569Z", '
                 '"updated_at":"2023-10-02T06:37:17.740Z", "deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", '
                 '"ready":true, "hold":{"value":"0", "currency":"ETH"}}, '
                 '{"uuid":"d3d620a9-6425-5fef-8a0a-8fe98c619c59", "name":"ATOM Wallet", "currency":"ATOM", '
                 '"available_balance":{"value":"0", "currency":"ATOM"}, "default":true, "active":true, '
                 '"created_at":"2021-04-13T18:18:37.568Z", "updated_at":"2021-04-13T18:18:37.568Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"ATOM"}}, {"uuid":"271c653e-b0d8-53ac-8742-d30971ca9cf9", "name":"ALGO Wallet", '
                 '"currency":"ALGO", "available_balance":{"value":"0", "currency":"ALGO"}, "default":true, '
                 '"active":true, "created_at":"2021-04-13T18:18:36.771Z", "updated_at":"2021-04-13T18:18:36.771Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"ALGO"}}, {"uuid":"bba250d3-d3f2-55a4-ab0e-bc2727f77184", "name":"XTZ Wallet", '
                 '"currency":"XTZ", "available_balance":{"value":"0", "currency":"XTZ"}, "default":true, '
                 '"active":true, "created_at":"2021-04-13T18:18:35.725Z", "updated_at":"2021-04-13T18:18:35.725Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"XTZ"}}, {"uuid":"9272fbff-e021-5474-819c-1ad874cd1182", "name":"DAI Wallet", '
                 '"currency":"DAI", "available_balance":{"value":"0", "currency":"DAI"}, "default":true, '
                 '"active":true, "created_at":"2021-04-13T18:18:27.718Z", "updated_at":"2021-04-13T18:18:27.718Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"DAI"}}, {"uuid":"ef107cac-5043-5da7-ab48-23d9fc1b29dc", "name":"BSV Wallet", '
                 '"currency":"BSV", "available_balance":{"value":"0", "currency":"BSV"}, "default":true, '
                 '"active":true, "created_at":"2021-04-13T10:26:12.165Z", "updated_at":"2021-04-13T10:26:12.165Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":false, "hold":{"value":"0", '
                 '"currency":"BSV"}}, {"uuid":"0accba31-74f7-5338-9934-4e53ac3fa195", "name":"BCH Wallet", '
                 '"currency":"BCH", "available_balance":{"value":"0", "currency":"BCH"}, "default":true, '
                 '"active":true, "created_at":"2021-04-13T10:26:12.070Z", "updated_at":"2021-04-13T10:26:12.070Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", "ready":true, "hold":{"value":"0", '
                 '"currency":"BCH"}}, {"uuid":"fec4cfd3-8bbe-508e-a031-010aa2297425", "name":"GBP Wallet", '
                 '"currency":"GBP", "available_balance":{"value":"5.0003600247", "currency":"GBP"}, "default":false, '
                 '"active":true, "created_at":"2021-04-13T09:01:08.467Z", "updated_at":"2023-10-04T15:14:43.525Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_FIAT", "ready":true, "hold":{"value":"0", '
                 '"currency":"GBP"}}, {"uuid":"a5969490-8fa9-571c-ba4d-5c73d70c0855", "name":"EUR Wallet", '
                 '"currency":"EUR", "available_balance":{"value":"0", "currency":"EUR"}, "default":false, '
                 '"active":true, "created_at":"2021-04-13T09:01:08.278Z", "updated_at":"2021-04-13T09:01:08.278Z", '
                 '"deleted_at":null, "type":"ACCOUNT_TYPE_FIAT", "ready":true, "hold":{"value":"0", '
                 '"currency":"EUR"}}, {"uuid":"d47e88b6-5ce7-5b7d-b916-dfc2d26cd7bf", "name":"BTC Wallet", '
                 '"currency":"BTC", "available_balance":{"value":"0.0004305957311716", "currency":"BTC"}, '
                 '"default":true, "active":true, "created_at":"2021-04-13T09:00:42.125Z", '
                 '"updated_at":"2023-10-04T16:52:29.325Z", "deleted_at":null, "type":"ACCOUNT_TYPE_CRYPTO", '
                 '"ready":true, "hold":{"value":"0", "currency":"BTC"}}], "has_next":false, "cursor":"", "size":22}')

orders = json.dumps({'cursor': '',
                             'has_next': False,
                             'orders': [{'average_filled_price': '22594.37',
                                         'cancel_message': '',
                                         'client_order_id': '93527120-f50d-4ef5-ae99-4f6c6ac9866d',
                                         'completion_percentage': '100.00',
                                         'created_time': '2023-10-04T15:07:56.016546Z',
                                         'edit_history': [],
                                         'fee': '',
                                         'filled_size': '0.00022131',
                                         'filled_value': '5.0003600247',
                                         'is_liquidation': False,
                                         'last_fill_time': '2023-10-04T15:07:56.106947Z',
                                         'leverage': '',
                                         'margin_type': 'UNKNOWN_MARGIN_TYPE',
                                         'number_of_fills': '1',
                                         'order_configuration': {'market_market_ioc': {'base_size': '0.00022131'}},
                                         'order_id': '4132c103-52c8-4bac-84c9-6d6e6b73e01e',
                                         'order_placement_source': 'RETAIL_ADVANCED',
                                         'order_type': 'MARKET',
                                         'outstanding_hold_amount': '0',
                                         'pending_cancel': False,
                                         'product_id': 'BTC-GBP',
                                         'product_type': 'SPOT',
                                         'reject_message': '',
                                         'reject_reason': 'REJECT_REASON_UNSPECIFIED',
                                         'settled': True,
                                         'side': 'SELL',
                                         'size_in_quote': False,
                                         'size_inclusive_of_fees': False,
                                         'status': 'FILLED',
                                         'time_in_force': 'IMMEDIATE_OR_CANCEL',
                                         'total_fees': '0',
                                         'total_value_after_fees': '5.0003600247',
                                         'trigger_status': 'INVALID_ORDER_TYPE',
                                         'user_id': '0ad12a7e-147a-5672-9b22-9171a5c0762d'},
                                        {'average_filled_price': '1412.499999999996351',
                                         'cancel_message': '',
                                         'client_order_id': '67026024-4cdb-4e56-9cc6-2d74d0116393',
                                         'completion_percentage': '100.00',
                                         'created_time': '2023-10-02T06:30:21.885150Z',
                                         'edit_history': [],
                                         'fee': '',
                                         'filled_size': '0.0106194690265487',
                                         'filled_value': '15',
                                         'is_liquidation': False,
                                         'last_fill_time': '2023-10-02T06:30:22.006953990Z',
                                         'leverage': '',
                                         'margin_type': 'UNKNOWN_MARGIN_TYPE',
                                         'number_of_fills': '2',
                                         'order_configuration': {'market_market_ioc': {'quote_size': '15'}},
                                         'order_id': '561bd5e5-22db-49a9-837d-5734e6dbbf7b',
                                         'order_placement_source': 'RETAIL_ADVANCED',
                                         'order_type': 'MARKET',
                                         'outstanding_hold_amount': '0',
                                         'pending_cancel': False,
                                         'product_id': 'ETH-GBP',
                                         'product_type': 'SPOT',
                                         'reject_message': '',
                                         'reject_reason': 'REJECT_REASON_UNSPECIFIED',
                                         'settled': True,
                                         'side': 'BUY',
                                         'size_in_quote': True,
                                         'size_inclusive_of_fees': True,
                                         'status': 'FILLED',
                                         'time_in_force': 'IMMEDIATE_OR_CANCEL',
                                         'total_fees': '0',
                                         'total_value_after_fees': '15',
                                         'trigger_status': 'INVALID_ORDER_TYPE',
                                         'user_id': '0ad12a7e-147a-5672-9b22-9171a5c0762d'},
                                        {'average_filled_price': '23009.5099999994288196',
                                         'cancel_message': '',
                                         'client_order_id': 'af5da90c-0b8a-4e89-97e0-35eb998c735f',
                                         'completion_percentage': '100.00',
                                         'created_time': '2023-10-02T06:29:43.182281Z',
                                         'edit_history': [],
                                         'fee': '',
                                         'filled_size': '0.0006519043647605',
                                         'filled_value': '15',
                                         'is_liquidation': False,
                                         'last_fill_time': '2023-10-02T06:29:43.312596505Z',
                                         'leverage': '',
                                         'margin_type': 'UNKNOWN_MARGIN_TYPE',
                                         'number_of_fills': '2',
                                         'order_configuration': {'market_market_ioc': {'quote_size': '15'}},
                                         'order_id': '7c753a3f-c8a6-4730-920c-8a371d2a2854',
                                         'order_placement_source': 'RETAIL_ADVANCED',
                                         'order_type': 'MARKET',
                                         'outstanding_hold_amount': '0',
                                         'pending_cancel': False,
                                         'product_id': 'BTC-GBP',
                                         'product_type': 'SPOT',
                                         'reject_message': '',
                                         'reject_reason': 'REJECT_REASON_UNSPECIFIED',
                                         'settled': True,
                                         'side': 'BUY',
                                         'size_in_quote': True,
                                         'size_inclusive_of_fees': True,
                                         'status': 'FILLED',
                                         'time_in_force': 'IMMEDIATE_OR_CANCEL',
                                         'total_fees': '0',
                                         'total_value_after_fees': '15',
                                         'trigger_status': 'INVALID_ORDER_TYPE',
                                         'user_id': '0ad12a7e-147a-5672-9b22-9171a5c0762d'},
                                        {'average_filled_price': '1316.99000000000366',
                                         'cancel_message': '',
                                         'client_order_id': 'ba07685a-90e4-4d1e-bceb-bbe9e7fb8817',
                                         'completion_percentage': '100.00',
                                         'created_time': '2023-09-27T17:05:59.131580Z',
                                         'edit_history': [],
                                         'fee': '',
                                         'filled_size': '0.0113516427611447',
                                         'filled_value': '14.95',
                                         'is_liquidation': False,
                                         'last_fill_time': '2023-09-27T17:05:59.260475772Z',
                                         'leverage': '',
                                         'margin_type': 'UNKNOWN_MARGIN_TYPE',
                                         'number_of_fills': '2',
                                         'order_configuration': {'market_market_ioc': {'quote_size': '14.95'}},
                                         'order_id': '09e52492-bd23-42bc-a1af-bc77a0beffe5',
                                         'order_placement_source': 'RETAIL_ADVANCED',
                                         'order_type': 'MARKET',
                                         'outstanding_hold_amount': '0',
                                         'pending_cancel': False,
                                         'product_id': 'ETH-GBP',
                                         'product_type': 'SPOT',
                                         'reject_message': '',
                                         'reject_reason': 'REJECT_REASON_UNSPECIFIED',
                                         'settled': True,
                                         'side': 'BUY',
                                         'size_in_quote': True,
                                         'size_inclusive_of_fees': True,
                                         'status': 'FILLED',
                                         'time_in_force': 'IMMEDIATE_OR_CANCEL',
                                         'total_fees': '0',
                                         'total_value_after_fees': '14.95',
                                         'trigger_status': 'INVALID_ORDER_TYPE',
                                         'user_id': '0ad12a7e-147a-5672-9b22-9171a5c0762d'},
                                        {'average_filled_price': '21626.5800000014932778',
                                         'cancel_message': '',
                                         'client_order_id': 'f051e610-61ce-4744-9b34-49a3a82b3898',
                                         'completion_percentage': '100.00',
                                         'created_time': '2023-09-27T17:05:34.818490Z',
                                         'edit_history': [],
                                         'fee': '',
                                         'filled_size': '0.0006917413664111',
                                         'filled_value': '14.96',
                                         'is_liquidation': False,
                                         'last_fill_time': '2023-09-27T17:05:34.943114150Z',
                                         'leverage': '',
                                         'margin_type': 'UNKNOWN_MARGIN_TYPE',
                                         'number_of_fills': '2',
                                         'order_configuration': {'market_market_ioc': {'quote_size': '14.96'}},
                                         'order_id': '097cfa37-a3e9-40b3-b893-425584b3fca2',
                                         'order_placement_source': 'RETAIL_ADVANCED',
                                         'order_type': 'MARKET',
                                         'outstanding_hold_amount': '0',
                                         'pending_cancel': False,
                                         'product_id': 'BTC-GBP',
                                         'product_type': 'SPOT',
                                         'reject_message': '',
                                         'reject_reason': 'REJECT_REASON_UNSPECIFIED',
                                         'settled': True,
                                         'side': 'BUY',
                                         'size_in_quote': True,
                                         'size_inclusive_of_fees': True,
                                         'status': 'FILLED',
                                         'time_in_force': 'IMMEDIATE_OR_CANCEL',
                                         'total_fees': '0',
                                         'total_value_after_fees': '14.96',
                                         'trigger_status': 'INVALID_ORDER_TYPE',
                                         'user_id': '0ad12a7e-147a-5672-9b22-9171a5c0762d'},
                                        {'average_filled_price': '0',
                                         'cancel_message': 'User requested cancel',
                                         'client_order_id': '5770c16d-ff56-46d8-814a-836a545409e9',
                                         'completion_percentage': '0',
                                         'created_time': '2023-09-27T16:09:07.360518Z',
                                         'edit_history': [],
                                         'fee': '',
                                         'filled_size': '0',
                                         'filled_value': '0',
                                         'is_liquidation': False,
                                         'last_fill_time': None,
                                         'leverage': '',
                                         'margin_type': 'UNKNOWN_MARGIN_TYPE',
                                         'number_of_fills': '0',
                                         'order_configuration': {'limit_limit_gtc': {'base_size': '22.43',
                                                                                     'limit_price': '1',
                                                                                     'post_only': False}},
                                         'order_id': '3bd9a14d-dad4-4db3-a896-2e1bcad8355c',
                                         'order_placement_source': 'RETAIL_ADVANCED',
                                         'order_type': 'LIMIT',
                                         'outstanding_hold_amount': '0',
                                         'pending_cancel': False,
                                         'product_id': 'BTC-GBP',
                                         'product_type': 'SPOT',
                                         'reject_message': '',
                                         'reject_reason': 'REJECT_REASON_UNSPECIFIED',
                                         'settled': False,
                                         'side': 'BUY',
                                         'size_in_quote': False,
                                         'size_inclusive_of_fees': False,
                                         'status': 'CANCELLED',
                                         'time_in_force': 'GOOD_UNTIL_CANCELLED',
                                         'total_fees': '0',
                                         'total_value_after_fees': '0',
                                         'trigger_status': 'INVALID_ORDER_TYPE',
                                         'user_id': '0ad12a7e-147a-5672-9b22-9171a5c0762d'}],
                             'sequence': '0'})
