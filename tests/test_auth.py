from urllib import response
from flask import url_for

def test_auth_no_user(app_with_db):
    #when
    response = app_with_db.post(
        url_for("main.dashboard"),
        json = {"admin_user":"Akash", "admin_password":"Akash@123"}
    )

    #then
    assert response.status_code == 404


def test_auth_no_user(app_with_data):
    #when
    response = app_with_data.post(
        url_for("main.dashboard"),
        json = {"admin_user":"Akash", "admin_password":"Akash@123"}
    )

    #then
    assert response.status_code == 200

    data = response.json
    assert "token" in data