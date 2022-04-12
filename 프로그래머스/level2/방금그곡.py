def solution(m, musicinfos):
    m=m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    answer = ('(None)', None)

    for info in musicinfos:
        l=info.split(',')
        start,end,name,code=l
        sh,sm,eh,em=map(int,start.split(':')+end.split(':'))
        time=(eh-sh)*60+(em-sm)
        code = code.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        melody_played = (code*time)[:time]
        if m in melody_played:
            if (answer[1] == None) or (time > answer[1]):
                answer = (name, time)

    return answer[0]