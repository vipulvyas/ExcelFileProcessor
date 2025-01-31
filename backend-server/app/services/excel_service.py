import pandas as pd
import numpy as np

class ExcelService:
    @staticmethod
    def process_excel_file(file):
        """Process the uploaded Excel file and return the data"""
        df = pd.read_excel(file)
        return {
            'columns': df.columns.tolist(),
            'data': df.to_dict('records')
        }

    @staticmethod
    def add_column(data, columns, expression):
        """Add a new column based on expression"""
        df = pd.DataFrame(data)
        
        try:
            # Verify required columns exist
            if expression['columnName1'] not in df.columns or expression['columnName2'] not in df.columns:
                raise ValueError(f"DataFrame must contain both {expression['columnName1']} and {expression['columnName2']} columns")

            # Convert columns to numeric, replacing any non-numeric values with NaN
            df[expression['columnName1']] = pd.to_numeric(df[expression['columnName1']], errors='coerce')
            df[expression['columnName2']] = pd.to_numeric(df[expression['columnName2']], errors='coerce')

            # Add new column
            df[expression['newColumnName']] = df[expression['columnName1']] + df[expression['columnName2']]

            return {
                'columns': df.columns.tolist(),
                'data': df.to_dict('records')
            }
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {str(e)}")

    @staticmethod
    def filter_rows(data, columns, condition):
        """Filter rows based on condition"""
        df = pd.DataFrame(data)

        try:
            filtered_df = df.query(condition)
            return {
                'columns': columns,
                'data': filtered_df.to_dict('records')
            }
        except Exception as e:
            raise ValueError(f"Error applying filter: {str(e)}")

    @staticmethod
    def combine_columns(data, columns, combination):
        """Combine two columns into one"""
        df = pd.DataFrame(data)

        try:
            df[combination['newColumnName']] = df[combination['columnName1']].astype(str) + \
                                          combination['separator'] + \
                                          df[combination['columnName2']].astype(str)
            return {
                'columns': df.columns.tolist(),
                'data': df.to_dict('records')
            }
        except Exception as e:
            raise ValueError(f"Error combining columns: {str(e)}")

    
