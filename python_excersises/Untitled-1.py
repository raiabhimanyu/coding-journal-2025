time=input("what time is it?")
def main():
    t = convert(time)
    if t>= 07.00 and t<=08.00:
        print("breakfast time")
    elif t>= 12.00 and t<=13.00:
        print("lunch time")
    elif t>= 18.00 and t<=19.00:
        print("lunch time")


def convert(time):
    hours, minutes = time.split(":")
    minutes=int(minutes)
    hours=int(hours)
    minutes=(minutes/60)
    x=hours+minutes

    return x


if __name__ == "__main__":
    main()
