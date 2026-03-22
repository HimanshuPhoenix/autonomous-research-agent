import os
import logging
# import google.cloud.logging
from dotenv import load_dotenv
from google.adk import Agent
from .tools import wikipedia_tool, add_prompt_to_state

# Setup Logging and Environment
#cloud_logging_client = google.cloud.logging.Client()
#cloud_logging_client.setup_logging()
load_dotenv()
model_name = os.getenv("MODEL", "gemini-2.5-flash")

# Define the Autonomous Research Agent
root_agent = Agent(
    name="researcher",
    model=model_name,
    description="An autonomous research assistant that finds academic insights.",
    instruction="""
    You are an autonomous AI research assistant. Your goal is to help users answer their PROMPT by finding and summarizing information.
    For this phase, use the Wikipedia tool to search for academic topics, methodologies, and concepts.
    When the user responds, use the 'add_prompt_to_state' tool to save their response.
    Synthesize the results from your tools into a structured literature review or summary.
    """,
    tools=[wikipedia_tool, add_prompt_to_state]
)