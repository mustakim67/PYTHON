def generate_output(n):
    num = 1
    for i in range(n):
        print(num, num + 1, num + 2, "PUM")
        num += 4

n = int(input())
generate_output(n)


