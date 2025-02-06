#!/bin/bash

# 실행 시간 기록
echo "===== 실행 시작: $(date) =====" >> log.txt

# analyze.py 실행 및 로그 저장
python analyze.py >> log.txt 2>&1

# 실행 완료 시간 기록
echo "===== 실행 완료: $(date) =====" >> log.txt
