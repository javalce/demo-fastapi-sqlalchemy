#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 2023

@author: javalce
"""

from pydantic import BaseModel, Field

from .comment_dto import CommentDTO


class PostDTO(BaseModel):
    id: int | None = Field(default=None)
    title: str
    body: str
    comments: list[CommentDTO]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
