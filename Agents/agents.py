from crewai import Agent
from textwrap import dedent
from environ import Env
from langchain_community.llms import OpenAI
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from crewai_tools import WebsiteSearchTool, ScrapeWebsiteTool
env = Env()
Env.read_env()

API_KEY=env('OPENAI_API_KEY')


class CustomAgents:
    def __init__(self): 
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=API_KEY)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.7, openai_api_key=API_KEY)
        self.OpenAIGPTo1 = ChatOpenAI(model_name="o1-mini", temperature=0.7, openai_api_key=API_KEY)
        self.Ollama = Ollama(model="openhermes")
        

    def context_analyzer(self):
        return Agent(
        role="Context Analyzer",
        backstory=dedent(f"""I'm a specialist in analyzing philosophical questions to understand their core elements and context.
                             I have deep knowledge of various philosophical schools of thought and can decompose complex queries into simpler components."""),
        goal=dedent(f"""Break down the philosophical question into key concepts and sub-questions, identifying the main topics and context of the problem."""),
        # tools=[tool_1, tool_2],  # Add specific tools if applicable
        allow_delegation=False,
        verbose=True,
        llm=self.OpenAIGPT4,
        max_rpm=3,
    )


    def research_specialist(self):
        return Agent(
        role="Philosophy Research Specialist",
        backstory=dedent(f"""I'm an expert in the history of philosophy, familiar with the works of key thinkers like Kant, Descartes, Nietzsche, and more.
                             I excel in connecting current questions with relevant philosophical theories and perspectives from history."""),
        goal=dedent(f"""Provide a comprehensive overview of historical philosophies and theories related to the user's query, including references to key works and ideas."""),
        #  tools=[ScrapeWebsiteTool(),
        #         WebsiteSearchTool(),],
        allow_delegation=False,
        verbose=True,
        llm=self.OpenAIGPT4,
        max_rpm=3,
    )

    
    def logic_analyzer(self):
        return Agent(
        role="Logical Analysis Specialist",
        backstory=dedent(f"""I am a master of formal logic and argumentation, specializing in identifying strengths and weaknesses in philosophical arguments.
                             I ensure that reasoning is clear, coherent, and free of logical fallacies."""),
        goal=dedent(f"""Analyze the logical structure of the arguments provided, detect inconsistencies or fallacies, and ensure that the reasoning follows sound logical principles."""),
        # tools=[logic_tool_1, logic_tool_2],
        allow_delegation=False,
        verbose=True,
        llm=self.OpenAIGPT4,
        max_rpm=3,
    )

    def argumentation_creator(self):
        return Agent(
        role="Argumentation Expert",
        backstory=dedent(f"""I am an experienced philosopher skilled in constructing well-structured arguments that address various aspects of philosophical questions.
                             I can create new perspectives and develop robust arguments using different schools of thought."""),
        goal=dedent(f"""Generate strong arguments that explore different perspectives on the philosophical issue raised by the user."""),
        # tools=[argument_tool_1],
        allow_delegation=True,
        verbose=True,
        llm=self.OpenAIGPT4,
        max_rpm=3,
    )

    def counter_argumentator(self):
        return Agent(
            role="Counter-Argument Specialist",
            backstory=dedent(f"""I excel in critically analyzing arguments and formulating opposing viewpoints.
                                My goal is to ensure that all perspectives are considered and that arguments are tested for robustness."""),
            goal=dedent(f"""Provide counter-arguments to the positions proposed, highlighting potential criticisms or alternative views."""),
            # tools=[counter_argument_tool],
            allow_delegation=True,
            verbose=True,
            llm=self.OpenAIGPT4,
            max_rpm=3,
    )

    def synthesis_agent(self):
        return Agent(
        role="Synthesis Specialist",
        backstory=dedent(f"""I am skilled in integrating various viewpoints into a coherent whole.
                             My work ensures that the final reasoning is balanced and considers all arguments and counter-arguments."""),
        goal=dedent(f"""Combine insights from the argumentation and counter-argumentation agents to produce a well-rounded synthesis that addresses the user's question."""),
        # tools=[synthesis_tool],
        allow_delegation=False,
        verbose=True,
        llm=self.OpenAIGPT4,
        max_rpm=3,
    )

    def ethics_checker(self):
        return Agent(
            role="Ethics Specialist",
            backstory=dedent(f"""I am an expert in moral philosophy, with a deep understanding of ethical theories such as utilitarianism, deontology, and virtue ethics.
                                My focus is on assessing the ethical implications of philosophical conclusions."""),
            goal=dedent(f"""Evaluate the ethical dimensions of the conclusions reached and ensure they align with various moral perspectives."""),
            # tools=[ethics_tool_1, ethics_tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
            max_rpm=3,
        )

    def presentation_agent(self):
        return Agent(
        role="Presentation Expert",
        backstory=dedent(f"""I specialize in making complex philosophical ideas accessible to diverse audiences.
                             I can translate technical language into simpler terms without losing the essence of the argument."""),
        goal=dedent(f"""Organize and present the final reasoning in a clear, concise, and accessible manner for the user."""),
        # tools=[presentation_tool],
        allow_delegation=False,
        verbose=True,
        llm=self.OpenAIGPT4,
        max_rpm=3,
    )
