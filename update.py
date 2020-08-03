import datetime

def main():
    today = datetime.datetime.now()
    f_today = today.strftime("%B %d %Y \t %H:%M")
    print(f_today)

    with open("test.csv", "a+") as fp:
        buff = f_today + ','
        raw_inp = input("Please enter diary entry here: ")
        fp.write(f_today + ',"' + raw_inp + '"\n');


if __name__ == "__main__":
    main()

