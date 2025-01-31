import axios from "axios";

const API_URL = process.env.REACT_APP_BASE_URL || "http://localhost:2000";
console.log(process.env.REACT_APP_BASE_URL)

const ApiService = {
  async uploadFile(file) {
    const formData = new FormData();
    formData.append("file", file);
    const response = await axios.post(`${API_URL}/api/document/upload`, formData);
    return response.data;
  },

  async performOperation(documentId, operation, params) {
    if (!documentId || !operation) {
      throw new Error("Invalid documentId or operation");
    }
    const payload = {
        operation: { 
            type: operation,
            params
        }
    }
    const response = await axios.post(`${API_URL}/api/document/${documentId}/operations`, payload);
    return response.data;
  }
};

export default ApiService;