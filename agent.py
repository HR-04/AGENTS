from crewai import Agent
from tools import tool
# from dotenv import load_dotenv
# load_dotenv()
import os
os.environ["OPENAI_API_KEY"] = "NA"
from langchain_community.llms import Ollama

llm = Ollama(model="llama3") 

news_researcher = Agent(
    role = 'Senior Researcher',
    goal = 'Uncover Ground Breaking Technologies in {topic}',
    verbose = True,
    memory = True,
    backstory= (
        "Driven  by curiosity,You're at the forefront of "
        "Innovation ,eager to explore and share knowledge that could change"
        "the world"
    ),
    tools=[tool],
    llm = llm,
    allow_delegation = True
)

news_writer = Agent(
    role="writer",
    goal = "Narrate compelling tech stories about {topic}",
    verbose = True,
    memory = True,
    backstory=(
        "with a flair for simplifying complex topics,you craft"
        "engaging narratives that captivate and educate,bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools= [tool],
    llm = llm,
    allow_delegation = False
)