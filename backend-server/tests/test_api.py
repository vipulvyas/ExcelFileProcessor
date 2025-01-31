import pytest
import json
from app import create_app
from io import BytesIO
import pandas as pd

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def sample_excel():
    def create_excel(data=None):
        if data is None:
            data = {
                'Product': ['A', 'B', 'C'],
                'Price': [100, 200, 300],
                'Tax': [10, 20, 30]
            }
        df = pd.DataFrame(data)
        excel_file = BytesIO()
        df.to_excel(excel_file, index=False)
        excel_file.seek(0)
        return excel_file
    return create_excel

class TestFileUpload:
    def test_successful_upload(self, client, sample_excel):
        excel_file = sample_excel()
        data = {'file': (excel_file, 'test.xlsx')}
        
        response = client.post('/api/document/upload',
                             content_type='multipart/form-data',
                             data=data)
        
        assert response.status_code == 200
        assert 'document_id' in response.json
        assert isinstance(response.json['document_id'], str)

    def test_upload_without_file(self, client):
        response = client.post('/api/document/upload',
                             content_type='multipart/form-data',
                             data={})
        
        assert response.status_code == 400
        assert 'error' in response.json

    def test_upload_invalid_file_format(self, client):
        data = {'file': (BytesIO(b'invalid data'), 'test.txt')}
        
        response = client.post('/api/document/upload',
                             content_type='multipart/form-data',
                             data=data)
        
        assert response.status_code == 400
        assert 'error' in response.json

class TestColumnOperations:
    @pytest.fixture
    def uploaded_document_id(self, client, sample_excel):
        excel_file = sample_excel()
        data = {'file': (excel_file, 'test.xlsx')}
        response = client.post('/api/document/upload',
                             content_type='multipart/form-data',
                             data=data)
        return response.json['document_id']

    def test_add_column_success(self, client, uploaded_document_id):
        operation = {
            'operation': {
                'type': 'addColumn',
                'params': {
                    'columnName1': "Price",
                    'columnName2': "Tax",
                    'newColumnName': "Total"
                }
            }
        }
        
        response = client.post(f'/api/document/{uploaded_document_id}/operations',
                             json=operation)
        
        assert response.status_code == 200
        assert 'Total' in response.json['columns']
        assert 'data' in response.json

