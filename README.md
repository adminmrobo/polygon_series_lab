# 그릴 수 있는 등비급수 — 정다각형 속 나선의 넓이

정다각형의 각 변의 중점을 이으면 안에 같은 모양의 작은 정다각형이 생깁니다. 이것을 끝없이 되풀이하며 모서리 조각을 칠한 나선 하나로 **등비수열 → 로그 눈금 → 등비급수 → 단위 읽기**를 차례로 보는 데이터시각화 연구실 해설입니다. 연구실 스킬 ai-lab-explainer v1.14("낮의 연구실", 흰 배경)와 비전공자판(ai-lab-explainer-plain)을 따릅니다. 박사·조수 하루·초파리 연구원·주판봇과 인턴 모아가 진행합니다.

- 사이트: https://adminmrobo.github.io/polygon_series_lab/
- 글 · 안상선 ((주)M-Robo 대표) · [저자 소개](https://adminmrobo.github.io/who_am_i/who_am_i.html)

| 칸 | 내용 | 시각화 포인트 |
|---|---|---|
| ① 중점 | 변의 중점을 이으면 넓이 r = cos²(π/n)배인 닮은꼴 | 버블 차트: 반지름이 아니라 넓이로 |
| ② 등비수열 | 넓이 1, r, r², … | 로그 눈금이면 곧은 직선 |
| ③ 등비급수 | 부분합이 1/(1 − r)에 멈춤, 99% 도달 조각 수 | 누적 그래프 + 끝값 점선 + 기준선 |
| ④ 단위 | S는 "첫 조각 = 1" 단위, 실제 넓이는 언제나 도형의 **1/n** | 이중 축 대신 두 차트로 |
| 대결 | 포스터를 가장 많이 칠하려면 몇 각형? → 초파리 승 (F) | 축 제목 읽기 |

## 원자료와 검산

- 바탕: matharium 인포그래픽 「A regular polygon is a geometric series you can draw」(사용자 제공 이미지, 원 게시물 주소·게시일 미확인). 원본 그림은 저장소에 넣지 않았고, 도형과 차트는 모두 새로 그렸습니다.
- 원자료의 r·S 예시 네 가지(삼각형 1/4·4/3, 정사각형 1/2·2, 정오각형 (3 + √5)/8·≈2.89, 정육각형 3/4·4)는 검산해 맞습니다.
- 고친 곳 두 가지: "꼭짓점을 잇는다" → "변의 중점을 잇는다", "색칠한 넓이 = 1/(1 − cos²(π/n))" → "첫 조각을 1로 둔 크기 S". 실제 넓이 = 도형의 1/n은 이 페이지에서 더한 결론입니다.
- 검산: `python3 code/check_numbers.py` (도형을 실제로 100단계 쪼개 넓이를 잼)

## 폴더

```
.
├─ index.html                 완성 페이지 (build/에서 만듦, 외부 요청은 글꼴 하나)
├─ build/
│  ├─ p0.src.html             페이지 원본
│  ├─ common.css · common.js  공용 디자인·모듈 (optimization_3d_map과 같은 판)
│  ├─ kgx.js · backbone.json  지식 색인·꾸러미 모듈과 영역 뼈대
│  ├─ sprites96.js            캐릭터 팩에서 고른 표정 그림
│  ├─ kg_defs.py              지식 그래프·참고문헌·페이지 서지 → kg_0 / refs_0 / meta_0.json
│  └─ build.js                조립: node build/build.js
├─ code/check_numbers.py      수치 검산
├─ COVER_PROMPTS_polygon_series_lab.md   표지 Genspark 지시문 (아직 받지 않음)
├─ IMG_spec_polygon_series_lab.md        이미지 제작 명세서
└─ cover_manifest.json                   표지 현황판 연결
```

다시 만들기: `python3 build/kg_defs.py && node build/build.js`

캐릭터 이름·설정·그림은 저작권자 안상선의 허락 없이 사용할 수 없습니다.
