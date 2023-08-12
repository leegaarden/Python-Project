from tkinter import *
root=Tk()
root.title("학점 계산하기")

score_one=0
score_two=0
score_three=0
score_four=0
score_five=0
score_six=0
score_seven=0
score_average=0

def grade_one():
    global score_one
    if e8.get() == 'A+':
        score_one=4.5
        L23.config(text=float(score_one))
    elif e8.get() == 'A':
        score_one=4.0
        L23.config(text=float(score_one))
    elif e8.get() == 'A-':
        score_one=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L23.config(text=score_one)
    elif e8.get() == 'B+':
        score_one=3.5
        L23.config(text=float(score_one))
    elif e8.get() == 'B':
        score_one=3.0
        L23.config(text=float(score_one))
    elif e8.get()== 'B-':
        score_one=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L23.config(text=score_one)
    elif e8.get() == 'C+':
        score_one=2.5
        L23.config(text=float(score_one))
    elif e8.get() == 'C':
        score_one=2.0
        L23.config(text=float(score_one))
    elif e8.get() == 'C-':
        score_one=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L23.config(text=score_one)
    elif e8.get() == 'F':
        score_one=0
        L23.config(text=float(score_one))

def grade_two():
    global score_two
    if e9.get() == 'A+':
        score_two=4.5
        L24.config(text=float(score_two))
    elif e9.get() == 'A':
        score_two=4.0
        L24.config(text=float(score_two))
    elif e9.get() == 'A-':
        score_two=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L24.config(text=score_two)
    elif e9.get() == 'B+':
        score_two=3.5
        L24.config(text=float(score_two))
    elif e9.get() == 'B':
        score_two=3.0
        L24.config(text=float(score_two))
    elif e9.get()== 'B-':
        score_two=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L24.config(text=score_two)
    elif e9.get() == 'C+':
        score_two=2.5
        L24.config(text=float(score_two))
    elif e9.get() == 'C':
        score_two=2.0
        L24.config(text=float(score_two))
    elif e9.get() == 'C-':
        score_two=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L24.config(text=score_two)
    elif e9.get() == 'F':
        score_two=0
        L24.config(text=float(score_two))

def grade_three():
    global score_three
    if e10.get() == 'A+':
        score_three=4.5
        L25.config(text=float(score_three))
    elif e10.get() == 'A':
        score_three=4.0
        L25.config(text=float(score_three))
    elif e10.get() == 'A-':
        score_three=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L25.config(text=score_three)
    elif e10.get() == 'B+':
        score_three=3.5
        L25.config(text=float(score_three))
    elif e10.get() == 'B':
        score_three=3.0
        L25.config(text=float(score_three))
    elif e10.get()== 'B-':
        score_three=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L25.config(text=score_three)
    elif e10.get() == 'C+':
        score_three=2.5
        L25.config(text=float(score_three))
    elif e10.get() == 'C':
        score_three=2.0
        L25.config(text=float(score_three))
    elif e10.get() == 'C-':
        score_three=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L25.config(text=score_three)
    elif e10.get() == 'F':
        score_three=0
        L25.config(text=float(score_three))

def grade_four():
    global score_four
    if e11.get() == 'A+':
        score_four=4.5
        L26.config(text=str(score_four))
    elif e11.get() == 'A':
        score_four=4.0
        L26.config(text=float(score_four))
    elif e11.get() == 'A-':
        score_four=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L26.config(text=score_four)
    elif e11.get() == 'B+':
        score_four=3.5
        L26.config(text=float(score_four))
    elif e11.get() == 'B':
        score_four=3.0
        L26.config(text=float(score_four))
    elif e11.get()== 'B-':
        score_four=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L26.config(text=score_four)
    elif e11.get() == 'C+':
        score_four=2.5
        L26.config(text=float(score_four))
    elif e11.get() == 'C':
        score_four=2.0
        L26.config(text=float(score_four))
    elif e11.get() == 'C-':
        score_four=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L26.config(text=score_four)
    elif e11.get() == 'F':
        score_four=0
        L26.config(text=float(score_four))

def grade_five():
    global score_five
    if e12.get() == 'A+':
        score_five=4.5
        L27.config(text=float(score_five))
    elif e12.get() == 'A':
        score_five=4.0
        L27.config(text=float(score_five))
    elif e12.get() == 'A-':
        score_five=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L27.config(text=score_five)
    elif e12.get() == 'B+':
        score_five=3.5
        L27.config(text=float(score_five))
    elif e12.get() == 'B':
        score_five=3.0
        L27.config(text=float(score_five))
    elif e12.get()== 'B-':
        score_five=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L27.config(text=score_five)
    elif e12.get() == 'C+':
        score_five=2.5
        L27.config(text=float(score_five))
    elif e12.get() == 'C':
        score_five=2.0
        L27.config(text=float(score_five))
    elif e12.get() == 'C-':
        score_five=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L27.config(text=score_five)
    elif e12.get() == 'F':
        score_five=0
        L27.config(text=float(score_five))

def grade_six():
    global score_six
    if e13.get() == 'A+':
        score_six=4.5
        L28.config(text=float(score_six))
    elif e13.get() == 'A':
        score_six=4.0
        L28.config(text=float(score_six))
    elif e13.get() == 'A-':
        score_six=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L28.config(text=score_six)
    elif e13.get() == 'B+':
        score_six=3.5
        L28.config(text=float(score_six))
    elif e13.get() == 'B':
        score_six=3.0
        L28.config(text=float(score_six))
    elif e13.get()== 'B-':
        score_six=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L28.config(text=score_six)
    elif e13.get() == 'C+':
        score_six=2.5
        L28.config(text=float(score_six))
    elif e13.get() == 'C':
        score_six=2.0
        L28.config(text=float(score_six))
    elif e13.get() == 'C-':
        score_six=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L28.config(text=score_six)
    elif e13.get() == 'F':
        score_six=0
        L28.config(text=float(score_six))

def grade_seven():
    global score_seven
    if e14.get() == 'A+':
        score_seven=4.5
        L29.config(text=float(score_seven))
    elif e14.get() == 'A':
        score_seven=4.0
        L29.config(text=float(score_seven))
    elif e14.get() == 'A-':
        score_seven=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L29.config(text=score_seven)
    elif e14.get() == 'B+':
        score_seven=3.5
        L29.config(text=float(score_seven))
    elif e14.get() == 'B':
        score_seven=3.0
        L29.config(text=float(score_seven))
    elif e14.get()== 'B-':
        score_seven=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L29.config(text=score_seven)
    elif e14.get() == 'C+':
        score_seven=2.5
        L29.config(text=float(score_seven))
    elif e14.get() == 'C':
        score_seven=2.0
        L29.config(text=float(score_seven))
    elif e14.get() == 'C-':
        score_seven=str("4.5만점 유형에는 존재하지 않는 성적입니다.")
        L29.config(text=score_seven)
    elif e14.get() == 'F':
        score_seven=0
        L29.config(text=float(score_seven))

def average():
    global score_average
    score_average=round(((3*score_one)+(3*score_two)+(3*score_three)+(3*score_four)+(3*score_five)+(3*score_six)+(3*score_seven)) /21,2)
    L30.config(text=score_average)


#tkinter

L1=Label(root,text="7과목이 기본 세팅입니다. 성적란 빈칸에만 0을 입력해 주세요.")
L1.grid(row=0, column=0, columnspan=7)

#과목명 입력

L2=Label(root, text="과목명")
L2.grid(row=1, column=0)
e1=Entry(root)
e1.grid (row=1, column=1, columnspan=2)

L3=Label(root, text="과목명")
L3.grid(row=2, column=0)
e2=Entry(root)
e2.grid (row=2, column=1, columnspan=2)

L4=Label(root, text="과목명")
L4.grid(row=3, column=0)
e3=Entry(root)
e3.grid (row=3, column=1, columnspan=2)

L5=Label(root, text="과목명")
L5.grid(row=4, column=0)
e4=Entry(root)
e4.grid (row=4, column=1, columnspan=2)

L6=Label(root, text="과목명")
L6.grid(row=5, column=0)
e5=Entry(root)
e5.grid (row=5, column=1, columnspan=2)

L7=Label(root, text="과목명")
L7.grid(row=6, column=0)
e6=Entry(root)
e6.grid (row=6, column=1, columnspan=2)

L8=Label(root, text="과목명")
L8.grid(row=7, column=0)
e7=Entry(root)
e7.grid (row=7, column=1, columnspan=2)

#성적 입력

L9=Label(root, text="성적")
L9.grid(row=1, column=3)
e8=Entry(root)
e8.grid (row=1, column=4)

L10=Label(root, text="성적")
L10.grid(row=2, column=3)
e9=Entry(root)
e9.grid (row=2, column=4)

L11=Label(root, text="성적")
L11.grid(row=3, column=3)
e10=Entry(root)
e10.grid (row=3, column=4)

L12=Label(root, text="성적")
L12.grid(row=4, column=3)
e11=Entry(root)
e11.grid (row=4, column=4)

L13=Label(root, text="성적")
L13.grid(row=5, column=3)
e12=Entry(root)
e12.grid (row=5, column=4)

L14=Label(root, text="성적")
L14.grid(row=6, column=3)
e13=Entry(root)
e13.grid (row=6, column=4)

L15=Label(root, text="성적")
L15.grid(row=7, column=3)
e14=Entry(root)
e14.grid (row=7, column=4)


# 과목 학점

B1=Button(root, text="학점", command=grade_one)
B1.grid(row=1, column=5)
L23=Label(root, text=score_one)
L23.grid(row=1, column=6)


B2=Button(root, text="학점" , command=grade_two)
B2.grid(row=2, column=5)
L24=Label(root, text=score_two)
L24.grid(row=2, column=6)


B3=Button(root, text="학점", command=grade_three)
B3.grid(row=3, column=5)
L25=Label(root, text=score_three)
L25.grid(row=3, column=6)


B4=Button(root, text="학점", command=grade_four)
B4.grid(row=4, column=5)
L26=Label(root, text=score_four)
L26.grid(row=4, column=6)

B5=Button(root, text="학점", command=grade_five)
B5.grid(row=5, column=5)
L27=Label(root, text=score_five)
L27.grid(row=5, column=6)


B6=Button(root, text="학점", command=grade_six)
B6.grid(row=6, column=5)
L28=Label(root, text=score_six)
L28.grid(row=6, column=6)


B7=Button(root, text="학점", command=grade_seven)
B7.grid(row=7, column=5)
L29=Label(root, text=score_seven)
L29.grid(row=7, column=6)


#평균 입력

B8=Button(root, text="평균", command=average)
B8.grid(row=8, column=0)
L30=Label(root, text=score_average)
L30.grid(row=8, column=1)
