# Event Driven AI Workflow Engine

Phase 1 focuses on building the foundation of an enterprise AI workflow platform using event-driven backend architecture.

This phase is designed to understand how real production systems process webhooks, queues, workers, AI workflows, and async operations.

---

# Objective

Build a scalable backend workflow engine that can:

* receive webhook events
* persist events into Postgres
* publish events to Redis queues
* process events asynchronously
* execute AI workflows using LangGraph
* perform AI-based classification and routing
* trigger automated actions

---

# Completed Features

* FastAPI webhook ingestion
* Neon/Postgres event storage
* Redis queue publishing
* Background worker processing
* LangGraph workflow orchestration
* AI issue classification
* AI severity calculation
* Conditional routing
* Incident escalation flow
* Auto-response flow

---

# Architecture

```text id="y0l67q"
Webhook
   ↓
Postgres
   ↓
Redis Queue
   ↓
Worker
   ↓
LangGraph
   ↓
AI Decision
   ↓
Action / Tool
```

---

# Tech Stack

* FastAPI
* Redis
* Neon/Postgres
* SQLAlchemy Async
* LangGraph
* Groq LLM
* Python 3.11

---

# Workflow

## 1. Webhook Ingestion

FastAPI receives incoming events.

Example:

```json id="vbr8ca"
{
  "message": "Payment failing for multiple stores",
  "customer_email": "test@example.com"
}
```

---

## 2. Event Persistence

Events are stored in Postgres for:

* audit tracking
* retries
* observability
* workflow history

---

## 3. Queue Publishing

Events are pushed into Redis queues.

Why queues?

* non-blocking processing
* high scalability
* async workflows
* retry capability
* worker distribution

---

## 4. Worker Processing

Background workers continuously consume events from Redis.

Workers invoke LangGraph workflows asynchronously.

---

## 5. AI Workflow Execution

LangGraph performs:

* issue classification
* severity analysis
* routing decisions

---

## 6. Conditional Routing

High severity:

```text id="zv7m3s"
→ escalation flow
→ incident creation
```

Low severity:

```text id="k7m3pl"
→ automated response
```

---

# Project Structure

```text id="rw7mqa"
app/
├── ai/
├── db/
├── models/
├── queues/
├── schemas/
├── services/
├── tools/
└── main.py

worker.py
```

---

# Key Learning Outcomes

This phase helps understand:

* event-driven architecture
* queue-first systems
* async workers
* AI orchestration basics
* workflow routing
* distributed backend patterns
* LangGraph fundamentals

---

# Next Phases

## Phase 2

Multi-Agent Architecture

## Phase 3

Human Approval Workflows

## Phase 4

Memory & Document Retrieval

## Phase 5

Workflow Builder

## Phase 6

External Integrations
