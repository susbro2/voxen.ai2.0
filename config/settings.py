"""
Configuration settings for the AI Chat System
"""

import os
from typing import Dict, Any

# Model Configuration
MODEL_CONFIG = {
    "default_model": "gpt2",  # Classic GPT-2 - good quality and reasonable size
    "voxen_model": "gpt2",
    "max_length": 1000,
    "temperature": 0.7,
    "do_sample": True,
}

# UI Configuration
UI_CONFIG = {
    "page_title": "Voxen2.0 AI Assistant",
    "page_icon": "🤖",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "theme": {
        "primaryColor": "#FF6B6B",
        "backgroundColor": "#FFFFFF",
        "secondaryBackgroundColor": "#F0F2F6",
        "textColor": "#262730",
        "font": "sans serif"
    },
    "dark_theme": {
        "primaryColor": "#FF6B6B",
        "backgroundColor": "#0E1117",
        "secondaryBackgroundColor": "#262730",
        "textColor": "#FAFAFA",
        "font": "sans serif"
    }
}

# Chat Configuration
CHAT_CONFIG = {
    "max_history": 50,
    "welcome_message": "Hello! I'm Voxen2.0, your AI assistant powered by DialoGPT. I can help you with:\n• Answering questions\n• Having conversations\n• Providing information\n• And much more!\n\nJust ask me anything!",
    "system_prompt": "You are Voxen2.0, a helpful AI assistant powered by DialoGPT. Provide clear, informative, and helpful responses to user questions. Be friendly and engaging in your conversations.",
}

# File Paths
PATHS = {
    "data_dir": "data",
    "models_dir": "models",
    "logs_dir": "logs",
    "cache_dir": ".cache",
}

# API Configuration (for future external API integration)
API_CONFIG = {
    "timeout": 30,
    "retry_attempts": 3,
    "rate_limit": 100,  # requests per minute
}

# Logging Configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "logs/app.log",
}

# Create necessary directories
def create_directories():
    """Create necessary directories if they don't exist"""
    for path in PATHS.values():
        os.makedirs(path, exist_ok=True)

# Initialize directories
create_directories()

# Environment variables
ENV_VARS = {
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", ""),
    "HUGGINGFACE_TOKEN": os.getenv("HUGGINGFACE_TOKEN", ""),
    "DEBUG": os.getenv("DEBUG", "False").lower() == "true",
}

# Feature flags
FEATURES = {
    "enable_voice": True,
    "enable_file_upload": True,
    "enable_export": True,
    "enable_history": True,
    "enable_themes": True,
}

# Sample questions for quick access
SAMPLE_QUESTIONS = [
    "What is artificial intelligence?",
    "Tell me a joke",
    "How does machine learning work?",
    "What's the weather like?",
    "Explain quantum computing",
    "What are the benefits of renewable energy?",
    "How do neural networks function?",
    "What is the future of technology?",
]

# Additional configuration for utilities
UTILITY_CONFIG = {
    "decimal_precision": 4,
    "max_iterations": 1000,
    "tolerance": 1e-6,
    "max_response_length": 2000,
}

# Visualization configuration
VISUALIZATION_CONFIG = {
    "plot_theme": "plotly_white",
    "colors": ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"],
    "chart_height": 400,
    "chart_width": 600,
}

VOXEN_CONFIG = {
    "model": MODEL_CONFIG,
    "ui": UI_CONFIG,
    "chat": CHAT_CONFIG,
    "paths": PATHS,
    "api": API_CONFIG,
    "logging": LOGGING_CONFIG,
    "env": ENV_VARS,
    "features": FEATURES,
    "sample_questions": SAMPLE_QUESTIONS,
    "utility": UTILITY_CONFIG,
    "visualization": VISUALIZATION_CONFIG,
    # Direct access keys for backward compatibility
    "decimal_precision": UTILITY_CONFIG["decimal_precision"],
    "max_iterations": UTILITY_CONFIG["max_iterations"],
    "tolerance": UTILITY_CONFIG["tolerance"],
    "max_response_length": UTILITY_CONFIG["max_response_length"],
    "plot_theme": VISUALIZATION_CONFIG["plot_theme"],
    "colors": VISUALIZATION_CONFIG["colors"],
    "chart_height": VISUALIZATION_CONFIG["chart_height"],
    "chart_width": VISUALIZATION_CONFIG["chart_width"],
} 