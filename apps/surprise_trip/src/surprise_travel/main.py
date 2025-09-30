#!/usr/bin/env python
from crew import SurpriseTravelCrew
import streamlit as st
import os
from dotenv import load_dotenv
import datetime
import json
import yaml

# Page configuration
st.set_page_config(
    page_title="Trip Surprise", 
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="✈️"
)

# Title and subtitle with custom HTML for blue color
st.markdown("<h1 style='color: #0066cc;'>✈️ Trip Surprise</h1>", unsafe_allow_html=True)

# Sidebar for API key input
with st.sidebar:
    st.markdown("### 🔧 Configuration")
    st.markdown("Enter your API keys to start planning your trip:")
    
    serper_api_key = st.text_input(
        "SERPER API Key", 
        type="password", 
        value=os.environ.get("SERPER_API_KEY"),
        help="Get your free API key from serper.dev"
    )
    openai_api_key = st.text_input(
        "OpenAI API Key", 
        type="password", 
        value=os.environ.get("OPENAI_API_KEY"),
        help="Get your API key from platform.openai.com"
    )
    
    # Store API key and Project ID as environment variables
    if serper_api_key:
        os.environ["SERPER_API_KEY"] = serper_api_key
        st.success("✅ SERPER API Key stored!")
    
    if openai_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key
        st.success("✅ OpenAI API Key stored!")
    
    # Add some helpful information
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.markdown("- Use specific cities for better results")
    st.markdown("- Add special requests for personalized recommendations")
    st.markdown("- Trip duration affects activity suggestions")

# Load environment variables
load_dotenv()  # take environment variables from .env.

# Load country and state data from YAML configuration
def load_countries_config():
    """Load countries and states data from YAML configuration file."""
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'countries.yaml')
    with open(config_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

# Load configuration data
config = load_countries_config()
COUNTRIES = config['countries']
STATES_DATA = config['states']
DEFAULTS = config['defaults']

# Extract specific state lists for easier access
US_STATES = STATES_DATA['USA']
CANADA_PROVINCES = STATES_DATA['CANADA']
BRAZIL_STATES = STATES_DATA['BRAZIL']

# Main content
st.markdown("---")

# Flight search form
st.markdown("### ✈️ Plan Your Surprise Trip")
st.markdown("Fill in the details below to get personalized trip recommendations!")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("#### 🏠 Origin Details")
    
    # Origin Country with select box
    origin_country = st.selectbox(
        "Origin Country", 
        COUNTRIES, 
        index=COUNTRIES.index(DEFAULTS['origin_country']) if DEFAULTS['origin_country'] in COUNTRIES else 0,
        help="Select your departure country"
    )
    
    # Origin State/Province - conditional based on country
    if origin_country.upper() in STATES_DATA:
        states_list = STATES_DATA[origin_country.upper()]
        default_state = DEFAULTS['origin_state'].get(origin_country, states_list[0])
        state_label = "Origin Province" if origin_country.upper() == "CANADA" else "Origin State"
        origin_state = st.selectbox(
            state_label,
            states_list,
            index=states_list.index(default_state) if default_state in states_list else 0,
            help=f"Select your departure {state_label.lower()}"
        )
    else:
        origin_state = st.text_input("Origin State/Province", "State/Province")
    
    origin_city = st.text_input(
        "Origin City", 
        "São Paulo",
        help="Enter your departure city"
    )
    
    departure_date = st.date_input(
        "Departure Date", 
        datetime.date.today() + datetime.timedelta(days=30),
        help="Select your departure date"
    )
    
    age = st.number_input(
        "Traveler Age", 
        min_value=18, 
        max_value=80, 
        value=30,
        help="Enter the age of the traveler"
    )
    
    hotel_location = st.text_input(
        "Preferred Hotel Location", 
        "Brooklyn",
        help="Specify your preferred hotel area or neighborhood"
    )
    
    trip_goals_and_plans = st.text_area(
        "Trip Goals, Companions, and Plans",
        "",
        height=120,
        help=(
            "Describe your main goals for this trip (e.g., relaxation, adventure, sightseeing, business, etc.). "
            "Mention if you are traveling with someone (family, friends, partner, etc.). "
            "List any plans, commitments, or must-do activities that should be considered in your itinerary. "
            "Share anything else important for planning your surprise trip!"
        )
    )

with col2:
    st.markdown("#### 🎯 Destination & Trip Info")
    
    # Destination Country with select box
    destination_country = st.selectbox(
        "Destination Country", 
        COUNTRIES, 
        index=COUNTRIES.index(DEFAULTS['destination_country']) if DEFAULTS['destination_country'] in COUNTRIES else 0,
        help="Select your destination country"
    )
    
    # Destination State/Province - conditional based on country
    if destination_country.upper() in STATES_DATA:
        states_list = STATES_DATA[destination_country.upper()]
        default_state = DEFAULTS['destination_state'].get(destination_country, states_list[0])
        state_label = "Destination Province" if destination_country == "Canada" else "Destination State"
        destination_state = st.selectbox(
            state_label,
            states_list,
            index=states_list.index(default_state) if default_state in states_list else 0,
            help=f"Select your destination {state_label.lower()}"
        )
    else:
        destination_state = st.text_input("Destination State/Province", "State/Province")
    
    destination_city = st.text_input(
        "Destination City", 
        "New York",
        help="Enter your destination city"
    )
    
    flight_information = st.text_input(
        "Flight Information", 
        "GOL 1234, leaving at June 30th, 2024, 10:00",
        help="Enter flight details (airline, number, departure time)"
    )
    
    trip_duration_options = ["3 days", "5 days", "7 days", "10 days", "14 days", "21 days", "30 days", "Custom..."]
    trip_duration = st.selectbox(
        "Trip Duration", 
        trip_duration_options,
        index=4,  # Default to 14 days
        help="Select your preferred trip duration"
    )
    if trip_duration == "Custom...":
        custom_duration = st.text_input(
            "Enter custom trip duration (e.g. 17 days, 2 weeks, etc.)",
            "",
            help="Specify your preferred trip duration"
        )
        if custom_duration.strip():
            trip_duration = custom_duration.strip()
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    search_button = st.button(
        "🔍 Search for My Surprise Trip!", 
        type="primary", 
        use_container_width=True,
        help="Click to generate your personalized trip itinerary"
    )

# Search functionality
if search_button:
    # Form validation
    if not origin_city.strip():
        st.error("Please enter your origin city!")
    elif not destination_city.strip():
        st.error("Please enter your destination city!")
    elif not os.environ.get("SERPER_API_KEY") or not os.environ.get("OPENAI_API_KEY"):
        st.error("Please enter your SERPER API Key and OPENAI API Key in the sidebar first!")
    else:
        with st.spinner("🔍 Searching for your perfect trip... This may take a few minutes."):
            # Create origin and destination strings
            origin = f"{origin_city}, {origin_state}, {origin_country}"
            destination = f"{destination_city}, {destination_state}, {destination_country}"
            
            # Format the request
            request = f"flights from {origin} to {destination} on {departure_date.strftime('%B %d')}"
            
            # Execute the search
            try:
                # Replace with your inputs, it will automatically interpolate any tasks and agents information
                inputs = {
                    'origin': origin,
                    'destination': destination,
                    'age': age,
                    'hotel_location': hotel_location,
                    'flight_information': flight_information,
                    'trip_duration': trip_duration,
                    'trip_goals_and_plans': trip_goals_and_plans
                }
                result = SurpriseTravelCrew().crew().kickoff(inputs=inputs)
                
                result = json.loads(result.json)

                # Display results with better formatting
                st.success("🎉 Your trip itinerary is ready!")
                st.markdown("---")
                
                # Display trip name/title
                trip_name = result.get('name', result.get('title', 'Your Surprise Trip'))
                st.markdown(f"### ✈️ {trip_name}")
                
                # Display hotel information
                hotel = result.get('hotel', result.get('hotel_info', 'N/A'))
                if hotel and hotel != 'N/A':
                    st.markdown(f"🏨 **Hotel:** {hotel}")
                
                st.markdown("---")

                # Display day plans
                day_plans = result.get('day_plans', result.get('itinerary', []))
                if day_plans:
                    for i, day in enumerate(day_plans, 1):
                        st.markdown(f"#### 📅 Day {i}: {day.get('date', f'Day {i}')}")
                        
                        # Activities
                        activities = day.get('activities', [])
                        if activities:
                            for activity in activities:
                                st.markdown(f"🎉 **Activity:** {activity.get('name', 'Activity')}")
                                st.markdown(f"- 📍 **Location:** {activity.get('location', 'N/A')}")
                                st.markdown(f"- 📝 **Description:** {activity.get('description', 'N/A')}")
                                st.markdown(f"- 🍽️ **Cuisine:** {activity.get('cousine', activity.get('cuisine', 'N/A'))}")
                                st.markdown(f"- 🤩 **Why it's suitable:** {activity.get('why_its_suitable', 'N/A')}")
                                st.markdown(f"- ⭐ **Rating:** {activity.get('rating', 'N/A')}")
                                
                                reviews = activity.get('reviews', [])
                                if reviews:
                                    st.markdown("- 💬 **Reviews:**")
                                    for review in reviews:
                                        st.markdown(f"    - {review}")
                        
                        # Restaurants
                        restaurants = day.get('restaurants', [])
                        if restaurants:
                            st.markdown("🍴 **Restaurants:**")
                            for r in restaurants:
                                st.markdown(f"- {r}")
                        
                        # Flight
                        if day.get('flight'):
                            st.markdown(f"🛫 **Flight:** {day['flight']}")
                        
                        st.markdown("---")
                else:
                    # If no structured day plans, display the raw content
                    content = result.get('content', str(result))
                    st.markdown("### 📋 Trip Details")
                    st.markdown(content)
                    
            except Exception as e:
                st.error(f"❌ An error occurred during the search: {str(e)}")
                st.error("Please check your API keys and try again.")

