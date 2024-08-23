// app.js
document.getElementById("contentForm").addEventListener("submit", function(event){
    event.preventDefault();
    
    const inputText = document.getElementById("inputText").value;
    const numWords = document.getElementById("numWords").value;
    const contentType = document.getElementById("contentType").value;
    const errorDiv = document.getElementById("error");
    const responseDiv = document.getElementById("response");

    // Basic validation
    if (inputText === "" || isNaN(numWords)) {
        errorDiv.textContent = "Please enter a valid topic and number of words.";
        return;
    }

    // Clear previous error and response
    errorDiv.textContent = "";
    responseDiv.textContent = "";

    // Here, you can call your backend to generate content
    responseDiv.textContent = "Generating content..."; // Placeholder for actual content
});
