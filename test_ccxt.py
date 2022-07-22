import ccxt
from exchange_config import api,secret

# for exchange binance 

# this method instantiate the exchange

exchange_binance = ccxt.binance({'has' :{'create_order' : True} ,'apiKey': api['api_binance'], 'secret': secret['secret_binance'] })
print(exchange_binance)

# this method check the credential required

exc_cre = exchange_binance.checkRequiredCredentials()
print(exc_cre)

# this method fetch he the balance of user from exchange

balance = exchange_binance.fetch_balance()
print(balance['total']['BUSD'])

# this method show all the transection made by user 

transfer = exchange_binance.fetch_transfers()
print(transfer)

# this method shows all the orders 

orders = exchange_binance.fetch_orders(symbol='BNBBTC')
print(orders)

# this method place a buy order for the user

# order = exchange_binance.create_order(symbol='SHIBBUSD', amount= 0.1,type='market',side='buy',params= {'trading_agreement': 'agree'})#,price=0.01
# print(order)

# mk_order=exchange_binance.create_order(symbol='BNBBUSD',amount=0.1,type='market',side='buy',params= {'trading_agreement': 'agree'})
# print(mk_order)


# for exchange wazirx

exchange_wazirx = ccxt.wazirx({'has' :{'create_order' : True} ,'apiKey': api['api_wazirx'], 'secret': secret['secret_wazirx'] })
print(exchange_wazirx)

exc_cre = exchange_wazirx.checkRequiredCredentials()
print(exc_cre)

balance = exchange_wazirx.fetch_balance()
print(balance['total'])

# transfer = exchange_wazirx.fetch_trades()
# print(transfer)

orders = exchange_wazirx.fetch_orders(symbol='BTC/INR')
print(orders)

# order = exchange_wazirx.create_order(symbol='BNBBTC', amount= 1,type='market',side='buy',params= {'trading_agreement': 'agree'})#,price=0.01
# print(order)