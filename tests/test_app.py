from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_add_task():
    client = app.test_client()

    response = client.post(
        "/add",
        data={"task": "Learn Docker"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Learn Docker" in response.data


def test_complete_task():
    client = app.test_client()

    client.post(
        "/add",
        data={"task": "Learn Jenkins"}
    )

    response = client.get("/complete/0")

    assert response.status_code == 302