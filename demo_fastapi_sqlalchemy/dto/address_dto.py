#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 2023

@author: javalce
"""

from typing import List

from pydantic import BaseModel, Field


class AddressDTO(BaseModel):
    id: int
    email_address: str = Field(alias="email")
    user_id: int = Field(alias="userId")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
