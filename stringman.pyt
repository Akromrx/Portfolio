def to_camel_case(text):
    text = text.replace("-", "_")
    print(text)
    s = text.split("_")
    print(s)
    s[1:] = [i.capitalize() for i in s[1:]]
    res = "".join(s)
    print(res)

to_camel_case("the_Stealth-Warrior")