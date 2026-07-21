# Notification Broadcasting Service

## Brief Description

This project is a backend service for broadcasting notifications (email and push) via asynchronous task queues.  
It provides a REST API built with **FastAPI** for creating broadcast campaigns, tracking their status, and viewing delivery details.

Task processing is handled by **Celery** with **RabbitMQ** as a message broker, ensuring high reliability and scalability.  
Data is stored in a relational database using **SQLAlchemy ORM**, with migrations managed by **Alembic**.  
Dependency management and virtual environment are handled by **uv**.

---

## Tech Stack

| Component                | Technology               |
|--------------------------|--------------------------|
| Web Framework            | FastAPI                  |
| Async Task Queue         | Celery                   |
| Message Broker           | RabbitMQ                 |
| ORM                      | SQLAlchemy               |
| Database Migrations      | Alembic                  |
| Dependency & Env Manager | uv                       |
| Database                 | PostgreSQL (expected)    |
| Language                 | Python 3.14+             |

---

> *This document will be expanded as development progresses.*