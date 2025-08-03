# 📱 SubManager – Microservices-Based Subscription Management Backend

## Overview

SubManager is a backend system developed in Python that manages mobile app subscriptions using a scalable microservices architecture, designed for deployment in the cloud. It simulates a SaaS business model used by modern app-based startups where users can install mobile apps for free but must maintain an active paid subscription to use them.

This project is fully functional and built with modern backend practices, including domain-driven design, inter-service communication via events, and an internal caching strategy for performance.

---

## System Features

The platform provides a comprehensive set of features required for managing app subscriptions:
- ✅ Manage clients: Register and view client records
- 📱 Manage apps: Register and update apps and their subscription prices
- 📄 Create subscriptions: Clients can subscribe to apps with an automatic 7-day free trial
- 🔄 Update subscription validity based on payment status
- 📬 Receive payment notifications from banks and register them
- ⚡ Quickly verify if a subscription is active, with internal caching for performance
- 📊 List all subscriptions by client or app, filterable by status (active/cancelled)

---

## Microservices Architecture

The system is composed of three decoupled services:

1. ServicoCadastramento
- Main service responsible for managing clients, apps, and subscriptions.
- Updates subscription validity upon receiving payment events.
- Exposes endpoints for listing clients, apps, and subscriptions.

3. ServicoPagamentos
- Handles all payment registrations.
- Emits asynchronous events upon new payments to update subscription status.

4. ServicoAssinaturasValidas
- High-performance service queried frequently by mobile apps.
- Uses an internal cache to quickly check if a subscription is valid.
- Listens to payment events to keep its cache in sync with the database.

---

## Tech Stack
-	Language: Python
-	Architecture: Microservices
-	Persistence: (e.g., SQLite/PostgreSQL – depending on your implementation)
-	Deployment: (e.g., Docker + Azure)

---

## License

This project was developed as part of the Software Engineering II course and is intended for academic use.
