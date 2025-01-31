# utils/validator.py
import magic

ALLOWED_EXCEL_MIMES = [
    'application/vnd.ms-excel',                                       # .xls
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', # .xlsx
]

def validate_excel_file(file):
    """
    Validates if the uploaded file is a valid Excel file by checking its MIME type
    Args:
        file: The uploaded file object to validate
    Returns:
        bool: True if file is a valid Excel file, False otherwise
    """
    if not file:
        return False
    
    # Get the mime type of the file using python-magic
    mime = magic.from_buffer(file.read(2048), mime=True)
    # Reset file pointer
    file.seek(0)
    
    return mime in ALLOWED_EXCEL_MIMES
