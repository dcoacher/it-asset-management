# main.py
# --- This is a Main file which will contain Welcome Screen and Main Menu features. 
import functions  # Importing functions module from functions.py file
import demo       # Importing Dummy Data (preloaded Users and Items with different status)
import os, sys


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
    functions.main_menu_handler()
    # 1) If env var provided, use it
    auto = os.getenv("AUTO_CHOICE")
    if auto is not None:
        choice = auto
    # 2) If no TTY (non-interactive container), default to 'q'
    elif not sys.stdin.isatty():
        choice = "q"
    else:
        try:
            choice = input_func("✨ Please choose menu option (q for exit)✨: ")
        except (EOFError, KeyboardInterrupt):
            # Gracefully exit if stdin is closed or user cancels
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