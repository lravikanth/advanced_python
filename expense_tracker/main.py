import initiate


def main():
    print("Hello from expense-tracker!")
    print(initiate.get_input())
    ex = initiate.get_input()
    print(ex.total_amount())
    print('discount: ', ex.price_discount())


if __name__ == "__main__":
    main()
