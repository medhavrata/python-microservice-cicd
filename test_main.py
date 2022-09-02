from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API for search or wiki"}

def test_main_phrases():
    response = client.get("/phrase/Barack")
    assert response.status_code == 200
    assert response.json() == {"phrases value":["barack hussein obama ii","bə-rahk hoo-sayn oh-bah-mə","august","american politician","44th president"]}