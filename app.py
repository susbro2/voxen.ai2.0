"""
Voxen2.0 AI Assistant - Main Application
A conversational AI assistant with mathematical capabilities
"""

import streamlit as st
import logging
import sys
import os
from datetime import datetime
from typing import Dict, List, Any

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config.settings import VOXEN_CONFIG
from models.voxen_model import VoxenModel
from models.chat_model import ChatModel
from utils.math_utils import VoxenMathProcessor
from utils.visualization import VoxenVisualizer
from utils.text_processing import VoxenTextProcessor, TextProcessor
from ui.components import VoxenUI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_session_state():
    """Initialize Streamlit session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    if 'voxen_model' not in st.session_state:
        st.session_state.voxen_model = None
    
    if 'chat_model' not in st.session_state:
        st.session_state.chat_model = None
    
    if 'math_utils' not in st.session_state:
        st.session_state.math_utils = None
    
    if 'visualizer' not in st.session_state:
        st.session_state.visualizer = None
    
    if 'text_processor' not in st.session_state:
        st.session_state.text_processor = None
    
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []
    
    if 'current_topic' not in st.session_state:
        st.session_state.current_topic = "general"

def load_models():
    """Load and initialize AI models"""
    try:
        with st.spinner("Loading Voxen2.0 AI models..."):
            # Initialize Voxen model
            if st.session_state.voxen_model is None:
                st.session_state.voxen_model = VoxenModel()
            
            # Initialize chat model
            if st.session_state.chat_model is None:
                st.session_state.chat_model = ChatModel()
            
            # Initialize utilities
            if st.session_state.math_utils is None:
                st.session_state.math_utils = VoxenMathProcessor()
            
            if st.session_state.visualizer is None:
                st.session_state.visualizer = VoxenVisualizer()
            
            if st.session_state.text_processor is None:
                st.session_state.text_processor = VoxenTextProcessor()
        
        st.success("Models loaded successfully!")
        return True
        
    except Exception as e:
        st.error(f"Error loading models: {str(e)}")
        logger.error(f"Model loading error: {e}")
        return False

def process_user_input(user_input: str) -> Dict[str, Any]:
    """Process user input and generate response"""
    try:
        # Initialize text processor for input analysis
        text_processor = TextProcessor()
        
        # Analyze input type
        classification = text_processor.classify_math_question(user_input)
        
        response_data = {
            "user_input": user_input,
            "classification": classification,
            "response": "",
            "confidence": 0.0,
            "visualization": None,
            "timestamp": datetime.now().isoformat()
        }
        
        # Generate response based on classification
        if classification['is_math'] and classification['confidence'] > 0.5:
            # Use Voxen model for mathematical queries
            response = st.session_state.voxen_model.generate_response(user_input)
            response_data["response"] = response
            response_data["confidence"] = classification['confidence']
            
        else:
            # Use chat model for general conversation
            response = st.session_state.chat_model.generate_response(user_input)
            response_data["response"] = response
            response_data["confidence"] = 0.8
        
        return response_data
        
    except Exception as e:
        logger.error(f"Error processing user input: {e}")
        return {
            "user_input": user_input,
            "response": f"I apologize, but I encountered an error: {str(e)}",
            "confidence": 0.0,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

def main():
    """Main application function"""
    st.set_page_config(
        page_title="Voxen2.0 AI Assistant",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # Initialize UI
    ui = VoxenUI()
    
    # Display header
    ui.display_header()
    
    # Load models
    if not load_models():
        st.stop()
    
    # Display sidebar
    ui.display_sidebar()
    
    # Main chat interface
    ui.display_chat_interface()
    
    # Note: Chat input is handled within ui.display_chat_interface()

if __name__ == "__main__":
    main() 