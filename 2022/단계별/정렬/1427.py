#소트인사이드
N = list(input()) # 굳이 int 형변환 필요 x => 나중에 join 쓰려면 문자열이어야 하므로
                # => python은 암시적 형변환을 해서 list 원소가 str형이어도 sort 가능
N.sort(reverse=True) # 내림차순 정렬
print(''.join(N))