import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user_details():
    # שליחת בקשת GET למשתמש מספר 1
    response = requests.get(f"{BASE_URL}/users/1")
    
    # בדיקת Status Code (צריך להיות 200)
    assert response.status_code == 200
    
    # בדיקת תוכן ה-JSON
    data = response.json()
    assert data["username"] == "Bret"
    assert "email" in data

def test_create_post():
    # סימולציה של יצירת פוסט חדש (POST request)
    payload = {
        "title": "Automation is Great",
        "body": "This is a test post",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    
    # בדיקה שנוצר משאב חדש (201 Created)
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]