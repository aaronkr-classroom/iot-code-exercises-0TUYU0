# 4_P.33_2
for month in range(1, 12):
    if month == 2: n = 28
    elif month % 2 == 0:
        n = 30 if month < 8 else 31
    elif month % 2 == 1:
        n = 31 if month < 8 else 30

    count = 0
    print(f"<{month}월>")
        
    for day in range(1, n):
        if count == 7:
            count = 0
            print()
            
        if month == 8 and day == 15:
            print(f"\033[31m{month}월 {day}일(광복일)\033[0m  ", end = '')
        elif (month % 2 == 0 and day == 16) or (month % 2 == 1 and day == 15):
            print(f"\033[31m{month}월 {day}일(그  날)\033[0m  ", end = '')
        else:
            print(f"{month}월 {day}일(평  일)  ", end = '')
            
        count += 1
        
    print("\n")