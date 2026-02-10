from crewai import Agent

summarizer_agent = Agent(
    role="Content Summarizer",
    goal="Summarize research notes into concise bullet points.",
    backstory="You extract only the key insights from large text.",
    llm_model="gpt-3.5-turbo",
    verbose=True

)

