def solution(new_id):
    new_id=new_id.lower()
    new_id=list(new_id)
    for i in range(len(new_id)):
        if not (97<= ord(new_id[i]) <=122 or 48<= ord(new_id[i]) <=57 or ord(new_id[i])==45 or ord(new_id[i])==46 or ord(new_id[i])==95):
             new_id[i]=' '
    new_id=' '.join(new_id).split()

    for i in range(1,len(new_id)):
        if new_id[i-1] == new_id[i] == '.':
                new_id[i-1] = ' '
                continue
    new_id=' '.join(new_id).split()
    if new_id and new_id[-1]=='.':
        new_id.pop(-1)
    if new_id and new_id[0]=='.':
        new_id.pop(0)
    if not new_id:
        new_id.append('a')
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1]=='.':
            del new_id[-1]
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id.append(new_id[-1])
    return ''.join(new_id)