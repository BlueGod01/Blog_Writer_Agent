# Blog Writing Agent

An intelligent, multi-agent AI system built to automate the end-to-end process of researching, planning, and writing high-quality technical blog posts.

## 🚀 Overview

Blog Writing Agent uses a directed graph architecture powered by [LangGraph](https://github.com/langchain-ai/langgraph) to orchestrate a team of specialized AI nodes. By simply providing a topic and an "as-of" date, the system will:

1. **Decide** if web research is required based on the nature of the topic (e.g., evergreen vs. latest news).
2. **Research** the web using Tavily for up-to-date, authoritative sources.
3. **Plan** a comprehensive outline including specific goals, bullet points, target word counts, and required citations for each section.
4. **Write** each section in parallel matching the required tone, audience, and constraints.
5. **Decide & Enrich** the final blog post by generating and placing relevant diagrams/images using Google Gemini.

## 🗂️ Project Structure

```text
blog-writing-agent-main/
├── backend/
│   ├── schemas.py      # Pydantic data models for structured LLM outputs and State types
│   ├── nodes.py        # LangGraph node functions (Router, Research, Orchestrator, Worker, etc.)
│   ├── graph.py        # Directed graph definitions and edge routing logic
│   └── backend_api.py  # Compilation point exposing the `app` instance
├── frontend.py         # Streamlit-based interactive UI
├── notebooks/          # Jupyter notebooks documenting the iterative evolution of the agent
├── pyproject.toml      # Project initialization metadata 
└── requirements.txt    # Required Python dependencies
```

## 🛠️ Technology Stack

- **Orchestration**: [LangGraph](https://github.com/langchain-ai/langgraph) & [LangChain](https://github.com/hwchase17/langchain)
- **Language Model**: OpenAI GPT models via `langchain-openai`
- **Web Research**: [Tavily Search API](https://tavily.com/)
- **Image Generation**: Gemini 2.5 Flash via `google-genai`
- **Data Validation**: [Pydantic](https://docs.pydantic.dev/)
- **Frontend**: [Streamlit](https://streamlit.io/)

## ⚙️ Setup and Installation

1. **Clone the repository and enter the directory**:
   ```bash
   cd blog-writing-agent-main
   ```

2. **Install dependencies**:
   Using `uv` (recommended):
   ```bash
   uv pip install -r requirements.txt
   ```
   Or using standard `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:
   Create a `.env` file in the root directory and add your necessary API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   TAVILY_API_KEY=your_tavily_api_key
   GOOGLE_API_KEY=your_google_api_key  # For Gemini Image Generation
   ```

## 💻 Usage

Run the Streamlit frontend locally:

```bash
streamlit run frontend.py
```

The intuitive UI provides distinct tabs during and after generation:
- **Plan**: Visualizes the AI-generated outline and sectional goals.
- **Evidence**: Lists the sources gathered by the research node.
- **Markdown Preview**: Fully rendered preview of the resulting blog with inline images.
- **Images**: Displays the generated images and their prompts.
- **Logs**: Raw outputs and execution traces from the LangGraph nodes.

You can download the final Markdown file alone or fetch a bundled `.zip` file containing both the Markdown and locally saved generated images. You can also view past generated blogs directly in the sidebar.

## 📓 Reference Notebooks

The `notebooks/` directory contains experiments and prototypes showcasing how the agent was built step-by-step:
- `1_bwa_basic.ipynb`: Basic generation logic layout.
- `2_bwa_improved_prompting.ipynb`: Enhancements in system prompting and structured planning.
- `3_bwa_research.ipynb`: Integration of Tavily for live web search and evidence extraction.
- `4_bwa_research_fine_tuned.ipynb`: Advanced constraints and grounded generation.
- `5_bwa_image.ipynb`: Subgraph experiments for image planning and generation.
- `tavily_test.ipynb`: Standalone testing of the Tavily extraction pipeline.

A huge shoutout to Nitish Singh of CampusX for this notebook references
