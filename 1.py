#!/usr/bin/env python3
"""
Simple langchain request to LLM
examples:
What is the date today?
How many vacations are in Agiliway company?
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()

def main():
    # Initialize the LLM
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Get user input
    print("Enter your question (or 'quit' to exit):")
    user_input = input("> ")
    
    if user_input.lower() == 'quit':
        return
    
    # Create message and get response
    print("\nThinking...")
    messages = [HumanMessage(content=user_input)]
    response = llm.invoke(messages, config={"run_name": "1.py - Simple LLM Request"})
    
    # Print the response
    print("\n" + "="*50)
    print("Response:")
    print("="*50)
    print(response.content)
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
