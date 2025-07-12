"""
Mathematical utilities for Voxen2.0 AI responses
"""

import numpy as np
import sympy as sp
from typing import Dict, List, Any, Optional, Union
import logging
import re

from config.settings import VOXEN_CONFIG

logger = logging.getLogger(__name__)

class VoxenMathProcessor:
    """Handles mathematical processing for Voxen2.0 AI responses"""
    
    def __init__(self):
        self.precision = VOXEN_CONFIG["decimal_precision"]
        self.max_iterations = VOXEN_CONFIG["max_iterations"]
        self.tolerance = VOXEN_CONFIG["tolerance"]
    
    def evaluate_expression(self, expression: str) -> Dict[str, Any]:
        """Evaluate a mathematical expression"""
        try:
            # Use sympy for safe evaluation
            x = sp.Symbol('x')
            result = sp.sympify(expression)
            return {
                "success": True,
                "result": str(result),
                "type": "expression"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "type": "expression"
            }
    
    def solve_equation(self, equation: str) -> Dict[str, Any]:
        """Solve a mathematical equation"""
        try:
            x = sp.Symbol('x')
            # Parse equation (assume form: expression = expression)
            if '=' in equation:
                left, right = equation.split('=', 1)
                expr = sp.sympify(left) - sp.sympify(right)
                solutions = sp.solve(expr, x)
                return {
                    "success": True,
                    "solutions": [str(sol) for sol in solutions],
                    "type": "equation"
                }
            else:
                return {
                    "success": False,
                    "error": "No equals sign found in equation",
                    "type": "equation"
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "type": "equation"
            } 