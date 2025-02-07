import pandas as pd
from sklearn.datasets import load_wine

# 1. 와인 데이터셋 로드
wine = load_wine()

# 2. DataFrame으로 변환
df = pd.DataFrame(data=wine.data, columns=wine.feature_names)

# 3. 분석 결과 저장할 리스트 생성
output = []

# 4. 데이터셋 크기 출력
num_rows, num_cols = df.shape
output.append(f"데이터셋 크기: {num_rows} 행, {num_cols} 열\n")

# 5. 각 특성(컬럼)의 평균(mean)과 표준편차(std) 계산하여 추가 (가독성 개선)
output.append("=" * 40)
output.append("각 특성(컬럼)의 평균 및 표준편차:\n")
output.append(df.describe().loc[['mean', 'std']].to_string())
output.append("=" * 40 + "\n")

# 6. 특정 특성('alcohol')의 최대값, 최소값 출력
alcohol_max = df['alcohol'].max()
alcohol_min = df['alcohol'].min()
output.append(f"'alcohol' 특성의 최대값: {alcohol_max}")
output.append(f"'alcohol' 특성의 최소값: {alcohol_min}\n")

# 7. 결과를 파일(output.txt)에 저장
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output))
