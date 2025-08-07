const apiUrl = "http://127.0.0.1:8000/memories/";

function openTab(tabId, event) {
  document.querySelectorAll(".tabcontent").forEach(el => el.style.display = "none");
  document.querySelectorAll(".tablink").forEach(el => el.classList.remove("active"));
  document.getElementById(tabId).style.display = "block";
  event.currentTarget.classList.add("active");
  if (tabId === "memoriesTab") loadMemories();
  if (tabId === "oldTab") loadOldMemories();
}

async function addMemory() {
  const content = document.getElementById("contentInput").value;
  const salience = parseFloat(document.getElementById("salienceInput").value);
  await fetch(apiUrl, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ content, salience })
  });
  showToast("✅ Memory added!");
  document.getElementById("contentInput").value = "";
  loadMemories();
}

async function loadMemories() {
  const res = await fetch(apiUrl);
  const data = await res.json();
  const list = document.getElementById("memoriesList");
  list.innerHTML = "";
  data.forEach(mem => {
    const div = document.createElement("div");
    div.className = "memory-card";
    if (mem.pinned) div.classList.add("pinned");
    div.innerHTML = `
      ${mem.pinned ? '<div class="pin-icon">📌</div>' : ''}
      <strong>${mem.content}</strong><br>
      <span class="small">Salience: ${mem.salience.toFixed(2)}</span><br>
      <span class="small">Created: ${new Date(mem.timestamp).toLocaleString()}</span>
      <div class="actions">
        ${mem.pinned 
          ? `<button onclick="unpinMemory('${mem._id}')">Unpin</button>` 
          : `<button onclick="pinMemory('${mem._id}')">Pin</button>`}
        <button class="delete" onclick="deleteMemory('${mem._id}')">Delete</button>
      </div>`;
    list.appendChild(div);
  });
}

async function searchMemories() {
  const text = document.getElementById("searchInput").value;
  const res = await fetch(apiUrl + "?search=" + encodeURIComponent(text));
  const data = await res.json();
  const list = document.getElementById("searchResults");
  list.innerHTML = "";
  data.forEach(mem => {
    const div = document.createElement("div");
    div.className = "memory-card";
    if (mem.pinned) div.classList.add("pinned");
    div.innerHTML = `
      ${mem.pinned ? '<div class="pin-icon">📌</div>' : ''}
      <strong>${mem.content}</strong><br>
      <span class="small">Salience: ${mem.salience.toFixed(2)}</span><br>
      <span class="small">Created: ${new Date(mem.timestamp).toLocaleString()}</span>`;
    list.appendChild(div);
  });
}

async function loadOldMemories() {
  const res = await fetch(apiUrl.replace("/memories/", "/old_memories/"));
  const data = await res.json();
  const list = document.getElementById("oldMemoriesList");
  list.innerHTML = "";
  data.forEach(mem => {
    const div = document.createElement("div");
    div.className = "memory-card";
    div.innerHTML = `
      <strong>${mem.content}</strong><br>
      <span class="small">Salience: ${mem.salience.toFixed(2)}</span><br>
      <span class="small">Created: ${new Date(mem.timestamp).toLocaleString()}</span>
      <div class="actions">
        <button class="delete" onclick="deleteOldMemory('${mem._id}')">Delete</button>
      </div>`;
    list.appendChild(div);
  });
}

async function deleteMemory(id) {
  await fetch(apiUrl + id, { method: "DELETE" });
  showToast("🗑️ Memory deleted!");
  loadMemories();
}

async function deleteOldMemory(id) {
  await fetch(apiUrl + id, { method: "DELETE" });
  showToast("🗑️ Old memory deleted!");
  loadOldMemories();
}

async function pinMemory(id) {
  await fetch(apiUrl + id + "/pin", { method: "PATCH" });
  showToast("📌 Pinned!");
  loadMemories();
}

async function unpinMemory(id) {
  await fetch(apiUrl + id + "/unpin", { method: "PATCH" });
  showToast("Unpinned!");
  loadMemories();
}

function showToast(message) {
  const toast = document.getElementById("toast");
  toast.innerText = message;
  toast.className = "show";
  setTimeout(() => { toast.className = toast.className.replace("show", ""); }, 2000);
}

