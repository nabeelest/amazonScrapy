import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([]); // State to store JSON data
  const [query, setQuery] = useState("headphones"); // Default category

  // Fetch the JSON data based on the selected category
  useEffect(() => {
    fetch(`/output/${query}.json`) // Corrected fetch path
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch data");
        }
        return response.json();
      })
      .then((data) => setData(data))
      .catch((error) => console.error("Error fetching data:", error));
  }, [query]);

  return (
    <div>
      <h1>Amazon Product Data</h1>
      {/* Dropdown to select the category */}
      <select onChange={(e) => setQuery(e.target.value)}>
        <option value="headphones">Headphones</option>
        <option value="laptops">Laptops</option>
        <option value="smartphones">Smartphones</option>
        <option value="smartwatches">Smartwatches</option>
        <option value="tablets">Tablets</option>
      </select>

      {/* Display data in a table */}
      <table border="1" style={{ marginTop: "20px", width: "100%" }}>
        <thead>
          <tr>
            <th>Title</th>
            <th>Total Reviews</th>
            <th>Price</th>
            <th>Image</th>
          </tr>
        </thead>
        <tbody>
          {data.length > 0 ? (
            data.map((item, index) => (
              <tr key={index}>
                <td>{item.title || "N/A"}</td>
                <td>{item.total_reviews || "N/A"}</td>
                <td>{item.price || "N/A"}</td>
                <td>
                  <img
                    src={item.image_url}
                    alt={item.title}
                    width="50"
                    style={{ borderRadius: "5px" }}
                  />
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4" style={{ textAlign: "center" }}>
                No data available for the selected category.
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default App;
