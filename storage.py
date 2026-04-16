import json
from datetime import datetime, timedelta
from config import SENT_FILE


def load_sent_posts():
    """
    발송 기록 파일(sent.json)을 읽어서 반환

    Returns:
        dict: {"링크": "발송_시간", ...}
    """
    try:
        with open(SENT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # 파일이 없으면 빈 딕셔너리 반환
        return {}
    except json.JSONDecodeError:
        # JSON 형식이 잘못되었으면 빈 딕셔너리 반환
        print(f"경고: {SENT_FILE} 파일이 손상되었습니다. 초기화합니다.")
        return {}


def save_sent_posts(sent_posts):
    """
    발송 기록을 파일에 저장

    Args:
        sent_posts (dict): {"링크": "발송_시간", ...}
    """
    with open(SENT_FILE, "w", encoding="utf-8") as f:
        json.dump(sent_posts, f, ensure_ascii=False, indent=2)


def is_already_sent(link, sent_posts):
    """
    이미 발송한 글인지 확인

    Args:
        link (str): 확인할 글의 링크
        sent_posts (dict): 발송 기록

    Returns:
        bool: 이미 발송했으면 True, 아니면 False
    """
    return link in sent_posts


def add_sent_post(link, sent_posts):
    """
    발송 기록에 추가

    Args:
        link (str): 발송한 글의 링크
        sent_posts (dict): 발송 기록
    """
    sent_posts[link] = datetime.now().isoformat()


def clean_old_records(sent_posts, days=7):
    """
    오래된 발송 기록 삭제 (기본 7일)

    Args:
        sent_posts (dict): 발송 기록
        days (int): 보관 기간 (일)

    Returns:
        dict: 정리된 발송 기록
    """
    cutoff_date = datetime.now() - timedelta(days=days)
    cleaned = {}

    for link, sent_time in sent_posts.items():
        try:
            sent_datetime = datetime.fromisoformat(sent_time)
            if sent_datetime > cutoff_date:
                # 최근 기록만 유지
                cleaned[link] = sent_time
        except ValueError:
            # 잘못된 날짜 형식은 무시
            continue

    return cleaned


if __name__ == "__main__":
    print("=== storage.py 테스트 ===\n")

    # 1. 기록 불러오기
    print("1. 발송 기록 불러오기")
    sent = load_sent_posts()
    print(f"   현재 기록 수: {len(sent)}개\n")

    # 2. 테스트 링크 추가
    print("2. 테스트 링크 추가")
    test_link = "https://example.com/test"
    add_sent_post(test_link, sent)
    print(f"   추가된 링크: {test_link}")
    print(f"   발송 시간: {sent[test_link]}\n")

    # 3. 중복 체크
    print("3. 중복 체크")
    print(f"   {test_link}")
    print(f"   → 이미 발송? {is_already_sent(test_link, sent)}\n")

    new_link = "https://example.com/new"
    print(f"   {new_link}")
    print(f"   → 이미 발송? {is_already_sent(new_link, sent)}\n")

    # 4. 저장
    print("4. 파일에 저장")
    save_sent_posts(sent)
    print(f"   {SENT_FILE} 저장 완료\n")

    # 5. 오래된 기록 정리
    print("5. 7일 이상 오래된 기록 정리")
    cleaned = clean_old_records(sent, days=7)
    print(f"   정리 전: {len(sent)}개")
    print(f"   정리 후: {len(cleaned)}개")

    if len(cleaned) < len(sent):
        print(f"   삭제된 기록: {len(sent) - len(cleaned)}개")
