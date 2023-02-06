#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 2023

@author: javalce
"""

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base

if TYPE_CHECKING:
    from .post import Post


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column("id_comment", primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column("name", String(255))
    email: Mapped[str] = mapped_column("email", String(255), unique=True)
    body: Mapped[str] = mapped_column("body", Text)
    id_post: Mapped[int] = mapped_column("id_post", ForeignKey("posts.id_post"))

    post: Mapped["Post"] = relationship(back_populates="comments")
