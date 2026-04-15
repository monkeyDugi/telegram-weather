# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 절대 규칙
- `config.py`의 토큰, 채팅 ID 등 민감한 값을 다른 파일에 하드코딩하지 말 것
- 코드를 바로 작성하지 말고, 설명 먼저 → 사용자가 직접 작성 → 리뷰 순서로 진행
- 항상 한국어로 답변
- 사용자는 파이썬 입문자이므로 초보자 눈높이에 맞춰 설명

## 프로젝트 개요
GeekNews(news.hada.io) 인기글을 텔레그램으로 알림 발송하는 봇.
포인트 기준 이상인 글만 필터링하고, 이미 보낸 글은 중복 발송하지 않음.

## 기술 스택
- Python 3
- requests, BeautifulSoup4 (웹 스크래핑)
- Telegram Bot API (메시지 발송)

## 프로젝트 구조
```
telegram-alarm/
├── CLAUDE.md
├── requirements.txt
├── config.py        # 설정값 (토큰, 채팅 ID, 포인트 기준 등)
├── scraper.py       # GeekNews 웹 파싱
├── notifier.py      # 텔레그램 메시지 발송
├── storage.py       # sent.json 읽기/쓰기 및 7일 이상 기록 삭제
├── main.py          # 전체 흐름 연결
└── sent.json        # 발송 기록 (자동 생성)
```

## 실행 방법
```bash
pip install -r requirements.txt
python main.py
```

## 실행 흐름
```
main.py → scraper.py (글 수집) → 포인트 필터링 → storage.py (중복 체크) → notifier.py (발송) → storage.py (기록 저장)
```

## 코딩 컨벤션
- 함수명: snake_case
- 파일 하나에 역할 하나 (scraper는 스크래핑만, notifier는 발송만)
- 각 파일은 단독 실행 시 테스트 가능하도록 작성
- 커밋 컨벤션: @docs/commit-convention.md

## 클로드 코드 사용 가이드 참조
아래 3개 파일이 클로드 코드 사용 가이드입니다. 항상 이 가이드를 기반으로 현재 상황에 맞는 방법을 판단하고 적용하세요.
- 입문 (단축키, CLAUDE.md, 슬래시 명령어): @claude-code-guide-1
- 실전 워크플로우 (컨텍스트 관리, Plan Mode, TDD, TODO.md, WAT 프레임워크): @claude-code-guide-2
- 고급 자동화 (Skills, Sub-Agent, Hooks, Git Worktree): @claude-code-guide-3

프로젝트가 작을 때는 가이드 1~2편 위주로 적용하고, 복잡해지면 가이드 3편의 고급 기능을 판단해서 도입을 제안하세요.

## 클로드 코드 사용 정책

### 워크플로우
- **모든 작업은 Plan Mode 먼저** (`Shift+Tab`): 계획 확인 후 Accept Mode로 실행
- **한 세션 = 한 기능**: 기능 하나 완료 후 반드시 `/clear`로 컨텍스트 초기화
- **작업 루프**: 코드 작성 → `!python 파일명.py`로 즉시 테스트 → 커밋 → 다음 기능
- 에러 발생 시 로그를 해석 없이 그대로 붙여넣을 것

### Claude가 자동으로 해야 할 것

#### 세션 시작/종료
- 새 기능 시작 전 "Plan Mode로 시작하세요 (`Shift+Tab`)"를 상기시킬 것
- 기능 하나 완료 시 "커밋 후 `/clear`로 새 세션 시작하세요"를 안내할 것
- 세션 종료 시 TODO.md가 있으면 진행 상황 업데이트를 제안할 것

#### 컨텍스트 관리
- 작업이 길어지면 `/context`로 토큰 사용량 확인을 권고할 것
- 대화가 길어져서 출력이 많아지면 `/compact` 사용을 권고할 것
- 무거운 데이터 처리가 필요하면 대화 안에서 하지 말고 스크립트로 오프로드할 것

#### 코딩 진행
- 코드를 바로 작성하지 말고 반드시 설명 → 사용자 직접 작성 → 리뷰 순서로 진행할 것
- thinking 로그에서 잘못된 가정을 하고 있다면 사용자에게 `Escape`로 중단하라고 안내할 것
- 작업이 막히면 `/export`로 다른 AI에게 비평 받는 방법을 제안할 것

#### 도구 도입 판단
- 같은 프롬프트를 반복하게 되면 Skills(SKILL.md) 도입을 제안할 것
- 독립적인 작업이 여러 개면 Sub-Agent 병렬 처리를 제안할 것
- 매번 수동으로 하는 반복 동작이 있으면 Hooks 자동화를 제안할 것
- 작업 복잡도에 따라 `/models`로 모델 전환을 제안할 것 (간단한 질문은 Haiku, 복잡한 로직은 Opus)

### 사용자가 알아두면 좋은 단축키 & 명령어
- `Shift+Tab`: Plan Mode ↔ Accept Mode 전환
- `Escape`: 잘못된 방향이면 즉시 중단
- `Escape × 2`: 입력 삭제 / 이전 입력 복원
- `!python 파일명.py`: 대화 끊지 않고 바로 실행
- `/clear`: 새 기능 시작 전 컨텍스트 초기화
- `/compact`: 맥락 유지하며 토큰 압축
- `/context`: 토큰 사용량 확인
- `/memory`: 클로드가 학습한 내용 확인 ("기억해줘"로 저장 가능)
- `/resume`: 실수로 터미널 닫았을 때 이전 세션 복구
- `/voice`: 복잡한 요구사항을 음성으로 전달
