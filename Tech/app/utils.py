from bson import ObjectId


class MongoIdConverter:

    @staticmethod
    def id_to_string(data):

        if isinstance(data, list):
            for rec in data:
                MongoIdConverter.__to_string(rec)
        elif isinstance(data, dict):
            MongoIdConverter.__to_string(data)
        elif isinstance(data, ObjectId):
            data = {'_id': data}
            MongoIdConverter.__to_string(data)

        return data

    @classmethod
    def __to_string(cls, record):

        if '_id' in record:
            record['id'] = str(record['_id'])
            del record['_id']
