"""
UI Components for the Voxen2.0 AI Chat System
"""

import streamlit as st
from typing import Dict, List, Any, Optional
import logging
from config.settings import VOXEN_CONFIG

logger = logging.getLogger(__name__)

class VoxenUI:
    """
    Simplified UI for Voxen2.0 AI Assistant
    """
    
    def __init__(self):
        """Initialize the UI"""
        pass

    def display_header(self):
        """Display the main header"""
        st.title("🤖 Voxen2.0 AI Assistant")
        st.markdown("""
        Welcome to Voxen2.0! Your AI assistant for conversation and information.
        """)

    def display_sidebar(self):
        """Display a simple sidebar"""
        with st.sidebar:
            st.title("🤖 Voxen2.0")
            st.markdown("---")
            
            # Model info
            st.subheader("🤖 Model Info")
            st.info("Using DialoGPT for AI responses")
            
            # Quick stats
            st.subheader("📈 Quick Stats")
            if "messages" in st.session_state:
                total_messages = len(st.session_state.messages)
                st.metric("Total Messages", total_messages)
            
            # Clear chat button
            if st.button("🗑️ Clear Chat", key="clear_chat"):
                if "messages" in st.session_state:
                    st.session_state.messages = []
                    st.rerun()
            
            st.markdown("---")
            
            # Sample questions
            st.subheader("💡 Sample Questions")
            sample_questions = VOXEN_CONFIG.get("sample_questions", [])
            for i, question in enumerate(sample_questions[:5]):  # Show first 5
                if st.button(question, key=f"sample_{i}"):
                    st.session_state.messages.append({"role": "user", "content": question})
                    st.rerun()
            
            st.markdown("---")
            st.markdown("**Made with ❤️ using Streamlit**")

    def display_chat_interface(self):
        """Display the main chat interface"""
        st.header("💬 Chat with Voxen2.0")
        
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Ask me anything...", key="main_chat_input"):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generate AI response using the actual models
            with st.chat_message("assistant"):
                with st.spinner("Voxen2.0 is thinking..."):
                    try:
                        # Use the Voxen model for responses
                        if st.session_state.voxen_model:
                            ai_response = st.session_state.voxen_model.generate_response(prompt)
                        else:
                            ai_response = "I apologize, but the AI model is not available at the moment."
                        
                        # Add AI response to chat history
                        st.session_state.messages.append({"role": "assistant", "content": ai_response})
                        
                        # Display response
                        st.markdown(ai_response)
                        
                    except Exception as e:
                        error_msg = f"I apologize, but I encountered an error: {str(e)}"
                        st.session_state.messages.append({"role": "assistant", "content": error_msg})
                        st.error(error_msg) 