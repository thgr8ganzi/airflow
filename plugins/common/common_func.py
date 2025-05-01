def get_sftp():
    print("sftp 작업 실행")

def regist(name, sex, *args):
    print(f"이름: {name}")
    print(f"성별: {sex}")
    print(f"기타: {args}")

def regist2(name, sex, *args, **kwargs):
    print(f"이름: {name}")
    print(f"성별: {sex}")
    print(f"기타: {args}")
    email = kwargs.get("email") or None
    phone = kwargs["phone"] or None
    if email:
        print(f"이메일: {email}")
    if phone:
        print(f"전화번호: {phone}")