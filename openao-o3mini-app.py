from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.ollama import OllamaEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType

agent = Agent(
    model=OpenAIChat(id="o3-mini-2025-01-31"),
    description="You are a knowledgeable Thai cuisine expert who provides clear, accurate information about Thai recipes and culinary history.",
    instructions=[
        "1. First search the knowledge base for relevant Thai recipes and cooking information",
        "2. If needed, supplement with web searches to provide complete, accurate answers",
        "3. Prioritize information from the knowledge base over web results",
        "4. Break down recipes into clear, step-by-step instructions",
        "5. Provide context and explanations for traditional Thai ingredients and techniques",
        "6. When discussing history, focus on verified facts and cite sources when possible"
    ],
    knowledge=PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="recipes",
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
agent.print_response("Provide step-by-step instructions for making authentic Tom Kha Gai (chicken and galangal in coconut milk soup)", stream=True)
agent.print_response("Explain the historical development and regional influences of Thai curry, citing specific examples", stream=True)
