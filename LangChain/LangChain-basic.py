from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Create prompt
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple language."
)

# 2. Create model
model = ChatOpenAI(
    model="gpt-4o-mini"
)

# 3. Create output parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt | model | parser

# 5. Run chain
response = chain.invoke({
    "topic": "LangChain"
})

print(response)