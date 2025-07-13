import React, { useState, useEffect } from "react";

// Top-level React component

export default function App() {
  const [fighters, setFighters] = useState([]);
  const [fighter1, setFighter1] = useState("");
  const [fighter2, setFighter2] = useState("");
  const [result, setResult] = useState(null);

  // Load fighter list on mount
  useEffect(() => {
    fetch("/api/fighters")  // your backend route to get all fighters
      .then((res) => res.json())
      .then(setFighters)
      .catch(console.error);
  }, []);

  const handleSimulate = async () => {
    if (!fighter1 || !fighter2) return alert("Select both fighters!");

    const res = await fetch(`/api/simulate?f1=${encodeURIComponent(fighter1)}&f2=${encodeURIComponent(fighter2)}`);
    const data = await res.json();
    setResult(data);
  };
  return (
    <h1> TEST 2 </h1>
  )
}