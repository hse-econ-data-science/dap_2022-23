import os
from shutil import copyfile

def repl(s1):
    s2 = []
    for line in s1:
        if line.startswith('#'):
            continue
        if line.find('//') != -1:
            line = line[:line.find('//')]
        s2.append(line)
    syms = set('+-*/%^:;"\'<>!=[](){}&|.,?')
    prev = ''
    ans = []
    s = ''.join(s2).replace('\n', '')
    s = s.replace(' ', '')
    s = s.replace('\t', '')
    for c in s:
        if c not in syms and prev != '#':
            ans.append('#')
            prev = '#'
        elif c in syms:
            ans.append(c)
            prev = c
    return ''.join(ans)

def check(s1, s2):
    return repl(s1) == repl(s2)
    
dirs = os.listdir()
sols = {}
badass = {}
stop = 10**9
for ndir in range(len(dirs)):
    if stop <= 0:
        break

    if dirs[ndir] == 'cheat.py' or dirs[ndir] == 'log.txt' or dirs[ndir] == 'lex_cheat.py':
        continue
    tfiles = os.listdir(dirs[ndir])
    files = []
    for file in tfiles:
        if True:#file.find('OK') != -1:
            files.append(file)
        
    for pdir in range(ndir):
        if stop <= 0:
            break
        if dirs[pdir] == 'cheat.py' or dirs[pdir] == 'log.txt' or dirs[pdir] == 'lex_cheat.py':
            continue
        pfiles = sols[dirs[pdir]]
        for nfn in files:
            p1 = dirs[ndir] + '/' + nfn
            #print(p1)
            s1 = os.path.getsize(p1)
            for pfn in pfiles:
                if nfn[0] == pfn[0]:
                    p2 = dirs[pdir] + '/' + pfn
                    #print(p2)
                    s2 = os.path.getsize(p2)
                    fn = open(p1, 'r', encoding = 'utf8')
                    fp = open(p2, 'r', encoding = 'utf8')
                    st1 = fn.readlines()
                    st2 = fp.readlines()
                    fn.close()
                    fp.close()
                    if s1 == s2:
                        flag = False
                        if len(st1) == len(st2):
                            flag = True
                            for i in range(len(st1)):
                                if st1[i].strip() != st2[i].strip():
                                    flag = False
                            
                        if flag:
                            pair = dirs[ndir], dirs[pdir]
                            if pair not in badass:
                                badass[pair] = set()
                            badass[pair].add(pfn[0])
                            print('146%', dirs[ndir], dirs[pdir], pfn[0], sep = '\t')
                            stop -= 1
                    #if check(st1, st2):
                    #    print('prob', dirs[ndir], dirs[pdir], pfn[0], sep = '\t')
                    
                
    sols[dirs[ndir]] = files
    pass
pass
ans = []
for pair in badass:
    ans.append((badass[pair], pair))
ans.sort(reverse=True, key=lambda x: (len(x[0]), x[1]))
fout = open('log.txt', 'w', encoding='utf8')
for now in ans:
    print(now[1][0], now[1][1], len(now[0]), ''.join(sorted(now[0])), sep='\t', file=fout)
fout.close()