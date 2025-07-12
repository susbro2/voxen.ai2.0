"""
AI Model wrapper using Hugging Face Transformers with modern language models
"""

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from typing import Dict, Any, Optional, List
import logging
from config.settings import MODEL_CONFIG

logger = logging.getLogger(__name__)

class VoxenModel:
    """
    AI model wrapper using Hugging Face Transformers with modern language models
    """
    
    def __init__(self, model_name: str = "gpt2"):
        """
        Initialize the model with Transformers
        
        Args:
            model_name: Name of the pre-trained model to use
        """
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self.is_loaded = False
        self.conversation_history = []
        
        logger.info(f"Initializing VoxenModel with {model_name}")
    
    def load_model(self):
        """Load the pre-trained model using Transformers"""
        try:
            logger.info(f"Loading model: {self.model_name}")
            
            # Load tokenizer and model
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name, 
                torch_dtype=torch.float32,  # Use float32 for better compatibility
                low_cpu_mem_usage=True
            )
            
            # Set pad token if not present
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            
            # Move model to GPU if available (optional for small model)
            if torch.cuda.is_available():
                self.model = self.model.to('cuda')
                logger.info("Model moved to GPU")
            else:
                logger.info("Using CPU for model inference")
            
            self.is_loaded = True
            logger.info("Model loaded successfully")
            
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            raise
    
    def create_prompt(self, user_input: str) -> str:
        """Create a well-formatted prompt for the model"""
        # Add system message for better responses
        system_prompt = "You are Voxen2.0, a helpful and intelligent AI assistant. Provide clear, informative, and helpful responses."
        
        # Format conversation history
        if self.conversation_history:
            conversation_text = "\n".join([
                f"User: {msg}" if i % 2 == 0 else f"Assistant: {msg}"
                for i, msg in enumerate(self.conversation_history)
            ])
            full_prompt = f"{system_prompt}\n\n{conversation_text}\nUser: {user_input}\nAssistant:"
        else:
            full_prompt = f"{system_prompt}\n\nUser: {user_input}\nAssistant:"
        
        return full_prompt
    
    def generate_response(self, prompt: str, max_length: int = None) -> str:
        """
        Generate AI response using the language model
        
        Args:
            prompt: User's question
            max_length: Maximum length of response
            
        Returns:
            Generated response
        """
        if not self.is_loaded:
            self.load_model()
        
        try:
            # Add user input to conversation history
            self.conversation_history.append(prompt)
            
            # Create formatted prompt
            formatted_prompt = self.create_prompt(prompt)
            
            # Encode the prompt
            input_ids = self.tokenizer.encode(
                formatted_prompt, 
                return_tensors='pt',
                truncation=True,
                max_length=2048  # Limit input length
            )
            
            # Move to GPU if available
            if torch.cuda.is_available():
                input_ids = input_ids.to('cuda')
            
            # Generate response
            with torch.no_grad():
                output = self.model.generate(
                    input_ids,
                    max_length=max_length or MODEL_CONFIG["max_length"],
                    temperature=MODEL_CONFIG["temperature"],
                    do_sample=MODEL_CONFIG["do_sample"],
                    pad_token_id=self.tokenizer.eos_token_id,
                    eos_token_id=self.tokenizer.eos_token_id,
                    num_return_sequences=1,
                    repetition_penalty=1.1,
                    top_p=0.9
                )
            
            # Decode the response
            response_ids = output[0][input_ids.shape[-1]:]
            response_text = self.tokenizer.decode(
                response_ids, 
                skip_special_tokens=True
            ).strip()
            
            # Clean up response
            response_text = response_text.split('\n')[0].strip()  # Take first line
            
            # Add response to conversation history
            self.conversation_history.append(response_text)
            
            # Limit conversation history to prevent memory issues
            if len(self.conversation_history) > 6:  # Keep 3 exchanges
                self.conversation_history = self.conversation_history[-6:]
            
            return response_text if response_text else "I understand. Please continue."
            
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return f"I apologize, but I encountered an error while processing your question. Please try rephrasing it."
    
    def process_query(self, query: str) -> Dict[str, Any]:
        """
        Process a query using the AI model
        
        Args:
            query: User's question
            
        Returns:
            Dictionary containing the response
        """
        try:
            response = self.generate_response(query)
            return {
                "query": query,
                "response": response,
                "type": "ai_response"
            }
        except Exception as e:
            logger.error(f"Error processing query: {e}")
            return {
                "error": f"Could not process query: {str(e)}",
                "type": "error"
            }
    
    def clear_conversation(self):
        """Clear conversation history"""
        self.conversation_history = []
        logger.info("Conversation history cleared")
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get information about the loaded model"""
        return {
            "model_name": self.model_name,
            "is_loaded": self.is_loaded,
            "model_type": "Language Model",
            "conversation_length": len(self.conversation_history),
            "device": "cuda" if torch.cuda.is_available() else "cpu"
        } 