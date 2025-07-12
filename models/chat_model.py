"""
Chat model for handling conversation flow and message processing
"""

import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
from config.settings import CHAT_CONFIG, SAMPLE_QUESTIONS

logger = logging.getLogger(__name__)

class ChatModel:
    """
    Handles chat conversation flow and message processing
    """
    
    def __init__(self):
        """Initialize the chat model"""
        self.conversation_history = []
        self.max_history = CHAT_CONFIG["max_history"]
        self.system_prompt = CHAT_CONFIG["system_prompt"]
        self.welcome_message = CHAT_CONFIG["welcome_message"]
        
        logger.info("ChatModel initialized")
    
    def add_message(self, role: str, content: str, metadata: Dict[str, Any] = None):
        """
        Add a message to the conversation history
        
        Args:
            role: 'user' or 'assistant'
            content: Message content
            metadata: Additional metadata about the message
        """
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        
        self.conversation_history.append(message)
        
        # Keep only the last max_history messages
        if len(self.conversation_history) > self.max_history:
            self.conversation_history = self.conversation_history[-self.max_history:]
        
        logger.debug(f"Added {role} message: {content[:50]}...")
    
    def get_conversation_context(self, max_messages: int = 10) -> str:
        """
        Get conversation context for AI model
        
        Args:
            max_messages: Maximum number of recent messages to include
            
        Returns:
            Formatted conversation context
        """
        recent_messages = self.conversation_history[-max_messages:] if self.conversation_history else []
        
        context = f"{self.system_prompt}\n\n"
        
        for message in recent_messages:
            role = "User" if message["role"] == "user" else "Assistant"
            context += f"{role}: {message['content']}\n"
        
        return context.strip()
    
    def process_user_input(self, user_input: str) -> Dict[str, Any]:
        """
        Process user input and prepare for AI response
        
        Args:
            user_input: User's message
            
        Returns:
            Dictionary containing processed input and metadata
        """
        # Add user message to history
        self.add_message("user", user_input)
        
        return {
            "input": user_input,
            "context": self.get_conversation_context(),
            "timestamp": datetime.now().isoformat()
        }
    
    def add_ai_response(self, response: str):
        """
        Add AI response to conversation history
        
        Args:
            response: AI response
        """
        metadata = {
            "response_type": "ai_generated"
        }
        
        self.add_message("assistant", response, metadata)
    
    def get_conversation_summary(self) -> Dict[str, Any]:
        """
        Get summary of the current conversation
        
        Returns:
            Dictionary containing conversation summary
        """
        if not self.conversation_history:
            return {
                "total_messages": 0,
                "user_messages": 0,
                "assistant_messages": 0,
                "duration": "0 minutes"
            }
        
        user_messages = sum(1 for msg in self.conversation_history if msg["role"] == "user")
        assistant_messages = sum(1 for msg in self.conversation_history if msg["role"] == "assistant")
        
        # Calculate duration
        if len(self.conversation_history) >= 2:
            start_time = datetime.fromisoformat(self.conversation_history[0]["timestamp"])
            end_time = datetime.fromisoformat(self.conversation_history[-1]["timestamp"])
            duration = end_time - start_time
            duration_str = f"{duration.seconds // 60} minutes"
        else:
            duration_str = "0 minutes"
        
        return {
            "total_messages": len(self.conversation_history),
            "user_messages": user_messages,
            "assistant_messages": assistant_messages,
            "duration": duration_str
        }
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        logger.info("Conversation history cleared")
    
    def export_conversation(self, format: str = "json") -> str:
        """
        Export conversation history
        
        Args:
            format: Export format ('json' or 'txt')
            
        Returns:
            Exported conversation as string
        """
        if format == "json":
            return json.dumps(self.conversation_history, indent=2)
        
        elif format == "txt":
            export_text = "AI Chat Conversation\n"
            export_text += "=" * 30 + "\n\n"
            
            for message in self.conversation_history:
                role = "User" if message["role"] == "user" else "Assistant"
                timestamp = message["timestamp"]
                content = message["content"]
                
                export_text += f"[{timestamp}] {role}:\n{content}\n\n"
            
            return export_text
        
        else:
            raise ValueError(f"Unsupported export format: {format}")
    
    def get_sample_questions(self, category: str = None) -> List[str]:
        """
        Get sample questions for quick access
        
        Args:
            category: Optional category filter
            
        Returns:
            List of sample questions
        """
        if category:
            # Filter questions by category (simplified implementation)
            return [q for q in SAMPLE_QUESTIONS if category.lower() in q.lower()]
        
        return SAMPLE_QUESTIONS
    
    def get_recent_messages(self, count: int = 5) -> List[Dict[str, Any]]:
        """
        Get recent messages from conversation history
        
        Args:
            count: Number of recent messages to return
            
        Returns:
            List of recent messages
        """
        return self.conversation_history[-count:] if self.conversation_history else []
    
    def search_messages(self, query: str) -> List[Dict[str, Any]]:
        """
        Search messages in conversation history
        
        Args:
            query: Search query
            
        Returns:
            List of matching messages
        """
        query_lower = query.lower()
        matching_messages = []
        
        for message in self.conversation_history:
            if query_lower in message["content"].lower():
                matching_messages.append(message)
        
        return matching_messages 