def convert(t):
    if type(t) == str:
        minute = int(t.split(":")[0])
        sec = int(t.split(":")[1])
        return sec + minute * 60
    else:
        minute = t // 60
        sec = t % 60
        return f"{minute:02d}:{sec:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = convert(video_len)
    pos = convert(pos)
    op_start = convert(op_start)
    op_end = convert(op_end)
    
    # 위치 보정
    if op_start <= pos <= op_end:
        pos = op_end

    for c in commands:
        if c == 'next':
            pos = min(video_len, pos + 10)
        else: pos = max(0, pos - 10)
            # 위치 보정
        if op_start <= pos <= op_end:
            pos = op_end
            
    answer = convert(pos)
    return answer