def cw12():
    num = int(input("Po co ci dual boot, kup drugiego laptopa z amso...: "))

    a = 10
    while num != 0:
        temp = num%10
        num = num //10 
        if temp >= a:
            return False
        a = temp
    return True


if __name__ == "__main__":
    print(cw12())