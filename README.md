# GeekNews 텔레그램 알림 봇

GeekNews(news.hada.io)의 인기글을 텔레그램으로 자동 알림해주는 봇입니다.

## 기능

- 포인트 기준 이상의 인기글만 필터링
- 이미 발송한 글은 중복 발송하지 않음
- 7일 이상 오래된 기록 자동 삭제

## 설치

```bash
# 1. 가상환경 생성
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. 라이브러리 설치
pip install -r requirements.txt

# 3. 환경변수 설정
cp .env.example .env
# .env 파일을 열어서 토큰과 채팅 ID 입력
```

## 텔레그램 봇 설정

### 1. 봇 생성
1. 텔레그램에서 @BotFather 검색
2. `/newbot` 명령어 입력
3. 봇 이름과 username 설정
4. 받은 토큰을 `.env`의 `TELEGRAM_BOT_TOKEN`에 입력

### 2. 채팅 ID 확인
1. 텔레그램에서 @userinfobot 검색
2. `/start` 명령어 입력
3. 받은 ID를 `.env`의 `TELEGRAM_CHAT_ID`에 입력

## 실행

```bash
# 가상환경 활성화
source venv/bin/activate

# 실행
python main.py
```

## 자동 실행

### ⭐ GitHub Actions (추천)

매일 아침 7시 자동 실행:

1. **GitHub 저장소 생성 및 코드 푸시**
2. **Settings** → **Secrets and variables** → **Actions**
3. **New repository secret** 클릭하여 추가:
   - `TELEGRAM_BOT_TOKEN`: 봇 토큰
   - `TELEGRAM_CHAT_ID`: 채팅 ID
4. **Actions** 탭에서 워크플로우 확인
5. 수동 테스트: **Run workflow** 버튼 클릭

설정 완료! 매일 아침 7시에 자동으로 알림이 옵니다.

### Mac/Linux Cron

30분마다 자동 실행하려면:

```bash
# crontab 편집
crontab -e

# 아래 줄 추가 (경로는 실제 경로로 변경)
*/30 * * * * cd /path/to/telegram-weather && /path/to/venv/bin/python main.py >> /path/to/logs/bot.log 2>&1
```

## 설정

`config.py`에서 포인트 기준 조정 가능:

```python
POINT_THRESHOLD = 40  # 이 점수 이상만 알림
```

## 파일 구조

```
telegram-weather/
├── main.py          # 메인 실행 파일
├── scraper.py       # GeekNews 스크래핑
├── storage.py       # 발송 기록 관리
├── notifier.py      # 텔레그램 발송
├── config.py        # 설정
├── requirements.txt # 라이브러리 목록
├── .env             # 환경변수 (git 제외)
└── sent.json        # 발송 기록 (자동 생성)
```

## 라이센스

MIT
