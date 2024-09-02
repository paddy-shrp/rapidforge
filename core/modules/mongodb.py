import time
import logging

from pymongo.mongo_client import MongoClient

from utils import settings, paths

logging.basicConfig(filename=paths.get_logs_path("internal.log"), 
                    level=logging.INFO,
                     encoding="utf-8",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

mongodb_set = settings.get_module_settings("mongodb", 
                                           {
                                               "uri": "",
                                               "password": ""
                                           })

uri = mongodb_set["uri"]
uri = uri.replace("<password>", mongodb_set["password"])

client = MongoClient(uri)

try:
    client.admin.command('ping')
    logging.info("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    logging.exception(e)

# Generic Getters

def get_points(db_name, cl_name, query=None, with_id=True):
    try:
        id_addon = {}
        if not with_id: id_addon = {"_id": 0}
        results = client.get_database(db_name).get_collection(cl_name).find(query, id_addon)
        return [r for r in results]
    except Exception as e:
        logging.exception(e)

def get_point(db_name, cl_name, id):
    try:
        return client.get_database(db_name).get_collection(cl_name).find_one(get_id_filter(id))
    except Exception as e:
        logging.exception(e)
        
def get_document_count(db_name, cl_name, query={}):
    try:
        return client.get_database(db_name).get_collection(cl_name).count_documents(query)
    except Exception as e:
        logging.exception(e)
        return -1

# Generic Updates

def add_point(db_name, cl_name, data, id=None, with_timestamp=False):
    
    if id != None: data["_id"] = id
    if with_timestamp: data["timestamp"] = int(time.time())
    
    try:
        client.get_database(db_name).get_collection(cl_name).insert_one(data)
        return True
    except Exception as e:
        logging.exception(e)
        return False
    
def update_point(db_name, cl_name, id=None, data=None):
    update = { "$set": data }
    try:
        client.get_database(db_name).get_collection(cl_name).update_one(get_id_filter(id), update)
        return True
    except Exception as e:
        logging.exception(e)
        return False
    
def remove_point(db_name, cl_name, id=None):
    try:
        client.get_database(db_name).get_collection(cl_name).delete_one(get_id_filter(id))
        return True
    except Exception as e:
        logging.exception(e)
        return False
    
def remove_points(db_name, cl_name, query={}):
    try:
        client.get_database(db_name).get_collection(cl_name).delete_many(query)
        return True
    except Exception as e:
        logging.exception(e)
        return False

def get_id_filter(id):
    return {"_id": id}
