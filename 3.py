#!/usr/bin/env python3
"""
Langchain Agent with a tool to get the Agiliway info from txt file
examples:
How many vacations can you take in Agiliway?
Where is the Agileway office located?
"""
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from datetime import datetime

# Load environment variables
load_dotenv()

def get_agiliway_info() -> str:
    """Get information about Agiliway company from the company information file.
    Use this tool when you need to answer questions about Agiliway company details,
    such as number of employees, vacation days, office locations, benefits, etc."""
    try:
        with open("./db/agiliway_info.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Company information file not found."

def get_today_date() -> str:
    """Get today's date.
    Use this tool when you need to know the current date, day of the week, or answer questions about today."""
    return datetime.now().strftime("%A, %B %d, %Y")

def main():
    # Create tools list
    tools = [get_agiliway_info, get_today_date]
    
    # Create agent using the new create_agent function
    agent = create_agent(
        model="gpt-4o-mini",
        tools=tools,
        system_prompt="""You are a helpful AI assistant for Agiliway company. 
You provide accurate, concise, and professional responses.
If you don't know something, admit it rather than making up information.""",
        name="3.py - Agent with Tools"
    )
    
    # Get user input
    print("Enter your question (or 'quit' to exit):")
    user_input = input("> ")
    
    if user_input.lower() == 'quit':
        return
    
    # Run the agent
    print("\nThinking...")
    result = agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]}
    )
    
    # Print the response
    print("\n" + "="*50)
    print("Response:")
    print("="*50)
    print(result["messages"][-1].content)
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
