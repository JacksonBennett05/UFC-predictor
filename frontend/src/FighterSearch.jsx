import { useState } from "react";

function FighterSearch({ onSelect }) {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Fetch matching fighters from backend as user types
  const fetchFighters = async (value) => {
    if (!value) {
      console.log("Querying for:", value);
      setResults([]);
      return;
    }

    setLoading(true);
    setError("");

    try {
      // Call backend API to get fighter list filtered by name
      // Adjust URL and query params as your backend supports
      const response = await fetch(
        `http://127.0.0.1:5000/fighters?search=${value}`
      );
      if (!response.ok) throw new Error("Failed to fetch fighters");

      const data = await response.json(); // Assume returns array of fighters
      setResults(data);
      console.log("Fetched fighters:", data);
    } catch (err) {
      setError(err.message || "Error fetching fighters");
    } finally {
      setLoading(false);
    }
  };

  // Handle input change
  const handleChange = (e) => {
    const value = e.target.value;
    console.log("Querying for:", value);
    setQuery(value);
    fetchFighters(value.toLowerCase());
  };

  // Handle selecting a fighter from the list
  const handleSelect = (name) => {
    setQuery(name);
    setResults([]);
    onSelect(name);
  };

  return (
    <div className="fighter-search" style={{ position: "relative" }}>
      <input
        type="text"
        placeholder="Search Fighter"
        value={query}
        onChange={handleChange}
        style={{ width: "300px", padding: "8px" }}
      />
      {loading && <div>Loading...</div>}
      {error && <div style={{ color: "red" }}>{error}</div>}
      {results.length > 0 && (
        <ul
          className="search-results"
          style={{
            position: "absolute",
            backgroundColor: "#fff",
            border: "1px solid #ccc",
            listStyle: "none",
          }}
        >
          {results.map((fighter, idx) => (
            <li
              key={idx}
              onClick={() => handleSelect(fighter)}
              style={{ padding: "8px", cursor: "pointer" }}
            >
              {fighter}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default FighterSearch;
