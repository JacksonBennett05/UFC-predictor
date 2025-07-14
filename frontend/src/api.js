const API_BASE_URL = "http://127.0.0.1:5000";

export async function simulateFight(fighter1, fighter2) {
  try {
    const response = await fetch(`${API_BASE_URL}/simulate`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ fighter1, fighter2 })
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const data = await response.json();

    return data;
  } catch (error) {
    console.error("Error calling simulate API:", error);
    throw error;
  }
}
