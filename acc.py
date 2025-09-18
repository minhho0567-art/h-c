import random
import re
def gmail(a):
    b = r"^[a-zA-Z0-9_.+-]+@gmail.com$"
    if re.match(b, a):
        print('Gmail is valid!')
        return True
    else:
        return False

def strong_pass(password):
    if len(password) < 8:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*()_+=-]", password):
        return False
    return True


kho_cn = [] # Save account information, password, student code.
kho_thong_tin = [] # Save student code, full name, phone number, date of birth, address information.
kho = {
    'personal information repository' : kho_cn,
    'information repository' : kho_thong_tin
}
# The repository of all information.
z = None
t = None
h = None
g = None
print('1) Register personal information')
print('2) View saved information')
print('3) Exit')
print('4) Change information')


while True:
    num = str(input('Select item: '))
    if num == '1' and num.isdigit():
        while True:
            ten_dang_nhap = input('- Gmail username: ')
            if gmail(ten_dang_nhap):
                q = True
                while q:
                    mat_khau = input('- New password:')
                    if strong_pass(mat_khau):
                        q = False

                        while True:
                            nhac_lai = input('- Enter password again:')
                            if nhac_lai == mat_khau:
                                ma_sv = random.randint(1000, 9999)
                                print(f'- Student ID: {ma_sv} \nplease save the student ID so you can change the password')
                                kho_luu_cn = [ten_dang_nhap,ma_sv,mat_khau]
                                kho_cn.append(kho_luu_cn)
                                # Chèn thông tin từ kho_luu_cn vào kho_cn.

                                print('- Registration completed.')

                                while True:
                                    name = str(input('- Enter full name: '))
                                    so_dt = int(input('- Enter phone number: '))
                                    ngay_sinh = input('- Enter date of birth: dd/mm/yyyy: ')
                                    add = str(input('- Enter address: '))
                                    kho_luu = [ma_sv,name,so_dt,ngay_sinh,add]
                                    kho_thong_tin.append(kho_luu)
                                    # Chèn kho_luu vào kho_thong_tin.
                                    print('- Goodbye.')
                                    break
                                break
                            else:
                                print('- Passwords do not match.')

                        break
                break
            else:
                print('- You left the username blank; the username should be your Gmail address.')
    elif num == '2' and num.isdigit():
        while True:
            tk = str(input('- Account: '))
            for i in kho_cn:
                if tk == i[0]:
                    # tạo vòng lặp tìm kiếm đến khi tk trùng tài khoản trong kho cá nhân.
                    while True:
                        mk = str(input('- Password: '))
                        if mk ==  i[2] :
                            for q in kho_thong_tin:
                                # tạo vòng lặp tìm kiếm đến khi mật khẩu trùng với tài khoản đó thì dừng.
                                if i[1]==q[0]:
                                    (masv,hoten,sdt,ngaysinh,diachi) = q
                                    print(f'- Student ID: {masv}')
                                    print(f'- Full name: {hoten}')
                                    print(f'- Phone number: {sdt}')
                                    print(f'- Date of birth: {ngaysinh}')
                                    print(f'- Address: {diachi}')
                                    break
                            break

                        else:
                            print('- Incorrect password.')
                    break
                else:
                    print('- Account does not exist.')
            break
    elif num == '3' and num.isdigit(): # Chọn 3 để kết thúc chương trình.
        print('Good bye')
        break
    elif num == '4' and num.isdigit():
        # Chọn 4 để thay đổi  mật khẩu và thông tin cá nhân.
        while True:
            tk = str(input('- Account: '))
            for i in kho_cn:
                if tk == i[0]:
                    # Tìm tài khoản trong kho cá nhân đến khi tk == i[0] (với i[0] nằm trong kho cá nhân .
                    while True:
                        ma = int(input('Student ID: '))
                        if ma == i[1] :
                            # tạo vòng lặp nhập mã sinh viên.
                            (taikhoan, masv, mk) = i
                            print(taikhoan)
                            print(mk)
                            print(masv)
                            print('- Choose an option: \n1) Change password  \n2) Update informatio ')
                            while True:
                                # tạo vòng lặp chọn mục cần thay đổi.
                                doi = str(input('- Choose an option: '))
                                if doi == '1' and doi.isdigit():
                                    #  chọn mục 1 để thay đổi mật khẩu.
                                    doi_mk = input('- New password: ')
                                    if strong_pass(doi_mk):
                                        while True:
                                            doi_mk1 = input('- Re-enter password: ')
                                            if doi_mk1 == doi_mk:
                                                i[2]=doi_mk
                                                # Thay đổi  và lưu mật khẩu mới trong kho cá nhân .


                                                print('- Password has been changed.')
                                                break
                                            else:
                                                print('- Does not match.')
                                        break
                                elif doi == '2' and doi.isdigit():

                                        while True:
                                            print('- Select the item to change:: \n1) Change full name: \n2) Change phone number: \n3) - Change date of birth (dd/mm/yyy): \n4) Change address: \n5) Select the field to change ')
                                            td = int(input(' Select the item to change: '))
                                            for x in kho_thong_tin:

                                                if x[0] == i[1]:
                                                    if td == 1 :
                                                        ten = str(input('- Change full name: '))
                                                        x[1]=ten
                                                        print('- Updated successfully.')
                                                        print(kho_thong_tin)
                                                    elif td == 2 :
                                                        so = int(input('- Change phone number: '))
                                                        x[2]=so
                                                        print('- Updated successfully.')
                                                        print(kho_thong_tin)
                                                    elif td == 3 :
                                                        day = input('- Change date of birth (dd/mm/yyy): ')
                                                        x[3]=day
                                                        print('- Updated successfully.')
                                                        print(kho_thong_tin)
                                                    elif td == 4 :
                                                        add = str(input('- Change address: '))
                                                        x[4]=add
                                                        print('- Updated successfully.')
                                                        print(kho_thong_tin)
                                                    elif td == 5 :
                                                        print(kho_thong_tin)
                                                        break
                                                    else:
                                                        print('- This option does not exist.')
                                            break
                                        break
                                else:
                                    print('- This option does not exist.')
                            break
                        else:
                            print('- Incorrect student ID.')
                    break
                else:
                    print('- Account does not exist.')
            break



    else:
        print('- This option does not exist.')



























































