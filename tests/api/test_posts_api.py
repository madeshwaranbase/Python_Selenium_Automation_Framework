import pytest

@pytest.mark.api
def test_get_existing_post_returns_expected_contract(api_client):
    response = api_client.get("/posts/1")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert isinstance(body["title"], str)
    assert isinstance(body["body"], str)

@pytest.mark.api
def test_create_post_returns_created_resource(api_client):
    payload = {
        "title": "automation framework validation",
        "body": "created by pytest requests client",
        "userId": 1,
    }
    response = api_client.post("/posts", payload)

    assert response.status_code == 201
    body = response.json()
    assert body["title"] == payload["title"]
    assert body["userId"] == payload["userId"]

@pytest.mark.api
@pytest.mark.parametrize("post_id", [0, -1, 999999])
def test_unknown_post_is_handled_by_api(api_client, post_id):
    response = api_client.get(f"/posts/{post_id}")
    assert response.status_code == 404
