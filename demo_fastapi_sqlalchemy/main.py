#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 2023

@author: javalce
"""


from fastapi import FastAPI

from . import settings
from .controller import address_controller, user_controller
from .database import DBSessionMiddleware


def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)

    app.include_router(user_controller.router)
    app.include_router(address_controller.router)

    return app
