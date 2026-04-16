import requests
import re
from bs4 import BeautifulSoup

from config import GEEKNEWS_URL, POINT_THRESHOLD


def get_geeknews_posts():
  """
  GeekNews에서 인기글을 가져와 포인트 기준 이상인 글만 반환

  :return:
    list: [{"title": "제목", "link": "링크", "points": 포인트}, ...]
  """

  try:
    response = requests.get(GEEKNEWS_URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    # GeekNews는 각 게시글이 <div class="topic_row"> 안에 있음
    post_rows = soup.find_all("div", class_="topic_row")

    posts = []

    for row in post_rows:
      try:
        # 제목과 링크는 id가 "tr"로 시작하는 <a> 태그에 있음
        title_tag = row.find("a", id=lambda x: x and x.startswith("tr"))
        if not title_tag:
          continue

        title = title_tag.get_text(strip=True)

        # GeekNews 자체 페이지 링크 찾기 (topic?id=XXX)
        geeknews_link_tag = row.find("a", href=lambda x: x and "topic?id=" in x)
        if geeknews_link_tag:
          link = GEEKNEWS_URL + "/" + geeknews_link_tag.get("href", "")
        else:
          # fallback: 원본 링크 사용
          link = title_tag.get("href", "")
          if link.startswith("/"):
            link = GEEKNEWS_URL + link

        # 포인트는 row 전체 텍스트에서 "X points by" 형태로 추출
        points_text = row.get_text()
        match = re.search(r'(\d+)\s+points', points_text)
        points = int(match.group(1)) if match else 0

        if points >= POINT_THRESHOLD:
          posts.append({"title": title, "link": link, "points": points})

      except Exception as e:
        print(f"게시글 파싱 오류: {e}")
        continue

    return posts

  except Exception as e:
    print(f"GeekNews 접속 오류: {e}")
    return []

if __name__ == "__main__":
    print("GeekNews 스크래핑 테스트...")
    print(f"포인트 기준: {POINT_THRESHOLD}점 이상\n")

    posts = get_geeknews_posts()

    if posts:
        print(f"총 {len(posts)}개의 인기글을 찾았습니다:\n")
        for i, post in enumerate(posts, 1):
            print(f"{i}. [{post['points']}점] {post['title']}")
            print(f"   {post['link']}\n")
    else:
        print("기준에 맞는 글을 찾지 못했습니다.")