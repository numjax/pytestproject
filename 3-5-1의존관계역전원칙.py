
class Sword:
    """검 클래스"""
    def __init__(self, damage):
        self.damage = damage

    def slash(self, other_character):
        """검 사용 메소드"""
        other_character.get_damage(self.damage)


class GameCharacter:
    """게임 캐릭터 클래스"""
    def __init__(self, name, hp, sword: Sword):
        self.name = name
        self.hp = hp
        self.sword = sword

    def attack(self, other_character):
        """다른 유저를 공격하는 메소드"""
        if self.hp > 0:
            self.sword.slash(other_character)
        else:
            print(self.name + "님은 사망해서 공격할 수 없습니다.")

    def change_sword(self, new_sword):
        """검을 바꾸는 메소드"""
        self.sword = new_sword

    def get_damage(self, damage):
        """캐릭터가 공격받았을 때 자신의 체력을 깎는 메소드"""
        if self.hp <= damage:
            self.hp = 0
            print(self.name + "님은 사망했습니다.")
        else:
            self.hp -= damage

    def __str__(self):
        """남은 체력을 문자열로 리턴하는 메소드"""
        return self.name + "님은 hp: {}이(가) 남았습니다.".format(self.hp)


bad_sword = Sword(1)
good_sword = Sword(100)

game_char1= GameCharacter("Hong", 100, bad_sword)
game_char2 = GameCharacter("Amu", 1000, good_sword)

game_char1.attack(game_char2)
game_char1.attack(game_char2)
game_char1.attack(game_char2)


game_char2.attack(game_char1)

print(game_char1)
print(game_char2)


"""
어떤 클래스 A가 다른 클래스 B를 사용하고 있을 때
A는 B의 상위모듈이 된다. 
즉 위의 코드에서 GameChar가 Sword를 사용하고 있으므로 
GameChar는 상위 모듈이 되고 Sword는 하위 모듈이 된다.


위 코드에서 보면 
상위 GameChar 모듈에서 하위 Sword 모듈의 slash를 사용하고 있다.
이런 경우 Sword에서 slash의 값이나 이름이 변경되면, GameChar에서 slash의 호출을 변경해 주어야 하는데, 
이런 상황을 GameChar는 Sword에 의존하고 있다라고 표현한다.

이를 정리하면, 
상위 모듈인 GameChar가 하위모듈인 Sword에 의존하고 있는데, 
이를 의존관계 역전이라 부른다. - oop에서는 이런 상황을 만들지 말라고 하고 있다. 

이런 상황을 피하기 위해서는 
상위, 하위 막론하고 추상화된 클래스에 의존하게 만들어야 한다.

"""
