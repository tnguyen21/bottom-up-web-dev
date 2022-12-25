// demo code for manipulating the DOM
function createHeading() {
  const heading = document.createElement("h1");
  const headingText = document.createTextNode("Big Head!");
  heading.appendChild(headingText);
  document.body.appendChild(heading);
}

// demo code for manipulating text content
function manipulateText() {
  const story = document.body.querySelector(".story");

  const setText = document.body.querySelector("#set-text");
  setText.addEventListener("click", () => {
    story.textContent = "It was a dark and stormy night...";
  });

  const clearText = document.body.querySelector("#clear-text");
  clearText.addEventListener("click", () => {
    story.textContent = "";
  });
}
