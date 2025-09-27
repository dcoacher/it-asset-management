import main
import builtins

# Test Condition 1: Exit flow (q)
def test_exit_flow(monkeypatch, capsys):
    # Simulate entering 'q' and verify program wants to exit + message appears
    cont = main.run_once(lambda _: "q")
    captured = capsys.readouterr()
    assert cont is False
    assert "Thank you for using our service" in captured.out

# Test Condition 2: Invalid menu option
def test_invalid_option(monkeypatch, capsys):
    # Simulate invalid option and verify we keep looping + error message shown
    cont = main.run_once(lambda _: "99")
    captured = capsys.readouterr()
    assert cont is True
    assert "Incorrect menu option" in captured.out
