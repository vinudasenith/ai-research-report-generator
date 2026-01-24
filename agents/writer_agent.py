from crewai import Agent
import os

writer_agent = Agent(
    role="Report Writer",
    goal="Write a professional research report using summaries.",
    backstory="You write clear, structured academic-style reports.",
    llm_model="gpt-3.5-turbo",
    verbose=True
)


