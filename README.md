# 🤖 AI Research & Report Generator

## 📌 Description

An intelligent multi-agent AI system built with **CrewAI** and **Streamlit** that fully automates the research, summarization, writing, and review of high-quality research reports on any topic.

## ✨ Features

- Multi-agent orchestration powered by CrewAI for coordinated agent collaboration
- Automated report generation from topic input to final polished output
- Export options to Markdown and PDF formats
- Agentic AI pipeline with sequential, role-specialized agents
- Real-world usefulness for researchers, analysts, students, and content creators

## AI Skills Demonstrated

- CrewAI multi-agent framework
- Agent design and role specialization
- Workflow automation and orchestration
- Advanced prompt engineering
- Streamlit integration for interactive web UI

## 🗂️ Project Structure

```bash
AI-Research-Report-Generator/
├── agents/
├── tasks/
├── utils/
├── venv/
├── .env
├── .gitignore
├── app.py
├── crew.py
├── main.py
├── run.txt
└── README.md

```

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/vinudasenith/ai-research-report-generator.git
cd ai-research-report-generator
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Linux / macOS:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Setup OpenAI API Key

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-your-openai-api-key-here
```

For Streamlit Cloud, add to `secrets.toml`:

```toml
OPENAI_API_KEY = "sk-your-openai-api-key-here"
```

## ▶️ Running the App

```bash
streamlit run app.py
```

## Usage

1. Launch the application using the command above
2. Enter your research topic in the input field
3. Click "Generate Report" to start the multi-agent workflow
4. Wait for the agents to research, write, and review the content
5. Download the final report in Markdown or PDF format

## Technologies Used

- **CrewAI** - Multi-agent orchestration framework
- **Streamlit** - Interactive web interface
- **OpenAI API** - Language model for content generation
- **Python** - Core programming language

## 👤 Author

Vinuda Senith - [LinkedIn Profile](https://www.linkedin.com/in/vinudasenith/)
