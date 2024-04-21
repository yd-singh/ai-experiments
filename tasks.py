from crewai import Agent, Task, Crew
from textwrap import dedent

class productTasks():
    def research_topic(self, agent, topic):
        return Task(description=dedent(f"""Perform thorough research on the shared topic: 

			Instructions
			------------
    	{topic}
			"""),
			agent=agent,
            expected_output = dedent(f"""Your Final answer must be crisp bullet points, Compile all in sections for below: 
                            Market Analysis: Conducting in-depth market research to identify trends, competitors, and consumer behavior in the market.
                             User Insights: Gathering and analyzing user feedback, reviews, and behavior patterns related to digital products to understand user needs and preferences.
                             Search News: Gather any news, product launches, around products and features.
                             Competitive Analysis: Assessing competitors' digital products, features, pricing strategies, and market positioning to identify opportunities and gaps for product improvement or differentiation.
                             Content Analysis: Analyzing content related to digital products across various online platforms, including websites, forums, social media, and blogs, to gather insights and assess market sentiment.
                             Data Interpretation: Interpreting data from various sources, including Google Analytics, to track and measure product performance, user engagement, and conversion metrics.
                             Technology Trends: Staying updated on emerging technologies, innovations, and industry developments relevant to digital products, and incorporating insights into product research and strategy.
                             Reporting and Recommendations: Summarizing research findings, insights, and recommendations into actionable reports and presentations for product development teams and stakeholders.."""),
		)
    def compliance_recommendations(self, agent, topic, context):
        return Task(
            description=dedent(f"""Analyze the feature from compliance lesnse, specifically from RBI and NPCI POV
                Instructions
                ------------
                {topic}

            """),
            agent=agent,
            Context = context,
            expected_output=dedent("""Search RBI and NPCI and analyst the impact of the feautre from compliance POV. Ensure the feature doesnt brach any RBI or NPCI regulations
                                   or guidelines. Share recommendations, links of guidelines where applicable.""")
    )
    def consumer_product_analysis(self, agent, topic, context):
        return Task(
            description=dedent(f"""Analyze the provided topic from a consumer product manager point of view. 
                Instructions
                ------------
                  {topic}
            """),
            Context = context,
            agent=agent,
            expected_output=dedent("""List of why of feature from customer pov, think of great features and list them out. Mention sequencing and prioritisation"""),
    )
    def platform_product_analysis(self, agent, topic, context):
        return Task(
            description=dedent(f"""Analyze the provided topic from a platform product manager point of view. 
                              

                Instructions
                ------------
                {topic}
            """),
            Context = context,
            agent=agent,
            expected_output=dedent("""List out 'how to implement' feature from platform and reusability pov, think of great domain design and list them out. Mention sequencing and prioritisation"""),
    )
    def write_prd(self, agent, topic, context):
        return Task(
            description=dedent(f""" Collect inputs from product_researcher,  compliance_officer, consumer_product and platform_product to write a comprehensive PRD for the feature. 
                                

                Instructions
                ------------
                {topic}
            """),
            agent=agent,
            Context = context,
            expected_output=dedent("""Write a detailed document covering the below:  
                            Problem Statement: Write a detailed section with a clear problem statment. 
                            Background : Write a detailed section on the problem at hand, news, research in detail. Add important items as bullet points. 
                            Compliance & Regulatory: Write a detailed section on the take of RBI, NPCI. Add Mission Critial Compliance adherence items as bullet points. 
                            Proposed Solution: Write a detailed section on proposed solution covering platform product and consumer product recommendations. 
                            Stories: Write a detailed section on writing detailed stories breaking down the feature into smaller tasks. Write Story name, description in multiple bullet points. 
                            Acceptance Criteria: Write a comprehensive section on acceptance criteria. Make these multiple bullet points covering all functionalities proposed in stories. 
                            Risks & Assumptions: Write a comprehensive section on risks and assumptions with the feature and solutions.      
                                   """),
    )


