# Excel File Processor

Excel File Processor is a web application that allows users to upload an Excel file and perform various operations such as adding a new column (Sum of two columns), filtering rows, combining columns and undo operation. The application dynamically updates the displayed data in a table format.

## Features

- Upload and process Excel files (.xlsx, .csv)
- Perform operations:
  - Add new columns (Sum of two columns)
  - Filter rows
  - Combine columns
  - Undo operation
  - Download updated file
- Display processed data dynamically in a tabular format
- Frontend built using **React.js** with **Semantic UI React** and **SCSS** for styling
- Backend powered by **Flask** for data processing
- **MongoDB** used for storage

## Tech Stack

- **Frontend**: React.js, Semantic UI React, SCSS
- **Backend**: Flask, Pandas
- **Storage**: MongoDB

## Installation & Setup

### Backend (Flask)

1. Clone the repository:
   ```sh
   git clone https://github.com/vipulvyas/ExcelFileProcessor.git
   cd ExcelFileProcessor/backend-server
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask server:
   ```sh
   flask run --port 2000
   ```
   The backend will be available at `http://127.0.0.1:2000`

### Frontend (React.js)

1. Navigate to the frontend directory:
   ```sh
   cd ../frontend-server
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm start
   ```
   The frontend will be available at `http://localhost:3000`

## API Endpoints

### Upload an Excel File
#### Endpoint: `POST /api/document/upload`
##### Payload: 
```json
{    
  "file": "<Excel file>" // in form data
}
```
##### Response:
```json
{
  "message": "File uploaded successfully",
  "document_id": "<document_id>",
  "data": [<processed data>],
  "columns": [<column names>]
}
```

### Perform an Operation on a Document
#### Endpoint: `POST /api/document/<document_id>/operations`
##### Payload Examples:

**Add Column**
```json
{
  "type": "addColumn",
  "params": {
      "columnName1": "Price",
      "columnName2": "Tax",
      "newColumnName": "Total"
  }
}
```

**Filter Rows**
```json
{
  "type": "filterRows",
  "params": {
      "condition": "Price > 70000"
  }
}
```

**Combine Columns**
```json
{
  "type": "combineColumns",
  "params": {
      "columnName1": "Price",
      "columnName2": "Tax",
      "separator": " % ",
      "newColumnName": "Price % Tax"
  }
}
```

**Undo Operation**
```json
{
  "type": "undo",
  "params": {}
}
```

##### Response:
```json
{
  "message": "Operation completed successfully",
  "version": <new_version>,
  "data": [<updated data>],
  "columns": [<updated columns>]
}
```

### Retrieve the Latest Document Version
#### Endpoint: `GET /api/document/<document_id>/latest`
##### Response:
```json
{
  "document_id": "<document_id>",
  "version": <latest_version>,
  "data": [<latest data>],
  "columns": [<latest columns>]
}
```

### Retrieve a Specific Document Version
#### Endpoint: `GET /api/document/<document_id>/versions/<int:version>`
##### Response:
```json
{
  "document_id": "<document_id>",
  "version": <requested_version>,
  "data": [<versioned data>],
  "columns": [<versioned columns>]
}
```

| Method | Endpoint                                             | Description                          |
| ------ | ---------------------------------------------------- | ------------------------------------ |
| POST   | `/api/document/upload`                               | Upload an Excel file                 |
| POST   | `/api/document/<document_id>/operations`             | Perform an operation on a document   |
| GET    | `/api/document/<document_id>/latest`                 | Retrieve the latest document version |
| GET    | `/api/document/<document_id>/versions/<int:version>` | Retrieve a specific document version |


## Running Tests

To run tests, run the following command in backend-server folder

```bash
  pytest
```


## Demo

Check out the demo video: [Demo.mp4](./Demo.mp4)

## Author

Developed by **Vipul Vyas**

---
