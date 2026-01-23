from crewai import Agent
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

writer_agent = Agent(
    role="Report Writer",
    goal="Write a professional research report using summaries.",
    backstory="You write clear, structured academic-style reports.",
    llm_model="gpt-3.5-turbo",
    verbose=True
)

def write_report(summary):
    task_description = f"Write a structured research report based on these points:\n{summary}"
    return writer_agent.run(task_description)
