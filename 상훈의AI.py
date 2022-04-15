Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(123)
123
type(12345)
<class 'int'>
type("인공지능")
<class 'str'>
type(123.45)
<class 'float'>
type(true)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
type(True)
<class 'bool'>
print("AI인공지능")
AI인공지능
print(""AI인공지능"")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('"AI인공지능"')
"AI인공지능"
print("\"AI인공지능\"")
"AI인공지능"
print("AI인공\n지능")
AI인공
지능
print("AI인공\t지능")
AI인공	지능
print("AI인공\t지능")
AI인공	지능
print("""\AI인공지능 융합학부"""\)
      
SyntaxError: unexpected character after line continuation character
print("""
AI인공지능 융합학부""")
      

AI인공지능 융합학부
print("""\
AI인공지능 융합학부""")
      
AI인공지능 융합학부
print("""\
AI인공지능 융합학부""")
      
AI인공지능 융합학부
print("""\
AI인공지능 융합학부\
""")
      
AI인공지능 융합학부
print('''\
AI인공지능 융합학부\
''')
      
AI인공지능 융합학부
print('''\
AI인공지능\n융합학부\
''')
      
AI인공지능
융합학부
print('''\
AI인공지능\
융합학부\
''')
      
AI인공지능융합학부
print('''\
AI인공지능
융합학부\
''')
      
AI인공지능
융합학부
print("AI"+"인공지능"+"융합")
      
AI인공지능융합
print("AI"+"인공지능"-"융합")
      
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print("AI"+"인공지능"-"융합")
TypeError: unsupported operand type(s) for -: 'str' and 'str'
print("AI"+"인공지능"*2,"융합"*3)
      
AI인공지능인공지능 융합융합융합
print("AI인공지능\n"8*10)
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("AI인공지능\n"*10)
      
AI인공지능
AI인공지능
AI인공지능
AI인공지능
AI인공지능
AI인공지능
AI인공지능
AI인공지능
AI인공지능
AI인공지능

print("AI인공지능\t"*10)
      
AI인공지능	AI인공지능	AI인공지능	AI인공지능	AI인공지능	AI인공지능	AI인공지능	AI인공지능	AI인공지능	AI인공지능	
print("AI인공지능\t"[0])
      
A
print("AI인공지능\t"[1])
      
I
print("AI인공지능\t"[2])
      
인
print("AI인공지능\t"[3])
      
공
print("AI인공지능\t"[0:3])
      
AI인
print("AI인공지능\t"[2:3])
      
인
print("AI인공지능\t"[2:4])
      
인공
print("AI인공지능\t"[2:6])
      
인공지능
print("AI인공지능\t"[2:])
      
인공지능	
print("AI인공지능\t"[4:])
      
지능	
print("AI인공지능\t"[:3])
      
AI인
print("AI인공지능\t"[-2:-6])
      

print("AI인공지능\t"[-5:-2])
      
인공지
print("AI인공지능"[:-3])
      
AI인
print("AI인공지능"[-5:])
      
I인공지능
len("인공지능융합학부")
      
8
type(len("인공지능"))
      
<class 'int'>
print(len("인공지능")+len("융합학부"))
      
8
type(12345)
      
<class 'int'>
type(123.45)
      
<class 'float'>
int(123.45)
      
123
float(123)
      
123.0
int(True)
      
1
int(False)
      
0
float(True)
      
1.0
str(123)
      
'123'
true(str(123))
      
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    true(str(123))
NameError: name 'true' is not defined. Did you mean: 'True'?
str(123)
      
'123'
str(-12345)
      
'-12345'
type(True)
      
<class 'bool'>
bool(0)
      
False
bool(123.45)
      
True
bool(0.0)
      
False
bool(tree)
      
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    bool(tree)
NameError: name 'tree' is not defined. Did you mean: 'True'?
bool("tree")
      
True
bool("Tree")
      
True
bool(" ")
      
True
bool("")
      
False
