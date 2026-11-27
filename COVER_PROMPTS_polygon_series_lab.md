# 그림 지시문 — 그릴 수 있는 등비급수 (v2.0)

연구실 스킬 v1.19 기준입니다. 그림체는 **고해상도 16비트 RPG 픽셀아트**(가로 1600 이상에서 직접 그린 촘촘한 픽셀)이고, "작은 격자로 그린 뒤 확대"는 쓰지 않습니다. 낮의 연구실(흰 벽)입니다. 받은 그림은 LANCZOS로 줄여 WebP로 넣고, 페이지의 px-fix v1이 화면 배율에 맞춰 그립니다.

**참고 이미지 (매번 함께 올리기):** GitHub `adminmrobo/fruitfly-lab-expressions`의 박사·조수·초파리 연구원·주판봇·인턴 시아·인턴 모아 기본 표정(E13), 미공개 X1~X3 기본 그림(X?_e13). 표지를 먼저 받아 그림체를 확인한 뒤, 장면 두 장에는 받은 표지도 참고 그림으로 함께 올립니다.

만드는 순서: ① cover_01 → ② sc_01_aic → ③ sc_01_outro

---

## 1. 표지 — `cover_01`

| 항목 | 내용 |
|---|---|
| 키 · 비율 | cover_01 · 16:9 (가로 1920 이상으로 받기) → 1600×900 WebP, 220 KB 이하 |
| 그림체 | 16비트 RPG풍 픽셀아트, 고해상도 촘촘한 픽셀 (필수) |
| 넣을 곳 | 페이지 맨 위 표지 자리(`data-img="cover_01"`), og:image도 이 그림에서 잘라 교체 |
| 대체 글 (alt) | 흰 보드 위 정칠각형 안으로 감겨 드는 테라코타색 나선 앞에서 조수 하루와 인턴 시아가 묻고 답하고, 연구실 식구들이 둘러싼 장면 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지에 넣을 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (가로 1600 이상에서 그린 작고 촘촘한 픽셀로 세밀하게 — 작은 그림을 확대한 큰 네모 블록 금지, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 캐릭터(박사, 조수 하루, 인턴 시아, 초파리 연구원, 주판봇, 인턴 모아, 방청석 X1~X3)를 같은 외형으로, 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것 (보드·종이·화면도 글자 없이 도형과 선만)
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (each art pixel about 2 screen pixels at 1600 px width — NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a bright daytime laboratory with a large white easel board in the center.
Characters:
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, standing left of the board facing right, pointing at the spiral with one hand and holding a clipboard, explaining;
  calm girl maid intern, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron, standing right of the board facing left toward the girl researcher, hands politely together, asking a question with a curious look;
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, small, at the center back behind the board, presenting the outer corner of the heptagon with an open palm;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, at the far left facing right, examining the center of the spiral with a magnifying glass, doubtful look;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, at the far right facing left, confident, raising the abacus;
  gentle girl maid intern, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt, small in the right background, hugging a blank rolled poster, cheering;
  three small cute solid dark navy-black silhouettes with a thin purple rim light, two round white dot eyes and pink blush pixels each, one colored accessory only each (pink ribbon / teal glasses glint / yellow bell), not scary, tiny in the bottom-right foreground as an audience, one holding up a blank hint card.
Visual metaphor of the topic: on the white board, a large regular heptagon with smaller heptagons nested inside, each slightly rotated; one corner triangle of each layer is painted terracotta, forming a spiral that winds inward toward the center.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the spiral and the two talking girls.
Mood: curious, friendly question-and-answer, the moment of discovery.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same characters, same high-resolution 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art with small dense pixels, still no text.`

---

## 2. AI 판단 코너 장면 — `sc_01_aic`

| 항목 | 내용 |
|---|---|
| 키 · 비율 | sc_01_aic · 3:2 (가로 1536 이상으로 받기) → 1200×800 WebP, 180 KB 이하 |
| 그림체 | 16비트 RPG풍 픽셀아트, 고해상도 촘촘한 픽셀 (필수) |
| 넣을 곳 | AI 판단 코너 머리(`#aic`), 대화 위 |
| 대체 글 (alt) | 주판봇이 AI 보고서를 그대로 내려 하자 박사가 멈추게 하고, 하루와 시아가 수상한 막대를 가리키며 확인하는 장면 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지에 넣을 그림 1장을 만들어 줘.
- 비율 3:2, 가로 1536px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (가로 1600 이상에서 그린 작고 촘촘한 픽셀로 세밀하게 — 작은 그림을 확대한 큰 네모 블록 금지, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 캐릭터(박사, 조수 하루, 인턴 시아, 주판봇, 방청석 X2)를 같은 외형으로, 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것 (보드·종이·화면도 글자 없이 도형과 선만)
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website scene illustration, 3:2 landscape.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (each art pixel about 2 screen pixels at 1600 px width — NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a bright daytime laboratory desk with a large blank monitor showing only a simple rising line chart with no labels.
Characters:
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the left facing right, proudly holding up the long printed report, eager to submit it;
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, in the center, raising one hand gently as if saying "wait", thoughtful look;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, on the right facing left, leaning in and pointing at the suspicious tall bar;
  calm girl maid intern, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron, next to the girl researcher, holding a small blank card labeled only with a ruler icon, checking calmly;
  three small cute solid dark navy-black silhouettes with a thin purple rim light, two round white dot eyes and pink blush pixels each, one colored accessory only each (pink ribbon / teal glasses glint / yellow bell), not scary, only the one with teal glasses glint, tiny at the bottom, quietly offering a blank card.
Visual metaphor of the topic: a long printed report sheet (blank lines only, no letters) flowing out of the monitor; one bar on the chart is suspiciously tall.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the suspicious tall bar and the report.
Mood: careful checking, gentle doubt, friendly.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same characters, same high-resolution 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art with small dense pixels, still no text.`

---

## 3. 아웃트로 장면 — `sc_01_outro`

| 항목 | 내용 |
|---|---|
| 키 · 비율 | sc_01_outro · 3:2 (가로 1536 이상으로 받기) → 1200×800 WebP, 180 KB 이하 |
| 그림체 | 16비트 RPG풍 픽셀아트, 고해상도 촘촘한 픽셀 (필수) |
| 넣을 곳 | 아웃트로(`#outro`) 대화 위 |
| 대체 글 (alt) | 삼각형 나선 포스터 앞에서 초파리 연구원이 이기고 주판봇이 머쓱해하며, 하루와 시아가 마무리하는 장면 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지에 넣을 그림 1장을 만들어 줘.
- 비율 3:2, 가로 1536px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (가로 1600 이상에서 그린 작고 촘촘한 픽셀로 세밀하게 — 작은 그림을 확대한 큰 네모 블록 금지, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 캐릭터(박사, 조수 하루, 인턴 시아, 초파리 연구원, 주판봇, 인턴 모아, 방청석 X1~X3)를 같은 외형으로, 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것 (보드·종이·화면도 글자 없이 도형과 선만)
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website scene illustration, 3:2 landscape.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (each art pixel about 2 screen pixels at 1600 px width — NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: the same bright daytime laboratory; a finished poster with a terracotta spiral inside a triangle hangs on the white wall.
Characters:
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, in the front left facing right, arms crossed, satisfied winner;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, in the front right facing left, sighing with a sheepish look, abacus lowered;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, in the middle, giving a thumbs up toward the poster;
  calm girl maid intern, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron, beside the girl researcher, raising a small blank signal flag as the referee;
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, behind them, smiling and gesturing to the poster;
  gentle girl maid intern, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt, pinning the poster to the wall, happy;
  three small cute solid dark navy-black silhouettes with a thin purple rim light, two round white dot eyes and pink blush pixels each, one colored accessory only each (pink ribbon / teal glasses glint / yellow bell), not scary, tiny at the bottom clapping, one with a yellow bell.
Visual metaphor of the topic: a small triangle with a terracotta inward spiral on the poster, clearly larger share painted than a faint dodecagon spiral sketch beside it.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the finished poster.
Mood: warm wrap-up, the result is clear, everyone learned something.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same characters, same high-resolution 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art with small dense pixels, still no text.`
