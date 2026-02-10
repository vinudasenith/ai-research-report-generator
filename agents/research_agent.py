from crewai import Agent

research_agent=Agent(
    role="Research Analyst",
    goal="Given a topic, research and gather accurate, up-to-date information.",
    backstory="You are an expert researcher who finds reliable sources.",
    llm_model="gpt-3.5-turbo",
    verbose=True

)
