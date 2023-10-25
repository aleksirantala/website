// script.js
import React, { useState } from "react";
import ReactDOM from "react-dom";
import axios from "axios";

const App = () => {
  const [file, setFile] = useState(null);
  const [data, setData] = useState([]);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post("/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    setData(response.data); // Assuming the response contains the parsed Excel data.
  };

  return (
    <div>
      <h2>Upload an Excel File</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>

      <h2>Excel Data</h2>
      <table>
        <thead>
          <tr>
            {/* Assuming the data has headers "Column1", "Column2" */}
            <th>Column1</th>
            <th>Column2</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row, index) => (
            <tr key={index}>
              <td>{row.Column1}</td>
              <td>{row.Column2}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById("root"));
