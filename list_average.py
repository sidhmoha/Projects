if __name__ == '__main__':
    n = int(input())
    sum=0
    avg=1
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    print (student_marks)
    query_name=input()

    for name in student_marks:
        if (name==query_name):
            for i in student_marks[name]:
                sum+=i
            avg=sum/len(student_marks[name])
            print (avg)
    print (format(avg,'.2f'))