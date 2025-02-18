def generate_webpage_summary_template():
    return """{text}

    -------------------

    Using the above text, answer in short the following question related to demolition services:

    > {question}

    -------------------
    If the question cannot be answered using the text, simply summarize the text. Include all factual information, numbers, stats, specific demolition techniques mentioned, equipment used, and any regulatory information.
    """

def generate_search_queries_prompt():
    return 'Write 3 google search queries to research demolition services and form an objective opinion from the following task: "{question}"' \
           'Also include in the queries specified task details such as locations (city, state, region), names of demolition companies, types of demolition (e.g., building implosion, bridge demolition, interior demolition), specific equipment (e.g., high-reach excavator, crusher), regulatory keywords (e.g., asbestos abatement, demolition permits), and any other relevant demolition-specific terms.\n' \
           'You must respond with a list of search queries strictly in the following format: ["query 1", "query 2", "query 3"].'

def generate_research_report_prompt():
    return (
        'Information: """{context}"""\n\n'
        'Using the above information, write a detailed report addressing the following query related to demolition services: "{question}".\n\n'
        '### Report Guidelines:\n'
        '- The report should be well-structured, informative, and unbiased.\n'
        '- Provide in-depth analysis with factual details (minimum 1000 words).\n'
        '- Use markdown syntax for formatting.\n'
        '- Formulate a concrete opinion based on the given data; avoid vague conclusions.\n\n'
        '### Key Report Elements:\n'
        '- **Specific Demolition Techniques**:\n'
        '  - Discuss techniques such as implosion, controlled demolition, and dismantling.\n'
        '  - Reference competitors and highlight which techniques they specialize in or are known for.\n\n'
        '- **Types of Equipment Used**:\n'
        '  - Include equipment like excavators, crushers, and high-reach demolition booms.\n'
        '  - Compare equipment used by major competitors and identify any unique or advanced tools they employ.\n\n'
        '- **Safety Protocols and Certifications**:\n'
        '  - Cover industry standards such as OSHA compliance and asbestos abatement certifications.\n'
        '  - Highlight how competitors adhere to safety protocols or any certifications they prominently advertise.\n\n'
        '- **Environmental Considerations**:\n'
        '  - Discuss sustainable practices like recycling, waste management, and minimizing environmental impact.\n'
        '  - Analyze how competitors incorporate sustainability into their operations and whether they promote it as a key differentiator.\n\n'
        '- **Regulatory Compliance**:\n'
        '  - Address local, state, and federal permitting requirements.\n'
        '  - Compare how competitors handle regulatory compliance and their reputation for meeting or exceeding standards.\n\n'
        '- **Cost Considerations**:\n'
        '  - Explore pricing models in the demolition industry.\n'
        '  - Provide insights into competitors’ pricing strategies (if available) or their positioning in terms of cost-effectiveness versus premium services.\n\n'
        '- **Key Players and Competitive Landscape**:\n'
        '  - Identify major competitors in the demolition market.\n'
        '  - Analyze their market share, service offerings, and any notable projects that set them apart.\n\n'
        '- **Emerging Trends and Technologies**:\n'
        '  - Discuss innovations like BIM for demolition, robotics, or other advancements shaping the industry.\n'
        '  - Highlight which competitors are early adopters of these technologies or are leading innovation efforts.\n\n'
        '### Referencing:\n'
        '- Cite all sources with hyperlinks ([source name](url)).\n'
        '- Include inline citations for referenced data.\n\n'
        '### Example Report Structure:\n\n'
        '# Report Title\n\n'
        'Introduction...\n\n'
        '## Key Techniques...\n\n'
        '## Equipment Used...\n\n'
        '[Source Name](url)\n\n'
    )
