# def lover(a):
#     return a.lover()
#
#
# def upper(a):
#     return a.upper()
#
#
# list_1 = "WeLLcoMe tO AmErICa!".split()
# print(list(map(lover, list_1)))
# print(list(map(upper, list_1)))

def up(s):
    return s.upper()


def lo(s):
    return s.lower()


l = "We all love PYTHON!".split()
print(list(map(lo, l)))
print(list(map(up, l)))