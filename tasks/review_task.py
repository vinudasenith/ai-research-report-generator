from agents.reviewer_agent import reviewer_agent
from crewai import Task

def create_review_task():
    return Task(
        description="Review and improve the report for clarity and grammar",
        agent=reviewer_agent,
        expected_output="Polished final report"
    )
