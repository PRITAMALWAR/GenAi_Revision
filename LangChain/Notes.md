# LangChain

# what is LangChain ?

 LangChain is a framework for building applications powered by LLMs.
 LangChain is a framework for building LLM-based applications that helps connect or orchestrate models, prompts, retrieval, tools, agents, and other components.


                          LANGCHAIN
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
        MODELS             PROMPTS           PARSERS
          │                  │                  │
          └──────────────────┼──────────────────┘
                             ▼
                          RUNNABLES
                             │
                             ▼
                           CHAINS
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
          RETRIEVERS       TOOLS          MEMORY
              │              │
              ▼              ▼
        VECTOR STORE     EXTERNAL APIs
                             │
                             ▼
                           AGENTS
                             │
                             ▼
                       AI APPLICATION


Document
Document Loader
Text Splitter
Embeddings
Vector Store
Retriever
Prompt Template
Chain
LCEL

