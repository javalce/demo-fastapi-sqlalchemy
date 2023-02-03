#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 2023

@author: javalce
"""


from ..database import CRUDRepository
from ..model import Address


class AddressRepository(CRUDRepository[Address, int]):
    def __init__(self) -> None:
        super().__init__(Address)
