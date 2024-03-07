import sys
N, name = sys.stdin.readline().split()
chat = {}
for _ in range(int(N)):
    nick, chatting = sys.stdin.readline().split()
    if nick == name:
        if chatting in chat: print(chat[chatting])
        else: print(0)
        break
    else:
        if chatting in chat: chat[chatting] += 1
        else: chat[chatting] = 1