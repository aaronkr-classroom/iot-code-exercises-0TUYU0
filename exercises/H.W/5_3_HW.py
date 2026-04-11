# 5_3_HW

class SayDays:
    def __init__(self, year, month, day):
        self.y = year
        self.m = month
        self.d = day
        # 해당 연도가 윤년인지 판단
        self.is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        # 월별 일수 리스트
        self.month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap:
            self.month_days[2] = 29

    def days(self):
        """1월 1일부터 입력된 날짜까지 며칠째인지 계산"""
        total = sum(self.month_days[:self.m]) + self.d
        return total

    def days_left(self):
        """12월 31일 기준으로 남은 일수 계산"""
        year_total = 366 if self.is_leap else 365
        return year_total - self.days()

    def week(self):
        """Zeller의 공식을 이용한 요일 숫자 (0:토, 1:일, ... 6:금)"""
        y, m, d = self.y, self.m, self.d
        # Zeller 공식: 1월, 2월 = 전년도 13월, 14월
        if m < 3:
            m += 12
            y -= 1
        
        K = y % 100
        J = y // 100
        
        # 공식 계산
        h = (d + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
        return h

    def week_name(self):
        """숫자 요일을 한글로 변환"""
        names = ["토요일", "일요일", "월요일", "화요일", "수요일", "목요일", "금요일"]
        return names[self.week()]

while True:
    try:
        user_input = input("날짜를 입력하세요 (예: 2024 10 25, 종료: q): ")
        if user_input.lower() == 'q':
            break
            
        y, m, d = map(int, user_input.split())
        
        sd = SayDays(y, m, d)
        
        print(f"--- {y}년 {m}월 {d}일 정보 ---")
        print(f"1. 올해의 며칠째: {sd.days()}일")
        print(f"2. 올해 남은 일수: {sd.days_left()}일")
        print(f"3. 요일 숫자(0:토): {sd.week()}")
        print(f"4. 요일 이름: {sd.week_name()}")
        print("-" * 30)
        
    except ValueError:
        print("숫자 3개를 공백으로 구분하여 입력해주세요 (예: 2024 1 1).")
    except Exception as e:
        print(f"오류 발생: {e}")

