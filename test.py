import pytest,requests
from fastapi.testclient import TestClient
from main import app,NOTES

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.json() == {"root":"The app is launched"}

def test_allNotes():
    response = client.get("/notes")
    assert response.json() == requests.get("http://127.0.0.1:8000/notes").json()