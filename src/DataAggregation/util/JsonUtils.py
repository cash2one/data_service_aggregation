import json

def jsonStr2object(data):
    if isinstance(data, list):
        return [jsonStr2object(i) for i in data]
    elif isinstance(data, tuple):
        return tuple([jsonStr2object(i) for i in data])
    elif isinstance(data, dict):
        return Storage({jsonStr2object(k): jsonStr2object(data[k]) for k in data.keys()})
    else:
        try:
            obj = json.loads(data)
            if obj == data:
                return data
        except:
            return data
        return jsonStr2object(obj)


class Storage(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __repr__(self):
        return '<Storage ' + dict.__repr__(self) + '>'


class Struct:
    def __init__(self, **entries): 
        self.__dict__.update(entries)
