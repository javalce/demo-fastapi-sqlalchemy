#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 2023

@author: javalce
"""


from typing import List

from fastapi import APIRouter, Depends

from ..dto import AddressDTO
from ..service import AddressService

router = APIRouter(prefix="/addresses", tags=["addresses"])


@router.get("", status_code=200, response_model=List[AddressDTO])
def find_all(address_service: AddressService = Depends()):
    return address_service.find_all()


@router.get("/{id}", status_code=200, response_model=AddressDTO)
def find_address(id: int, address_service: AddressService = Depends()):
    return address_service.find_by_id(id)
