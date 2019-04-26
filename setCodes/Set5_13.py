
class Set5:
    set_a = set(["Phy", "sci", "Math", "History"])

    # remove string from set if present in list using discard
    set_a.discard("Phy")

    set_a.update(["chem", "sports"])
    print(set_a)

