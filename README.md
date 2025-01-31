# Excel File Processor

&#x20;&#x20;

Excel File Processor is a web application that allows users to upload an Excel file and perform various operations such as adding a new column, filtering rows, combining columns and undo operation. The application dynamically updates the displayed data in a table format.

## Features

- Upload and process Excel files (.xlsx, .csv)
- Perform operations:
  - Add new columns
  - Filter rows
  - Combine columns
  - Undo operation
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
   cd ExcelFileProcessor/backend
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
   cd ../frontend
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

| Method | Endpoint                                             | Description                          |
| ------ | ---------------------------------------------------- | ------------------------------------ |
| POST   | `/api/document/upload`                               | Upload an Excel file                 |
| POST   | `/api/document/<document_id>/operations`             | Perform an operation on a document   |
| GET    | `/api/document/<document_id>/latest`                 | Retrieve the latest document version |
| GET    | `/api/document/<document_id>/versions/<int:version>` | Retrieve a specific document version |

## Demo

Check out the demo video: [Demo.webm](./Demo.webm)

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Developed by **Vipul Vyas**
