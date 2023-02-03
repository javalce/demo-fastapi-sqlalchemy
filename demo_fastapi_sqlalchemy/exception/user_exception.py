#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 2023

@author: javalce
"""

from .exception import NotFoundException


class UserNotFound(NotFoundException):
    def __init__(self, id: int):
        super().__init__(f"User with id '{id}' not found")
