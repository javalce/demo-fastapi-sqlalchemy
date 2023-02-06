#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 2023

@author: javalce
"""

from ..database import CRUDRepository
from ..model.post import Post


class PostRepository(CRUDRepository[Post, int]):
    def __init__(self) -> None:
        super().__init__(Post)
