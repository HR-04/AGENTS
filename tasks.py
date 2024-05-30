from crewai import Task,Agent
from tools import tool
from agent import news_researcher,news_writer

research_task = Task(
    role = 'Senior Researcher',
    goal = 'Uncover Ground Breaking Technologies in {topic}',
    verbose = True,
    memory = True,
    backstory=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
    ),
    expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
    tools=[tool],
    agent=news_researcher,
     description="Perform research on groundbreaking technologies in {topic}"
)

write_task = Task(
    role="writer",
    goal = "Narrate compelling tech stories about {topic}",
    verbose = True,
    memory = True,
    backstory=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
    ),
    expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
    tools=[tool],
    description="Create a new blog post about {topic}",
    agent=news_writer,
    async_execution=False,
    output_file='new-blog-post.md'  
)
