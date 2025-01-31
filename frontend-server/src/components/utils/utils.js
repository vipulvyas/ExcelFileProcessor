import * as XLSX from 'xlsx';

export const handleExcelExport = (data) => {
    // Convert JSON data to worksheet
    const ws = XLSX.utils.json_to_sheet(data);

    // Create a new workbook and append the worksheet
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'Sheet1');

    // Export the workbook to a file
    XLSX.writeFile(wb, 'data.xlsx');
}
