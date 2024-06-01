# AI Agents

## Description

This project runs on the Command Line Interface (CLI) and features two main agents:
- **news_researcher**: This agent researches the web about the provided topic.
- **news_writer**: This agent provides content based on the research done by the news_researcher.

The project uses the Google Search API ([serpAPI](https://serpapi.com/)) to fetch information from the web.

## Tech Stack

- **Programming Language**: Python
- **API**: Google Search API ([serpAPI](https://serpapi.com/))

## Installation

### Prerequisites
- Python 3.8+
- serpAPI Key

### Steps

1. **Clone the Repository**
    ```sh
    git clone https://github.com/HR-04/AGENTS.git
    cd ai-agents
    ```

2. **Set Up the Environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up serpAPI Key**
    - Obtain your serpAPI key from [serpAPI](https://serpapi.com/)
    - Create a `.env` file in the project root directory and add your key:
      ```sh
      SERPAPI_KEY=your_serpapi_key
      ```

## Usage

### Set Up CrewAI

1. **Install CrewAI and Necessary Packages**
    ```sh
    pip install crewai
    ```

2. **Define Your Agents**
    - Define agents with distinct roles, backstories, and capabilities in your project script.

3. **Define the Tasks**
    - Specify the tasks for each agent.

4. **Form the Crew**
    - Initialize and configure the agents.

5. **Kick It Off**
    - Run the main script to start the agents:
      ```sh
      python crew.py
      ```


