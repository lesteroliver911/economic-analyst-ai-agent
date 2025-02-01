# Economic Analyst AI Agent w/ Agno Agent Framework
A lightning-fast, locally-running RAG (Retrieval-Augmented Generation) implementation using the Agno AI framework. The agent leverages Ollama (Llama 3.2 3b) combining structured knowledge from financial reports (PDF Url's) with real-time web searches (duckduckgo). This project demonstrates how to build an efficient question-answering system for PDFs using local models and embeddings.

![Agno AI RAG Demo](https://github.com/lesteroliver911/economic-analyst-ai-agent/blob/main/asset/agno-ai.gif)

## Features

- **Lightweight Implementation**: Built with Agno AI framework requiring minimal code
- **Local Model Support**: Uses Llama 3.2 (3B parameters) for inference (toolcalling)
- **Local Embeddings**: Implements Nomic embeddings for document processing
- **PDF Processing**: Direct URL-to-PDF processing capability
- **High Performance**: Optimized for speed and efficiency
- **Easy Model Switching**: Flexible architecture supporting both open and closed-source models

## Technical Stack

- **Framework**: [Agno AI](https://github.com/agno-ai/agno)
- **Language Model**: Llama 3.2 (3B)
- **Embeddings**: Nomic

## 💻 System Requirements

- **Tested Hardware**: MacBook M1 2021, 8GB RAM
- **Model Setup**: Running Ollama with Llama 3.2 3B
- **Model Performance**: Llama 3.2 3B demonstrated superior performance compared to other tested models in terms of speed and response quality

## Data Source

- **PDF Url**: [US Economics Analyst 2025](https://www.goldmansachs.com/pdfs/insights/goldman-sachs-research/2025-us-economic-outlook-new-policies-similar-path/2025USEconomicOutlook.pdf)

## Getting Started

1. Clone the repository
2. Install dependencies
3. Configure your local models
4. Run the application

## Performance

The implementation shows significant speed improvements compared to traditional RAG implementations, particularly in:
- Document processing time
- Query response latency
- Memory efficiency

## Acknowledgments

Special thanks to:
- [Ashpreet Bedi](https://www.linkedin.com/in/ashpreetbedi/) for introducing the Agno AI framework
- The Agno AI team for their excellent documentation and support

## Resources

- [Agno AI Documentation](https://docs.agno.com)
- [Agno AI GitHub Repository](https://github.com/agno-ai/agno)

## Note

This is a side project created for educational purposes and to contribute to the developer community. Feel free to use, modify, and share!

## License

MIT
