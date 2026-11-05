from add_orders import discount_percentages


def mune():

    pick = int(input("""========== ORDER MANAGER ==========
1. Create order
2. Show all orders
3. Find order by ID
4. Close order
5. Show sales report
0. Exit
Choose option:
"""))
    if pick == 1:
        print(discount_percentages())


if __name__ == "__main__":
    mune()
