def get_num():
    num = []
    while True:
        try:
            number = float(input("Enter a number (or type 'ENTER' when you are done): "))
            num.append(number)
        except ValueError:
            print("PROCESSING...")
            break
    return num

def calc_sum(numbers):
    return sum(numbers)

def main():
    print("Welcome")
    numbers = get_num()
    if numbers:
        result = calc_sum(numbers)
        print(f"SUM:" + str(result))
    else:
        print("Enter Numbers and Try again")



if __name__ == "__main__":
    main()
