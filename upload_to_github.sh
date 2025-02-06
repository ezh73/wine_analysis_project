#!/bin/bash

# GitHub 리포지토리 URL (자신의 리포지토리 URL로 변경)
REPO_URL=https://github.com/ezh73/wine_analysis_project.git

# Git 사용자 설정 (이메일 및 이름이 설정되어 있지 않으면 오류가 발생할 수 있습니다)
git config --global user.name "ezh73"
git config --global user.email "ezh737@gmail.com"

# 1. Git 초기화 (이미 초기화된 경우 무시됨)
if [ ! -d ".git" ]; then
    git init
    git remote add origin $REPO_URL
    echo "Git 리포지토리가 초기화되었습니다."
else
    echo "이미 Git 리포지토리가 초기화되었습니다."
fi

# 2. 변경된 파일 스테이징
git add .

# 3. 커밋 메시지 설정
COMMIT_MESSAGE="자동 커밋: $(date)"

# 4. 커밋
git commit -m "$COMMIT_MESSAGE"

# 5. 원격 리포지토리에 푸시
git push -u origin master

echo "✅ 스크립트와 결과물이 GitHub에 자동으로 업로드되었습니다."
