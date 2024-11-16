import os
import logging
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI


from textwrap import dedent

from sympy import residue
from .agents import CustomAgents
from .tasks import CustomTasks





class CustomCrew:
    def __init__(self, query):
        self.query = query
  
    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents here
        context_analyzer = agents.context_analyzer()
        research_specialist = agents.research_specialist()
        logic_analyzer = agents.logic_analyzer()
        argumentation_creator = agents.argumentation_creator()
        counter_argumentator = agents.counter_argumentator()
        synthesis_agent = agents.synthesis_agent()
        ethics_checker = agents.ethics_checker()
        presentation_agent = agents.presentation_agent()

        # Custom tasks include agent name and variables as input
        context_analysis_task = tasks.make_context_analysis(
            context_analyzer,
            self.query,
        )

        historical_research_task = tasks.make_historical_research(
            research_specialist,
            self.query,
        )

        logical_analysis_task = tasks.make_logical_analysis(
            logic_analyzer,
            self.query,
        )

        argumentation_task = tasks.make_argumentation(
            argumentation_creator,
            self.query,
        )

        counter_argument_task = tasks.make_counter_arguments(
            counter_argumentator,
            self.query,
        )

        synthesis_task = tasks.make_synthesis(
            synthesis_agent,
            self.query,
        )

        ethics_analysis_task = tasks.make_ethics_analysis(
            ethics_checker,
            self.query,
        )

        dissertation_task = tasks.make_dissertation(
            presentation_agent,
            self.query,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[
                context_analyzer,
                research_specialist,
                logic_analyzer,
                argumentation_creator,
                counter_argumentator,
                synthesis_agent,
                #ethics_checker,
                presentation_agent
            ],
            tasks=[
                context_analysis_task,
                historical_research_task,
                logical_analysis_task,
                argumentation_task,
                counter_argument_task,
                synthesis_task,
                #ethics_analysis_task,
                dissertation_task
            ],
            verbose=False,
            full_output=True,
        )

        result = crew.kickoff()
        return result



# This is the main function that you will use to run your custom crew.
# if __name__ == "__main__":
#     print("## Welcome to Crew AI Template")
#     print("-------------------------------")
#     query = input(dedent("""Enter your query : """))
    
#     custom_crew = CustomCrew(query)
#     result = custom_crew.run()
#     print("\n\n########################")
#     print("## Here is you custom crew run result:")
#     print("########################\n")
#     print(result)

def activate_agents(query):
    try:
        custom_crew = CustomCrew(query)
        result = custom_crew.run()
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
        return None
    else:
        return result['Final Answer']
    finally:
        logging.info("Agent activation attempted.")