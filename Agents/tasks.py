from multiprocessing import context
from crewai import Task
from textwrap import dedent

# from .agents import CustomAgents


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $100,000 on your annual bonus!"

    def make_context_analysis(self, agent, query):
        return Task(
        description=dedent(
            f"""
            You will analyze the philosophical question posed by the user to identify key concepts, themes, and context.
            **Params**
            - Query: {query}
            - Language: You have to use the language of the question {query}
           
            **Note**: Focus on breaking down the query into manageable parts, identifying underlying concepts and potential sub-questions.
            """
        ),
        agent=agent,
        expected_output=dedent(""" 
            A list of bullet points outlining the key themes, concepts, and sub-questions derived from the user's query.
            Your analysis should choose extremely thoughfull questions on the subject, not some generic questions.
        """)
    )

    
    def make_historical_research(self, agent, query):
        return Task(
        description=dedent(
            f"""
            You will research and summarize historical philosophical perspectives and theories relevant to each sub question prepared earlier.
            **Params**
            - Language: You have to use the language of the question {query}
           
            **Note**: Include references to key philosophers and their contributions to the topic.
            """
        ),
        agent=agent,
        expected_output=dedent(""" 
            A list summarizing key philosophical theories and historical perspectives related to each sub question prepared earlier.
            The list should contain a maximum of 10 points for each sub questions, each referencing a philosopher or a philosophical idea.
        """)
    )


    def make_logical_analysis(self, agent, query):
        return Task(
        description=dedent(
            f"""
            You will analyze the logical structure of the arguments related to each sub philosophical question, identifying strengths and weaknesses.
            **Params**
            - Language: You have to use the language of the question {query}
           
            **Note**: Focus on identifying potential logical fallacies, inconsistencies, and gaps in reasoning.
            """
        ),
        agent=agent,
        expected_output=dedent(""" 
            A list of bullet points highlighting logical strengths, potential fallacies, and areas where the reasoning could be improved for each sub questions.
            
        """)
    )

    
    def make_argumentation(self, agent, query):
        return Task(
        description=dedent(
            f"""
            You will construct well-structured arguments addressing each sub philosophical question detailled.
            **Params**
            - Language: You have to use the language of the question {query}
           
            **Note**: Focus on building arguments from different perspectives, considering multiple schools of thought.
            """
        ),
        agent=agent,
        expected_output=dedent(""" 
            A list of bullet points presenting structured arguments related to each sub philosophical question.
            
        """)
    )

    def make_counter_arguments(self, agent, query):
        return Task(
            description=dedent(
                f"""
                You will provide counter-arguments to challenge the main arguments related to each sub philosophical question.
                **Params**
    
                - Language: You have to use the language of the question {query}
            
                **Note**: Focus on highlighting alternative viewpoints and potential criticisms of the existing arguments.
                """
            ),
            agent=agent,
            expected_output=dedent(""" 
                A list of bullet points outlining counter-arguments to challenge each original arguments.
            
            """)
        )

    def make_synthesis(self, agent, query):
        return Task(
            description=dedent(
                f"""
                You will synthesize the information from arguments, counter-arguments, and historical research to form a cohesive response to each sub philosophical question.
                **Params**
                - Language: You have to use the language of the question {query}
            
                **Note**: Focus on balancing the different perspectives and providing a well-rounded conclusion.
                """
            ),
            agent=agent,
            expected_output=dedent(""" 
                A list of bullet points that synthesize the arguments and counter-arguments into a cohesive summary.
               
            """)
        )
    def make_ethics_analysis(self, agent, query):
        return Task(
            description=dedent(
                f"""
                You will analyze the ethical implications and moral considerations related to the user's philosophical question.
                **Params**
                - Language: You have to use the language of the question {query}
            
                **Note**: Focus on evaluating the ethical consequences of the arguments and their alignment with different moral theories.
                """
            ),
            agent=agent,
            expected_output=dedent(""" 
                A list of bullet points summarizing the ethical considerations and implications of the reasoning.
                The analysis should not exceed 10 points and should reference relevant ethical theories.
            """)
        )

    def make_dissertation(self, agent, query):
        return Task(
        description=dedent(
            f"""
            You are tasked with writing a comprehensive dissertation that synthesizes the results from all other tasks.
            This dissertation should be written as if by a top 0.1% philosopher in the world, showcasing depth, rigor, and thorough understanding of the philosophical question.
            **Params**
            - Language: You have to use the language of the question {query}

            **Note**: The dissertation must cover all aspects analyzed by the previous agents, including the context, historical perspectives, logical analysis, arguments, counter-arguments, synthesis, and ethical considerations.
            The writing should be formal, structured, and thoroughly argumentative, with proper citations where necessary.
            """
        ),
        agent=agent,
        expected_output=dedent(""" 
            A detailed, multi-page dissertation that fully explores the philosophical question.
            The dissertation should be well-structured, with sections including an introduction, analysis of context, historical perspectives, logical arguments, counter-arguments, ethical analysis, and a conclusion. Do not include them on the dissertation. You do not need to make title or bullet point.Your writing needs to have the ability to be choosen of the top philosophical dissertation on the subject.
            It should be written in a style that reflects deep philosophical expertise.
        """)
    )


