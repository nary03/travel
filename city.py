def calculate_final_score(midterm, final, performance):
    # 각 점수의 반영 비율
    midterm_weight = 0.30
    final_weight = 0.30
    performance_weight = 1.0
    
    # 최종 점수 계산
    final_score = (midterm * midterm_weight) + (final * final_weight) + (performance * performance_weight)
    return final_score

# 사용자 입력 받기
midterm_score = float(input("중간고사 성적을 입력하세요 (0-100): "))
final_score = float(input("기말고사 성적을 입력하세요 (0-100): "))
performance_score = float(input("수행평가 점수를 입력하세요 (0-100): "))

# 최종 점수 계산
final_score = calculate_final_score(midterm_score, final_score, performance_score)

# 결과 출력
print(f"100점 만점에 해당하는 최종 점수는: {final_score:.2f}점 입니다.")
