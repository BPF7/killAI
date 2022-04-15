Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# range 와 for 반복문

range(5)
range(0, 5)
print(list(range(5)))
[0, 1, 2, 3, 4]
print(list(range(5))


      
KeyboardInterrupt
print(list(range(5)))
      
[0, 1, 2, 3, 4]
print(tuple(range(5)))
      
(0, 1, 2, 3, 4)
ran_list =  [ x for x in range(5) ]
      
ran_list
      
[0, 1, 2, 3, 4]
ran_list =  [ x*2 for x in range(5) ]
      
ran_list
      
[0, 2, 4, 6, 8]
for i in range(5):
      print(i)

      
0
1
2
3
4
for i in range(5):
      print(i)1
      
SyntaxError: invalid syntax
2
      
2
for r in ran_list:
      print(r)

      
0
2
4
6
8
for r in ran_list[0:]:
      print(r)

      
0
2
4
6
8
for i in ran_list(10,2):
      print(i)

      
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    for i in ran_list(10,2):
TypeError: 'list' object is not callable
for i in range(10,2):
      print(i)

      

for i in range(0,10,2):
      print(i)

      
0
2
4
6
8
for i in range(0,20,2):
      print(i)

      
0
2
4
6
8
10
12
14
16
18
for i in range(5):
      print("python study")

      
python study
python study
python study
python study
python study
for i in range(5):
      print("python study"*i)

      

python study
python studypython study
python studypython studypython study
python studypython studypython studypython study
for i in ran_list:
      print(i)

      
0
2
4
6
8
for i in ran_list:
      print(ran_list)

      
[0, 2, 4, 6, 8]
[0, 2, 4, 6, 8]
[0, 2, 4, 6, 8]
[0, 2, 4, 6, 8]
[0, 2, 4, 6, 8]




# 숫자 1부터 10까지 덧셈 모델
      

for number in range(1,11):
      total_s = number + total_s

      
Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    total_s = number + total_s
NameError: name 'total_s' is not defined
total_s = 0
      
for number in range(1,11):
      total_s = number + total_s

      
print(total_s)
      
55
total_s = 0
      
for number in range(1,11):
      total_s += number

      
print(total_s)
      
55
def tptal_sum( ):
    for number in range(1,11):
      total_s += number
      print(total_s)

      
total_sum()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    total_sum()
NameError: name 'total_sum' is not defined. Did you mean: 'tptal_sum'?
def total_sum( ):
    for number in range(1,11):
      total_s += number
      print(total_s)

      
total_sum()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    total_sum()
  File "<pyshell#64>", line 3, in total_sum
    total_s += number
UnboundLocalError: local variable 'total_s' referenced before assignment
def total_sum( ):
    total_s = 0
    for number in range(1,11):
      total_s += number
      print(total_s)

      
total_sum()
1
3
6
10
15
21
28
36
45
55
def total_sum(n):
    total_s = 0
    for number in range(1,n+1):
      total_s += number
      print(total_s)

      
total_sum(10)
1
3
6
10
15
21
28
36
45
55
total_sum(20)
1
3
6
10
15
21
28
36
45
55
66
78
91
105
120
136
153
171
190
210
total_sum(100)
1
3
6
10
15
21
28
36
45
55
66
78
91
105
120
136
153
171
190
210
231
253
276
300
325
351
378
406
435
465
496
528
561
595
630
666
703
741
780
820
861
903
946
990
1035
1081
1128
1176
1225
1275
1326
1378
1431
1485
1540
1596
1653
1711
1770
1830
1891
1953
2016
2080
2145
2211
2278
2346
2415
2485
2556
2628
2701
2775
2850
2926
3003
3081
3160
3240
3321
3403
3486
3570
3655
3741
3828
3916
4005
4095
4186
4278
4371
4465
4560
4656
4753
4851
4950
5050


# 1부터 어떤 숫자까지 곱하는 모델

time_s =1
for x in range(1,6)
SyntaxError: expected ':'
for x in range(1,6)
SyntaxError: expected ':'
for x in range(1,6):
    time_s = x*time_s

    
print(time_s)
120
def time sum( ):
    
SyntaxError: invalid syntax
def time_sum( ):
    time_s =1
    for x in range(1,6):
        time_s = x*time_s
        print("1부터 {}숫자까지 곱: {}".format(6,time_s))

        
time_sum()
1부터 6숫자까지 곱: 1
1부터 6숫자까지 곱: 2
1부터 6숫자까지 곱: 6
1부터 6숫자까지 곱: 24
1부터 6숫자까지 곱: 120
def time_sum( ):
    time_s =1
    for x in range(1,6):
        time_s = x*time_s
        print("1부터 {}숫자까지 곱: {}".format(6,time_s))

        
total_s = 0
for number in range(1,11):
    total_s += number
    print("1부터 {}까지의 총합: {}".\
          format(number, total_s))

    
1부터 1까지의 총합: 1
1부터 2까지의 총합: 3
1부터 3까지의 총합: 6
1부터 4까지의 총합: 10
1부터 5까지의 총합: 15
1부터 6까지의 총합: 21
1부터 7까지의 총합: 28
1부터 8까지의 총합: 36
1부터 9까지의 총합: 45
1부터 10까지의 총합: 55
for number in range(1,11):
    total_s += number
print("1부터 {}까지의 총합: {}".\
          format(number, total_s))
SyntaxError: invalid syntax

======= RESTART: C:/Users/이상훈/AppData/Local/Programs/Python/Python310/dkanrjsk.py ======
Traceback (most recent call last):
  File "C:/Users/이상훈/AppData/Local/Programs/Python/Python310/dkanrjsk.py", line 2, in <module>
    total_s += number
NameError: name 'total_s' is not defined


======= RESTART: C:/Users/이상훈/AppData/Local/Programs/Python/Python310/dkanrjsk.py ======
Traceback (most recent call last):
  File "C:/Users/이상훈/AppData/Local/Programs/Python/Python310/dkanrjsk.py", line 2, in <module>
    total_s += number
NameError: name 'total_s' is not defined

# 구구단

left_num = 8
for number in range(1,10):
    gugudan = left_num* number
    print("{}x{} = {}".\
          format(left_num, number, gugudan))

    
8x1 = 8
8x2 = 16
8x3 = 24
8x4 = 32
8x5 = 40
8x6 = 48
8x7 = 56
8x8 = 64
8x9 = 72
left_num = int(input("몇 단? "))
몇 단? 9
for number in range(1,10):
    gugudan = left_num* number
    print("{}x{} = {}".\
          format(left_num, number, gugudan))

    
9x1 = 9
9x2 = 18
9x3 = 27
9x4 = 36
9x5 = 45
9x6 = 54
9x7 = 63
9x8 = 72
9x9 = 81

====================== RESTART: C:/Users/이상훈/OneDrive/바탕 화면/ggd.py =====================
몇 단? 6
6x1 =
6x2 =
6x3 =
6x4 =
6x5 =
6x6 =
6x7 =
6x8 =
6x9 =

====================== RESTART: C:/Users/이상훈/OneDrive/바탕 화면/ggd.py =====================
gugudans()
몇 단? 4
4x1 =
4x2 =
4x3 =
4x4 =
4x5 =
4x6 =
4x7 =
4x8 =
4x9 =
gugudans(8)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    gugudans(8)
TypeError: gugudans() takes 0 positional arguments but 1 was given

====================== RESTART: C:/Users/이상훈/OneDrive/바탕 화면/ggd.py =====================
gugudans(8)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    gugudans(8)
TypeError: gugudans() takes 0 positional arguments but 1 was given
