if __name__ == "__main__":
    phones = {
        "Bob Marley" : "11-22-33",
        "Another Guy" : "44 - 55 - 11",
        "Justin" : None
    }
    print(phones)
    phones["Justin"] = "555555"
    print(phones)

    print(phones.keys())
    print(phones.values())

    for key in phones:
        print(key)
    for value in phones.values():
        print(value)

    for key in phones:
        print(key, phones[key])

    for key, value in phones.items():
        print(key, value)


    prev_phones = phones.copy()
    print(phones.get("900"))
    print(phones.get("50", "No value"))

    phones.update({"will": "numer"})

    phones.pop("will")

    phones.pop("will")


