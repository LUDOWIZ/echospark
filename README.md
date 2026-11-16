# ✦ EchoSpark

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Engine-Gemini_2.5_Flash-8E75B2?logo=googlegemini&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

En minimal, autonom AI-agent byggd från grunden i Python utan tunga ramverk. Demonstrerar en ren **ReAct-loop (Reason + Act)** med verktygsanrop, konversationsminne och ett interaktivt terminalgränssnitt via `rich`.

## Kom igång

```bash
git clone [https://github.com/DITT-ANVANDARNAMN/echospark.git](https://github.com/DITT-ANVANDARNAMN/echospark.git)
cd echospark
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env       # Lägg in din GEMINI_API_KEY
echospark
```