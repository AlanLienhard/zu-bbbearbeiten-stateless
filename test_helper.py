import helper


def setup_function():
    # jedes Mal eine leere Ausgangslage
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
