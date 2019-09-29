import json
from flask import current_app


class Serializer(object):
    __public__ = None
    "Must be implemented by implementors"

    def to_serializable_dict(self):
        dict = {}
        for public_key in self.__public__:
            value = getattr(self, public_key)
            # if value:
            dict[public_key] = value
        return dict

    @staticmethod
    def to_serializable_list(l):
        return [m.to_serializable_dict() for m in l]
