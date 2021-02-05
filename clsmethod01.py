class User:

    def __init__ ( self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

    def __str__(self):
        return "{} {} {}".format(self.name,self.email,self.pw)

    @classmethod
    def from_string(cls, string_param):
        parameter_list = string_param.split(",")
        name = parameter_list[0]
        email = parameter_list[1]
        pw = parameter_list[2]
        return cls(name, email, pw)

    @classmethod
    def from_list(cls, list_param):
        name = list_param[0]
        email = list_param[1]
        pw = list_param[2]
        return cls(name, email, pw)



info_string= ("knag, kang@gmail.com, 1234")
info_list = ["lee", "lee@gmail.com", "1234"]

kang = User.from_string(info_string)

lee= User.from_list(info_list)

print (kang)
print (lee)