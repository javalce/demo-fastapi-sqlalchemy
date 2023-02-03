#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 2023

@author: javalce
"""

from .exception import NotFoundException


class AddressNotFound(NotFoundException):
    def __init__(self, id: int) -> None:
        super().__init__(f"Address with id '{id}' not found")
