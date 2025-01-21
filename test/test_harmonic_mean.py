from imppkg.harmony import main 
import sys 
from termcolor import colored
import pytest 


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["3", "3", "3"], 3.0),
        ([], 0.0),
        (["foo", "bar"], 0.0),
    ],
)
def test_harmony_happy_path(inputs, monkeypatch, capsys, expected):
    monkeypatch.setattr(sys, "argv", ["harmony"] + inputs)
    main()
    assert capsys.readouterr().out.strip() == colored(
        expected,
        "red",
        "on_cyan",
        attrs = ["bold"]
    )