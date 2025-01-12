
import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([]);
  const [query, setQuery] = useState("headphones");

  useEffect(() => {
    fetch(`/output/${query}.json`)
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error("Error fetching data:", error));
  }, [query]);

  return (
    <div>
      <h1>Amazon Product Data</h1>
      <select onChange={(e) => setQuery(e.target.value)}>
        <option value="headphones">Headphones</option>
        <option value="smartphones">Smartphones</option>
      </select>
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Total Reviews</th>
            <th>Price</th>
            <th>Image</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item.title}</td>
              <td>{item.total_reviews}</td>
              <td>{item.price}</td>
              <td>
                <img src={item.image_url} alt={item.title} width="50" />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
