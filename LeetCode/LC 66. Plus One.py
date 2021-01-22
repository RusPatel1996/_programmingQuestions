def plusOne(digits):
    digits = str(int("".join(map(str, digits))) + 1)
    return [int(num) for num in digits]

if __name__ == "__main__":
    xs = [9,9,9]

    print(plusOne(xs)) # --> [1,0,0,0]