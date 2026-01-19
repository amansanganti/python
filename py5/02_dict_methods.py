marks = {
"Aman"  : 85,
"Rahul" : 92,
"Sonia" : 78,
}


# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Aman": 95, "Renuka": 100})

print(marks.get("Aman"))
print(marks)


# difference between () and [] when accessing dictionary elements
# print(marks["John"])  # you will get a key error in this because "John" key is not present
# print(marks.get("John"))  # you will get None in this because "John" key is not present