class PromoDataParser(object):
    _ALL_FIELDS_MAP = {b'unread': b'count', 
       b'sent_at': b'timestamp', 
       b'data': b'lastPromo'}
    _DATA_FIELDS_MAP = {b'id': b'promoID', 
       b'promo_name': b'description', 
       b'image': b'image', 
       b'promoscreen_url': b'url', 
       b'version_name': b'version', 
       b'video': b'video', 
       b'expiration_time': b'finishTime', 
       b'type': b'promoType', 
       b'slug': b'slug'}
    _DATA_FIELD_NAME = b'data'
    _INT_FIELDS = (b'id', b'unread', b'sent_at')
    _INT64_FIELDS = (b'expiration_time',)

    @classmethod
    def parse(cls, data):
        return cls.__abstractParse(data, cls.__extractFromArray)

    @classmethod
    def parseXML(cls, data):
        return cls.__abstractParse(data, cls.__extractFromXML)

    @classmethod
    def __abstractParse(cls, data, extractor):
        result = {}
        promoData = {}
        for source, target in cls._ALL_FIELDS_MAP.iteritems():
            if source == cls._DATA_FIELD_NAME:
                promoData = result[target] = {}
            else:
                result[target] = extractor(data, source)

        promoDataSource = data[cls._DATA_FIELD_NAME]
        for source, target in cls._DATA_FIELDS_MAP.iteritems():
            promoData[target] = extractor(promoDataSource, source)

        return result

    @classmethod
    def __extractFromXML(cls, data, key):
        if key in cls._INT_FIELDS:
            return data.readInt(key)
        if key in cls._INT64_FIELDS:
            return data.readInt64(key)
        return data.readString(key)

    @staticmethod
    def __extractFromArray(data, key):
        return data.get(key)
