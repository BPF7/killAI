Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# 원의 둘레와 넓이

# 구의 겉넓이와 부피

pi = 3.141592
r = 10
type(pi)
<class 'float'>
type(r)
<class 'int'>
print("구의 겉넓이: ",4*pi*r**2)
구의 겉넓이:  1256.6368
out_area = 4*pi*r**2
print("구의 겉넓이: ",out_area)
구의 겉넓이:  1256.6368
print("구의 겉넓이: ",format(out_area,".2f"))
구의 겉넓이:  1256.64
type(format(out_area,".2f"))
<class 'str'>
type(round(out_area,2))
<class 'float'>
type(round(out_area,2))
<class 'float'>
input()
12
'12'
type(input())
12
<class 'str'>
r = input("반지름? ")
반지름? 10
ㄱ
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    ㄱ
NameError: name 'ᄀ' is not defined
r
'10'
int(r)
10

=== RESTART: C:/Users/이상훈/AppData/Local/Programs/Python/Python310/dlstnah.py ===
# 구의 겉넓이와 부피
-------------------------

원주율? 3.141592

구의 반지름? 10

Traceback (most recent call last):
  File "C:/Users/이상훈/AppData/Local/Programs/Python/Python310/dlstnah.py", line 10, in <module>
    print("구의 겉넓이:", 4*pi*r**2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

=== RESTART: C:/Users/이상훈/AppData/Local/Programs/Python/Python310/dlstnah.py ===
# 구의 겉넓이와 부피
-------------------------

원주율? 3.141592

구의 반지름? 10

구의 겉넓이: 1256.6368

=== RESTART: C:/Users/이상훈/AppData/Local/Programs/Python/Python310/dlstnah.py ===
# 구의 겉넓이와 부피
-------------------------

원주율? 3.141592

구의 반지름? 10

구의 겉넓이: 1257

=== RESTART: C:/Users/이상훈/AppData/Local/Programs/Python/Python310/dlstnah.py ===
# 구의 겉넓이와 부피
-------------------------

원주율? 3.141592

구의 반지름? 10

구의 겉넓이: 1256.64

=== RESTART: C:/Users/이상훈/AppData/Local/Programs/Python/Python310/dlstnah.py ===
# 구의 겉넓이와 부피
-------------------------

원주율? 3.141592

구의 반지름? 10

out_area = 4*pi*r**2 : 구의 겉넓이 모델

구의 겉넓이: 1256.64

=== RESTART: C:/Users/이상훈/AppData/Local/Programs/Python/Python310/dlstnah.py ===
ball_vol()
# 구의 겉넓이와 부피
-------------------------

원주율? 3.141592

구의 반지름? 10

out_area = 4*pi*r**2 : 구의 겉넓이 모델

구의 겉넓이: 1256.64

=== RESTART: C:/Users/이상훈/AppData/Local/Programs/Python/Python310/dlstnah.py ===
ball_vol()
# 구의 겉넓이와 부피
-------------------------

원주율? 3.141592

구의 반지름? 12

out_area = 4*pi*r**2 : 구의 겉넓이 모델

구의 겉넓이: 1809.56
ball-vol()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    ball-vol()
NameError: name 'ball' is not defined. Did you mean: 'all'?
3.141592
3.141592
ball_vol()
# 구의 겉넓이와 부피
-------------------------

원주율? 3.141592

구의 반지름? 5

out_area = 4*pi*r**2 : 구의 겉넓이 모델

구의 겉넓이: 314.16

=== RESTART: C:/Users/이상훈/AppData/Local/Programs/Python/Python310/dlstnah.py ===
ball_vol()
# 구의 겉넓이와 부피
-------------------------


구의 반지름? 7

out_area = 4*pi*r**2 : 구의 겉넓이 모델

구의 겉넓이: 615.75
ball_vol()
# 구의 겉넓이와 부피
-------------------------


구의 반지름? 15

out_area = 4*pi*r**2 : 구의 겉넓이 모델

구의 겉넓이: 2827.43

=== RESTART: C:/Users/이상훈/AppData/Local/Programs/Python/Python310/dlstnah.py ===
ball_vol(r)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    ball_vol(r)
NameError: name 'r' is not defined
ball_vol(10)
# 구의 겉넓이와 부피
-------------------------


out_area = 4*pi*r**2 : 구의 겉넓이 모델

구의 겉넓이: 1256.64
ball_vol(100)
# 구의 겉넓이와 부피
-------------------------


out_area = 4*pi*r**2 : 구의 겉넓이 모델

구의 겉넓이: 125663.68
total = 100
total =total + 50
total
150
total += 50
total
200
total *= 2
total
400
total /= 4
total
100.0

subject_score = (78,95,68,62)
type(subject_score)
<class 'tuple'>
subject_score = [78,95,68,62]
type(subject_score)
<class 'list'>
subject_score = {78,95,68,62]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
subject_score = {"kor":78,:"eng":95,"math":68,"che":62 }
SyntaxError: invalid syntax
subject_score = { "kor":78,:"eng":95,"math":68,"che":62 }
SyntaxError: invalid syntax
subject_score = { "kor":78,"eng":95,"math":68,"che":62 }
type(subject_score)
<class 'dict'>



subject_score = ( 78,95,68,62 )

subject_score[0]
78
subject_score[4]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    subject_score[4]
IndexError: tuple index out of range
subject_score[3]
62
subject_score[1:3]
(95, 68)
subject_score[1:]
(95, 68, 62)
subject_score[:2]
(78, 95)
total = subject_score[0:4]
total
(78, 95, 68, 62)
total = subject_score[0]+subject_score[1]+subject_score[2]+subject_score[3]
total
303
avr =  total / 4
avr
75.75
print("과목 총점:",total,"과목평균:",avr)
과목 총점: 303 과목평균: 75.75



subject_score = ( 78,95,68,62 )


kor,eng,math,che=subject_score
kor
78
eng
95
math
68
che
62
total = kor + eng + math + che
total
303
avr = total / 4
avr
75.75
'


subject_score = ( (78,95),(68,62) )


subject_score[0]
(78, 95)
subject_score[0][0]
78
subject_score[0][1]
95
subject_score[1][1]
62
kor_t = subject_score[0][0]+subject_score[0][1]
kor_t
173


subject_score = ( (78,95),(68,62) )


kor, eng, = subject_score
kor
(78, 95)
eng
(68, 62)
kor_t = kor[0]+kor[1]
kor_t
173
eng = eng[0]+eng[1]
eng
130
