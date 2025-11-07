#!/usr/bin/env python3
"""
Langchain Agent with a tool to get the product info from API
examples:
What is the price of the laptop?
Tell me about the smartphone features
Which products are in stock?
"""
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from datetime import datetime
import json
from db.products_db import PRODUCTS_DB

# Load environment variables
load_dotenv()

def search_product(product_name: str) -> str:
    """Search for product information by product name.
    Use this tool when you need to find details about a specific product like laptop, smartphone, or headphones.
    
    Args:
        product_name: The name of the product to search for (e.g., 'laptop', 'smartphone', 'headphones')
    
    Returns:
        Product information as JSON string or error message if not found
    """
    product_name_lower = product_name.lower().strip()
    
    # Try exact match first
    if product_name_lower in PRODUCTS_DB:
        return json.dumps(PRODUCTS_DB[product_name_lower], indent=2)
    
    # Try partial match
    for key in PRODUCTS_DB.keys():
        if product_name_lower in key or key in product_name_lower:
            return json.dumps(PRODUCTS_DB[key], indent=2)
    
    # List available products if not found
    available_products = ", ".join(PRODUCTS_DB.keys())
    return f"Product '{product_name}' not found. Available products: {available_products}"

def list_all_products() -> str:
    """Get a list of all available products in the catalog.
    Use this tool when you need to see all products or when the user asks about available items.
    
    Returns:
        List of all products with basic information as JSON string
    """
    products_summary = []
    for key, product in PRODUCTS_DB.items():
        products_summary.append({
            "name": product["name"],
            "price": f"{product['price']} {product['currency']}",
            "in_stock": product["in_stock"],
            "category": product["category"]
        })
    return json.dumps(products_summary, indent=2)

def get_today_date() -> str:
    """Get today's date.
    Use this tool when you need to know the current date, day of the week, or answer questions about today."""
    return datetime.now().strftime("%A, %B %d, %Y")

def main():
    # Create tools list
    tools = [search_product, list_all_products, get_today_date]
    
    # Create agent using the new create_agent function
    agent = create_agent(
        model="gpt-4o-mini",
        tools=tools,
        system_prompt="""You are a helpful AI shopping assistant. 
You help customers find product information, check availability, and answer questions about our products.
You provide accurate, concise, and professional responses.
When showing prices or product details, format them in a clear and readable way.""",
        name="4.py - Product Search Chat"
    )
    
    print("=" * 60)
    print("Welcome to the AI Shopping Assistant!")
    print("Ask me about products, prices, availability, and more.")
    print("Type 'quit' or 'exit' to end the conversation.")
    print("=" * 60 + "\n")
    
    # Chat loop
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
            
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("\nThank you for shopping with us! Goodbye! 👋\n")
            break
        
        # Run the agent
        print("\nThinking...")
        try:
            result = agent.invoke(
                {"messages": [{"role": "user", "content": user_input}]}
            )
            
            # Print the response
            print(f"\nAssistant: {result['messages'][-1].content}\n")
            print("-" * 60 + "\n")
            
        except Exception as e:
            print(f"\nError: {str(e)}\n")
            print("Please try again.\n")

if __name__ == "__main__":
    main()
