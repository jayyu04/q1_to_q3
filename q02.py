print("-" * 28)
print("        員工薪資輸入        ")
print("    若姓名處未輸入則代表結束")
print("-" * 28)

employees = []

while True:
    name = input("請輸入姓名: ")
    if not name:
        break

    salary = int(input("請輸入薪資："))

    emp = {'eName': name, 'eSalary': salary}
    employees.append(emp)

print("-" * 28)
max_name_length = max(len(emp['eName']) for emp in employees)
for emp in employees:
        space = max_name_length - len(emp['eName'])
        print(f"員工{emp['eName']}{' ' * space}的薪資為 {emp['eSalary']:>9,}")
print("-" * 28)

total = sum(emp['eSalary'] for emp in employees)
avg = total / len(employees) if emp else 0
print(f"合計薪資：{total:>17,}")
print(f"平均薪資：{avg:>17,.2f}")
print("=" * 28)
