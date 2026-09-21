# LangChain Updates

This repository tracks practical changes introduced in the LangChain platform.
It is organized as a small, executable learning log rather than a production
application.

## Current content

- `updatedLangchain/01-creating-agents.ipynb`: first notebook for the LangChain
	v1 update series.
- `main.py`: a minimal command-line entry point for checking the repository.

## Setup

Python 3.12 or newer is required.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

For the notebook's Groq integration, copy `.env.example` to `.env` and set
`GROQ_API_KEY` to your own key. Never commit `.env` or API keys.

Start the notebook with:

```powershell
jupyter notebook updatedLangchain/01-creating-agents.ipynb
```

## Scope

The repository is intentionally limited to LangChain platform updates and
their accompanying examples. Each new update should be added as a focused
notebook or example with its required dependency documented here.
