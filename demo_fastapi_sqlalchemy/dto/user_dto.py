#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 2023

@author: javalce
"""

from typing import List

from pydantic import BaseModel

from .address_dto import AddressDTO


class UserDTO(BaseModel):
    id: int
    name: str
    fullname: str
    addresses: List[AddressDTO]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
