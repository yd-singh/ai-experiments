
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import ProductAgents
from tasks import productTasks


tasks = productTasks()
agents = ProductAgents()

print("## Welcome to the Product Jarvis")
print('-------------------------------')
print(f"""Welcome to your Product Manager Bot! 🤖

I can assist you with the following:
      
Conducting Research
Assessing Risk
Identifying Compliance Issues with Your Features
Defining a Feature List
Prioritizing the Feature List
Crafting Effective Acceptance Criteria
Let's dive in and streamline your product management tasks together! How can I help you today?
      
Please note: As an assistive AI model, I can offer guidance, but errors may occur. Your input and oversight are invaluable in ensuring accuracy and achieving optimal results.""")

# Capture Topic of research. 
researchTopic = input("\n What would you like me to work on? Pls describe the requirements\n")
print(f"""\nGot it. thanks. I will now work on this and get back to you. Sit back and relax.""")

# Create Agents
product_reseacher = agents.product_researcher()
consumer_product_manager = agents.consumer_product()
compliance_officer = agents.compliance_officer()
platform_product = agents.platform_product()

# Create Tasks
resarch_topic_task = tasks.research_topic(product_reseacher, researchTopic) 
consumer_product_analysis = tasks.consumer_product_analysis(consumer_product_manager, researchTopic, resarch_topic_task)
compliance_research = tasks.compliance_recommendations(compliance_officer, researchTopic, [resarch_topic_task, consumer_product_analysis])
platform_product_analysis = tasks.platform_product_analysis(platform_product, researchTopic, [resarch_topic_task, consumer_product_analysis, compliance_research])
write_prd = tasks.write_prd(platform_product, researchTopic, [resarch_topic_task, consumer_product_analysis, compliance_research, platform_product_analysis])

crew = Crew (
    agents = [product_reseacher, consumer_product_manager, compliance_officer, platform_product],
    tasks = [resarch_topic_task, consumer_product_analysis, compliance_research, platform_product_analysis, write_prd],
    process=Process.hierarchical,
    manager_llm=ChatOpenAI(model="gpt-3.5-turbo-0125"),
    full_output=False,
    verbose = False
)

result = crew.kickoff()
# Print results
print("\n\n########################")
print("## Here is the result")
print(researchTopic)
print(result)
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