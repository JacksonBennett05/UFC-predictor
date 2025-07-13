export async function simulateFight(fighter1, fighter2) {
    const response = await fetch(
      `http://localhost:5000/simulate?f1=${encodeURIComponent(fighter1)}&f2=${encodeURIComponent(fighter2)}`
    );
    if (!response.ok) throw new Error("Fight simulation failed.");
    return response.json();
  }
