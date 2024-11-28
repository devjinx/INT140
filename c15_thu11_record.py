from c15_thu00_record import Record
from functools import cmp_to_key, reduce

r1 = Record(1, "First", 101.01)
print("r1=", r1)
try:
    r2 = Record(2, "Second", -1.0)
    print("r2=", r2)
except Exception as e:
    print("cannot create r2:", e)

r3 = Record(2, "Third", 103.03)
print("r3=", r3)

for k in Record.get_all_keys():
    print("key=", k)

ls = []
ls.append(Record(10, "Ten", 10.01))
ls.append(Record(19, "Nineteen", 19.019))
ls.append(Record(8, "Eight", 88.08))
ls.append(Record(12, "Twelve", 112.012))
ls.append(Record(7, "Seven", 777.01))

for i in sorted(ls,key=cmp_to_key(Record.cmp_value)):
    print("sorted by value:", i)

for i in sorted(ls):
    print("sorted naturally:", i)

for i in ls:
    if i.get_value() > 100:
        print("value>100:", i)

print(
    reduce(lambda x, y: x + "\n" + y,
        map(lambda x: "after filtering:" + str(x),
            filter(lambda x: x.get_value() > 100,
                ls))))
