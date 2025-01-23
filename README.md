# AI Crew for Risk Assesment
## Introduction
This project demonstrates the use of the CrewAI framework to automate the decsion of risk assesment. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently.

- [CrewAI Framework](#crewai-framework)
- [Running the script](#running-the-script)


## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, these agents work together to analyze company culture and identify role requirements to create comprehensive job postings and industry analysis.

## Running the Script
It uses Bedrock by default so you should have access to that to run it.

***Disclaimer:** This will use gpt-4o unless you change it to use a different model, and by doing so it may incur in different costs.*

- **Configure Environment**: Copy `.env.example` and set up the environment variables for [OpenAI](https://platform.openai.com/api-keys) and other tools as needed, like [Serper](serper.dev).
- **Install Dependencies**: Run `pip install` to install crewai and crewai_tools

## Details & Explanation
- **Running the Script**: Execute `python main.py`. The script will leverage the CrewAI framework to generate a detailed job posting.
- **Key Components**:
  - `src/risk_asses/main.py`: Main script file.
  - `src/risk_asses/crew.py`: Main crew file where agents and tasks come together, and the main logic is executed.
  - `src/risk_asses/config/agents.yaml`: Configuration file for defining agents.
  - `src/risk_asses/config/tasks.yaml`: Configuration file for defining tasks.
  - `src/risk_asses/tools`: Contains tool classes used by the agents.


