Wine Analysis Project
이 프로젝트는 Scikit-learn의 Wine 데이터셋을 사용하여 데이터 분석 및 시각화를 수행하는 데 중점을 둡니다. Python을 활용해 데이터를 분석하고, 그 결과를 GitHub에 업로드하여 버전 관리를 자동화합니다.

wine_analysis_project/
│
├── analyze.py             # 데이터셋 분석 스크립트
├── run_analysis.sh        # 분석 스크립트를 실행하고 로그 저장
├── upload_to_github.sh    # GitHub 자동 업로드 스크립트
├── environment.yml        # Conda 환경 설정 파일
├── output.txt             # 분석 결과 출력 파일
└── log.txt                # 분석 실행 로그 파일


analyze.py
Scikit-learn의 Wine 데이터셋을 불러와 데이터의 통계적 정보를 계산합니다.
데이터셋의 평균(mean), 표준편차(std) 등을 계산하고 **특정 특성(alcohol)**의 최대/최소값을 구합니다.
결과를 output.txt로 저장합니다.

run_analysis.sh
analyze.py를 실행하고 **실행 로그(log.txt)**를 기록합니다.

upload_to_github.sh
변경된 파일을 자동으로 GitHub에 커밋하고 푸시합니다.
현재 디렉토리의 모든 변경 사항을 포함합니다.

environment.yml
프로젝트에서 사용된 모든 패키지를 포함한 Conda 환경 설정 파일입니다.
다른 시스템에서도 동일한 환경을 쉽게 재현할 수 있습니다.

설치 및 실행 방법

1단계: Conda 환경 생성
conda env create -f wine_analysis_project/environment.yml
conda activate wine_analysis_env

2단계: 분석 실행
cd wine_analysis_project
./run_analysis.sh

3단계: GitHub 업로드
cd wine_analysis_project
./upload_to_github.sh

결과 확인
output.txt: 분석 결과가 저장된 파일입니다.
log.txt: 실행 중 발생한 로그 정보를 확인할 수 있습니다.

주요 패키지
numpy
pandas
scikit-learn