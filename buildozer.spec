from database import (
    load_data,
    add_item,
    delete_item,
    update_price
)


# Load saved data
items = load_data()


# ==========================================
# SHOW LIST
# ==========================================

def show_list():

    print()
    print("\033[1;96m╔══════════════════════════════╗\033[0m")
    print("\033[1;96m║       📒 PRICE NOTEBOOK      ║\033[0m")
    print("\033[1;96m╚══════════════════════════════╝\033[0m")

    if not items:
        print("\033[91m❌ No items saved.\033[0m")
        return

    print()

    for number, data in enumerate(items, 1):

        print(
            f"\033[1;94m{number}.\033[0m "
            f"\033[97m{data['item']}\033[0m "
            f"\033[95m— ₹{data['price']}\033[0m"
        )

    print()


# ==========================================
# FIND
# ==========================================

def find_item(keyword):

    found = False

    print()
    print("\033[1;96m🔍 SEARCH RESULT\033[0m")

    for number, data in enumerate(items, 1):

        if keyword.lower() in data["item"].lower():

            print(
                f"\033[1;94m{number}.\033[0m "
                f"{data['item']} "
                f"\033[95m— ₹{data['price']}\033[0m"
            )

            found = True

    if not found:
        print("\033[91m❌ Item not found.\033[0m")

    print()


# ==========================================
# MAIN CLI
# ==========================================

print("\033[1;96m")
print("╔══════════════════════════════╗")
print("║       📒 PRICE NOTEBOOK      ║")
print("╚══════════════════════════════╝")
print("\033[0m")

print("\033[93mCommands:\033[0m")
print("  ls")
print("  find Rice")
print("  edit Rice")
print("  del Rice")
print("  clear")
print("  exit")
print()


while True:

    try:
        user_input = input("\033[1;93m>>> \033[0m").strip()

    except (KeyboardInterrupt, EOFError):

        print("\n\033[93mGoodbye! 👋\033[0m")
        break


    # Empty input
    if not user_input:
        continue


    command = user_input.lower()


    # ======================================
    # EXIT
    # ======================================

    if command == "exit":

        print("\033[93mGoodbye! 👋\033[0m")
        break


    # ======================================
    # LS
    # ======================================

    if command == "ls":

        show_list()
        continue


    # ======================================
    # FIND
    # ======================================

    if command.startswith("find "):

        keyword = user_input[5:].strip()

        if keyword:

            find_item(keyword)

        else:

            print("\033[91m❌ Enter an item name.\033[0m")

        continue


    # ======================================
    # DELETE
    # ======================================

    if command.startswith("del "):

        item_name = user_input[4:].strip()

        if not item_name:

            print("\033[91m❌ Enter an item name.\033[0m")
            continue


        deleted = delete_item(items, item_name)


        if deleted:

            print(
                f"\033[1;92m"
                f"🗑️ Deleted: {deleted['item']} — ₹{deleted['price']}"
                f"\033[0m"
            )

        else:

            print("\033[91m❌ Item not found.\033[0m")

        continue


    # ======================================
    # EDIT
    # ======================================

    if command.startswith("edit "):

        item_name = user_input[5:].strip()

        if not item_name:

            print("\033[91m❌ Enter an item name.\033[0m")
            continue


        # Check whether item exists
        found = False

        for data in items:

            if data["item"].lower() == item_name.lower():

                found = True

                try:

                    new_price = int(
                        input(
                            "\033[1;93mNew price: \033[0m"
                        )
                    )

                    if new_price < 0:

                        raise ValueError


                    update_price(
                        items,
                        item_name,
                        new_price
                    )

                    print(
                        "\033[1;92m"
                        "✅ Price updated successfully!"
                        "\033[0m"
                    )

                except ValueError:

                    print(
                        "\033[1;91m"
                        "❌ Invalid price."
                        "\033[0m"
                    )

                break


        if not found:

            print("\033[91m❌ Item not found.\033[0m")

        continue


    # ======================================
    # CLEAR
    # ======================================

    if command == "clear":

        if not items:

            print("\033[91m❌ No data to delete.\033[0m")
            continue


        confirm = input(
            "\033[1;93m"
            "⚠️ Delete ALL items? Type YES: "
            "\033[0m"
        )


        if confirm.lower() == "yes":

            items.clear()

            from database import save_data
            save_data(items)

            print(
                "\033[1;92m"
                "✅ All data deleted."
                "\033[0m"
            )

        else:

            print(
                "\033[93m❌ Cancelled.\033[0m"
            )

        continue


    # ======================================
    # ADD ITEM + PRICE
    # ======================================

    try:

        parts = user_input.rsplit(" ", 1)

        if len(parts) != 2:

            raise ValueError


        item = parts[0].strip()
        price = int(parts[1])


        if not item or price < 0:

            raise ValueError


        add_item(
            items,
            item,
            price
        )


        print(
            "\033[1;92m"
            f"✅ Saved: {item} — ₹{price}"
            "\033[0m"
        )


    except (ValueError, IndexError):

        print(
            "\033[1;91m"
            "❌ ERROR: Wrong format."
            "\033[0m"
        )

        print(
            "\033[91m"
            "Example: Rice 650"
            "\033[0m"
        )
