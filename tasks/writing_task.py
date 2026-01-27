from agents.writer_agent import writer_agent
from crewai import Task

def create_writing_task():
    return Task(
        description="Write a professional research report using summaries.",
        agent=writer_agent,
        expected_output="A well-structured, professional research report."
    )