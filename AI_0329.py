Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a_list = [ 1,2,3,4 ]
b_list = [ 5,6,7,8 ]
t_list = a_list + b_list
print(t_list)
[1, 2, 3, 4, 5, 6, 7, 8]
print(a_list*2)
[1, 2, 3, 4, 1, 2, 3, 4]
len(a_list)
4
len(t_list)
8
print(len(a_list)/len(b_list))
1.0
print(len(a_list)/len(t_list))
0.5
a_list.clear()
print(a_list)
[]
b_list.count(7)
1
t_list.count(4)
1
b_list.index(6)
1
b_list.reverse()
b_list
[8, 7, 6, 5]
b_list.sort()
b_list
[5, 6, 7, 8]
10 in b_list
False
10 not in b_list
True
type(10 in b_list)
<class 'bool'>
sub_score = [ [ 78,95 ], [68,62] ]
sub_score[0][1]
95
kor, eng = sub_score
type(kor)
<class 'list'>
print(kor)
[78, 95]
t_list = sub_score[0][0]+sub_score[0][1]
print(t_list)
173
t_kor = kor[0]+kor[1]
print(t_kor)
173
eng[0] = 86
print(eng)
[86, 62]
t_eng = eng[0]+eng[1]
print("국어점수 평균",t_kor,"점", "평균
      
SyntaxError: unterminated string literal (detected at line 1)
print("국어점수 평균",t_kor,"점", "평균",t_kor/2)
      
국어점수 평균 173 점 평균 86.5
print("국어점수 총점",t_kor,"점", "평균",t_kor/2)
      
국어점수 총점 173 점 평균 86.5
t_kor
      
173
print("국어점수 총점 {}점,평균 {}점".format(t_kor,t_kor/2))
      
국어점수 총점 173점,평균 86.5점
print("영어점수 총점 {}점,평균 {}점".format(t_eng,t_eng/2))
      
영어점수 총점 148점,평균 74.0점
print("영어점수 총점 {0}점,평균 {1}점".format(t_eng,t_eng/2))
      
영어점수 총점 148점,평균 74.0점
print("영어점수 총점 {1}점,평균 {0}점".format(t_eng,t_eng/2))
      
영어점수 총점 74.0점,평균 148점






#리스트 자료 수정
      

data_list = [87, 95, 68, 92 ]
      
data_list*2
      
[87, 95, 68, 92, 87, 95, 68, 92]
score_list = [ data for data in data_list]
      
score_list = [ data*2 for data in data_list]
      
score_list
      
[174, 190, 136, 184]
div_score = [ score for score in div_score ]
      
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    div_score = [ score for score in div_score ]
NameError: name 'div_score' is not defined. Did you mean: 'sub_score'?
div_score = [ score/3 for score in score_list ]
      
print(score)
      
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(score)
NameError: name 'score' is not defined
print(div_score)
      
[58.0, 63.333333333333336, 45.333333333333336, 61.333333333333336]
div_score = [ int(score/3) for score in score_list ]
      
print(div_score)
      
[58, 63, 45, 61]
div_score = [ int(score/3,"2f") for score in score_list ]
      
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    div_score = [ int(score/3,"2f") for score in score_list ]
  File "<pyshell#60>", line 1, in <listcomp>
    div_score = [ int(score/3,"2f") for score in score_list ]
TypeError: 'str' object cannot be interpreted as an integer
div_score = [ int(score/3,".2f") for score in score_list ]
      
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    div_score = [ int(score/3,".2f") for score in score_list ]
  File "<pyshell#61>", line 1, in <listcomp>
    div_score = [ int(score/3,".2f") for score in score_list ]
TypeError: 'str' object cannot be interpreted as an integer
adj_list = [ data + 5 for data in data_list ]
      
data_list
      
[87, 95, 68, 92]
adj_list
      
[92, 100, 73, 97]
scd_list = [ x-5 for x in data_list ]
      
scd_list
      
[82, 90, 63, 87]
scd_list
      
[82, 90, 63, 87]


# 자료의 구조: 사전
      


score = { "math":78, "english":95,
          "science":68, "chemistry":62
          }
      
score
      
{'math': 78, 'english': 95, 'science': 68, 'chemistry': 62}
type(score)
      
<class 'dict'>
score["music":86]
      
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    score["music":86]
TypeError: unhashable type: 'slice'
score["music"]=86
      
score
      
{'math': 78, 'english': 95, 'science': 68, 'chemistry': 62, 'music': 86}
del score[0]
      
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    del score[0]
KeyError: 0
del score["math"]
      
score
      
{'english': 95, 'science': 68, 'chemistry': 62, 'music': 86}
c