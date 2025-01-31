from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app.models.excel_document import ExcelDocument
from app.services.excel_service import ExcelService
import magic
import os

ALLOWED_EXCEL_MIMES = [
    'application/vnd.ms-excel',                                       # .xls
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', # .xlsx
]

def validate_excel_file(file):
    if not file:
        return False
    
    # Get the mime type of the file using python-magic
    mime = magic.from_buffer(file.read(2048), mime=True)
    # Reset file pointer
    file.seek(0)
    
    return mime in ALLOWED_EXCEL_MIMES

api = Blueprint('api', __name__)
excel_service = ExcelService()

@api.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if not validate_excel_file(file):
        return jsonify({'error': 'Invalid file type. Please upload an Excel file'}), 400

    try:
        # Process the file
        result = excel_service.process_excel_file(file)
        
        # Store in MongoDB
        document_id = ExcelDocument.create(
            filename=secure_filename(file.filename),
            data=result['data'],
            columns=result['columns']
        )
        
        return jsonify({
            'message': 'File uploaded successfully',
            'document_id': document_id,
            'data': result['data'],
            'columns': result['columns']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/api/document/<document_id>/operations', methods=['POST'])
def perform_operation(document_id):
    data = request.json
    operation = data.get('operation')
    
    # Get current document state
    document = ExcelDocument.get_latest(document_id)

    if not document:
        return jsonify({'error': 'Document not found'}), 404
    
    try:
        result = None
        if operation['type'] == 'addColumn':
            result = excel_service.add_column(
                document['data'],
                document['columns'],
                operation['params']
            )
        elif operation['type'] == 'filterRows':
            result = excel_service.filter_rows(
                document['data'],
                document['columns'],
                operation['params']['condition']
            )
        elif operation['type'] == 'combineColumns':
            result = excel_service.combine_columns(
                document['data'],
                document['columns'],
                operation['params']
            )
        elif operation['type'] == 'undo':
            result = ExcelDocument.get_version(document_id, document['current_version'] - 1)
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        if operation['type'] == 'undo': 
            new_version = document['current_version'] - 1
            ExcelDocument.remove_version(
                document_id,
                document['current_version']
            )
            
        else:
        # Create new version
            new_version = ExcelDocument.create_new_version(
                document_id,
                result['data'],
                result['columns'],
                requestData=data
            )
        
        return jsonify({
            'message': 'Operation completed successfully',
            'version': new_version,
            'data': result['data'],
            'columns': result['columns']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/api/document/<document_id>/versions/<int:version>', methods=['GET'])
def get_version(document_id, version):
    result = ExcelDocument.get_version(document_id, version)
    if not result:
        return jsonify({'error': 'Version not found'}), 404
    
    return jsonify(result)

@api.route('/api/document/<document_id>/latest', methods=['GET'])
def get_latest(document_id):
    result = ExcelDocument.get_latest(document_id)
    if not result:
        return jsonify({'error': 'Document not found'}), 404
    
    return jsonify(result)
