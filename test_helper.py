import helper


def setup_function():

    helper.todos.clear()


def test_add_creates_one_todo():
    helper.add("abc")
    assert len(helper.todos) == 1


def test_add_replaces_b_with_bbb():
    helper.add("abc")
    # "abc" -> "abbbc"
    assert helper.todos[0].text == "abbbc"


def test_update_toggles_isCompleted():
    helper.add("task")
    assert helper.todos[0].isCompleted is False
    helper.update(0)
    assert helper.todos[0].isCompleted is True


def test_add_saves_due_date_when_provided():
    helper.todos.clear()
    helper.add("task", "2025-10-25")
    assert helper.todos[0].due_date == "2025-10-25"


def test_add_works_without_due_date():
    helper.todos.clear()
    helper.add("task")
    assert helper.todos[0].due_date == ""
