"""정다각형 속 등비급수 — 페이지 숫자 검산 (python3 code/check_numbers.py)"""
import math
def poly(n, R=1.0, rot=0.0):
    return [(R*math.cos(rot+2*math.pi*k/n), R*math.sin(rot+2*math.pi*k/n)) for k in range(n)]
def area(P):
    return abs(sum(P[i][0]*P[(i+1)%len(P)][1]-P[(i+1)%len(P)][0]*P[i][1] for i in range(len(P))))/2
def mids(P):
    n=len(P); return [((P[i][0]+P[(i+1)%n][0])/2,(P[i][1]+P[(i+1)%n][1])/2) for i in range(n)]
def tri(a,b,c): return area([a,b,c])
print(f"{'n':>3} {'r=cos²':>8} {'면적비(실측)':>12} {'S=1/(1-r)':>10} {'첫조각/A':>9} {'나선/A(실측100단계)':>18} {'1/n':>7} {'99%단계':>7}")
for n in [3,4,5,6,7,8,10,12]:
    P=poly(n); A=area(P); r=math.cos(math.pi/n)**2
    Q=mids(P); ratio=area(Q)/A
    tot=0; cur=P; first=None
    for k in range(100):
        nx=mids(cur); t=tri(nx[-1],cur[0],nx[0])  # 꼭짓점 cur[0]의 모서리 삼각형
        if first is None: first=t
        tot+=t; cur=nx
    S=1/(1-r); k99=math.ceil(math.log(0.01)/math.log(r))
    print(f"{n:>3} {r:>8.4f} {ratio:>12.4f} {S:>10.4f} {first/A:>9.4f} {tot/A:>18.4f} {1/n:>7.4f} {k99:>7}")
# 원자료 식 확인
print("오각형 r=(3+√5)/8 =", (3+5**.5)/8, " cos²(36°)=", math.cos(math.pi/5)**2, " S=8/(5-√5)=", 8/(5-5**.5))
for n,k in [(4,3),(6,3),(3,3)]:
    r=math.cos(math.pi/n)**2; print(f"n={n} 부분합 S_{k} =", sum(r**i for i in range(k+1)))
