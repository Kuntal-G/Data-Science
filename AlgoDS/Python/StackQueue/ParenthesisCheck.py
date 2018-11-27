#Checking Parenthesis

def checkParenthesis(str):

    count=0

    for ch in str:

        if ch ==')':
            count-=1
        elif ch=='(':
            count+=1

    if count<0:
        return 'opening bracket missing'
    return count==0


str='()()(())'

print(checkParenthesis(str))

#Using Stack


def checkParenthesis2(str):

    mapping=dict(zip('({[',')}]'))
    print(mapping)
    st=[]

    for ch in str:
        if ch in  mapping:
            st.append(mapping[ch])
        elif ch not in mapping.values():
            raise ValueError('Proper parenthesis not found')
        elif not (st and ch==st.pop()):
            return False

    return not st


str='{}[]{[]}'

print(checkParenthesis2(str))
