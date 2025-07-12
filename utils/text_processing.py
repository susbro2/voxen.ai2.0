"""
Text processing utilities for Voxen2.0 AI responses
"""

import re
import logging
from typing import Dict, List, Any, Optional, Tuple
from config.settings import VOXEN_CONFIG

logger = logging.getLogger(__name__)

class VoxenTextProcessor:
    """Handles text processing for Voxen2.0 AI responses"""
    
    def __init__(self):
        self.max_length = VOXEN_CONFIG["max_response_length"]
        self.sensitive_words = VOXEN_CONFIG.get("sensitive_words", [])
    
    def clean_response(self, text: str) -> str:
        """Clean and format response text"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Truncate if too long
        if len(text) > self.max_length:
            text = text[:self.max_length] + "..."
        
        return text
    
    def extract_keywords(self, text: str) -> List[str]:
        """Extract keywords from text"""
        # Simple keyword extraction (can be enhanced)
        words = re.findall(r'\b\w+\b', text.lower())
        return list(set(words))
    
    def check_sensitive_content(self, text: str) -> bool:
        """Check if text contains sensitive content"""
        text_lower = text.lower()
        return any(word in text_lower for word in self.sensitive_words)

class TextProcessor:
    """
    Utility class for processing and analyzing text input
    """
    
    def __init__(self):
        """Initialize TextProcessor"""
        self.math_patterns = {
            'equation': r'([a-zA-Z]\s*[+\-*/]\s*[a-zA-Z0-9]+\s*=\s*[a-zA-Z0-9]+)',
            'derivative': r'(derivative|differentiate|d/d[a-zA-Z])',
            'integral': r'(integral|integrate|∫)',
            'function': r'([a-zA-Z]\s*\([^)]*\))',
            'number': r'(\d+\.?\d*)',
            'variable': r'([a-zA-Z])',
            'operator': r'([+\-*/^=<>])',
            'parentheses': r'([()])',
            'brackets': r'([\[\]])'
        }
        
        logger.info("TextProcessor initialized")
    
    def extract_math_expressions(self, text: str) -> List[str]:
        """
        Extract mathematical expressions from text
        
        Args:
            text: Input text
            
        Returns:
            List of mathematical expressions found
        """
        expressions = []
        
        # Look for patterns that might contain math
        for pattern_name, pattern in self.math_patterns.items():
            matches = re.findall(pattern, text, re.IGNORECASE)
            expressions.extend(matches)
        
        # Remove duplicates and clean up
        expressions = list(set(expressions))
        expressions = [expr.strip() for expr in expressions if expr.strip()]
        
        return expressions
    
    def classify_math_question(self, text: str) -> Dict[str, Any]:
        """
        Classify the type of mathematical question
        
        Args:
            text: User's question
            
        Returns:
            Dictionary with classification results
        """
        text_lower = text.lower()
        
        classification = {
            'is_math': False,
            'math_type': None,
            'confidence': 0.0,
            'keywords': [],
            'suggested_operations': []
        }
        
        # Math keywords by category
        math_keywords = {
            'algebra': ['equation', 'solve', 'variable', 'polynomial', 'factor', 'expand'],
            'calculus': ['derivative', 'integral', 'limit', 'differentiate', 'integrate', 'd/dx', '∫'],
            'geometry': ['area', 'volume', 'perimeter', 'circle', 'triangle', 'rectangle', 'sphere'],
            'statistics': ['mean', 'median', 'mode', 'standard deviation', 'probability', 'distribution'],
            'trigonometry': ['sin', 'cos', 'tan', 'angle', 'degree', 'radian'],
            'linear_algebra': ['matrix', 'vector', 'eigenvalue', 'determinant', 'inverse'],
            'number_theory': ['prime', 'factor', 'divisible', 'modulo', 'gcd', 'lcm']
        }
        
        # Check for math keywords
        found_keywords = []
        for category, keywords in math_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    found_keywords.append(keyword)
                    classification['is_math'] = True
                    classification['math_type'] = category
                    classification['confidence'] += 0.2
        
        classification['keywords'] = found_keywords
        
        # Additional confidence based on patterns
        if re.search(r'\d+', text):
            classification['confidence'] += 0.1
        
        if re.search(r'[+\-*/^=<>]', text):
            classification['confidence'] += 0.2
        
        if re.search(r'[a-zA-Z]\s*[+\-*/]\s*[a-zA-Z0-9]', text):
            classification['confidence'] += 0.3
        
        # Cap confidence at 1.0
        classification['confidence'] = min(classification['confidence'], 1.0)
        
        # Suggest operations based on classification
        if classification['math_type'] == 'algebra':
            classification['suggested_operations'] = ['solve_equation', 'evaluate_expression']
        elif classification['math_type'] == 'calculus':
            classification['suggested_operations'] = ['calculate_derivative', 'calculate_integral']
        elif classification['math_type'] == 'geometry':
            classification['suggested_operations'] = ['calculate_geometry']
        elif classification['math_type'] == 'statistics':
            classification['suggested_operations'] = ['calculate_statistics', 'calculate_probability']
        
        return classification
    
    def extract_equation(self, text: str) -> Optional[str]:
        """
        Extract equation from text
        
        Args:
            text: Input text
            
        Returns:
            Extracted equation string or None
        """
        # Look for patterns like "x + y = z" or "solve 2x + 5 = 13"
        patterns = [
            r'([a-zA-Z]\s*[+\-*/]\s*[a-zA-Z0-9]+\s*=\s*[a-zA-Z0-9]+)',
            r'solve\s+([^.!?]+)',
            r'([^.!?]*\s*=\s*[^.!?]*)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                # Clean up the extracted equation
                equation = matches[0].strip()
                # Remove common words that aren't part of the equation
                equation = re.sub(r'\b(solve|find|calculate|compute)\b', '', equation, flags=re.IGNORECASE)
                equation = equation.strip()
                if equation:
                    return equation
        
        return None
    
    def extract_function(self, text: str) -> Optional[str]:
        """
        Extract function expression from text
        
        Args:
            text: Input text
            
        Returns:
            Extracted function string or None
        """
        # Look for patterns like "f(x) = x^2 + 3x + 1" or "derivative of x^2"
        patterns = [
            r'([a-zA-Z]\s*\([^)]*\)\s*=\s*[^.!?]+)',
            r'(derivative|integral)\s+(?:of\s+)?([^.!?]+)',
            r'([a-zA-Z0-9^+\-*/()\s]+)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                func_expr = matches[0].strip()
                # Clean up the expression
                func_expr = re.sub(r'\b(derivative|integral|of)\b', '', func_expr, flags=re.IGNORECASE)
                func_expr = func_expr.strip()
                if func_expr and len(func_expr) > 2:
                    return func_expr
        
        return None
    
    def clean_math_expression(self, expression: str) -> str:
        """
        Clean and standardize mathematical expression
        
        Args:
            expression: Raw mathematical expression
            
        Returns:
            Cleaned expression
        """
        # Remove extra whitespace
        expression = re.sub(r'\s+', ' ', expression.strip())
        
        # Replace common mathematical notations
        replacements = {
            '×': '*',
            '÷': '/',
            '^': '**',
            '−': '-',  # Unicode minus sign
            '–': '-',  # En dash
            '—': '-',  # Em dash
            'π': 'pi',
            '∞': 'oo',
            '√': 'sqrt',
            '∫': 'integral',
            '∑': 'sum',
            '∏': 'product'
        }
        
        for old, new in replacements.items():
            expression = expression.replace(old, new)
        
        # Handle implicit multiplication (e.g., "2x" -> "2*x")
        expression = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expression)
        expression = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expression)
        expression = re.sub(r'([a-zA-Z])([a-zA-Z])', r'\1*\2', expression)
        
        # Handle parentheses multiplication
        expression = re.sub(r'(\d)\(', r'\1*(', expression)
        expression = re.sub(r'\)(\d)', r')*\1', expression)
        
        return expression
    
    def format_latex(self, expression: str) -> str:
        """
        Convert mathematical expression to LaTeX format
        
        Args:
            expression: Mathematical expression
            
        Returns:
            LaTeX formatted string
        """
        # Basic LaTeX formatting
        latex = expression
        
        # Replace operators
        latex = latex.replace('**', '^')
        latex = latex.replace('*', '\\cdot ')
        latex = latex.replace('/', '\\frac{')
        
        # Handle fractions
        if '\\frac{' in latex:
            # Simple fraction handling - in practice, you'd want more sophisticated parsing
            latex = latex.replace('\\frac{', '\\frac{}{')
        
        # Add math delimiters
        if not latex.startswith('$'):
            latex = f'${latex}$'
        
        return latex
    
    def extract_numbers(self, text: str) -> List[float]:
        """
        Extract numerical values from text
        
        Args:
            text: Input text
            
        Returns:
            List of extracted numbers
        """
        # Find all numbers (including decimals)
        number_pattern = r'-?\d+\.?\d*'
        matches = re.findall(number_pattern, text)
        
        numbers = []
        for match in matches:
            try:
                numbers.append(float(match))
            except ValueError:
                continue
        
        return numbers
    
    def extract_variables(self, text: str) -> List[str]:
        """
        Extract variable names from text
        
        Args:
            text: Input text
            
        Returns:
            List of variable names
        """
        # Find single letter variables (excluding common words)
        variable_pattern = r'\b[a-zA-Z]\b'
        matches = re.findall(variable_pattern, text)
        
        # Filter out common words that aren't variables
        common_words = {'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        variables = [match for match in matches if match.lower() not in common_words]
        
        return list(set(variables))  # Remove duplicates
    
    def validate_math_expression(self, expression: str) -> Dict[str, Any]:
        """
        Validate mathematical expression syntax
        
        Args:
            expression: Mathematical expression
            
        Returns:
            Dictionary with validation results
        """
        validation = {
            'is_valid': True,
            'errors': [],
            'warnings': []
        }
        
        # Check for balanced parentheses
        if expression.count('(') != expression.count(')'):
            validation['is_valid'] = False
            validation['errors'].append("Unbalanced parentheses")
        
        # Check for balanced brackets
        if expression.count('[') != expression.count(']'):
            validation['is_valid'] = False
            validation['errors'].append("Unbalanced brackets")
        
        # Check for consecutive operators
        if re.search(r'[+\-*/^]{2,}', expression):
            validation['warnings'].append("Consecutive operators detected")
        
        # Check for division by zero patterns
        if re.search(r'/\s*0', expression):
            validation['warnings'].append("Potential division by zero")
        
        # Check for valid characters
        invalid_chars = re.findall(r'[^a-zA-Z0-9+\-*/^()\[\].,\s]', expression)
        if invalid_chars:
            validation['warnings'].append(f"Unusual characters detected: {set(invalid_chars)}")
        
        return validation
    
    def suggest_corrections(self, expression: str) -> List[str]:
        """
        Suggest corrections for mathematical expressions
        
        Args:
            expression: Mathematical expression
            
        Returns:
            List of suggested corrections
        """
        suggestions = []
        
        # Check for common mistakes
        if '=' in expression and not re.search(r'[<>]', expression):
            suggestions.append("Consider using '==' for equality comparison")
        
        if re.search(r'\d\s+[a-zA-Z]', expression):
            suggestions.append("Consider adding '*' for implicit multiplication")
        
        if re.search(r'[a-zA-Z]\s+\d', expression):
            suggestions.append("Consider adding '*' for implicit multiplication")
        
        if expression.count('(') != expression.count(')'):
            suggestions.append("Check for balanced parentheses")
        
        return suggestions 