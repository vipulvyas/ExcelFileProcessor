import React, { useState } from "react";
import { Button, Input } from "semantic-ui-react";

const FileUpload = ({ onFileUpload }) => {
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (event) => {
        if (event.target.files && event.target.files[0]) {
            const file = event.target.files[0];
            const fileType = file.type;

            if (
                fileType === "application/vnd.ms-excel" || // .xls
                fileType === "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" // .xlsx
            ) {
                setSelectedFile(file);
            } else {
                alert("Please upload a valid Excel file (.xls or .xlsx)");
                event.target.value = null; // Reset file input
            }
        }
    };

    const handleUpload = () => {
        if (!selectedFile) {
            alert("Please select an Excel file before uploading.");
            return;
        }
        onFileUpload(selectedFile);
    };

    return (
        <div className="file-upload">
            <div className="upload-zone">
                <Input
                    type="file"
                    accept=".xls, .xlsx"
                    className="file-upload-input"
                    onChange={handleFileChange}
                />
            </div>
            <Button className="upload-button" onClick={handleUpload} primary>
                Upload
            </Button>
        </div>
    );
};

export default FileUpload;
