from pymongo.collection import Collection as MongoCollection
from pymongo.mongo_client import MongoClient

from management.database.exceptions import CollectionNameError


class Database:
    def __init__(self, uri: str, db_name: str) -> None:
        """
        Creates a database on MongoDB and provides methods to use it.

        :param uri: The MongoDB Atlas uri for connection to database

        :param db_name: The name of database to be created
        """
        self.__client = MongoClient(uri)
        self.__database = self.__client[db_name]

    def collection(self, collection_name: str):
        """
        Creates a collection in the database.

        :param collection_name: The collection name to be created or used for CRUD operations in database

        :return:- An instance of ~pymongo.collection.Collection .
        """
        collection = self.__database[collection_name]
        return collection

    def get_all_collections(self):
        """
        Get all the collections in the database.

        :return:- All the names of collections in a database .
        """
        return self.__database.list_collection_names()

    def delete_collection(self, collection_name):
        """
        Deletes a collection from a database if it exists else raise CollectionNameError

        :param collection_name: The name of the collection that has to be deleted
        """
        try:
            self.__collectionNotExists(collection_name=collection_name)
            result = self.__database.drop_collection(collection_name)
            return result
        except CollectionNameError as cne:
            print(cne)

    def add_item(self, document, collection: MongoCollection):
        """
        Adds a document to a collection

        :param document: The document to be added
        :param collection: The collection to which the document is to be added

        :return:- InsertOneResult 
        """
        result = collection.insert_one(document)
        return result

    def update_item(self, item_name: str, collection: MongoCollection, update_document, update_field=None, value=None):
        query = {item_name: {"$exists": True}}
        if update_field and value:
            update_query = {"$set": {f"{item_name}.{update_field}": value}}
        else:
            update_query = {"$set": {f"{item_name}": update_document}}
        item = collection.update_one(query, update_query)
        return item 

    def delete_item(self, item_name, collection: MongoCollection):
        query = {item_name: {"$exists": True}}
        result = collection.delete_one(query)
        return result

    def get_item(self, item_name, collection: MongoCollection):
        query = {item_name: {"$exists": True}}
        item = collection.find_one(query)
        return item

    def get_all_items(self, collection: MongoCollection):
        data = collection.find()
        return [x for x in data]

    def __collectionExists(self, collection_name):
        if collection_name in self.get_all_collections():
            raise CollectionNameError(
                f"CollectionNameError: '{collection_name}' already exits as collection. Try other names!"
            )

    def __collectionNotExists(self, collection_name):
        if collection_name not in self.get_all_collections():
            raise CollectionNameError(
                f"CollectionNameError: '{collection_name}' already doestn't exits as collection."
            )
