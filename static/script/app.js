document.addEventListener("DOMContentLoaded", () => {
  // Reset button element
  const resetButton = document.getElementById("reset-game");

  // Reset the game for all solvers
  const handleResetAll = async () => {
    try {
      const response = await fetch("/reset-all", { method: "POST" });
      if (!response.ok) {
        throw new Error("Failed to reset the game.");
      }

      alert("Game reset successfully!");
      // Optionally reload the page
      location.reload();
    } catch (error) {
      console.error("Error resetting the game:", error);
      alert("An error occurred while resetting the game.");
    }
  };

  // Attach event listener to the reset button
  if (resetButton) {
    resetButton.addEventListener("click", handleResetAll);
  }
});
