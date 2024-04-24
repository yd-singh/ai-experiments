from crewai import Agent, Task, Crew
from textwrap import dedent
from utils import append_text_to_file

def callback_function(output):
    append_text_to_file(output.description)
    append_text_to_file(output.result)

class productTasks():
    def research_topic(self, agent, topic, config):
        return Task(description=config['research_task']['description'].format(topic=topic),
			agent=agent,
            expected_output = config['research_task']['expected_output'],
            async_execution=True,
            callback_function=callback_function
		)
    def compliance_recommendations(self, agent, topic, config):
        return Task(
            description=config['compliance_task']['description'].format(topic=topic), 
            agent=agent,
            expected_output=config['compliance_task']['expected_output'],
            async_execution=True,
            # context=context,
            callback_function=callback_function
    )
    def consumer_product_analysis(self, agent, topic, config):
        return Task(
            description=config['consumer_product_task']['description'].format(topic=topic), 
            # context=context,
            async_execution=True,
            agent=agent,
            expected_output=config['consumer_product_task']['expected_output'],
            callback_function=callback_function
    )
    def platform_product_analysis(self, agent, topic, config, context):
        return Task(
            description=config['platform_product_task']['description'].format(topic=topic), 
            agent=agent,
            context = context,
            expected_output=config['platform_product_task']['expected_output'],
            callback_function=callback_function
    )
    def write_prd(self, agent, topic, config, context):
        return Task(
           description=config['documentation_task']['description'].format(topic=topic), 
            context=context,
            agent=agent,
            expected_output=config['documentation_task']['expected_output'],
            callback_function=callback_function
    )




