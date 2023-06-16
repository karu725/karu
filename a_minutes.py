# 초 단위 -> 분 단위 계산 프로그램

def calculate_hours_minutes_seconds(total_seconds):
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return hours, minutes, seconds

# 초 단위를 입력하세요.
total_seconds = 26280

hours, minutes, seconds = calculate_hours_minutes_seconds(total_seconds)
print(f"{total_seconds}초는 {hours}시간 {minutes}분 {seconds}초입니다.")