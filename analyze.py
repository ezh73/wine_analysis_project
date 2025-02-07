import pandas as pd
from sklearn.datasets import load_wine

# 1. 와인 데이터셋 로드 및 DataFrame 변환
df = pd.DataFrame(data=load_wine().data, columns=load_wine().feature_names)

# 2. 데이터 분석 결과를 파일로 저장
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(f"데이터셋 크기: {df.shape[0]} 행, {df.shape[1]} 열\n")
    f.write("=" * 40 + "\n")
    f.write("각 특성(컬럼)의 평균 및 표준편차:\n")
    f.write(df.describe().loc[['mean', 'std']].to_string() + "\n")
    f.write("=" * 40 + "\n")
    f.write(f"'alcohol' 특성의 최대값: {df['alcohol'].max()}\n")
    f.write(f"'alcohol' 특성의 최소값: {df['alcohol'].min()}\n")
