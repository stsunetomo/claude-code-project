from src.main import greet


def test_greet_world():
    assert greet("world") == "Hello, world!"


def test_greet_name():
    assert greet("Claude") == "Hello, Claude!"
