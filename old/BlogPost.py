class BlogPost:

    def __init__(self, date, contents):
        self.date = date
        self.contents = contents

    def __str__(self):
        return "Poseted on: {}{}".format(self.date, self.contents)



class BlogUser:

    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, date, contents):
        mypost = BlogPost(date, contents)
        self.posts.append(mypost)

    def show_all_posts (self):
        for post in self.posts:
            print(post)
            #print("\n")

    def __str__(self):
        return "안녕하세요 {}입니다.\n".format(self.username)



# 간단한 인사와 이름을 문자열로 리턴


# 블로그 유저 인스턴스 생성
blog_user_1 = BlogUser("성태호")

# 블로그 유저 인스턴스 출력(인사, 이름)
print(blog_user_1)

# 블로그 유저 게시글 2개 추가
blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이였다.
많은 사람들이 축하해줬다.
행복했다.
""")

blog_user_1.add_post("2019년 8월 31일", """
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
""")

# 블로그 유저의 모든 게시글 출력
blog_user_1.show_all_posts()