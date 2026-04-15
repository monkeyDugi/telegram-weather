from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

GEEKNEWS_URL = "https://news.hada.io"
POINT_THRESHOLD = 40
SENT_FILE = "sent.json"

if __name__ == "__main__":
    print("봇 토큰:", TELEGRAM_BOT_TOKEN)
    print("채팅 ID:", TELEGRAM_CHAT_ID)
    print("GeekNews URL:", GEEKNEWS_URL)
    print("포인트 기준:", POINT_THRESHOLD)
    print("발송 기록 파일:", SENT_FILE)