import helper
from main import app


def test_full_add_and_update_flow():
    helper.todos.clear()

    client = app.test_client()
    resp = client.post(
        "/add",
        data={"text": "abc", "due_date": "2025-10-25"},
        follow_redirects=True,
    )
    assert resp.status_code == 200

    assert len(helper.todos) == 1
    assert helper.todos[0].text == "abbbc"
    assert helper.todos[0].due_date == "2025-10-25"

    page = resp.data
    assert b"abbbc" in page
    assert b"2025-10-25" in page

    resp2 = client.get("/update/0", follow_redirects=True)
    assert resp2.status_code == 200
    assert helper.todos[0].isCompleted is True
