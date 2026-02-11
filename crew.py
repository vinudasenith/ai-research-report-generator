from tasks.research_task import create_research_task
from tasks.summarization_task import create_summarization_task
from tasks.writing_task import create_writing_task
from tasks.review_task import create_review_task
from crewai import Crew

def run_crew(topic):
    # Research
    research_task = create_research_task(topic)

    # Summarize
    summarize_task = create_summarization_task()

    # Write Report
    write_task = create_writing_task()

    # Review
    review_task = create_review_task()

    crew = Crew(
        agents=[
            research_task.agent,
            summarize_task.agent,
            write_task.agent,
            review_task.agent
        ],
        tasks=[
            research_task,
            summarize_task,
            write_task,
            review_task
        ],
        verbose=True
    )

    result = crew.kickoff()
    return result
