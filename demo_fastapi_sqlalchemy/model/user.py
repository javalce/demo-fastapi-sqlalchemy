#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 2023

@author: javalce
"""

from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base

if TYPE_CHECKING:
    from .address import Address


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
