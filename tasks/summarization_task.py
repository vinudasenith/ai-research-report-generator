from agents.summarizer_agent import summarizer_agent
from crewai import Task

def create_summarization_task():
    return Task(
        description="Summarize the research notes into clear bullet points",
        agent=summarizer_agent,
        expected_output="Concise bullet-point summary"
    )
