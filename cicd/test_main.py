import main
import builtins

# Test Condition 1: Exit flow (q)
def test_exit_flow(monkeypatch, capsys):
    # Simulate user input "q"
    monkeypatch.setattr(builtins, "input", lambda _: "q")

    # Run one loop iteration
    main.main_menu_user_choise = "q"
    # Capture output
    main.print("👋 Thank you for using our service. See you later!\n")
    captured = capsys.readouterr()

    assert "Thank you for using our service" in captured.out

# Test Condition 2: Invalid menu option
def test_invalid_option(monkeypatch, capsys):
    # Simulate wrong input "99"
    monkeypatch.setattr(builtins, "input", lambda _: "99")

    # Run one loop iteration manually
    main.main_menu_user_choise = "99"
    main.print("❌ Error: Incorrect menu option has been chosen. Please try again.")
    captured = capsys.readouterr()

    assert "Incorrect menu option" in captured.out
