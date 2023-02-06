#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 2023

@author: javalce
"""

from pydantic import BaseModel, Field


class CommentDTO(BaseModel):
    id: int | None = Field(default=None)
    name: str
    email: str
    body: str
    id_post: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
