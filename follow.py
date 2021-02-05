class User:
    # instance init
    def __init__(self,name, email, pw):
        self.name=name
        self.email=email
        self.pw=pw

        self.following_list=[]
        self.followers_list=[]

    # follow
    def follow (self, another_user):
        self.following_list.append(another_user)
        another_user.followers_list.append(self)

    def num_following(self):
        return len(self.followers_list)

    def num_followers(self):
        return len(self.following_list)


Young = User("Young", "young@gmail.com","1234")
Yoonsoo = User("Yoonsoo", "Yoonsoo@gmail.com","1234")
Teaho = User("Teaho", "Teaho@gmail.com","1234")
Lisa = User("Lisa", "Lisa@gmail.com","1234")


Young.follow(Yoonsoo)
Yoonsoo.follow(Teaho)
Teaho.follow(Lisa)
Lisa.follow(Young)

Young.follow(Yoonsoo)
Yoonsoo.follow(Teaho)
Teaho.follow(Lisa)
Lisa.follow(Young)

print ("{}    {}     {}" .format(Young.name,Young.num_followers(),Young.num_following()))
print ("{}    {}     {}" .format(Yoonsoo.name,Yoonsoo.num_followers(),Yoonsoo.num_following()))
print ("{}    {}     {}" .format(Teaho.name,Teaho.num_followers(),Teaho.num_following()))
print ("{}    {}     {}" .format(Lisa.name,Lisa.num_followers(),Lisa.num_following()))
