# Autonomous Research & Learning Agent

An autonomous AI research assistant built with Google's Agent Development Kit (ADK) and Gemini. This agent helps users find, read, extract, and store academic insights from sources like arXiv, Semantic Scholar, and Wikipedia. 

This project was built for the **[Google Cloud Gen AI Academy APAC 2026](https://vision.hack2skill.com/event/apac-genaiacademy/)** and is designed to fulfill the requirements for Track 1 and Track 2.

## Architecture & Track Submissions

This project is divided into two phases to align with the program's track submissions:

### Phase 1: Core Agent & Deployment (Track 1)
*   **Goal:** Build and deploy a single AI agent using ADK and Gemini on Cloud Run.
*   **Implementation:** A conversational research agent built using `google-adk`. For this phase, the agent uses the `langchain-community` Wikipedia tool as a fallback to search for academic topics and summarize findings.
*   **Deployment:** Deployed as a serverless container to Google Cloud Run via the `adk deploy cloud_run` command.

### Phase 2: Tool & Data Integration via MCP (Track 2)
*   **Goal:** Connect the AI agent to external tools and real-world data using the Model Context Protocol (MCP).
*   **Implementation:** 
    *   **Data Storage:** Integrates a local **SQLite** database to persistently store research summaries, insights, and citations. The database is connected to the agent using the **MCP Toolbox for Databases**.
    *   **External APIs:** Connects to specialized academic MCP servers (arXiv API, Semantic Scholar) to fetch the latest research papers and extract methodologies and gaps.

## 🚀 Step-by-Step Workflow
1.  **Goal Input:** User provides a research goal (e.g., "Find latest research on AI hallucination mitigation").
2.  **Agent Planning:** The Gemini model generates a research plan.
3.  **MCP Tool Usage:** The agent queries arXiv/Semantic Scholar (or Wikipedia as a fallback) to read papers and extract insights.
4.  **Persistent Memory:** The agent uses the MCP Toolbox to store insights and citations in SQLite.
5.  **Output Generation:** The agent returns a structured literature review, key methods, and experiment ideas to the user.

## 🛠️ Project Structure
```text
autonomous-research-agent/
├── .env                 # Environment variables (Project ID, API keys)
├── requirements.txt     # Project dependencies
├── __init__.py      
├── agent.py         # Main agent definition and instructions
└── tools.py         # Wikipedia Langchain tools and MCP toolsets
└── tools.yaml       # Database and query configurations (Only Wikipedia for Track1)
└── README.md
```

## 💻 Local Setup & Testing
* Instructions will be added as we buid

---

## Author
  Himanshu Saxena
  
  MSc Artificial Intelligence
  [IUBH, Germany](https://iu.org)
  
  GitHub: https://github.com/HimanshuPhoenix

---

## License
This project is for educational and research purposes.
