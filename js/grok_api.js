const apiKey = process.env.GROK_API_KEY;

if (!apiKey) {
  console.error("API Key is missing. Set GROK_API_KEY in your environment.");
} else {
  console.log("API Key Loaded");
}

async function fetchGrokResponse() {
  try {
    const response = await fetch('https://api.x.ai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        model: 'grok-2-latest',
        messages: [{ role: 'user', content: 'Hello, Grok!' }]
      })
    });

    if (!response.ok) {
      throw new Error(`HTTP Error! Status: ${response.status}`);
    }

    const data = await response.json();
    console.log("Response:", data.choices[0].message.content);
  } catch (error) {
    console.error("Error fetching Grok response:", error);
  }
}

fetchGrokResponse();
