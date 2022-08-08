if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for x,y in student_marks.items():
        if(x == query_name):
            k=round(sum(y)/len(y),2)
            k='{0:.2f}'.format(k)
            print(k)
        else:
            continue