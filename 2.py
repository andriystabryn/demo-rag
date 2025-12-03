#!/usr/bin/env python3
"""
Simple langchain request to LLM + some context
examples:
What is the date today?
How many vacations can you take in Agiliway?
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from datetime import datetime

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
    

    today = datetime.now().strftime("%A, %B %d, %Y")

    # System prompt with instructions
    system_prompt = f"""You are a helpful AI assistant for Agiliway company. 
    You provide accurate, concise, and professional responses.
    If you don't know something, admit it rather than making up information.
    Today is {today}.
    Agiliway company has 20 vacations.
    Agiliway has 200 employees and 3 offices in Ukraine (Lviv, Ivano-Frankivsk, and Kyiv, Chernihivtsi), one in Krakow, and one in Texas."""
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]
    response = llm.invoke(messages, config={"run_name": "2.py - LLM with Context"})
    
    # Print the response
    print("\n" + "="*50)
    print("Response:")
    print("="*50)
    print(response.content)
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
