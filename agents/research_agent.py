import os
from crewai import Agent
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

research_agent=Agent(
    role="Research Analyst",
    goal="Given a topic, research and gather accurate, up-to-date information.",
    backstory="You are an expert researcher who finds reliable sources.",
    localsm_model="gpt-3.5-turbo",
    verbose=True

)

def research(topic):
    task_description = f"Research the topic: {topic} and provide detailed notes."
    return research_agent.run(task_description)