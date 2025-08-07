## Table of Contents

* [About the Project](#about-the-project)
* [Why this Project Matters](#why-this-project-matters)
* [Real-world Use Cases](#real-world-use-cases)
* [Tech Stack](#tech-stack)
* [Key Features](#key-features)
* [Architecture & Data Flow](#architecture--data-flow)
* [Technical Overview](#technical-overview)
* [Implementation & Code Explanation](#implementation--code-explanation)
* [Example Output](#example-output)
* [How it all Connects](#how-it-all-connects)
* [Future Improvements & Research Directions](#future-improvements--research-directions)
* [Business & Research Impact](#business--research-impact)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

---

## About the Project

**ForgetMeNot AI** simulates human-like memory decay using exponential functions. Users can store "memories" with varying importance (salience), and the system will automatically reduce their value over time.

## Why this Project Matters

Understanding memory decay is crucial in cognitive science, education, and AI. This project provides a simple, interactive simulation of how information fades over time.

## Real-world Use Cases

* Adaptive learning systems
* Personal knowledge management tools
* Mental health research simulations
* Cognitive modeling in AI

## Tech Stack

* **Backend**: Python, FastAPI, MongoDB, Motor
* **Frontend**: HTML, CSS, JavaScript
* **Others**: dotenv, CORS middleware

## Key Features

* Add memories with timestamps and salience scores
* Automatic decay of salience over time
* REST API for integration
* Frontend UI to interact and visualize memory states

## Architecture & Data Flow

1. **Frontend** sends memory input via REST API
2. **Backend** (FastAPI) handles input and stores it in MongoDB
3. **Decay Logic** computes reduced salience over time
4. **Frontend** retrieves and displays decayed memory values

## Technical Overview

* Each memory has:

  * `content`: textual data
  * `salience`: float (importance)
  * `timestamp`: auto-generated
* The decay function uses:
  `salience * e^(-rate * age)` where `age` is in days
* MongoDB stores memories with `_id`, content, timestamp, and salience

## Implementation & Code Explanation

### decay.py

```python
def decay(salience, timestamp_str, rate=0.01):
    age = (now - timestamp) in days
    return salience * math.exp(-rate * age)
```

### main.py

* Uses FastAPI with CORS
* Accepts memory input
* Stores in MongoDB
* Retrieves with decayed salience based on current time

## Example Output

POST `/memories/`

```json
{
  "content": "Learned FastAPI",
  "salience": 1.0
}
```

GET `/memories/` (after a few days)

```json
[
  {
    "content": "Learned FastAPI",
    "salience": 0.76,
    "timestamp": "2025-08-01T10:00:00"
  }
]
```

## How it all Connects

* **Frontend** captures and displays user input/output
* **Backend** manages business logic and storage
* **Decay Module** acts like a memory engine to simulate forgetting

## Future Improvements & Research Directions

* Graphical decay curve visualization
* Adjustable decay rate per memory
* Integration with user authentication
* Long-term memory reinforcement logic

## Business & Research Impact

* Useful in EdTech for personalized revision tools
* Can support AI agents in prioritizing short-term vs long-term knowledge
* Base model for psychology simulations

## Installation

```bash
# Backend setup
cd backend
pip install -r requirements.txt

# Frontend setup
# Simply open frontend/index.html in browser or serve via live-server
```

## Usage

```bash
# Run backend
uvicorn main:app --reload
```

Then access the frontend in a browser and interact with the API.

## Contributing

Feel free to fork this repo, make enhancements, and raise pull requests. Bug reports and suggestions are welcome!

## License

This project is open-source under the MIT License.
