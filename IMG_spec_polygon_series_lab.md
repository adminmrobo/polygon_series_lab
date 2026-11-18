# 이미지 제작 명세서 — 그릴 수 있는 등비급수

## 1. 그림체와 고정 외형
캐릭터 팩 `CHAR_lab4.md` 18-3~18-5와 `fruitfly-lab-expressions` 기준 그림을 따른다. 그림 안에 글자를 넣지 않는다.

## 2. 필요한 그림 전체

| 키 | 종류 | 상태 | 출처 |
|---|---|---|---|
| cover_01 | 글 표지 16:9 | 새로 그릴 것 | `COVER_PROMPTS_polygon_series_lab.md` |
| og 미리보기 | 공유 미리보기 | 표지에서 자를 것 | cover_01 → `img/cover_01_960.webp` |
| doc_front·doc_think·doc_judge·doc_magic | 표정 | 캐릭터 팩 재사용 | sprites96.js |
| asst_smile·asst_shock·asst_spark·asst_report·asst_proud | 표정 | 캐릭터 팩 재사용 | sprites96.js |
| fly_magnify·fly_point·fly_arms·fly_coffee | 표정 | 캐릭터 팩 재사용 | sprites96.js |
| robo_coin·robo_calc·robo_happy·robo_sigh | 표정 | 캐릭터 팩 재사용 | sprites96.js |
| moa_sparkle·moa_cheer, x1~x3_hint | 표정 | 캐릭터 팩 재사용 | sprites96.js |

도형·차트는 모두 페이지 코드(Canvas 2D)가 그린다. 원자료(matharium 인포그래픽)의 그림은 쓰지 않는다.

## 3. 아웃트로·대결 표정 점검
대결 결과 F(초파리 승): 초파리 `fly_arms`, 주판봇 `robo_sigh`, 박사 `doc_judge`, 아웃트로 박사 `doc_magic` → 초파리 → 주판봇 → 조수 `asst_proud` 순서(이긴 쪽 먼저).

## 4. 넘겨받은 뒤 처리
1600×900 WebP(`img/cover_01.webp`)와 960 폭 WebP를 만들고, `build/p0.src.html`의 그림판 표지(`<canvas id="coverCv">`와 `.cast4`)를 `<picture>`로 바꾼 뒤 `node build/build.js`로 다시 만든다.
