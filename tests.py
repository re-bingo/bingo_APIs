from core.users import code2session, WeChatUser

code = "003Y2Fkl20Lx394ivSnl22dqFi1Y2FkI"


def test_code2session():
    print(f"\n{code2session(code)}")


def test_user():
    print(f"\n{WeChatUser(code).errmsg}")
