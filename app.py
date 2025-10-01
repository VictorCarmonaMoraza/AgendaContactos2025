from menu import show_menu, option_menu
from operation_menu import select_option_menu

# Step 1: Initialize an empty contact book
contact_book = {}

# Step 2: Display the menu
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")
    # guardamos el valor de retorno
    keep_running = select_option_menu(choice, contact_book)

    if not keep_running:
        break  #
