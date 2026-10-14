students = {
    "FA23-BSE-049": "Fatima Khalid",   # replace 000 with your real Reg#
}

reg = input("Enter your Reg#: ").strip().upper()
print("Name:", students.get(reg, "Reg# not found"))
