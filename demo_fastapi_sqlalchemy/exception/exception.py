#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 2023

@author: javalce
"""

from typing import Optional

from fastapi import HTTPException, status


class NotFoundException(HTTPException):
    def __init__(self, detail: Optional[str] = None) -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
