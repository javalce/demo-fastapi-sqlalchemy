#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 2023

@author: javalce
"""

from sqlalchemy import select

from ..database import CRUDRepository
from ..model.comment import Comment


class CommentRepository(CRUDRepository[Comment, int]):
    def __init__(self) -> None:
        super().__init__(Comment)

    def find_by_id_post(self, id_post: int) -> list[Comment]:
        query = select(Comment).where(Comment.id_post == id_post)
        return self.session.scalars(query).all()
