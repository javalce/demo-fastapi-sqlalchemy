#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 2023

@author: javalce
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


DATABASE_URL: str = f"sqlite:///{BASE_DIR}/database.db"
