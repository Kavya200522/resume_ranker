const rankBtn = document.getElementById("rankBtn");
const loader = document.getElementById("loader");
const progressBar = document.getElementById("progressBar");
const resultsEl = document.getElementById("results");

rankBtn.addEventListener("click", async () => {
  const job = document.getElementById("jobDesc").value.trim();
  const files = document.getElementById("resumes").files;
  if (!job || files.length === 0) {
    alert("Please provide a job description and upload resumes!");
    return;
  }

  const formData = new FormData();
  formData.append("job_description", job);
  for (let f of files) formData.append("resumes[]", f);

  loader.style.display = "block";
  progressBar.style.width = "0%";
  resultsEl.innerHTML = "";

  let progress = 0;
  const interval = setInterval(() => {
    if (progress < 90) {
      progress += 10;
      progressBar.style.width = progress + "%";
    }
  }, 400);

  try {
    const res = await fetch("/rank/keyword", {
      method: "POST",
      body: formData
    });
    const data = await res.json();

    clearInterval(interval);
    progressBar.style.width = "100%";
    loader.style.display = "none";

    if (data.results) {
      resultsEl.innerHTML = "<h2>Ranking Results</h2>";
      data.results.forEach(r => {
        resultsEl.innerHTML += `
          <div class="result-card">
            <h3>${r.filename}</h3>
            <p><strong>Score:</strong> ${r.score}</p>
            <p>${r.snippet}</p>
          </div>
        `;
      });
    } else {
      alert("Error: " + (data.error || "Unknown issue"));
    }
  } catch (err) {
    clearInterval(interval);
    loader.style.display = "none";
    progressBar.style.width = "0%";
    alert("Error connecting to backend.");
  }
});
