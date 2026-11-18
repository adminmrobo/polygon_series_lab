# 표지 지시문 — 그릴 수 있는 등비급수 (`cover_01`)

아직 받지 않았습니다. 그림을 받기 전까지 페이지는 코드로 그린 그림판 표지(정칠각형 나선 + 네 캐릭터)를 씁니다. 연구실 스킬 v1.14 "낮의 연구실"(흰 배경) 기준입니다. 그림을 받으면 ai-lab-explainer 18-15 절차로 `data-img="cover_01"` 자리에 넣고 `cover_manifest.json`의 `status`를 고칩니다.

**참고 이미지 (함께 올리기):** GitHub `adminmrobo/fruitfly-lab-expressions`의 박사·조수·초파리 연구원·주판봇 기본 표정(E13), 인턴 모아(E13).

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_01 · L (16:9, 1920 이상) → `img/cover_01.webp` 1600×900, `img/cover_01_960.webp` |
| 장소 (앵커) | 낮의 연구실, 큰 창과 흰 벽, 가운데에 이젤형 큰 흰 보드 |
| 주제 은유 | 보드 위의 큰 정칠각형 안에 작은 정칠각형이 끝없이 겹쳐 들어가고, 모서리 조각들이 테라코타색 나선으로 칠해짐 |
| 네 캐릭터 포즈 | 박사: 가운데 뒤에서 나선의 바깥 모서리를 손바닥으로 가리킴 / 조수: 오른쪽에서 클립보드를 들고 나선 안쪽을 들여다봄 / 초파리: 왼쪽에서 오른쪽을 보며 돋보기로 나선 가운데를 의심스럽게 살핌 / 주판봇: 오른쪽 끝에서 왼쪽을 보며 주판을 들고 자신만만 · 인턴 모아는 뒤쪽에 작게, 빈 포스터 종이를 안고 있음 |
| 대체 글 (alt) | 흰 보드 위 정칠각형 안으로 감겨 드는 테라코타색 나선을 연구실 식구들이 둘러싸고 보는 장면 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 캐릭터(박사, 조수, 초파리 연구원, 주판봇, 인턴 모아)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).
Bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a bright daytime laboratory with a large white easel board in the center.
All four characters together:
chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, standing at the center back and presenting the outer corner of the drawing with an open palm;
girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, standing at the right side holding a clipboard and peering into the center of the drawing;
anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, examining the center of the spiral with a magnifying glass, doubtful look;
boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, confident.
One small maid intern in the background: a gentle girl with long ash-beige wavy hair, white frilled maid headband, camel cardigan, hugging a blank rolled poster.
Visual metaphor of the topic: on the white board, a large regular heptagon with smaller heptagons nested inside, each one slightly rotated; one corner triangle of each layer is painted terracotta, forming a spiral that winds inward toward the center.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the spiral.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```
