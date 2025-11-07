# RAG demo

## Files:

1.py - Simple LLM request (no context)
2.py - Simple LLM request (plus context in system_prompt)
3.py - Agent with tools (info from txt file)
4.py - Agent with tools (info from API)
5.py - Agent with tools (info from API) and chat memory

## How to run:

1. Install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate && pip install --upgrade pip
source venv/bin/activate && pip install -r requirements.txt
```

2. Activate virtual environment:
```bash
source venv/bin/activate
```

3. Copy example environment variables and fill them:
```bash
cp .env.example .env
```

4. Run the script:
```bash
python 1.py
```
