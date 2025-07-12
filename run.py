#!/usr/bin/env python3
"""
Simple script to run the AI Math Chat System
"""

import subprocess
import sys
import os

def main():
    """Run the Streamlit application"""
    try:
        print("🚀 Starting AI Math Chat System...")
        print("📦 Installing dependencies...")
        
        # Install requirements if needed
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True)
        
        print("🤖 Starting the application...")
        print("🌐 The app will open in your browser at http://localhost:8501")
        print("⏹️  Press Ctrl+C to stop the application")
        
        # Run Streamlit app
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py", "--server.port", "8501"])
        
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 