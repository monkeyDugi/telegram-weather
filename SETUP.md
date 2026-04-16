# GitHub Actions 설정 가이드

## 📋 체크리스트

### ✅ 완료된 것 (제가 했어요!)
- [x] GitHub Actions 워크플로우 파일 생성 (`.github/workflows/daily-geeknews.yml`)
- [x] `.gitignore`에서 `sent.json` 제거
- [x] `sent.json` 초기 파일 생성
- [x] README.md 업데이트

### 🎯 사용자님이 해야 할 것

## 1️⃣ GitHub 저장소 생성 (Public)

1. https://github.com/new 접속
2. Repository name: `telegram-weather` (또는 원하는 이름)
3. **Public** 선택 ⭐
4. **Create repository** 클릭

---

## 2️⃣ 코드 푸시

```bash
# Git 초기화 (이미 했으면 생략)
git init

# 파일 추가
git add .

# 커밋
git commit -m "feat: GeekNews 텔레그램 봇 완성"

# GitHub 저장소 연결 (본인 저장소 주소로 변경!)
git remote add origin https://github.com/본인계정/telegram-weather.git

# Push
git branch -M main
git push -u origin main
```

---

## 3️⃣ GitHub Secrets 설정 (중요!)

1. GitHub 저장소 페이지로 이동
2. **Settings** 클릭
3. 왼쪽 메뉴에서 **Secrets and variables** → **Actions** 클릭
4. **New repository secret** 클릭

### 추가할 Secret 2개:

**첫 번째:**
- Name: `TELEGRAM_BOT_TOKEN`
- Secret: `본인의_텔레그램_봇_토큰`
- **Add secret** 클릭

**두 번째:**
- Name: `TELEGRAM_CHAT_ID`
- Secret: `본인의_채팅_ID`
- **Add secret** 클릭

---

## 4️⃣ 워크플로우 테스트

1. GitHub 저장소 페이지
2. **Actions** 탭 클릭
3. 왼쪽에서 **Daily GeekNews Alert** 클릭
4. **Run workflow** 버튼 클릭 (오른쪽)
5. **Run workflow** 확인

몇 초 후 실행 상태 확인 가능!

---

## 5️⃣ 텔레그램 확인

텔레그램 앱을 열어서 메시지가 왔는지 확인하세요! 🎉

---

## ⏰ 자동 실행 스케줄

설정 완료! 이제 **매일 아침 7시**에 자동으로 실행됩니다.

### 시간 변경하고 싶다면?

`.github/workflows/daily-geeknews.yml` 파일에서:

```yaml
schedule:
  - cron: '0 22 * * *'  # UTC 22:00 = KST 07:00
```

이 부분을 수정하세요.

**예시:**
- 오전 9시: `cron: '0 0 * * *'`  (UTC 00:00)
- 오후 6시: `cron: '0 9 * * *'`  (UTC 09:00)
- 매일 2회 (오전 7시, 오후 7시): `cron: '0 22,10 * * *'`

---

## 🐛 문제 해결

### Actions에서 에러가 나요
1. **Actions** 탭에서 실패한 워크플로우 클릭
2. 빨간색 X 표시된 step 클릭
3. 에러 로그 확인

### 메시지가 안 와요
1. Secrets 설정 확인 (TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)
2. 봇에게 `/start` 보냈는지 확인
3. Actions 로그에서 에러 확인

### 시간이 안 맞아요
- GitHub Actions는 UTC 기준이에요
- 한국시간 - 9시간 = UTC
- 예: 한국 07:00 = UTC 22:00 (전날)

---

## 📊 확인 방법

### Secrets 잘 설정됐나?
- **Settings** → **Secrets and variables** → **Actions**
- 2개 Secret이 보이면 OK!

### 워크플로우 파일 있나?
```bash
ls -la .github/workflows/
# daily-geeknews.yml 있으면 OK!
```

### sent.json Git에 포함됐나?
```bash
git ls-files | grep sent.json
# sent.json 나오면 OK!
```

---

## 🎉 완료!

모든 설정이 끝났어요! 이제:
- ✅ 매일 아침 7시 자동 실행
- ✅ 새 글만 텔레그램 알림
- ✅ 서버 관리 필요 없음
- ✅ 완전 무료

즐거운 GeekNews 구독 되세요! 📱
