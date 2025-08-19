import { simulateFight } from "./api.js";

async function testSimulateFight() {
  try {
    const result = await simulateFight("Fighter A", "Fighter B");
    console.log("Simulation result:", result);
  } catch (error) {
    console.error("Error during simulation:", error);
  }
}

testSimulateFight();