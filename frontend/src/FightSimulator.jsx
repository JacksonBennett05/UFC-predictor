// // Custom interactive component for UI logic

// import { useState } from "react";
// // import { simulateFight } from "./api";
// // import { FaSearch } from "react-icons/fa";

// function FightSimulator() {
//   const [fighter1, setFighter1] = useState("");
//   const [fighter2, setFighter2] = useState("");
//   const [result, setResult] = useState(null);
//   const [err, setError] = useState("");

// //   const handleSimulate = async () => {
// //     try {
// //       const res = await simulateFight(fighter1, fighter2);
// //       setResult(res);
// //       setError("");
// //     } catch (err) {
// //       setResult(null);
// //       setError(err.message || "An error has occured");
// //     }
// //   };

//   const fetchData = (value) => {
//     fetch("https://jsonplaceholder.typicode.com/users")
//       .then((response) => response.json())
//       .then((json) => {
//         const results = json.filter((user) => {
//             return (
//                 value &&
//                 user &&
//                 user.name &&
//                 user.name.toLowerCase().includes(value)
//             );
//         })
//         console.log(json);
//       });
//   };

//   const handleChange = (value) => {
//     setFighter1(value);
//     fetchData(value);
//   };

//   return (
//     <div className="fight-sim">
//       <h1>UFC Fight Simulator</h1>
//       <div className="Fighter1-search">
//         <div className="input-wrapper">
//           {/* <FaSearch id="search-icon" /> */}
//           <input
//             placeholder="Fighter One Name"
//             value={fighter1}
//             onChange={(e) => handleChange(e.target.value)}
//           />
//         </div>
//         <div>Search Results</div>
//       </div>
//       <p>Ready to fight? Click "Fight" button below</p>
//       {/* <button onClick={handleSimulate}>Fight</button> */}
//     </div>
//   );
// }

// export default FightSimulator;

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
