연필 = int(input("연필의 가격: "))
펜 = int(input("펜의 가격: "))
bp_pencil = int(input("연필의 갯수: "))
bp_pen = int(input("펜의 갯수: "))
js = int(input("할인율: "))
print("%.2f"%((연필*bp_pencil+펜*bp_pen)*(100-js)/100))
            
print("hello world")