def grade():
    score=int(input("score:"))
    if score<=100 and score>89:
        print("grade a")
    elif score<=89 and score>79:
        print("grade b")
    else:
        print("grade f")
grade()