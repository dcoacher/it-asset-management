# at top
import os, sys

def run_once(input_func=input) -> bool:
    """
    Runs exactly one iteration of the main menu.
    Prefers a custom input_func (used by tests). Only uses AUTO_CHOICE/TTY logic
    when the real builtin input is used.
    """
    functions.main_menu_handler()

    # If a custom input function is injected (e.g., tests), always use it.
    if input_func is not input:
        choice = input_func("✨ Please choose menu option (q for exit)✨: ")
        return handle_choice(choice)

    # Normal runtime behavior (no custom input_func):
    auto = os.getenv("AUTO_CHOICE")
    if auto is not None:
        choice = auto
    elif not sys.stdin.isatty():
        choice = "q"
    else:
        try:
            choice = input_func("✨ Please choose menu option (q for exit)✨: ")
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Thank you for using our service. See you later!\n")
            return False

    return handle_choice(choice)
