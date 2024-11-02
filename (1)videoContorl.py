# 문제 설명
# 당신은 동영상 재생기를 만들고 있습니다. 당신의 동영상 재생기는 10초 전으로 이동, 10초 후로 이동, 오프닝 건너뛰기 3가지 기능을 지원합니다. 각 기능이 수행하는 작업은 다음과 같습니다.

# 10초 전으로 이동: 사용자가 "prev" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 전으로 이동합니다. 현재 위치가 10초 미만인 경우 영상의 처음 위치로 이동합니다. 영상의 처음 위치는 0분 0초입니다.
# 10초 후로 이동: 사용자가 "next" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 후로 이동합니다. 동영상의 남은 시간이 10초 미만일 경우 영상의 마지막 위치로 이동합니다. 영상의 마지막 위치는 동영상의 길이와 같습니다.
# 오프닝 건너뛰기: 현재 재생 위치가 오프닝 구간(op_start ≤ 현재 재생 위치 ≤ op_end)인 경우 자동으로 오프닝이 끝나는 위치로 이동합니다.
# 동영상의 길이를 나타내는 문자열 video_len, 기능이 수행되기 직전의 재생위치를 나타내는 문자열 pos, 오프닝 시작 시각을 나타내는 문자열 op_start, 오프닝이 끝나는 시각을 나타내는 문자열 op_end, 사용자의 입력을 나타내는 1차원 문자열 배열 commands가 매개변수로 주어집니다. 이때 사용자의 입력이 모두 끝난 후 동영상의 위치를 "mm:ss" 형식으로 return 하도록 solution 함수를 완성해 주세요.

# 제한사항
# video_len의 길이 = pos의 길이 = op_start의 길이 = op_end의 길이 = 5
# video_len, pos, op_start, op_end는 "mm:ss" 형식으로 mm분 ss초를 나타냅니다.
# 0 ≤ mm ≤ 59
# 0 ≤ ss ≤ 59
# 분, 초가 한 자리일 경우 0을 붙여 두 자리로 나타냅니다.
# 비디오의 현재 위치 혹은 오프닝이 끝나는 시각이 동영상의 범위 밖인 경우는 주어지지 않습니다.
# 오프닝이 시작하는 시각은 항상 오프닝이 끝나는 시각보다 전입니다.
# 1 ≤ commands의 길이 ≤ 100
# commands의 원소는 "prev" 혹은 "next"입니다.
# "prev"는 10초 전으로 이동하는 명령입니다.
# "next"는 10초 후로 이동하는 명령입니다.






#추가 코멘트// 각 기능들(시간 정수로 변환, 최종 결과 출력 등)을 함수로 만들어서 작업했으면 훨 깔끔했을 듯. 습관 들여야 함.
def solution(video_len, pos, op_start, op_end, commands):
    d_video = int(video_len[:2]) * 60 + int(video_len[-2:])
    d_pos = int(pos[:2]) * 60 + int(pos[-2:])
    d_start = int(op_start[:2]) * 60 + int(op_start[-2:])
    d_end = int(op_end[:2]) * 60 + int(op_end[-2:])
    #여기서는 map함수와 split함수를 사용하면 쉽게 할 수 있었음 min , sec = map(int,video_len.split(":")) -> min*60+sec 리턴하는 함수로 만들면 훌륭.
    #map(적용할 함수,들어오는 값)
    
    if (d_pos >=d_start) & (d_pos <= d_end):
            d_pos = d_end
    for com in commands:
        if com == "next":
            #{
            if (d_pos + 10) >= d_video:
                d_pos = d_video
            else :
                d_pos += 10
            #}여기서 min함수 썼으면 더 깔끔 했음 d_pos = min(d_video , d_pos+10)
        else :
            #{
            if (d_pos - 10) <= 0 :
                d_pos = 0
            else :
                d_pos -= 10
            #}마찬가지로 max함수 썼으면 깔끔
            
        if (d_pos >=d_start) & (d_pos <= d_end):
            d_pos = d_end
    
    #여기 {
    if d_pos//60 >= 10 :
        f_answer = str(d_pos//60)
    else : 
        if d_pos//60 > 0 :
            f_answer = "0" + str(d_pos//60)
        else :
            f_answer = "00"
    if d_pos%60 >= 10 :
        b_answer = str(d_pos%60)
    else : 
        if d_pos//60 > 0 :
            b_answer = "0" + str(d_pos%60)
        else :
            b_answer = "00"
    #}새로운 공부
    # minutes, seconds = divmod(seconds, 60) -> 어떤 값을 나눈 몫과 나머지를 모두 갖고 싶을 때 사용하는 몫 , 나머지 = divmod(피제수, 제수)함수 
    # f"{minutes:02d}:{seconds:02d}" 그냥 값의 크기에 따라 str을 만들어줄 필요 없이 포멧 사용해서 정수 2자리 까지 나오도록 한 후 str으로 출력
        
    
    answer = f_answer + ":" + b_answer
    return answer
