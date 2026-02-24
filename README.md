<div align="center">

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=ForgetMeNot%20AI&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Simulating%20Human%20Memory%20Decay%20with%20Exponential%20Functions&descAlignY=58&descSize=16" />

<br/>

<a href="https://github.com/yourusername/forgetmenot-ai">
  <img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=600&size=18&duration=3500&pause=1000&color=818CF8&center=true&vCenter=true&width=600&height=45&lines=FastAPI+%2B+MongoDB+%2B+Python;Cognitive+Science+meets+Software+Engineering;Memory+Decay+%E2%86%92+salience+%C3%97+e%5E(%E2%88%92rate+%C3%97+age)" alt="Typing SVG" />
</a>

<br/><br/>

[![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](#)

<br/>

[![Stars](https://img.shields.io/github/stars/yourusername/forgetmenot-ai?style=flat-square&color=818CF8&label=Stars)](https://github.com/yourusername/forgetmenot-ai/stargazers)
[![Forks](https://img.shields.io/github/forks/yourusername/forgetmenot-ai?style=flat-square&color=818CF8&label=Forks)](https://github.com/yourusername/forgetmenot-ai/network)
[![License](https://img.shields.io/badge/License-MIT-818CF8?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-22D3EE?style=flat-square)](#)

<br/>

[**Live Demo**](#) &nbsp;·&nbsp; [**API Docs**](#) &nbsp;·&nbsp; [**Report Bug**](#) &nbsp;·&nbsp; [**Request Feature**](#)

<br/>

</div>

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## &nbsp; Table of Contents

&nbsp;&nbsp; [01 &nbsp; About the Project](#-about-the-project) &nbsp;·&nbsp;
[02 &nbsp; Why This Matters](#-why-this-matters) &nbsp;·&nbsp;
[03 &nbsp; Use Cases](#-real-world-use-cases) &nbsp;·&nbsp;
[04 &nbsp; Tech Stack](#-tech-stack)

&nbsp;&nbsp; [05 &nbsp; Key Features](#-key-features) &nbsp;·&nbsp;
[06 &nbsp; Architecture](#-architecture--data-flow) &nbsp;·&nbsp;
[07 &nbsp; Technical Overview](#-technical-overview) &nbsp;·&nbsp;
[08 &nbsp; Code](#-implementation--code)

&nbsp;&nbsp; [09 &nbsp; Example Output](#-example-output) &nbsp;·&nbsp;
[10 &nbsp; How It Connects](#-how-it-all-connects) &nbsp;·&nbsp;
[11 &nbsp; Roadmap](#-roadmap) &nbsp;·&nbsp;
[12 &nbsp; Impact](#-business--research-impact)

&nbsp;&nbsp; [13 &nbsp; Installation](#-installation) &nbsp;·&nbsp;
[14 &nbsp; Usage](#-usage) &nbsp;·&nbsp;
[15 &nbsp; Contributing](#-contributing) &nbsp;·&nbsp;
[16 &nbsp; License](#-license)

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<br/>

## ◈ About the Project

**ForgetMeNot AI** models the human brain's forgetting mechanism as a programmable system. Every memory stored has a salience score that decays exponentially over time — mirroring the Ebbinghaus Forgetting Curve from cognitive psychology.

```
Retention(t) = salience × e^(−rate × age_in_days)
```

Store a memory today with a salience of `1.0`. Come back in 30 days — it has faded to `0.74`. Come back in 100 days — it is `0.37`. This is not approximation. This is the math behind human forgetting.

<br/>

## ◈ Why This Matters

Memory decay sits at the intersection of neuroscience, AI, and education. Most software treats stored data as static — this project treats it as living, fading, and requiring reinforcement. That shift in perspective is what makes ForgetMeNot AI useful for research and extensible for production systems.

<br/>

## ◈ Real-World Use Cases

| Domain | Application |
|---|---|
| EdTech | Spaced repetition engines that schedule review at optimal decay thresholds |
| AI Agents | Agents that deprioritize stale knowledge and surface recent, high-salience context |
| Psychology | Baseline forgetting simulations for cognitive research |
| Healthcare | Memory degradation modelling for cognitive decline studies |
| PKM Tools | Personal knowledge bases with intelligent information aging |

<br/>

## ◈ Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | Python 3.10+, FastAPI | REST API, routing, business logic |
| **Database** | MongoDB + Motor | Async data persistence |
| **Frontend** | HTML, CSS, JavaScript | UI and API interaction |
| **Config** | python-dotenv, CORS | Environment and security middleware |

</div>

<br/>

## ◈ Key Features

- Store memories with custom salience scores and auto-generated timestamps
- Exponential decay computed live on every retrieval — no scheduled jobs
- Auto-generated interactive API docs via FastAPI at `/docs`
- Lightweight vanilla JS frontend with no build tooling required
- Fully async backend using Motor for non-blocking MongoDB operations

<br/>

## ◈ Architecture & Data Flow

```
┌─────────────────────────────────────────────────────────────┐
│                        Browser (Frontend)                    │
│          POST /memories/               GET /memories/        │
└────────────────────┬───────────────────────┬────────────────┘
                     │                       │
                     ▼                       ▼
┌─────────────────────────────────────────────────────────────┐
│                     FastAPI Backend                          │
│                                                             │
│  ┌─────────────────┐        ┌──────────────────────────┐   │
│  │  Input Handler  │        │      Decay Module         │   │
│  │  Validates &    │        │  salience × e^(−r × age) │   │
│  │  stores to DB   │        │  Applied on every GET     │   │
│  └────────┬────────┘        └──────────────┬───────────┘   │
│           │                                │                │
└───────────┼────────────────────────────────┼────────────────┘
            │                                │
            ▼                                ▼
┌───────────────────────────────────────────────────────────┐
│                       MongoDB                              │
│    { content, salience (original), timestamp, _id }       │
└───────────────────────────────────────────────────────────┘
```

<br/>

## ◈ Technical Overview

<div align="center">

| Field | Type | Description |
|---|---|---|
| `content` | `string` | The textual memory |
| `salience` | `float 0.0–1.0` | Importance at time of creation |
| `timestamp` | `datetime (UTC)` | Auto-generated on insert |

</div>

The original salience is stored unchanged in MongoDB. Decay is computed dynamically at query time — meaning historical data is never mutated and decay parameters can be changed retroactively.

<br/>

## ◈ Implementation & Code

**`decay.py`**

```python
import math
from datetime import datetime, timezone

def decay(salience: float, timestamp_str: str, rate: float = 0.01) -> float:
    timestamp = datetime.fromisoformat(timestamp_str).replace(tzinfo=timezone.utc)
    age_in_days = (datetime.now(timezone.utc) - timestamp).days
    return round(salience * math.exp(-rate * age_in_days), 4)
```

**`main.py`**

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime, timezone
from decay import decay
import os

app = FastAPI(title="ForgetMeNot AI")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])

client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client.forgetmenot

@app.post("/memories/")
async def add_memory(content: str, salience: float):
    doc = {"content": content, "salience": salience, "timestamp": datetime.now(timezone.utc)}
    await db.memories.insert_one(doc)
    return {"status": "stored"}

@app.get("/memories/")
async def get_memories():
    memories = await db.memories.find().to_list(100)
    for m in memories:
        m["salience"] = decay(m["salience"], m["timestamp"].isoformat())
        m["_id"] = str(m["_id"])
    return memories
```

<br/>

## ◈ Example Output

**`POST /memories/`** — Store a new memory

```json
{
  "content": "Learned FastAPI",
  "salience": 1.0
}
```

**`GET /memories/`** — Retrieved after 30 days

```json
[
  {
    "_id": "64f3a2...",
    "content": "Learned FastAPI",
    "salience": 0.7408,
    "timestamp": "2025-08-01T10:00:00+00:00"
  }
]
```

> Salience decayed from `1.0` → `0.74` over 30 days at the default rate of `0.01`.  
> At 100 days: `0.37`. At 200 days: `0.14`. The forgetting curve in action.

<br/>

## ◈ How It All Connects

```
Frontend   →   Captures user input · Renders decayed memory list
FastAPI    →   Routes requests · Validates input · Interfaces with MongoDB
Decay      →   Applies forgetting curve formula on every GET request
MongoDB    →   Stores original salience + timestamp — never mutated
```

Every retrieval recomputes decay in real time. No background jobs. No cron. No stale values.

<br/>

## ◈ Roadmap

- [ ] Graphical decay curve visualization per memory
- [ ] Configurable decay rate per individual memory entry
- [ ] User authentication and per-user memory isolation
- [ ] Spaced repetition — reinforcement logic to reset decay on review
- [ ] Memory export as JSON or CSV
- [ ] WebSocket support for live salience counter

<br/>

## ◈ Business & Research Impact

- **EdTech** — Build intelligent revision schedulers that surface content exactly when it is about to be forgotten
- **AI Agents** — Enable agents to weight recent, high-salience knowledge over stale context
- **Cognitive Research** — Baseline simulation layer for forgetting and memory reinforcement studies
- **Healthcare** — Provide a programmable model base for memory degradation analysis

<br/>

## ◈ Installation

**Backend**

```bash
git clone https://github.com/yourusername/forgetmenot-ai.git
cd forgetmenot-ai/backend
pip install -r requirements.txt
```

Create `backend/.env`:

```env
MONGO_URI=your_mongodb_connection_string
```

**Frontend**

```bash
# Open directly
open frontend/index.html

# Or serve with live-server
npx live-server frontend/
```

<br/>

## ◈ Usage

```bash
# Start the API server
uvicorn main:app --reload

# API base URL
http://localhost:8000

# Interactive Swagger docs (auto-generated)
http://localhost:8000/docs
```

<br/>

## ◈ Contributing

```bash
git checkout -b feature/your-feature
git commit -m "feat: describe your change"
git push origin feature/your-feature
# Open a Pull Request
```

Follow [Conventional Commits](https://www.conventionalcommits.org/). Issues and suggestions welcome.

<br/>

## ◈ License

MIT License — see [`LICENSE`](LICENSE) for full details.

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" />

<div align="center">

**Pendalwar Sainath**  
_Full-Stack Developer &nbsp;·&nbsp; AI & Cognitive Systems &nbsp;·&nbsp; Python &nbsp;·&nbsp; FastAPI_

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourusername)
[![Portfolio](https://img.shields.io/badge/Portfolio-818CF8?style=for-the-badge&logo=vercel&logoColor=white)](https://your-portfolio.dev)

<br/>

<sub>Built with precision &nbsp;·&nbsp; Grounded in science &nbsp;·&nbsp; Designed for impact</sub>

</div>
