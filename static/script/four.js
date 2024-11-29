async function sendFeedback() {
  const feedback = parseInt(document.getElementById("feedback").value);
  if (isNaN(feedback)) {
    alert("Please enter a valid number!");
    return;
  }
  const loadingElement = document.getElementById("loading");
  loadingElement.style.display = "block"; // Show the loading spinner

  try {
    // Simulate an asynchronous request (replace with your actual logic)
    await new Promise((resolve) => setTimeout(resolve, 1000)); // Simulate delay

    // Example of updating DOM with feedback (replace with actual response handling)
    document.getElementById(
      "words"
    ).innerText = `Feedback received: ${feedback}`;
  } catch (error) {
    console.error("Error processing feedback:", error);
  } finally {
    loadingElement.style.display = "none"; // Hide the loading spinner
  }
  const response = await fetch("/four/guess", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ feedback }),
  });
  const data = await response.json();
  if (response.ok) {
    document.getElementById(
      "remaining"
    ).textContent = `Remaining words: ${data.remaining_words}`;
    document.getElementById(
      "guess"
    ).textContent = `Next guess: ${data.next_guess}`;
    if (data.possible_words.length > 0) {
      document.getElementById(
        "words"
      ).textContent = `Possible words: ${data.possible_words.join(", ")}`;
    } else {
      document.getElementById("words").textContent =
        "Too many possible words to display.";
    }
  } else {
    alert(data.error || "An error occurred!");
  }
}
