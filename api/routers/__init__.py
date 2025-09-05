"""
Routers package initializer.
Groups all API endpoints for easy import in main.py.
"""

from . import upload, simplify, assistant, voice

__all__ = ["upload", "simplify", "assistant", "voice"]
