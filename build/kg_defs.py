"""지식 그래프·참고문헌·페이지 서지 정의 → kg_0.json / refs_0.json / meta_0.json (python3 build/kg_defs.py)"""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
PAGE = "index"
def node(i, t, ko, en, anchor, df=None, level=1):
    n = {"id": i, "type": t, "label": {"ko": ko, "en": en}, "page": PAGE, "anchor": anchor, "level": level,
         "status": "known", "confidence": "high", "coverage": "explained", "family": "geometric-series",
         "domain": ["math", "data"], "match": []}
    if df: n["definition"] = {"ko": df}
    return n
N = [
 node("lab:concept/regular-polygon","Concept","정다각형","Regular polygon","#c1","변의 길이와 각의 크기가 모두 같은 다각형."),
 node("lab:concept/midpoint-polygon","Concept","중점 다각형","Midpoint polygon","#c1","각 변의 중점을 이어 만든 안쪽 다각형. 정다각형이면 같은 모양이 된다."),
 node("lab:concept/similarity-area-ratio","Concept","닮음의 넓이비","Area ratio of similar figures","#c1","닮은 도형의 넓이비는 길이비의 제곱."),
 node("lab:concept/geometric-sequence","Concept","등비수열","Geometric sequence","#c2","앞의 수에 늘 같은 공비를 곱해 만든 수의 줄."),
 node("lab:concept/common-ratio","Concept","공비 r = cos²(π/n)","Common ratio","#c2","한 단계마다 넓이에 곱해지는 비율."),
 node("lab:concept/log-scale","Concept","로그 눈금","Logarithmic scale","#c2","10배마다 같은 간격인 축. 같은 비율의 변화가 직선으로 보인다."),
 node("lab:concept/partial-sum","Concept","부분합","Partial sum","#c3","처음부터 k번째까지 더한 값."),
 node("lab:concept/geometric-series","Concept","등비급수","Geometric series","#c3","등비수열을 끝없이 더한 것. |r| < 1이면 1/(1 − r)로 수렴한다."),
 node("lab:concept/convergence","Concept","수렴과 점근선","Convergence and asymptote","#c3","부분합이 끝값에 한없이 다가가는 것. 차트에서는 끝값 점선."),
 node("lab:concept/unit-of-measure","Concept","단위 (무엇을 1로 두었나)","Unit of measure","#c4","같은 양도 기준을 무엇으로 두느냐에 따라 숫자가 달라진다."),
 node("lab:concept/dual-axis","Concept","이중 축","Dual axis chart","#c4","한 차트에 서로 다른 단위의 축 두 개를 두는 방식. 오해를 부르기 쉽다."),
 node("lab:claim/spiral-one-over-n","Claim","나선의 넓이 = 도형의 1/n","Spiral area equals 1/n of the polygon","#c4","첫 조각 A(1 − r)/n에 1/(1 − r)을 곱하면 A/n.",2),
 node("lab:claim/source-fix-midpoint","Claim","원자료 정정: 꼭짓점 → 변의 중점","Correction: midpoints, not vertices","#fix"),
 node("lab:claim/source-fix-unit","Claim","원자료 정정: S는 첫 조각 단위","Correction: S is in units of the first piece","#fix"),
 node("lab:analogy/photocopy","Analogy","축소 복사 (A4 → A5)","Reduced photocopy","#c1"),
 node("lab:analogy/cake-halves","Analogy","케이크 반씩 먹기","Eating half the cake each time","#c3"),
 node("lab:sim/ps-midpoint","Simulation","중점 잇기 실험","Midpoint construction","#c1"),
 node("lab:sim/ps-bars","Simulation","단계별 넓이 막대 (로그 눈금)","Area bars with log scale","#c2"),
 node("lab:sim/ps-partial","Simulation","나선과 부분합","Spiral and partial sums","#c3"),
 node("lab:sim/ps-units","Simulation","두 단위 차트","Two-unit charts","#c4"),
 node("lab:sim/ps-duel","Simulation","대결: 몇 각형이 가장 많이 칠할까","Duel: which polygon fills most","#duel"),
 node("lab:concept/ai-output-check","Concept","AI 결과 확인 질문 (단위·가정·상식)","Checking AI output","#aic","AI가 낸 결과를 받으면 단위, 가정, 상식에 맞는지를 묻는다."),
 node("lab:sim/ps-aic","Simulation","AI 판단 코너: AI 보고 문장 점검","AI judgment corner","#aic"),
 node("lab:sim/ps-practice","Simulation","연습: 정팔각형으로 직접 계산","Practice with an octagon","#practice"),
 node("lab:limitation/ideal-infinite","Limitation","이상적 도형·무한 단계 가정","Ideal polygon and infinite steps","#c4"),
 node("lab:question/non-regular","Question","정다각형이 아니면 중점 다각형은 어떻게 될까?","What happens for non-regular polygons?","#sum"),
 node("lab:work/matharium_polygon_series","Work","matharium: A regular polygon is a geometric series you can draw","matharium infographic","#top"),
]
for c in ["c1","c2","c3","c4","duel"]:
    k = 1 if c=="duel" else 2
    for i in range(1,k+1):
        N.append(node(f"lab:quiz/ps-{c}-{i}","QuizItem",f"{c} 문제 {i}",f"Quiz {c}-{i}",f"#{c}"))
def e(s,p,o,a): return {"s":s,"p":p,"o":o,"anchor":a,"confidence":"high"}
E = [
 e("lab:concept/midpoint-polygon","lab:partOf","lab:concept/regular-polygon","#c1"),
 e("lab:concept/similarity-area-ratio","lab:prerequisiteOf","lab:concept/common-ratio","#c1"),
 e("lab:concept/common-ratio","lab:partOf","lab:concept/geometric-sequence","#c2"),
 e("lab:concept/geometric-sequence","lab:prerequisiteOf","lab:concept/geometric-series","#c3"),
 e("lab:concept/partial-sum","lab:partOf","lab:concept/geometric-series","#c3"),
 e("lab:concept/convergence","lab:relatedTo","lab:concept/geometric-series","#c3"),
 e("lab:concept/log-scale","lab:relatedTo","lab:concept/geometric-sequence","#c2"),
 e("lab:concept/unit-of-measure","lab:relatedTo","lab:concept/dual-axis","#c4"),
 e("lab:claim/spiral-one-over-n","lab:relatedTo","lab:concept/geometric-series","#c4"),
 e("lab:claim/spiral-one-over-n","lab:relatedTo","lab:concept/unit-of-measure","#c4"),
 e("lab:analogy/photocopy","lab:relatedTo","lab:concept/similarity-area-ratio","#c1"),
 e("lab:analogy/cake-halves","lab:relatedTo","lab:concept/geometric-series","#c3"),
 e("lab:concept/midpoint-polygon","lab:demonstratedBy","lab:sim/ps-midpoint","#c1"),
 e("lab:concept/log-scale","lab:demonstratedBy","lab:sim/ps-bars","#c2"),
 e("lab:concept/partial-sum","lab:demonstratedBy","lab:sim/ps-partial","#c3"),
 e("lab:claim/spiral-one-over-n","lab:demonstratedBy","lab:sim/ps-units","#c4"),
 e("lab:concept/unit-of-measure","lab:demonstratedBy","lab:sim/ps-duel","#duel"),
 e("lab:claim/spiral-one-over-n","lab:hasLimitation","lab:limitation/ideal-infinite","#c4"),
 e("lab:limitation/ideal-infinite","lab:raises","lab:question/non-regular","#sum"),
 e("lab:claim/source-fix-midpoint","lab:relatedTo","lab:work/matharium_polygon_series","#fix"),
 e("lab:claim/source-fix-unit","lab:relatedTo","lab:work/matharium_polygon_series","#fix"),
 e("lab:concept/geometric-series","lab:broader","lab:topic/series-convergence","#c3"),
 e("lab:concept/geometric-sequence","lab:broader","lab:topic/sequences-limits","#c2"),
 e("lab:concept/log-scale","lab:broader","lab:topic/chart-selection","#c2"),
 e("lab:concept/dual-axis","lab:broader","lab:topic/chart-selection","#c4"),
 e("lab:concept/unit-of-measure","lab:broader","lab:area/data-visualization","#c4"),
 e("lab:concept/ai-output-check","lab:relatedTo","lab:concept/unit-of-measure","#aic"),
 e("lab:concept/ai-output-check","lab:demonstratedBy","lab:sim/ps-aic","#aic"),
 e("lab:sim/ps-practice","lab:assesses","lab:claim/spiral-one-over-n","#practice"),
]
quiz_target = {"c1":"lab:concept/common-ratio","c2":"lab:concept/log-scale","c3":"lab:concept/geometric-series","c4":"lab:concept/unit-of-measure","duel":"lab:concept/unit-of-measure"}
for n in N:
    if n["type"]=="QuizItem":
        c = n["anchor"][1:]; E.append(e(n["id"],"lab:assesses",quiz_target[c],n["anchor"]))
json.dump({"version":"1.3","page":PAGE,"nodes":N,"edges":E}, open(os.path.join(D,"kg_0.json"),"w"), ensure_ascii=False, indent=1)
refs = [{"id":"matharium_polygon_series","type":"graphic","title":"A regular polygon is a geometric series you can draw",
  "author":[{"literal":"matharium"}],"accessed":{"date-parts":[[2026,11,18]]},
  "lab":{"work":"lab:work/matharium_polygon_series","role":"background",
   "supports":["lab:concept/common-ratio","lab:concept/geometric-series"],"locs":[],
   "verified":{"title":True,"author":True,"year":False,"url":False},
   "checkedBy":"사용자 제공 이미지에서 옮김. 원 게시물 주소·게시일은 받지 못함. 수식은 페이지에서 검산",
   "note":"r·S 예시 네 가지 검산 일치. '꼭짓점을 잇는다'와 넓이 단위 표기는 이 페이지에서 고침. 그림은 새로 그림"}}]
json.dump(refs, open(os.path.join(D,"refs_0.json"),"w"), ensure_ascii=False, indent=1)
meta = {"title":"그릴 수 있는 등비급수 — 정다각형 속 나선의 넓이","series":"데이터시각화 연구실","number":"1",
 "creator":[{"name":"안상선","role":"author","affiliation":"(주)M-Robo"}],
 "contributor":[{"name":"AI 보조 제작","role":"assistant"}],
 "date":"2026-11-27","version":"2.1","language":["ko"],"license":"",
 "url":"https://adminmrobo.github.io/polygon_series_lab/",
 "about":["lab:concept/geometric-series","lab:concept/log-scale","lab:concept/unit-of-measure"],
 "basedOn":["matharium_polygon_series"],"educationalLevel":"입문","learningResourceType":"interactive explainer",
 "registry":"KG_00_registry 0.2",
 "suggestedCitation":"안상선 (2026). 그릴 수 있는 등비급수 — 정다각형 속 나선의 넓이. 데이터시각화 연구실 1, v2.1."}
json.dump(meta, open(os.path.join(D,"meta_0.json"),"w"), ensure_ascii=False, indent=1)
print(len(N),"nodes",len(E),"edges")
