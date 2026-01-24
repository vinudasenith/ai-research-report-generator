from agents.research_agent import research_agent
from crewai import Task

def create_research_task(topic):
    return Task(
        description=f"Research the topic: {topic}",
        agent=research_agent,
        expected_output="Detailed research notes with facts and examples."
    )