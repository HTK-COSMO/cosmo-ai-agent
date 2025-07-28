
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from tools.excel_tools import handle_excel

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

tools = [
    Tool(
        name="ExcelTool",
        func=handle_excel,
        description="Dùng để xử lý Excel"
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="chat-conversational-react-description",
    memory=memory,
    verbose=True,
)

def run_agent(input_text):
    return agent.run(input_text)
