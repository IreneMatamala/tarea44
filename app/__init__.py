# app/__init__.py


__version__ = "1.0.0"
__author__ = "Irene"

# Importaciones que quieres disponibles a nivel del paquete
from .main import app

# Define qué se exporta con 'from app import *'
__all__ = ['app']
