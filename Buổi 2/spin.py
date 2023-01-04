def myfunction(txt):
    #Tách thành phần trong chuỗi đã nhập
    x = txt.split()
    #Tạo ra biến rỗng để hứng dữ liệu
    y = ''
    #Đếm ký tự trong chuỗi x
    for i in x:
        # nếu x bé hơn 5 thì gán biến y bằng y cộng với số i hiện có với chuổi rỗng
        if len(i)<5:
            y = y + i + ''
        else:
            y = y + i[::-1] + ''
    return y

txt = input("enter text")
print(myfunction(txt))