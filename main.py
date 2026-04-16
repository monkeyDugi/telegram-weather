#!/usr/bin/env python3
"""
GeekNews 텔레그램 알림 봇

실행: python main.py
"""

from scraper import get_geeknews_posts
from storage import (
    load_sent_posts,
    save_sent_posts,
    is_already_sent,
    add_sent_post,
    clean_old_records
)
from notifier import send_telegram_message
from config import POINT_THRESHOLD


def main():
    print("=" * 60)
    print("GeekNews 텔레그램 알림 봇 시작")
    print("=" * 60)
    print()

    # 1. 발송 기록 불러오기
    print("📂 발송 기록 불러오는 중...")
    sent_posts = load_sent_posts()
    print(f"   현재 기록: {len(sent_posts)}개\n")

    # 2. 오래된 기록 정리
    print("🧹 7일 이상 오래된 기록 정리 중...")
    sent_posts = clean_old_records(sent_posts, days=7)
    print(f"   정리 후: {len(sent_posts)}개\n")

    # 3. GeekNews 스크래핑
    print(f"🔍 GeekNews에서 {POINT_THRESHOLD}점 이상 글 검색 중...")
    posts = get_geeknews_posts()
    print(f"   찾은 글: {len(posts)}개\n")

    if not posts:
        print("❌ 기준에 맞는 글을 찾지 못했습니다.")
        print()
        return

    # 4. 새 글만 필터링
    print("🆕 새 글 확인 중...")
    new_posts = []
    for post in posts:
        if not is_already_sent(post["link"], sent_posts):
            new_posts.append(post)

    print(f"   새 글: {len(new_posts)}개\n")

    if not new_posts:
        print("✅ 모든 글이 이미 발송되었습니다.")
        print()
        return

    # 5. 텔레그램 발송
    print(f"📤 텔레그램 발송 시작 ({len(new_posts)}개)...")
    print("-" * 60)

    success_count = 0
    fail_count = 0

    for i, post in enumerate(new_posts, 1):
        print(f"\n[{i}/{len(new_posts)}] {post['title'][:50]}...")

        # 발송 시도
        if send_telegram_message(post):
            # 성공하면 기록에 추가
            add_sent_post(post["link"], sent_posts)
            success_count += 1
        else:
            fail_count += 1

    print()
    print("-" * 60)

    # 6. 기록 저장
    print("\n💾 발송 기록 저장 중...")
    save_sent_posts(sent_posts)
    print("   저장 완료\n")

    # 7. 결과 출력
    print("=" * 60)
    print("📊 실행 결과")
    print("=" * 60)
    print(f"✅ 성공: {success_count}개")
    print(f"❌ 실패: {fail_count}개")
    print(f"📝 총 기록: {len(sent_posts)}개")
    print("=" * 60)
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ 사용자에 의해 중단되었습니다.")
    except Exception as e:
        print(f"\n\n❌ 오류 발생: {e}")
        raise
