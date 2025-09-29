import { useState } from "react";

function FighterSearch({ onSelect, corner }) {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const fetchFighters = async (value) => {
    if (!value) {
      console.log("Querying for:", value);
      setResults([]);
      return;
    }

    setLoading(true);
    setError("");

    try {
      const response = await fetch(
        `http://127.0.0.1:5000/fighters?search=${value}`
      );
      if (!response.ok) throw new Error("Failed to fetch fighters");

      const data = await response.json();
      setResults(data);
      console.log("Fetched fighters:", data);
    } catch (err) {
      setError(err.message || "Error fetching fighters");
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    const value = e.target.value;
    console.log("Querying for:", value);
    setQuery(value);
    fetchFighters(value.toLowerCase());
  };

  const handleSelect = (name) => {
    setQuery(name);
    setResults([]);
    onSelect(name);
  };

  return (
    <div className="fighter-search" style={{ position: "relative" }}>
      <input
      className={`fighter-input ${corner}-corner`}
        type="text"
        placeholder="Search Fighter"
        value={query}
        onChange={handleChange}
        style={{ width: "350px", padding: "8px" }}
      />
      {loading && <div>Loading...</div>}
      {error && <div style={{ color: "red" }}>{error}</div>}
      {results.length > 0 && (
        <ul
          className="search-results"
          style={{
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
