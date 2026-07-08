def eat(students,sandwiches):
    count = [students.count(0),students.count(1)]
    for i in sandwiches:
        if count[i] == 0:
            break
        count[i]-=1
    return sum(count)
