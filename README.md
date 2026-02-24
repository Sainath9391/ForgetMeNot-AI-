<div align="center">

<br/>

<a href="https://github.com/yourusername/forgetmenot-ai">
  <img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=700&size=26&duration=3000&pause=800&color=A78BFA&center=true&vCenter=true&multiline=false&width=650&height=60&lines=ForgetMeNot+AI;Simulating+Human+Memory+Decay+with+Math+%26+ML" alt="ForgetMeNot AI" />
</a>

<br/><br/>

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

<br/>

[![Stars](https://img.shields.io/github/stars/yourusername/forgetmenot-ai?style=flat-square&color=A78BFA&label=Stars)](https://github.com/yourusername/forgetmenot-ai/stargazers)
[![Forks](https://img.shields.io/github/forks/yourusername/forgetmenot-ai?style=flat-square&color=A78BFA&label=Forks)](https://github.com/yourusername/forgetmenot-ai/network)
[![License](https://img.shields.io/badge/License-MIT-A78BFA?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-A78BFA?style=flat-square)](#)

<br/>

**[Live Demo](#)** &nbsp;·&nbsp; **[Report Bug](#)** &nbsp;·&nbsp; **[Request Feature](#)**

<br/>

---

</div>

## Table of Contents

- [About the Project](#about-the-project)
- [Why This Matters](#why-this-matters)
- [Real-World Use Cases](#real-world-use-cases)
- [Tech Stack](#tech-stack)
- [Key Features](#key-features)
- [Architecture & Data Flow](#architecture--data-flow)
- [Technical Overview](#technical-overview)
- [Implementation & Code](#implementation--code)
- [Example Output](#example-output)
- [How It All Connects](#how-it-all-connects)
- [Roadmap](#roadmap)
- [Business & Research Impact](#business--research-impact)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## About the Project

**ForgetMeNot AI** simulates human-like memory decay using exponential functions. Users store "memories" with varying importance scores (salience), and the system automatically reduces their value over time — modelling how the human brain forgets.

> Inspired by the Ebbinghaus Forgetting Curve — one of the most foundational models in cognitive psychology.

---

## Why This Matters

Memory decay is a core concept across cognitive science, education, and AI. This project provides an interactive, mathematically grounded simulation of how information fades — giving developers and researchers a programmable base to build upon.

---

## Real-World Use Cases

- Adaptive learning systems that schedule revision at optimal intervals
- Personal knowledge management tools with intelligent decay
- Mental health research simulations for memory modelling
- Cognitive architecture in AI agents that prioritize recency

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI, Motor (async MongoDB driver) |
| Database | MongoDB |
| Frontend | HTML, CSS, Vanilla JavaScript |
| Config | python-dotenv, CORS middleware |

---

## Key Features

- Store memories with custom salience scores and auto-generated timestamps
- Exponential decay applied automatically on every retrieval
- Clean REST API for third-party integration
- Lightweight frontend UI to interact with and visualize memory states

---

## Architecture & Data Flow

```
User (Browser)
     │
     │  POST /memories/     ←  Submit new memory + salience
     │  GET  /memories/     ←  Retrieve with live-computed decay
     ▼
FastAPI Backend
     │
     ├── Validates input
     ├── Stores in MongoDB  (content · salience · timestamp)
     │
     └── On retrieval →  Decay Module
                              │
                              └──  salience × e^(−rate × age_in_days)
                                          │
                                          ▼
                                   Decayed value returned to frontend
```

---

## Technical Overview

Each memory document holds three fields:

| Field | Type | Description |
|---|---|---|
| `content` | `string` | The textual memory |
| `salience` | `float` | Importance score at time of creation |
| `timestamp` | `datetime` | Auto-generated on insert |

**Decay Formula**

```
decayed_salience = salience × e^(−rate × age)
```

Where `age` is the number of days since the memory was created, and `rate` controls how quickly it fades (default: `0.01`). A higher rate means faster forgetting.

---

## Implementation & Code

**`decay.py`** — the memory engine

```python
import math
from datetime import datetime, timezone

def decay(salience: float, timestamp_str: str, rate: float = 0.01) -> float:
    timestamp = datetime.fromisoformat(timestamp_str).replace(tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    age = (now - timestamp).days
    return salience * math.exp(-rate * age)
```

**`main.py`** — FastAPI application

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from decay import decay

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.post("/memories/")
async def add_memory(content: str, salience: float):
    doc = {"content": content, "salience": salience, "timestamp": datetime.utcnow()}
    await db.memories.insert_one(doc)
    return {"status": "stored"}

@app.get("/memories/")
async def get_memories():
    memories = await db.memories.find().to_list(100)
    for m in memories:
        m["salience"] = decay(m["salience"], m["timestamp"].isoformat())
    return memories
```

---

## Example Output

**POST** `/memories/`

```json
{
  "content": "Learned FastAPI",
  "salience": 1.0
}
```

**GET** `/memories/` — retrieved after 30 days

```json
[
  {
    "content": "Learned FastAPI",
    "salience": 0.74,
    "timestamp": "2025-08-01T10:00:00"
  }
]
```

> Salience dropped from `1.0` to `0.74` over 30 days at the default decay rate.

---

## How It All Connects

```
Frontend        →   Captures user input, renders decayed memory list
FastAPI Backend →   Handles routing, validation, and MongoDB operations
Decay Module    →   Applies the forgetting curve formula on every retrieval
MongoDB         →   Persists memories with original salience and timestamp
```

Every GET request recomputes decay in real time — no scheduled jobs, no stale data.

---

## Roadmap

- [ ] Graphical decay curve visualization per memory
- [ ] Adjustable decay rate per individual memory
- [ ] User authentication and memory isolation
- [ ] Long-term memory reinforcement (spaced repetition logic)
- [ ] Export memory state as CSV or JSON
- [ ] WebSocket support for live decay updates

---

## Business & Research Impact

- **EdTech** — power personalized revision schedulers (e.g. spaced repetition engines)
- **AI Agents** — enable agents to weight short-term vs. long-term knowledge dynamically
- **Psychology Research** — base simulation for memory and forgetting models
- **Healthcare** — memory degradation modelling for cognitive studies

---

## Installation

**Backend**

```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file in `/backend`:

```env
MONGO_URI=your_mongodb_connection_string
```

**Frontend**

```bash
# Open directly in browser
open frontend/index.html

# Or serve with live-server
npx live-server frontend/
```

---

## Usage

```bash
# Start the backend
uvicorn main:app --reload

# API available at
http://localhost:8000

# Interactive API docs (auto-generated by FastAPI)
http://localhost:8000/docs
```

Open the frontend in a browser and interact with the memory interface directly.

---

## Contributing

```bash
git checkout -b feature/your-feature
git commit -m "feat: your change"
git push origin feature/your-feature
# Open a Pull Request
```

Follow [Conventional Commits](https://www.conventionalcommits.org/) for all messages. Bug reports and suggestions are welcome via [Issues](#).

---

## License

MIT License — see [`LICENSE`](LICENSE) for details.

---

<div align="center">

<br/>

**Pendalwar Sainath**  
_Full-Stack Developer · AI & Cognitive Systems · Python · FastAPI_

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourusername)
[![Portfolio](https://img.shields.io/badge/Portfolio-A78BFA?style=for-the-badge&logo=vercel&logoColor=white)](https://your-portfolio.dev)

<br/>

<sub>Built with precision · Grounded in science · Designed for impact</sub>

</div>
