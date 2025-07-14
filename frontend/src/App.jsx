import React from "react";
import FightSimulator from "./FightSimulator";
import "./App.css";

function App() {
  // const [results, setResults] = useState([]);

  return (
    <div className="App">
      <div className="search-bar">
        <FightSimulator />
      </div>
    </div>
  );
}

export default App;
