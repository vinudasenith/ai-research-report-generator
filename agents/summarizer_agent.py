import os
from crewai import Agent
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

summarizer_agent = Agent(
    role="Content Summarizer",
    goal="Summarize research notes into concise bullet points.",
    backstory="You extract only the key insights from large text.",
    llm_model="gpt-3.5-turbo",
    verbose=True

)

def summarize(text):
    task_description = f"Summarize the following research notes:\n{text}"
    return summarizer_agent.run(task_description)
