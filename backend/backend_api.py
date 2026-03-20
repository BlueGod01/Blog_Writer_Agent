import os
from dotenv import load_dotenv

# Load environment variables (such as OPENAI_API_KEY, TAVILY_API_KEY, GOOGLE_API_KEY)
load_dotenv()

from graph import create_main_graph

def create_app():
    """
    Compiles everything and creates a LangGraph app that can be 
    imported and used in the frontend script.
    """
    g = create_main_graph()
    app = g.compile()
    return app

# The constructed langgraph app that can be imported
app = create_app()
