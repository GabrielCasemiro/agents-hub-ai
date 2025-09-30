# Agents Hub IA 

Agents Hub IA is a repository of modular intelligent agents built with modern frameworks (like CrewAI).
The goal is to provide a hub of specialized agents that can automate repetitive and time-consuming tasks, making them available both for local use and future integration into a SaaS platform.

- 🧩 Modular architecture – each agent lives in its own folder, isolated but reusable.
- 🛠 Shared tools – utilities (e.g., stock price fetcher, news scraper, flight search) are centralized so any agent can access them.
- 🌍 Scalable – easily add new agents for new domains.
- 💡 Practical use cases – from financial analysis to news aggregation and travel planning.

## 🚀 Available Agents

### ✈️ Surprise Trip Planner (`apps/surprise_trip/`)
An intelligent travel planning agent that creates personalized surprise trip itineraries using CrewAI. Features three specialized AI agents working together to research activities, find restaurants, and compile comprehensive day-by-day travel plans.

**Key Features:**
- Personalized activity recommendations based on traveler preferences
- Restaurant and dining experience curation
- Interactive Streamlit web interface
- Support for 42+ countries worldwide
- Flexible trip durations (3 days to custom)

**Technologies:** CrewAI, Streamlit, SerperDev API, OpenAI API

[📖 View Full Documentation](./apps/surprise_trip/README.md)

---

*More agents coming soon: Financial Analyst Agent, News Fetcher, Flight Finder, and more!*
