def test_root_redirect(client):
    # Arrange
    url = "/"

    # Act
    response = client.get(url, follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities(client):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200
    assert "Soccer Team" in response.json()
    assert "Art Club" in response.json()


def test_signup_for_activity_success(client):
    # Arrange
    activity_name = "Chess Club"
    email = "new_student@mergington.edu"
    url = f"/activities/{activity_name}/signup"

    # Act
    response = client.post(url, params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}


def test_signup_for_activity_already_signed_up(client):
    # Arrange
    activity_name = "Soccer Team"
    email = "lucas@mergington.edu"
    url = f"/activities/{activity_name}/signup"

    # Act
    response = client.post(url, params={"email": email})

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up for this activity"


def test_unregister_from_activity_success(client):
    # Arrange
    activity_name = "Drama Club"
    email = "sarah@mergington.edu"
    url = f"/activities/{activity_name}/participants/{email}"

    # Act
    response = client.delete(url)

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}


def test_unregister_from_activity_not_signed_up(client):
    # Arrange
    activity_name = "Art Club"
    email = "missing_student@mergington.edu"
    url = f"/activities/{activity_name}/participants/{email}"

    # Act
    response = client.delete(url)

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is not signed up for this activity"
