
# Level 1 — Understand RAG

First understand the basic flow:

```text
User Question
     ↓
   RETRIEVE
     ↓
Relevant Information
     ↓
   AUGMENT
     ↓
Question + Relevant Information
     ↓
   GENERATE
     ↓
LLM Answer
```

RAG =

**R → Retrieve**
Find relevant information.

**A → Augment**
Put that information into the prompt.

**G → Generate**
Ask the LLM to generate the answer using that information.

---

# Level 2 — Tokens

Before embeddings, you should understand **tokens**.

For example:

```python
text = "Who is the Prime Minister of India?"
```

A tokenizer breaks the text into smaller pieces called **tokens**.

We'll learn:

```text
Text
 ↓
Tokenizer
 ↓
Tokens
 ↓
Token IDs
```

You'll understand:

- What is a token?
- What is a token ID?
- Why do LLMs use tokens?
- How tokenization works
- Context window
- Why token count matters

---

# Level 3 — Embeddings

This is one of the most important concepts in RAG.

You'll learn:

```text
Text
 ↓
Embedding Model
 ↓
Vector
```

For example:

```text
"Python is a programming language"
             ↓
        Embedding Model
             ↓
[0.12, -0.45, 0.78, ...]
```

You'll understand:

- What is an embedding?
- What is a vector?
- Why convert text into vectors?
- Semantic similarity
- Cosine similarity

---

# Level 4 — Vector Search

Now we make the **R** in RAG.

We'll have:

```text
Documents
   ↓
Chunks
   ↓
Embeddings
   ↓
Vector Database
```

Then:

```text
User Question
      ↓
Question Embedding
      ↓
Vector Search
      ↓
Relevant Chunks
```

You'll learn databases such as:

- FAISS
- Chroma
- later, production vector databases

---

# Level 5 — Document Processing

Real RAG doesn't usually start with a small string.

We'll learn how to work with:

```text
PDF
TXT
DOCX
Web pages
CSV
```

The pipeline becomes:

```text
Document
   ↓
Load
   ↓
Extract text
   ↓
Clean text
   ↓
Chunk text
   ↓
Create embeddings
   ↓
Store vectors
```

---

# Level 6 — Chunking

This is extremely important.

Suppose you have a 100-page PDF.

We don't normally send the entire PDF to the LLM every time.

Instead:

```text
100-page PDF
     ↓
   Chunks
     ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
...
```

Then retrieve only the useful chunks.

We'll learn:

- Fixed-size chunking
- Character chunking
- Token-based chunking
- Recursive chunking
- Chunk overlap
- How chunk size affects retrieval

---

# Level 7 — Build Your First RAG

Then we'll build a complete beginner RAG:

```text
PDF
 ↓
Text extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector database
 ↓
User question
 ↓
Similarity search
 ↓
Relevant chunks
 ↓
Prompt
 ↓
LLM
 ↓
Answer
```

You'll write the code yourself step by step.

---

# Level 8 — Improve RAG

Once basic RAG works, we'll move to:

### Retrieval

- Top-K retrieval
- Similarity threshold
- Metadata filtering
- Hybrid search
- Keyword + semantic search

### Generation

- Prompt design
- Context formatting
- Source citations
- Handling "I don't know"
- Reducing hallucinations

---

# Level 9 — Advanced RAG

After you are comfortable with basic RAG:

```text
Advanced RAG
│
├── Query rewriting
├── Query expansion
├── Multi-query retrieval
├── Reranking
├── Hybrid retrieval
├── Metadata filtering
├── Parent-child retrieval
├── Multi-vector retrieval
├── Context compression
└── Agentic RAG
```

---

# Level 10 — Production RAG

Finally:

```text
Production RAG
│
├── Evaluation
├── Retrieval evaluation
├── Answer evaluation
├── RAGAS
├── Latency
├── Cost optimization
├── Caching
├── Observability
├── Security
└── Deployment
```

---

## How we will learn

I recommend **not jumping directly into LangChain or complicated frameworks**.

We'll first understand what is happening underneath.

For example, instead of immediately doing:

```python
chain = ...
```

I want you to understand:

```python
documents
    ↓
chunks
    ↓
embeddings
    ↓
vector search
    ↓
context
    ↓
prompt
    ↓
LLM
```
