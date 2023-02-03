#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 2023

@author: javalce
"""


from ..database import CRUDRepository
from ..model.user import User


class UserRepository(CRUDRepository[User, int]):
    def __init__(self) -> None:
        super().__init__(User)
