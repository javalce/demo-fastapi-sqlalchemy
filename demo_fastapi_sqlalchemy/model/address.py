#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 2023

@author: javalce
"""

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base

if TYPE_CHECKING:
    from .user import User


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
