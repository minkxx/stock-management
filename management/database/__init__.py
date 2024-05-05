from pymongo.collection import Collection as MongoCollection
from pymongo.mongo_client import MongoClient

from management.database.exceptions import CollectionNameError


class Database:
    def __init__(self, uri: str, db_name: str) -> None:
        """
        :param uri: The MongoDB Atlas uri for connection to database

        :param db_name: The name of database to be created
        """
        self.__client = MongoClient(uri)
        self.__database = self.__client[db_name]

    def collection(self, collection_name: str):
        """
        :param collection_name: The collection name to be created or used for CRUD operations in database

        :return:- An instance of ~ pymongo.collection.Collection .
        """
        collection = self.__database[collection_name]
        return collection

    def get_all_collections(self):
        """
        :return:- All the names of collections in a database .
        """
        return self.__database.list_collection_names()

    def add_items(self, collection: MongoCollection, document):
        result = collection.insert_one(document)
        return result

    def remove_items(self):
        pass

    def __collectionExists(self, collection_name):
        if collection_name in self.get_all_collections():
            raise CollectionNameError(
                f"CollectionNameError: '{collection_name}' already exits as collection. Try other names!"
            )
