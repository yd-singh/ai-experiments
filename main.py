
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import ProductAgents
from tasks import productTasks
from utils import load_config
import gradio as gr
import json


def create_crew(researchTopic):
    tasks = productTasks()
    agents = ProductAgents()

    # Capture Topic of research. 
    #loading configs
    agentConfig = load_config('agentConfig.yaml')
    taskConfig = load_config('taskConfig.yaml')

    # Create Agents
    product_reseacher = agents.product_researcher(agentConfig)
    consumer_product_manager = agents.consumer_product(agentConfig)
    compliance_officer = agents.compliance_officer(agentConfig)
    platform_product = agents.platform_product(agentConfig)
    product_head = agents.product_head(agentConfig)



    # Create Tasks
    resarch_topic_task = tasks.research_topic(product_reseacher, researchTopic, taskConfig)
    consumer_product_analysis = tasks.consumer_product_analysis(consumer_product_manager, researchTopic, taskConfig)
    compliance_research = tasks.compliance_recommendations(compliance_officer, researchTopic, taskConfig)
    platform_product_analysis = tasks.platform_product_analysis(platform_product, researchTopic, taskConfig, [resarch_topic_task, consumer_product_analysis, compliance_research])
   # write_prd = tasks.write_prd(product_head, researchTopic, taskConfig, [resarch_topic_task, consumer_product_analysis, compliance_research, platform_product_analysis])
    crew = Crew (
        agents = [product_reseacher, consumer_product_manager, compliance_officer, platform_product, product_head],
        tasks = [resarch_topic_task, consumer_product_analysis, compliance_research, platform_product_analysis],
        process=Process.hierarchical,
        manager_llm=ChatOpenAI(model="gpt-4-turbo-2024-04-09"),
        full_output=True,
        memory=True,
        verbose = False
    )
    results = crew.kickoff()

    print("\n\n########################")
    print("## Here is the result")
    print(researchTopic)
    print(results)
    print("########################\n")
    print("final summary: :")

    print(f"""
        Searching and reporting on the topic: {researchTopic}
        # Task: {resarch_topic_task.output.description}
        Output: {resarch_topic_task.output.raw_output}

        Conducting consumer product analysis: {researchTopic}
        # Task: {consumer_product_analysis.output.description}
        Output: {consumer_product_analysis.output.raw_output}

        Conducting Compliance Review: {researchTopic}
        # Task: {compliance_research.output.description}
        Output: {compliance_research.output.raw_output}

        Conducting platform product analysis: {researchTopic}
        # Task: {platform_product_analysis.output.description}
        Output: {platform_product_analysis.output.raw_output}
    """)


    output = [researchTopic, 
              '\n\n',
              resarch_topic_task.output.description,
              '\n\n',
              resarch_topic_task.output.raw_output, 
              '\n\n',
              consumer_product_analysis.output.raw_output, 
              '\n\n',
              compliance_research.output.description, 
              '\n\n',
              compliance_research.output.raw_output,
              '\n\n',
              platform_product_analysis.output.description,
              '\n\n',
              platform_product_analysis.output.raw_output]
    return output


def product_jarvis(researchTopic):
    results = create_crew(researchTopic)
    return results

iface = gr.Interface(

    fn = product_jarvis,
    inputs="text",
    outputs="html",
    title="Product Jarvis",
    description=("""Welcome to your Product Manager Bot! 🤖 \n

    I can assist you with the following:\n
        
    Conducting Research\n
    Assessing Risk\n
    Identifying Compliance Issues with Your Features\n
    Defining a Feature List\n
    Prioritizing the Feature List\n
    Crafting Effective Acceptance Criteria\n
    Let's dive in and streamline your product management tasks together! How can I help you today?\n
        
    Please note: As an assistive AI model, I can offer guidance, but errors may occur. Your input and oversight are invaluable in ensuring accuracy and achieving optimal results.\n""")

)
iface.launch()
