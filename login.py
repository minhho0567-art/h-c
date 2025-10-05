def login():
    email = input("Enter your email: ")
    vi_tri = email.find("@")
    if vi_tri!=-1:
        b = email[vi_tri+1:]
        if b == "gmail.com":
            print("Email hợp lệ")
            password = input("Enter your password: ")
            if len(password) >=8:
                print("mật khẩu hợp lệ")
                nhaplai = input("nhập lại mật khẩu")
                if password == nhaplai:
                    print("đăng ký thành công")
                    return True
                else:
                    print("Không khớp")
                    return False
            else:
                print("Mật khẩu phải chứa 8 ký tự")
                return False
        else:
            print("Email phải có @gmail.com")
            return False
    else:
        print("Email phải có @gmail.com")
        return False
while True:
    login()






