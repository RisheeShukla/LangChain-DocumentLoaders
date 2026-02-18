from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
parser=StrOutputParser()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-235B-A22B-Instruct-2507",
    task="text-generation",
   
    temperature=2,
    max_new_tokens=100
)
model=ChatHuggingFace(llm=llm)
prompt=PromptTemplate(
    template='Write a summary of the following poem -\n {poem}',
    input_variables=['poem']
)
loader=TextLoader('cricket.txt',encoding='utf-8')
docs=loader.load()
chain=prompt|model|parser
print(chain.invoke({'poem':docs[0].page_content}))
