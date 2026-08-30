from collections import namedtuple
CONFIG_NAME = b'trade_in_config'
ConversionRule = namedtuple(b'ConversionRule', [
 4, 5, 6, 7, 
 8, 9])
TradeInInfo = namedtuple(b'TradeInInfo', [b'sellGroupId', b'buyGroupId', b'conversionRule'])
