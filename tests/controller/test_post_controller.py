#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 2023

@author: javalce
"""

from fastapi.testclient import TestClient

from demo_fastapi_sqlalchemy.dto.post_dto import PostDTO


def test_find_posts(client: TestClient):
    response = client.get("/posts")
    json_response = response.json()

    assert response.status_code == 200
    assert len(json_response) == 100


def test_find_post(client: TestClient):
    response = client.get("/posts/1")
    json_response = response.json()

    assert response.status_code == 200
    assert json_response["id"] == 1


def test_find_post_not_found_exception(client: TestClient):
    response = client.get("/posts/0")
    json_response = response.json()

    assert response.status_code == 404
    assert json_response["detail"] == "Post with id '0' not found"


def test_create_post_already_exists_exception(client: TestClient):
    body = PostDTO(id=1, title="a", body="a")
    response = client.post("/posts", json=body.dict())
    json_response = response.json()

    assert response.status_code == 409
    assert json_response["detail"] == "Post with id '1' already exists"
