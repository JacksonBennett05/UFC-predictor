import { useState } from "react";
import FighterSearch from "./FighterSearch";
import { simulateFight } from "./api";

function FightSimulator() {
  const [fighter1, setFighter1] = useState("");
  const [fighter2, setFighter2] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleSimulate = async () => {
    if (!fighter1 || !fighter2) {
      setError("Please select both fighters");
      return;
    }

    try {
      const res = await simulateFight(fighter1, fighter2);
      setResult(res);
      setError("");
    } catch (err) {
      setResult(null);
      setError(err.message || "An error occurred");
    }
  };

  return (
    <div className="fight-sim">
      <div className="title">
        <h1>UFC Fight Simulator</h1>
      </div>

      <div className="search-container">
        <div className="fighter-column1">
          <label>Fighter 1</label>
          <FighterSearch onSelect={setFighter1} />
        </div>

        <div className="fighter-column2">
          <label>Fighter 2</label>
          <FighterSearch onSelect={setFighter2} />
        </div>
      </div>

      <button onClick={handleSimulate}>Fight</button>

      {result && (
        <div className="result">
          <h2>🏆 Winner: {result.winner}</h2>
          <p>{result.explanation}</p>
        </div>
      )}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}

export default FightSimulator;
