from typing import TypedDict, Annotated
from dotenv import load_dotenv
import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_community.utilities import GoogleSerperAPIWrapper

from langgraph.graph import StateGraph
from agents.itinerary import generate_itinerary

# Load environment variables
load_dotenv()

# Set page title
st.set_page_config(page_title="AI Travel Planner", layout="wide", page_icon=":earth_asia:")

# Initialize LLM
try:
    llm = ChatOllama(model="llama3.2")
except Exception as e:
    st.error(f"Error initializing LLM: {e}")
    st.stop()
 
# Initialize GoogleSerperAPIWrapper
try:
    search = GoogleSerperAPIWrapper()
except Exception as e:
    st.error(f"Error initializing GoogleSerperAPIWrapper: {e}")
    st.stop()

# LangGraph
class GraphState(TypedDict):
    preferences_text: str
    preferences: dict
    itinerary: str
    activity_suggestions: str
    useful_links: list[dict]
    weather_forecast: str
    packing_list: str
    food_culture_info: str
    chat_history: Annotated[list[dict], "List of question-response pairs"]
    user_question: str
    chat_response: str

# Initialize LangGraph
workflow = StateGraph(GraphState)
workflow.add_node("generate_itinerary", generate_itinerary)


# Set page title
st.title("AI Travel Planner")

# Set page title