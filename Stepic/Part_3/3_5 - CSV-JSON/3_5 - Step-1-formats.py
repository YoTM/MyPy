import csv

# with open("exsample.tsv") as f:
#     reader = csv.reader(f, delimiter="\t")
#     for row in reader:
#         print(row)

students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]

with open("exsample.csv", "a") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    # for student in students:
    #     writer.writerow(student)
    writer.writerows(students)