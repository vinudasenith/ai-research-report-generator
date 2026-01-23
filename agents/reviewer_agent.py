from crewai import Agent
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

reviewer_agent = Agent(
    role="Quality Reviewer",
    goal="Review the report for grammar, clarity, and completeness.",
    backstory="You are a senior editor refining content quality.",
    llm_model="gpt-3.5-turbo",
    verbose=True
)

def review(report):
    task_description = f"Review and improve the following report:\n{report}"
    return reviewer_agent.run(task_description)
