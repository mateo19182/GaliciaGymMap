import React, { useState, useEffect } from 'react';

const CSVFilter = () => {
  const [categories, setCategories] = useState([]);
  const [data, setData] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [selectedType, setSelectedType] = useState('');

  useEffect(() => {
    fetch('/data')
      .then((response) => response.json())
      .then((data) => {
        setCategories(data.map((item) => item.category));
        setData(data);
      })
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  const handleCategoryChange = (event) => {
    setSelectedCategory(event.target.value);
    setSelectedType(''); // Clear type selection when category changes
    const filteredData = data.filter((item) => item.category === event.target.value);
    setData(filteredData);

    // Populate types if category filter is changed and data is returned
    if (filteredData.length > 0) {
      const types = [...new Set(filteredData.map((item) => item.type))];
      setTypes(types);
    }
  };

  const handleTypeChange = (event) => {
    setSelectedType(event.target.value);
  };

  const renderData = () => {
    if (data.length > 0) {
      return data.map((item) => (
        <li key={item.location_link}>
          <a href={item.location_link} target="_blank">{item.location_link}</a> - {item.category} - {item.type}
        </li>
      ));
    } else {
      return <p>No data found.</p>;
    }
  };

  return (
    <div>
      <label htmlFor="categoryFilter">Category:</label>
      <select id="categoryFilter" value={selectedCategory} onChange={handleCategoryChange}>
        <option value="">Select a category</option>
        {categories.map((category) => (
          <option key={category} value={category}>{category}</option>
        ))}
      </select>

      <label htmlFor="typeFilter">Type:</label>
      <select id="typeFilter" value={selectedType} onChange={handleTypeChange}>
        <option value="">Select a type</option>
      </select>

      <div id="dataDisplay">{renderData()}</div>
    </div>
  );
};

export default CSVFilter;