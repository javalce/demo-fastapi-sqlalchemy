#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 2023

@author: javalce
"""

from typing import List

from fastapi import Depends

from ..exception.address_exception import AddressNotFound
from ..model import Address
from ..repository.address_repository import AddressRepository


class AddressService:
    def __init__(self, repository: AddressRepository = Depends()) -> None:
        self._repository = repository

    def find_all(self) -> List[Address]:
        return self._repository.find_all()

    def find_by_id(self, id: int) -> Address:
        address = self._repository.find_by_id(id)

        if address is None:
            raise AddressNotFound(id)

        return address
