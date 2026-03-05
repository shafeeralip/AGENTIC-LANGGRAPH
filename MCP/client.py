from langchain_mcp_adapters.client import MultiServerMCPClient
# from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model 
from langchain.agents import create_agent


import os 
from dotenv import load_dotenv

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")


import asyncio

llm = init_chat_model("groq:llama-3.1-8b-instant")



async def main():
    client = MultiServerMCPClient(
        {
            "Math":{
                "command":"python",
                "args":["mathserver.py"],
                "transport":"stdio"

            },
            "Weather":{
                "url":"http://127.0.0.1:8000/mcp",
                "transport":"streamable_http"


            }
        }
    )



    tools = await client.get_tools()

    agent = create_agent(llm,tools)

    math_response = await agent.ainvoke({"messages":[{"role":"user","content":"what is 2 + 2 ?"}]})

    print("respone",math_response['messages'][-1].content)

    math_response = await agent.ainvoke({"messages":[{"role":"user","content":"what is the weather in chennai?"}]})

    print("respone",math_response['messages'][-1].content)


asyncio.run(main())