import src.app as app_module


def test_unregister_removes_registered_participant(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = app_module.activities[activity_name]["participants"][0]
    participants_before = len(app_module.activities[activity_name]["participants"])

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": existing_email},
    )
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert payload["message"] == f"Unregistered {existing_email} from {activity_name}"
    assert existing_email not in app_module.activities[activity_name]["participants"]
    assert len(app_module.activities[activity_name]["participants"]) == participants_before - 1


def test_unregister_returns_404_for_unknown_activity(client):
    # Arrange
    unknown_activity = "Unknown Activity"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{unknown_activity}/unregister",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_404_for_student_not_registered(client):
    # Arrange
    activity_name = "Chess Club"
    missing_email = "missing.student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": missing_email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not registered for this activity"


def test_unregister_returns_422_when_email_is_missing(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.delete(f"/activities/{activity_name}/unregister")

    # Assert
    assert response.status_code == 422
