def test_docs_endpoint_is_available(client):
    # Arrange
    docs_path = "/docs"

    # Act
    response = client.get(docs_path)

    # Assert
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_openapi_json_endpoint_is_available(client):
    # Arrange
    openapi_path = "/openapi.json"

    # Act
    response = client.get(openapi_path)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert "openapi" in payload
    assert "paths" in payload
