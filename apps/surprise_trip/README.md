# ✈️ Surprise Trip Planner

An intelligent travel planning agent that creates personalized surprise trip itineraries using CrewAI. This agent helps travelers discover amazing activities, restaurants, and experiences tailored to their preferences, age, and travel goals.

## 🎯 Features

- **Personalized Activity Planning**: AI-powered recommendations based on traveler demographics and preferences
- **Restaurant & Dining Scout**: Curated dining experiences and culinary recommendations
- **Comprehensive Itinerary Compilation**: Day-by-day travel plans with integrated flight and hotel information
- **Interactive Web Interface**: Beautiful Streamlit-based UI for easy trip planning
- **Multi-Country Support**: Extensive database of countries, states, and provinces
- **Flexible Trip Duration**: Support for trips from 3 days to custom durations
- **Real-time Research**: Uses web search and scraping tools for up-to-date information

## 🤖 AI Agents

The Surprise Trip Planner uses three specialized CrewAI agents:

### 1. Personalized Activity Planner
- **Role**: Activity Planner
- **Goal**: Research and find cool activities and events that match the traveler's interests and age group
- **Tools**: SerperDevTool, ScrapeWebsiteTool

### 2. Restaurant Scout
- **Role**: Restaurant Scout  
- **Goal**: Find highly-rated restaurants and dining experiences, plus scenic locations
- **Tools**: SerperDevTool, ScrapeWebsiteTool

### 3. Itinerary Compiler
- **Role**: Itinerary Compiler
- **Goal**: Compile all researched information into a comprehensive day-by-day itinerary
- **Tools**: SerperDevTool

## 🚀 Quick Start

### Prerequisites

- Python 3.10-3.13
- SERPER API Key (get free key from [serper.dev](https://serper.dev))
- OpenAI API Key (get from [platform.openai.com](https://platform.openai.com))

### Installation

1. Navigate to the surprise_trip directory:
```bash
cd apps/surprise_trip
```

2. Install dependencies:
```bash
pip install -r src/requirements.txt
```

### Running the Application

1. Set up your environment variables:
```bash
export SERPER_API_KEY="your_serper_api_key"
export OPENAI_API_KEY="your_openai_api_key"
```

2. Run the Streamlit application:
```bash
streamlit run src/surprise_travel/main.py
```

3. Open your browser to `http://localhost:8501`

## 💡 Usage

1. **Configure API Keys**: Enter your SERPER and OpenAI API keys in the sidebar
2. **Fill Trip Details**: 
   - Origin and destination information (country, state/province, city)
   - Travel dates and duration
   - Traveler age and preferences
   - Hotel location preferences
   - Flight information
   - Trip goals and special requests
3. **Generate Itinerary**: Click "Search for My Surprise Trip!" to create your personalized travel plan
4. **Review Results**: Get a comprehensive day-by-day itinerary with activities, restaurants, and recommendations

## 🏗️ Project Structure

```
surprise_trip/
├── src/
│   ├── surprise_travel/
│   │   ├── config/
│   │   │   ├── agents.yaml      # Agent configurations
│   │   │   ├── tasks.yaml       # Task definitions
│   │   │   └── countries.yaml   # Country/state data
│   │   ├── tools/
│   │   │   └── custom_tool.py   # Custom tools (optional)
│   │   ├── crew.py             # CrewAI crew definition
│   │   └── main.py             # Streamlit application
│   └── requirements.txt        # Python dependencies
├── pyproject.toml             # Project configuration
└── README.md                  # This file
```

## 🔧 Configuration

### Agent Configuration (`config/agents.yaml`)
Defines the roles, goals, and backstories for each AI agent.

### Task Configuration (`config/tasks.yaml`)
Specifies the tasks each agent performs and their expected outputs.

### Countries Configuration (`config/countries.yaml`)
Contains comprehensive lists of supported countries, states, and provinces with default selections.

## 🌍 Supported Destinations

The application supports planning for 42+ countries including:
- **Americas**: USA, Canada, Mexico, Brazil, Argentina, Chile, Colombia, Peru
- **Europe**: UK, France, Germany, Italy, Spain, Netherlands, Switzerland, Austria, and more
- **Asia**: Japan, South Korea, China, India, Thailand, Singapore, Malaysia, Indonesia
- **Oceania**: Australia, New Zealand
- **Africa**: South Africa, Egypt, Morocco

## 🛠️ Dependencies

- **crewai[tools]**: Core CrewAI framework with tools
- **crewai-tools**: Additional tools for web search and scraping
- **streamlit**: Web application framework
- **python-dotenv**: Environment variable management
- **PyYAML**: YAML configuration file parsing

## 🔑 API Keys Required

1. **SERPER API Key**: For web search functionality
   - Sign up at [serper.dev](https://serper.dev)
   - Free tier includes 2,500 searches per month

2. **OpenAI API Key**: For AI agent processing
   - Get from [platform.openai.com](https://platform.openai.com)
   - Usage varies based on itinerary complexity

## 📊 Example Output

The application generates structured itineraries including:
- Trip name and overview
- Hotel recommendations
- Day-by-day activity plans with:
  - Activity names and locations
  - Detailed descriptions
  - Cuisine recommendations
  - Suitability explanations
  - Ratings and reviews
- Restaurant recommendations
- Flight integration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is part of the Agents Hub IA repository. See the main README for licensing information.

## 🆘 Troubleshooting

**Common Issues:**

1. **API Key Errors**: Ensure both SERPER and OpenAI API keys are valid and have sufficient credits
2. **Slow Performance**: Complex itineraries may take 2-5 minutes to generate
3. **Empty Results**: Check that destination cities are spelled correctly and are supported
4. **Import Errors**: Ensure all dependencies are installed via requirements.txt

**Getting Help:**
- Check the main Agents Hub IA README for general troubleshooting
- Review the CrewAI documentation for agent-related issues
- Ensure Python version compatibility (3.10-3.13)

---

*Built with ❤️ using CrewAI and Streamlit*
