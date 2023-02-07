#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 2023

@author: javalce
"""

from fastapi.testclient import TestClient

from demo_fastapi_sqlalchemy.dto.comment_dto import CommentDTO


def test_find_comments(client: TestClient):
    response = client.get("/comments")
    json_response = response.json()

    assert response.status_code == 200
    assert len(json_response) == 500


def test_find_comment(client: TestClient):
    response = client.get("/comments/1")
    json_response = response.json()

    assert response.status_code == 200
    assert json_response["id"] == 1


def test_find_comment_not_found_exception(client: TestClient):
    response = client.get("/comments/0")
    json_response = response.json()

    assert response.status_code == 404
    assert json_response["detail"] == "Comment with id '0' not found"


def test_create_comment_already_exists_exception(client: TestClient):
    body = CommentDTO(id=1, name="a", email="a", body="a", id_post=1)
    response = client.post("/comments", json=body.dict())
    json_response = response.json()

    assert response.status_code == 409
    assert json_response["detail"] == "Comment with id '1' already exists"
