<p align="center">
  <img src="https://img.shields.io/badge/Netflix-Studio%20Connect-E50914?style=for-the-badge&logo=netflix&logoColor=white" alt="Netflix Studio Connect"/>
</p>

<h1 align="center">Netflix Studio Connect</h1>

<p align="center">
  <b>AI-powered multi-tenant SaaS platform unifying pitch-to-production workflows for Netflix partner studios.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/streamlit-1.28+-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/AI-Groq%20%7C%20Llama%203.1-00D4AA?style=flat-square"/>
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square"/>
</p>

---

## Overview

Netflix Studio Connect replaces fragmented email chains, spreadsheets, and disconnected tools with a single platform that handles the entire content partnership lifecycle — from pitch submission through production management to performance analytics.

Built for three distinct personas (**Studio Executives**, **Producers**, **Netflix Executives**) with role-based access control, multi-studio data isolation, and an AI engine powered by Groq API (Llama 3.1-8b) that delivers real-time pitch analysis and natural language analytics.

**Think:** *Salesforce meets Asana meets Netflix Analytics — purpose-built for entertainment production.*

---

## Key Features

### Pitch Portal (Studio Executive)
- Submit pitches with structured metadata (genre, format, budget, episodes, comps)
- **AI Feedback Preview** — instant LLM-powered content viability analysis before Netflix review
- Real-time pipeline tracking with status badges and review timelines
- Deal stage management and contract negotiation history

### Production Suite (Producer)
- Multi-project dashboard with budget health and milestone tracking
- Category-based budget creation with real-time variance alerts and burn-rate visualization
- Episode-by-episode deliverables checklist with Netflix approval gates
- Issue reporting system (weather, VFX, equipment, talent) with severity levels and escalation paths

### Netflix Executive Dashboard
- **Multi-studio tabbed interface** with tenant-isolated data environments
- Centralized pitch review queue with inline approve/reject/revision workflows
- Cross-studio analytics hub — pitch volume, acceptance rates, genre trends, studio rankings
- **AI Analytics Chatbot** — natural language queries across all platform data

### Shared
- Role-based authentication (studio_exec, producer, netflix_exec)
- In-app messaging with conversation threading
- Real-time notification system
- Netflix-branded dark theme UI (#141414 / #E50914)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| AI Engine | Groq API — Llama 3.1-8b-instant |
| Backend | Python 3.10+ |
| Database | JSON-based (MVP) → PostgreSQL (production) |
| Auth | Role-based access control |
| Hosting | Replit / AWS / GCP |

---

## Getting Started

### Prerequisites

- Python 3.10+
- Groq API key ([get one here](https://console.groq.com))

### Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/Netflix-Studio-Connect.git
cd Netflix-Studio-Connect

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Run the Application

```bash
streamlit run app.py
```

The app will launch at `http://localhost:8501`.

### Demo Credentials

| Role | Username | Password |
|---|---|---|
| Studio Executive | `studio_exec` | `studio123` |
| Producer | `producer` | `producer123` |
| Netflix Executive | `netflix_exec` | `netflix123` |

---

## Project Structure

```
Netflix-Studio-Connect/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed)
├── .gitignore
├── LICENSE
├── README.md
├── data/
│   ├── users.json          # User credentials & roles
│   ├── pitches.json        # Pitch submissions
│   ├── projects.json       # Production data
│   ├── contracts.json      # Contract records
│   ├── messages.json       # In-app messaging
│   ├── analytics.json      # Analytics data
│   ├── negotiations.json   # Deal negotiations
│   └── issues.json         # Production issues
└── assets/
    └── logo.png            # Branding assets
```

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                   STUDIO CONNECT                     │
│                                                      │
│  ┌──────────┐  ┌──────────┐  ┌───────────────────┐  │
│  │  Studio   │  │ Producer │  │ Netflix Executive │  │
│  │  Exec UI  │  │    UI    │  │        UI         │  │
│  └─────┬─────┘  └────┬─────┘  └────────┬──────────┘  │
│        │              │                 │             │
│        ▼              ▼                 ▼             │
│  ┌────────────────────────────────────────────────┐  │
│  │          Role-Based Access Control              │  │
│  └───────────────────┬────────────────────────────┘  │
│                      ▼                               │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │
│  │  Pitch   │  │Production│  │    Analytics      │   │
│  │  Engine  │  │  Engine  │  │     Engine        │   │
│  └────┬─────┘  └────┬─────┘  └────────┬─────────┘   │
│       │              │                 │              │
│       ▼              ▼                 ▼              │
│  ┌────────────────────────────────────────────────┐  │
│  │         Groq API  (Llama 3.1-8b-instant)       │  │
│  └────────────────────────────────────────────────┘  │
│                      │                               │
│                      ▼                               │
│  ┌────────────────────────────────────────────────┐  │
│  │             Data Layer (JSON / PostgreSQL)      │  │
│  └────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

## Roadmap

- [x] **Phase 1** — Core pitch portal, RBAC, AI feedback, messaging
- [x] **Phase 2** — Multi-studio support, production suite, budget tracking
- [ ] **Phase 3** — AI analytics chatbot, cross-studio intelligence, predictive models
- [ ] **Phase 4** — Third-party integrations (Movie Magic, StudioBinder), mobile app, white-label

---

## Market Context

The production management software market for Media & Entertainment is valued at **$2.95B (2024)**, growing at **8.69% CAGR** to **$4.90B by 2030**. Studio Connect targets this market with a differentiated AI-native approach and multi-tenant architecture designed for the streaming partnership model.

---

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

```
MIT License

Copyright (c) 2026 Kshitij

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Contact

**Kshitij** — Product Manager
- GitHub: [@iamkshitij](https://github.com/iamkshitij)

---