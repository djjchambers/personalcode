from operator import itemgetter

if __name__ == '__main__':
    n = int(input())
    students = [[input(), float(input())] for _ in range(n)]  
    second_lowest = sorted(list(set(score for name, score in sorted(students))))[1]
    print("\n".join(name for name, score in sorted(students) if score == second_lowest))