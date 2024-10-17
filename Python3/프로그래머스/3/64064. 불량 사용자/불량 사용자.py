total_count = set()
user_id_len = 0
banned_id_len = 0
chked_id = None
def solution(user_id, banned_id):
    global user_id_len
    global banned_id_len
    global chked_id
    
    user_id_len = len(user_id)
    banned_id_len = len(banned_id)
    chked_id = [False for _ in range(user_id_len)]
    
    banned_chk_list = []
    for banned in banned_id:
        tmp = []
        for i, user in enumerate(user_id):
            if len(banned) != len(user): continue
            chkAlphabetChecker = sum([user[j] != banned[j] if banned[j] != '*' \
                                  else False for j in range(len(banned))])
            if chkAlphabetChecker == 0: tmp.append(i)
        banned_chk_list.append(tmp)
    dfs(banned_chk_list, 0)
    return len(total_count)

def dfs(banned_chk_list, D):
    global total_count, chked_id
    if D == banned_id_len:
        total_count.add(tuple(chked_id))
    else:
        for tempId in banned_chk_list[D]:
            if not chked_id[tempId]:
                chked_id[tempId] = True
                dfs(banned_chk_list, D + 1)
                chked_id[tempId] = False