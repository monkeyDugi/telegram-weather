import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


def send_telegram_message(post):
    """
    텔레그램으로 메시지 발송

    Args:
        post (dict): {"title": "제목", "link": "링크", "points": 포인트}

    Returns:
        bool: 발송 성공 시 True, 실패 시 False
    """
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("오류: 텔레그램 토큰 또는 채팅 ID가 설정되지 않았습니다.")
        return False

    # 메시지 포맷
    message = f"""
🔥 GeekNews 인기글

📌 [{post['points']}점] {post['title']}

🔗 {post['link']}
    """.strip()

    # 텔레그램 API URL
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    # 요청 데이터
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "disable_web_page_preview": False  # 링크 미리보기 표시
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()

        result = response.json()
        if result.get("ok"):
            print(f"✅ 발송 성공: {post['title'][:50]}...")
            return True
        else:
            print(f"❌ 발송 실패: {result.get('description')}")
            return False

    except requests.RequestException as e:
        print(f"❌ 텔레그램 API 오류: {e}")
        return False


if __name__ == "__main__":
    print("=== notifier.py 테스트 ===\n")

    # 테스트용 게시글
    test_post = {
        "title": "테스트 제목: GeekNews 텔레그램 알림 봇",
        "link": "https://news.hada.io",
        "points": 42
    }

    print("테스트 메시지 발송 중...\n")
    success = send_telegram_message(test_post)

    if success:
        print("\n🎉 텔레그램 앱에서 메시지를 확인하세요!")
    else:
        print("\n⚠️ 메시지 발송 실패. 토큰과 채팅 ID를 확인하세요.")
        print("   - TELEGRAM_BOT_TOKEN:", "설정됨" if TELEGRAM_BOT_TOKEN else "❌ 없음")
        print("   - TELEGRAM_CHAT_ID:", "설정됨" if TELEGRAM_CHAT_ID else "❌ 없음")
