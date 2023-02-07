#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 2023

@author: javalce
"""

import pytest
from fastapi.testclient import TestClient

from demo_fastapi_sqlalchemy.main import create_app


@pytest.fixture
def client():
    app = create_app()
    client = TestClient(app)
    return client
