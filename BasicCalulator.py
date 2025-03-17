def addition(_num1_,_num2_):
    sum = _num1_+_num2_
    print(sum)

def subtraction(_num1_,_num2_):
    sum = _num1_-_num2_
    print(sum)

def multiplication(_num1_,_num2_):
    sum = _num1_*_num2_
    print(sum)

def division(_num1_,_num2_):
    sum = _num1_/_num2_
    print(sum)

while True:
    _num1_ = float(input("Enter your First Number...    "))
    _num2_ = float(input("Enter your Second Number...   "))
    _operator_ = input("""Enter you operator...   
                            For addition --> Type "+"
                            For subtraction --> Type "-"
                            For Multiplication --> Type "*"
                            For Division --> Type "/"
                       """)
    if _operator_ == "+":
        addition(_num1_,_num2_)
    elif _operator_ == "-":
        subtraction(_num1_,_num2_)
    elif _operator_ == "*":
        multiplication(_num1_,_num2_)
    elif _operator_ == "/":
        division(_num1_,_num2_)
    else:
        print(TypeError)
            
