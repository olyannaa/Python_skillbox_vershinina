
#task4
def frequency(s):
    dict={}
    for a in s:
        a=a.lower()
        if a>='a' and a<='z':
            if dict.get(a)==None:dict[a]=1
            else:dict[a]=dict[a]+1
    return dict

def make_pal(s):
    d=frequency(s)
    left=""
    right=""
    codd=0
    for (a,b) in d.items():
        if b%2==1:
            if codd !=0:return "NO"
            else:
                mid=a*b
                codd=1
        else:
            left=left+a*(b//2)
            right=a*(b//2)+right
    return left+mid+right

