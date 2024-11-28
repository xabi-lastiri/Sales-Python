from src.messages.instructions import instruction_return_menu


# Cancel the current operation
def cancel(answer):
    return True if str(answer) == "" else False


# Confirm the current operation.
def confirm():
    confirm = input("Do you want to proceed? [y/n] ").lower()
    return True if confirm == "y" else False


# Display the module's name and instructions (optional).
def introduce_module(module_name, instruction):
    module_name = module_name.upper()
    print(f"\n---\n{module_name}\n---\n")
    print(instruction) if instruction is not None else None


# Return to menu.
def wait_for_return_menu():
    while True:
        menu = input(instruction_return_menu)
        if menu == "m":
            break