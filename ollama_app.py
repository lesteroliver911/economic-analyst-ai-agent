from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.embedder.ollama import OllamaEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType

agent = Agent(
    model=Ollama(id="llama3.2"),
    description="You are an economic analyst expert who provides clear, accurate analysis of US economic trends, policies, and forecasts.",
    instructions=[
        "1. First search the knowledge base for relevant economic data and forecasts",
        "2. If needed, supplement with web searches to provide complete, accurate answers",
        "3. Prioritize information from the Goldman Sachs report over general web results",
        "4. Break down complex economic concepts into clear explanations",
        "5. Provide context and explanations for economic indicators and policy implications",
        "6. When discussing forecasts, focus on verified data and cite sources when possible"
    ],
    knowledge=PDFUrlKnowledgeBase(
        urls=["https://www.goldmansachs.com/pdfs/insights/goldman-sachs-research/2025-us-economic-outlook-new-policies-similar-path/2025USEconomicOutlook.pdf"],
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="economic_outlook",
            search_type=SearchType.hybrid,
            embedder=OllamaEmbedder(id="nomic-embed-text", dimensions=768),
        ),
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

# Load knowledge base only if needed
RELOAD_KNOWLEDGE = False  # Set to True to reload knowledge base
if agent.knowledge is not None and RELOAD_KNOWLEDGE:
    agent.knowledge.load()

# Example queries with clear objectives
agent.print_response("Analyze the key factors influencing US economic growth projections through 2025", stream=True)
agent.print_response("Explain the expected policy changes and their potential impact on inflation and employment", stream=True)
