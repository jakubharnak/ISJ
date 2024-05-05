def running_avg(obj):
    for i in range(1, len(obj)):
        yield sum(obj[1:i+1]) / i

print(list(running_avg(["age", 12, 20, 1])))

#[12.0, 16.0, 11.0]