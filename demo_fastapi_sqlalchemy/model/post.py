#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 2023

@author: javalce
"""

from typing import TYPE_CHECKING, List

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base

if TYPE_CHECKING:
    from .comment import Comment


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column("id_post", primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column("title", String(255))
    body: Mapped[str] = mapped_column("body", Text)

    comments: Mapped[List["Comment"]] = relationship(back_populates="post")
