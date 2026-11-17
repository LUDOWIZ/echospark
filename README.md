# ✦ EchoSpark

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Engine-Google_Gemini-8E75B2?logo=googlegemini&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

A minimal, autonomous software engineering agent built from scratch in Python without heavy frameworks. Powered by Google Gemini (configurable via `.env`), it demonstrates a clean **ReAct loop (Reason + Act)** with tool execution, conversation memory, and an interactive terminal interface built with `rich`.

## Architecture

```text
echospark/
├── echospark/
│   ├── __init__.py     # Package version
│   ├── agent.py        # Core ReAct loop and LLM client
│   ├── cli.py          # Interactive terminal interface
│   └── tools.py        # Tool definitions and JSON schemas
├── .env.example        # Environment variable template
├── .gitignore          # Git exclusion rules
└── README.md
