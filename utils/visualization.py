"""
Visualization utilities for mathematical plotting and data visualization
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
from typing import List, Dict, Any, Optional
import json
import re

from config.settings import VOXEN_CONFIG

class VoxenVisualizer:
    """Handles visualization for Voxen2.0 AI responses"""
    
    def __init__(self):
        self.plot_theme = VOXEN_CONFIG["plot_theme"]
        self.colors = VOXEN_CONFIG["colors"]
        self.chart_height = VOXEN_CONFIG["chart_height"]
        self.chart_width = VOXEN_CONFIG["chart_width"]
    
    def create_response_chart(self, response_data: Dict[str, Any]) -> go.Figure:
        """Create a chart from response data"""
        # Placeholder for chart creation logic
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 4, 2], mode='lines+markers'))
        fig.update_layout(
            title="Voxen2.0 Response Visualization",
            xaxis_title="X Axis",
            yaxis_title="Y Axis",
            template=self.plot_theme
        )
        return fig
    
    def create_confidence_chart(self, confidence_scores: List[float]) -> go.Figure:
        """Create a confidence score visualization"""
        fig = go.Figure(data=[
            go.Bar(x=list(range(len(confidence_scores))), y=confidence_scores)
        ])
        fig.update_layout(
            title="Response Confidence Scores",
            xaxis_title="Response Index",
            yaxis_title="Confidence Score",
            template=self.plot_theme
        )
        return fig
    
    def display_chart(self, fig: go.Figure):
        """Display a chart in Streamlit"""
        st.plotly_chart(fig, use_container_width=True) 