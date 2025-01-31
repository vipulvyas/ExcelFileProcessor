from datetime import datetime
from bson import ObjectId
from pymongo import MongoClient
from app.config import Config

client = MongoClient(Config.MONGO_URI)
db = client.get_default_database()

class ExcelDocument:
    excel_documents_collection = db.excel_documents
    excel_versions_collection = db.excel_versions

    @classmethod
    def create(cls, filename, data, columns):
        document = {
            'filename': filename,
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
            'current_version': 1
        }
        
        doc_id = cls.excel_documents_collection.insert_one(document).inserted_id
        
        # Create first version
        version = {
            'document_id': doc_id,
            'version': 1,
            'data': data,
            'columns': columns,
            'created_at': datetime.utcnow()
        }
        cls.excel_versions_collection.insert_one(version)
        
        return str(doc_id)

    @classmethod
    def get_latest(cls, document_id):
        doc = cls.excel_documents_collection.find_one({'_id': ObjectId(document_id)})
        if not doc:
            return None
            
        version = cls.excel_versions_collection.find_one({
            'document_id': ObjectId(document_id),
            'version': doc['current_version']
        })
        
        return {
            'id': str(doc['_id']),
            'filename': doc['filename'],
            'current_version': doc['current_version'],
            'data': version['data'],
            'columns': version['columns']
        }

    @classmethod
    def create_new_version(cls, document_id, data, columns, requestData):
        doc = cls.excel_documents_collection.find_one({'_id': ObjectId(document_id)})
        if not doc:
            return None
            
        new_version = doc['current_version'] + 1
        
        # Create new version
        version = {
            'document_id': ObjectId(document_id),
            'version': new_version,
            'data': data,
            'columns': columns,
            'requestData': requestData,
            'created_at': datetime.utcnow()
        }
        cls.excel_versions_collection.insert_one(version)
        
        # Update document
        cls.excel_documents_collection.update_one(
            {'_id': ObjectId(document_id)},
            {
                '$set': {
                    'current_version': new_version,
                    'updated_at': datetime.utcnow()
                }
            }
        )
        
        return new_version

    @classmethod
    def get_version(cls, document_id, version_number):
        version = cls.excel_versions_collection.find_one({
            'document_id': ObjectId(document_id),
            'version': version_number
        })
        
        if not version:
            return None
            
        return {
            'version': version['version'],
            'data': version['data'],
            'columns': version['columns']
        }

    @classmethod
    def remove_version(cls, document_id, version_number):
        cls.excel_versions_collection.delete_one({
            'document_id': ObjectId(document_id),
            'version': version_number
        })

        # Update document
        cls.excel_documents_collection.update_one(
            {'_id': ObjectId(document_id)},
            {
                '$set': {
                    'current_version': version_number - 1,
                    'updated_at': datetime.utcnow()
                }
            }
        )
        return True
