# My-first-project

This repository contains a simple voice journal application powered by OpenAI's Chat API. The app lets you speak to an AI assistant focused on health, wellness, and high performance. It records your entries, generates helpful responses, and speaks them back to you.

## Requirements

Install dependencies with pip:

```bash
pip install -r requirements.txt
```

## Usage

Set your `OPENAI_API_KEY` environment variable before running:

```bash
export OPENAI_API_KEY=your-key-here
python journal_app/app.py
```

Say "quit" or "exit" to end the conversation. Journal files are saved with the current date in the project directory.
