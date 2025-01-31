import React, { useState } from "react";
import { Container, Header } from "semantic-ui-react";
import FileUpload from "./components/FileUpload";
import DataTable from "./components/DataTable";
import OperationsPanel from "./components/OperationsPanel";
import ApiService from "./services/apiService";
import "./styles/App.scss";
import 'semantic-ui-css/semantic.min.css';

const App = () => {
  const [tableData, setTableData] = useState([]);
  const [documentId, setDocumentId] = useState(null);
  const [documentVersion, setDocumentVersion] = useState(null);
  const [showLoader, setShowLoader] = useState(false);

  const handleFileUpload = async (file) => {
    try {
      setShowLoader(true);
      const data = await ApiService.uploadFile(file);
      setDocumentId(data.document_id);
      setTableData(data);
    } catch (error) {
      console.error("Error uploading file:", error);
    } finally {
      setShowLoader(false);
    }
  };

  const handleOperation = async (operation, params) => {
    try {
      setShowLoader(true);
      const data = await ApiService.performOperation(documentId, operation, params);
      setDocumentVersion(data.version);
      setTableData(data);
    } catch (error) {
      console.error("Error performing operation:", error);
    } finally {
      setShowLoader(false);
    }
  };

  return (
    <Container className="app-container">
      <Header as="h1" className="app-header">Excel File Processor</Header>
      <FileUpload onFileUpload={handleFileUpload} />
      <OperationsPanel onOperation={handleOperation} documentVersion={documentVersion} />
      <DataTable data={tableData} showLoader={showLoader}/>
    </Container>
  );
};

export default App;