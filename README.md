# RAG Demo

## Overview
This repository demonstrates several examples of Retrieval-Augmented Generation (RAG) and LLM-based agents — starting from basic prompts and gradually adding context, tools, and memory.

## Files

- **1.py** – Simple LLM request (no context)
- **2.py** – Simple LLM request (adds context in the `system_prompt`)
- **3.py** – Agent with tools (reads information from a `.txt` file)
- **4.py** – Agent with tools (simulates a real API, where data comes from a mock database that returns product information)
- **5.py** – Agent with tools (same as `4.py`, but includes chat memory for multi-turn context)

## Setup

1. **Install dependencies:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

3. **Copy example environment variables and fill them:**
```bash
cp .env.example .env
```

4. **Run the script:**
```bash
python 1.py
python 2.py
python 3.py
python 4.py
python 5.py
```
