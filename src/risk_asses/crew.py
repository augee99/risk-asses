from typing import List
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool, FileReadTool, PDFSearchTool
from pydantic import BaseModel, Field
from PDFReaderTool import PDFReaderTool

AWS_DEFAULT_REGION='us-east-1' 
llm = LLM(model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0",aws_region_name='us-east-1' )


pdf_reader_tool = PDFReaderTool(pdf_path="./creditReport.pdf")

@CrewBase
class RiskAssesCrew:
    """RIskAsses crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def risk_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['risk_agent'],
            tools=[pdf_reader_tool],
            llm=llm,
            verbose=True
        )
    
    @agent
    def loan_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['loan_agent'],
#            tools=[file_read_tool],            
            llm=llm,
            verbose=True
        )
       
    @task
    def research_credit_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_credit_report_task'],
            agent=self.risk_agent()
        )

    @task
    def loan_assesment_task(self) -> Task:
        return Task(
            config=self.tasks_config['loan_assesment_task'],
            agent=self.loan_agent()
        )

    
    @crew
    def crew(self) -> Crew:
        """Creates the RiskAssesCrew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )