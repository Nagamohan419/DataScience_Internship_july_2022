def minion_game(string):
    # your code goes here
    # your code goes here
    # The Minion Game in Python - Hacker Rank Solution START
    p1 = 0;
    p2 = 0;
    str_len = len(string)
    for i in range(str_len):
        if s[i] in "AEIOU":
            p1 += (str_len)-i
        else :
            p2 += (str_len)-i
    
    if p1 > p2:
        print("Kevin", p1)
    elif p1 < p2:
        print("Stuart",p2)
    elif p1 == p2:
        print("Draw")
    else :
        print("Draw")
    # The Minion Game in Python - Hacker Rank SolutionEND
if __name__ == '__main__':
    s = input()
    minion_game(s)