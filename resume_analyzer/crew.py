from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from crewai_tools import FileReadTool, SerperDevTool

@CrewBase
class ResumeAnalyzer():
    """ResumeAnalyzer crew"""
    def __init__(self):
        self.agents: List[BaseAgent]
        self.tasks: List[Task]
        self.read_resume = FileReadTool(file_path='./fake_resume.md')
        self.search_tool = SerperDevTool()

    ################# List of Agents #################
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], 
            tools = [self.read_resume]
        )
    @agent
    def profiler(self) -> Agent:
        return Agent(
            config=self.agents_config['profiler'], 
            tools = [self.read_resume, self.search_tool]
        )
    @agent
    def resume_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_strategist'], 
            tools = [self.read_resume, self.search_tool]
        )
    @agent
    def interview_preparer(self) -> Agent:
        return Agent(
            config=self.agents_config['interview_preparer'], 
            tools = [self.read_resume, self.search_tool]
        )
    
    ################# List of Task #################
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], 
        )
    @task
    def profile_task(self) -> Task:
        return Task(
            config=self.tasks_config['profile_task'], 
        )
    @task
    def resume_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['resume_strategy_task'], 
        )
    @task
    def interview_preparation_task(self) -> Task:
        return Task(
            config=self.tasks_config['interview_preparation_task']
        )

    ################# Creating Crew #################
    @crew
    def crew(self) -> Crew:
        """Creates the ResumeAnalyzer crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            # process=Process.asynchronous
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
