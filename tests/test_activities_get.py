def test_get_activities_returns_expected_structure(client):
    # Arrange
    activities_path = "/activities"

    # Act
    response = client.get(activities_path)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload

    sample_activity = payload["Chess Club"]
    assert "description" in sample_activity
    assert "schedule" in sample_activity
    assert "max_participants" in sample_activity
    assert "participants" in sample_activity
    assert isinstance(sample_activity["participants"], list)
