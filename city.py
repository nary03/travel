def recommend_places(destination):
    recommendations = {
        "서울": ["경복궁", "명동", "남산타워", "인사동", "한강"],
        "부산": ["해운대", "광안리", "태종대", "감천문화마을", "자갈치 시장"],
        "제주도": ["한라산", "성산 일출봉", "섭지코지", "우도", "협재 해수욕장"],
        "경주": ["불국사", "석굴암", "첨성대", "경주월드", "안압지"],
        "인천": ["월미도", "차이나타운", "송도 센트럴파크", "인천대교", "연안부두"]
    }
    
    return recommendations.get(destination, "해당 관광지에 대한 정보가 없습니다. 다른 관광지를 입력해 주세요.")

# 사용자 입력
destination = input("관광지를 입력하세요: ")
places_to_visit = recommend_places(destination)

# 추천 결과 출력
if isinstance(places_to_visit, list):
    print(f"{destination}에서 가볼 만한 곳:")
    for place in places_to_visit:
        print(f"- {place}")
else:
    print(places_to_visit)
