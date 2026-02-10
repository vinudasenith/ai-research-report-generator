from crewai import Agent


reviewer_agent = Agent(
    role="Quality Reviewer",
    goal="Review the report for grammar, clarity, and completeness.",
    backstory="You are a senior editor refining content quality.",
    llm_model="gpt-3.5-turbo",
    verbose=True
)

