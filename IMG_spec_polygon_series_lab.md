# 이미지 제작 명세서 — 그릴 수 있는 등비급수 (v2.0)

## 1. 그림체와 고정 외형
캐릭터 팩 `CHAR_lab4.md` 18-3~18-5와 `fruitfly-lab-expressions` 기준 그림을 따른다. 고해상도 16비트 RPG 픽셀아트(기본 스킬 18-15-2 v1.19), 그림 안에 글자 없음.

## 2. 필요한 그림 전체

| 순서 | 키 | 종류 | 상태 | 출처 |
|---|---|---|---|---|
| 1 | cover_01 | 표지 16:9 (하루·시아 문답 + 식구들) | 받음 2026-11-27 → `img/cover_01.webp` 1600×900, 194 KB | `COVER_PROMPTS_polygon_series_lab.md` 1 |
| 2 | sc_01_aic | AI 판단 코너 장면 3:2 | 받음 → `img/sc_01_aic.webp` 1200×800, 152 KB | 같은 파일 2 |
| 3 | sc_01_outro | 아웃트로 장면 3:2 (초파리 승) | 받음 → `img/sc_01_outro.webp` 1200×800, 163 KB | 같은 파일 3 |
| — | og_cover · thumb_01 | 공유 미리보기 1200×630 · 목차 썸네일 600×400 | cover_01에서 잘라 만듦 | `img/og_cover.webp` |
| — | 표정 그림 | doc_front·doc_think·doc_judge·doc_magic, asst_smile·asst_shock·asst_spark·asst_report·asst_proud, sia_smile·sia_think·sia_guide·sia_explain·sia_signal, fly_magnify·fly_point·fly_arms·fly_coffee, robo_coin·robo_calc·robo_happy·robo_sigh, moa_sparkle·moa_ok·moa_cheer, x1_hint·x2_hint·x3_hint | 캐릭터 팩 재사용 | `build/sprites96.js` |

도형·차트는 모두 페이지 코드(Canvas 2D)가 그린다. 원자료(matharium 인포그래픽)의 그림은 쓰지 않는다.

## 3. 대결·아웃트로 표정 점검
대결 결과 F(초파리 승): 초파리 `fly_arms`, 주판봇 `robo_sigh`, 심판 시아 `sia_signal`, 박사 `doc_judge`. 아웃트로는 박사 `doc_magic` → 초파리 → 주판봇 → 시아·하루 문답 → 모아 → X3 순서(이긴 쪽 먼저). 장면 그림 sc_01_outro도 초파리가 앞, 주판봇이 머쓱한 표정.

## 4. 넘겨받은 뒤 처리
1. 받은 그림을 `grid_k`로 점검해 큰 네모 블록 그림이면 다시 받기를 권한다.
2. 표지는 LANCZOS 1600×900 WebP(220 KB 이하), 장면은 1200×800 WebP(180 KB 이하)로 `img/`에 넣는다.
3. `build/p0.src.html`의 그림판 표지(`<canvas id="coverCv">`와 `.cast4`)를 `<picture>`로 바꾸고, 장면 두 장은 `#aic`·`#outro` 대화 위에 넣는다. `image-rendering:pixelated`는 직접 쓰지 않는다(px-fix v1이 맡음).
4. `og_cover.webp`를 cover_01에서 1200×630으로 잘라 교체하고, `cover_manifest.json`의 `status`를 `ok`로 고친 뒤 `node build/build.js`.

## 5. 받은 그림 점검 (2026-11-27)
세 장 모두 `grid_k = 0`(큰 블록 그림 아님), 고해상도 픽셀아트로 확인. 남은 작은 차이: sc_01_aic의 시아 카드에 알아볼 수 없는 글자 모양이 조금 들어감, sc_01_outro의 주판봇 표정이 머쓱함보다 웃는 얼굴에 가까움. 페이지 사용에는 지장 없어 그대로 둠.
