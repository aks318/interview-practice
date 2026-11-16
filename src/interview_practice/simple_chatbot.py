import string

from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_core.tools import tool

llm = ChatOllama(model = "gpt-oss:20b")

message = []


@tool
def maths(a: float, b: float, operation: str) -> float:
    """
    Perform a mathematical operation on two numbers.

    Args:
        a: First number.
        b: Second number.
        operation: Operation to perform. Supported values:
                   add, subtract, multiply, divide.
    """
    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    else:
        raise ValueError("Unsupported operation")

llm_with_tools = llm.bind_tools(tools=[maths])

tool_func_bind = {
    "maths" : maths
}


while True:
    userInput = input("User: ")
    UserMessage = HumanMessage(content=userInput)

    if userInput.lower() in ["bye", "goodbye", "exit"]:
        print("AI: Goodbye!")
        break

    if not userInput:
        continue
    message.append(UserMessage)

    res = ""

    tool_res = llm_with_tools.invoke([UserMessage])

    print("AI:", end="")
    if tool_res.tool_calls:
        tool = tool_res.tool_calls[0]
        for chunk in maths.stream(tool["args"]):
            res += str(chunk)
            print(str(chunk), end=" ", flush=True)
            
    else:
       



        for  chunk in llm.stream(message):
            res += chunk.content
            print(chunk.content, end = " ", flush=True)
        print("\n")
    message.append(AIMessage(res))

