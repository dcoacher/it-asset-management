# main.py
# --- This is a Main file which will contain Welcome Screen and Main Menu features.
import os, sys
import functions   # <-- required
import demo        # <-- required (preloads dummy data)

def handle_choice(choice: str) -> bool:
    """
    Handle one menu choice.
    Returns:
        True  -> keep looping
        False -> exit loop
    """
    match choice:
        case "1":
            functions.main_menu_add_new_item()
            return True
        case "2":
            functions.main_menu_delete_item()
            return True
        case "3":
            functions.main_menu_modify_item()
            return True
        case "4":
            functions.main_menu_assign_item()
            return True
        case "5":
            functions.main_menu_add_new_user()
            return True
        case "6":
            functions.main_menu_show_all_users()
            return True
        case "7":
            functions.main_menu_show_all_items_by_the_user()
            return True
        case "8":
            functions.main_menu_show_all_stock_items()
            return True
        case "9":
            functions.main_menu_calculate_stock_by_categories()
            return True
        case "q":
            print("👋 Thank you for using our service. See you later!\n")
            return False
        case _:
            print("❌ Error: Incorrect menu option has been chosen. Please try again.")
            return True

def run_once(input_func=input) -> bool:
    """
    Runs exactly one iteration of the main menu.

    Test-friendly: if a custom input_func is injected (not builtin input),
    always use it. Only use AUTO_CHOICE/TTY fallbacks with the real input().
    """
    functions.main_menu_handler()

    if input_func is not input:
        choice = input_func("✨ Please choose menu option (q for exit)✨: ")
        return handle_choice(choice)

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

def main():
    functions.welcome_screen()
    while True:
        if not run_once():
            break

if __name__ == "__main__":
    main()
