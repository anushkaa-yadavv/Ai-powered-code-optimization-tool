# AI BASED CODE OPTIMIZATION TOOL

## AI-Powered Real-Time Code Optimization and Analysis System

It is an advanced AI-powered code optimization framework that performs real-time source code monitoring, AST-based static analysis, intelligent semantic optimization, risk analysis, syntax validation, and automated reporting.

The system integrates Groq LPU-powered Llama-3.3-70B models with Python-based static analysis techniques to provide intelligent code refactoring and maintainability improvements.

---

# Features

- Real-time source code monitoring
- AST-based static code analysis
- Cyclomatic Complexity calculation
- AI-assisted semantic optimization
- Automatic PEP8 formatting
- Risk score generation
- Syntax validation
- Code difference tracking
- Backup and recovery system
- Rich terminal reports
- VS Code extension support
- GitHub integration support
- LSP-based IDE communication
- Modular and scalable architecture

---

# Project Structure

```text
AI_CODE_ENGINE/
│
├── ai_code_engine/
│   ├── ai.py
│   ├── analyzer.py
│   ├── cache.py
│   ├── cli.py
│   ├── cli_report.py
│   ├── diff_generator.py
│   ├── engine.py
│   ├── github_bot.py
│   ├── lsp_server.py
│   ├── optimizer.py
│   ├── server.py
│   ├── utils.py
│   ├── validator.py
│   └── watcher.py
│
├── vs_code_extensions/
├── backups/
├── optimized/
├── reports/
├── test.py
├── .env
├── pyproject.toml
└── README.md
```

---

# Technologies Used

- Python 3.x
- Groq AI API
- Llama-3.3-70B
- AST (Abstract Syntax Tree)
- Watchdog
- autopep8
- Rich Library
- Tkinter
- VS Code Extension API

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_CODE_ENGINE.git
cd AI_CODE_ENGINE
```

---

## Install Dependencies

```bash
pip install watchdog autopep8 rich requests python-dotenv
```

---

## Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

# Run the Project

```bash
python -m ai_code_engine.engine
```

---

# Sample Workflow

```text
File Monitoring
      ↓
AST Analysis
      ↓
Risk Detection
      ↓
Backup Creation
      ↓
PEP8 Formatting
      ↓
AI Optimization
      ↓
Syntax Validation
      ↓
Diff Generation
      ↓
Report Generation
```

---

# Future Enhancements

- Multi-language optimization support
- CI/CD integration
- Docker deployment
- Web dashboard
- Security vulnerability analysis
- Cloud-based optimization

---

# Author

Anushka Yadav
Harshit Mehra 
Yash

---

# License

This project is developed for educational and research purposes.
