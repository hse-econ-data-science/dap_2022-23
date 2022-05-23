s = input()
if not(s.find('f') == -1):
    if s.find('f') == s.rfind('f'):
        print(s.find('f'))
    else:
        print(s.find('f'), end=' ')
        print(s.rfind('f'))
