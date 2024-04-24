from crewai import Agent
from crewai_tools import SerperDevTool
from crewai_tools import ScrapeElementFromWebsiteTool
from langchain_openai import ChatOpenAI
from confs import OPENAI_API_KEY
from textwrap import dedent
from langchain.agents import load_tools





search_tool = SerperDevTool()
ScrapeFromWebsiteTool = ScrapeElementFromWebsiteTool()


# Loading Human Tools
human_tools = load_tools(["human"])


class ProductAgents():
    
    def product_researcher(self, config):
        return Agent(
            role=config['product_researcher']['role'],
            goal=config['product_researcher']['goal'],
            backstory = config['product_researcher']['backstory'],
            allow_delegation=True,
            max_rpm=1000,
            tools=[search_tool, ScrapeFromWebsiteTool] + human_tools,
            llm = ChatOpenAI(model_name = config['product_researcher']['model'], openai_api_key =  OPENAI_API_KEY, temperature = 0.3),
            verbose=False
        )
    
    def compliance_officer(self, config):
        return Agent(
            role=config['compliance_officer']['role'],
            goal=config['compliance_officer']['goal'],
            backstory = config['compliance_officer']['backstory'],
            allow_delegation=True,
            max_rpm=1000,
            tools=[search_tool] + human_tools,
            llm = ChatOpenAI(model_name = config['compliance_officer']['model'], openai_api_key =  OPENAI_API_KEY, temperature = 0.3),
            verbose=True
        )
    def consumer_product(self,config):
        return Agent(
            role=config['consumer_product']['role'],
            goal=config['consumer_product']['goal'],
            backstory = config['consumer_product']['backstory'],
            allow_delegation=False,
            max_rpm=1000,
            llm = ChatOpenAI(model_name = config['consumer_product']['model'], openai_api_key =  OPENAI_API_KEY, temperature = 0.7),
            verbose=False
        )
    
    def platform_product(self, config):
        return Agent(
            role=config['platform_product']['role'],
            goal=config['platform_product']['goal'],
            backstory = config['platform_product']['backstory'],
            allow_delegation=False,
            max_rpm=1000,
            llm = ChatOpenAI(model_name = config['platform_product']['model'], openai_api_key =  OPENAI_API_KEY, temperature = 0.4),
            verbose=True
        )
    def domain_architect(self, config):
        return Agent(
            role=config['domain_architect']['role'],
            goal=config['domain_architect']['goal'],
            backstory = config['domain_architect']['backstory'],
            allow_delegation=False,
            max_rpm=1000,
            llm = ChatOpenAI(model_name = config['domain_architect']['model'], openai_api_key =  OPENAI_API_KEY, temperature = 0.4),
            verbose=True
        )
    def product_head(self, config):
        return Agent(
            role=config['product_head']['role'],
            goal=config['product_head']['goal'],
            backstory = config['product_head']['backstory'],
            allow_delegation=False,
            max_rpm=1000,
            llm = ChatOpenAI(model_name =config['product_head']['model'], openai_api_key =  OPENAI_API_KEY, temperature = 0.3),
            verbose=True
        )



