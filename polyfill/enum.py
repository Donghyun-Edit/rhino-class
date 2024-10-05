# -*- coding:utf-8 -*-


METHOD_DECORATORS = (
    property,
    staticmethod,
    classmethod,
)


class EnumMeta(type):
    def __new__(mcs, name, bases, attrs):
        cls = super(EnumMeta, mcs).__new__(mcs, name, bases, attrs)
        name_map = {}
        setattr(cls, "_name_map", name_map)
        value_map = {}
        setattr(cls, "_value_map", value_map)

        for key, value in attrs.items():
            is_variant = (
                not key.startswith("__")  # Dunder 멤버 및 메서드 제외
                and not callable(value)  # 메서드 제외
                and not isinstance(value, METHOD_DECORATORS)  # 데코레이터 메서드 제외
            )
            if not is_variant:
                continue
            instance = cls.__new__(cls)  # type: ignore
            setattr(instance, "_value", value)
            setattr(instance, "_name", key)
            name_map[key] = instance
            value_map[value] = instance
            setattr(cls, key, instance)

        return cls

    def __call__(cls, value):
        value_map = getattr(cls, "_value_map")
        if value not in value_map:
            cls_name = cls.__name__
            error_text = "{} is not a valid {}".format(value, cls_name)
            raise ValueError(error_text)
        return value_map[value]

    def __getitem__(cls, key):
        name_map = getattr(cls, "_name_map")
        return name_map[key]

    def __iter__(cls):
        name_map = getattr(cls, "_name_map")
        return iter(name_map.values())

    def __len__(cls):
        name_map = getattr(cls, "_name_map")
        return len(name_map.values())


class Enum:
    """
    파이썬 3에서 어떤 클래스가 `Enum` 클래스를 상속받는 경우
    해당 클래스의 멤버들은 해당 클래스의 인스턴스가 된다.
    이 클래스는 파이썬 3에 존재하는 `enum.Enum` 클래스를 대신한다.
    """

    __metaclass__ = EnumMeta

    @property
    def value(self):
        return getattr(self, "_value")

    @property
    def name(self):
        return getattr(self, "_name")

    def __repr__(self):
        cls_name = self.__class__.__name__
        return "<{}.{}: {!r}>".format(cls_name, self.name, self.value)

    def __str__(self):
        cls_name = self.__class__.__name__
        return "{}.{}".format(cls_name, self.name)

    def __hash__(self):
        return hash(self.name)


# # 사용 예:
# class Fruit(Enum):
#     Apple = 1
#     Banana = 2
#     Melon = 5

#     @property
#     def custom_yo(self):
#         return 4

#     @staticmethod
#     def custom_do():
#         pass

#     @classmethod
#     def custom_go():
#         pass

#     def custom_ho(self):
#         pass


# # 값을 Enum variant로 변환
# fruit = Fruit(5)
# print(fruit)  # 출력: Fruit.Melon
# print(repr(fruit))  # 출력: <Fruit.Melon: 5>

# # 싱글톤 패턴 확인
# print(Fruit(5) is Fruit(5))  # 출력: True

# # Variant의 `name` 필드 접근
# print(fruit.name)  # 출력: Melon

# # Enum Variant를 값으로 변환
# print(Fruit.Melon.value)  # 출력: 5

# # Enum 멤버 접근
# print(Fruit.Apple)  # 출력: Fruit.Apple

# # Variant 비교
# print(Fruit.Melon == Fruit(5))  # 출력: True
# print(Fruit.Apple == Fruit(5))  # 출력: False

# # 해시
# test_dict = {Fruit.Banana: None}
# print(Fruit(2) in test_dict)  # 출력: True
# print(Fruit(5) in test_dict)  # 출력: False

# # 탐색
# print(Fruit['Apple'])  # 출력: Fruit.Apple

# # 순회
# print(len(Fruit))  # 출력: 3
# for variant in Fruit:
#     print(variant)  # 출력: [각 Variant]

# # 잘못된 키로 접근 시 `KeyError` 발생
# try:
#     print(Fruit['Orange'])
# except KeyError as e:
#     print("KeyError: {}".format(e))
#     # 출력: KeyError: 'Orange'

# # 잘못된 값으로 접근 `시 ValueError` 발생
# try:
#     fruit = Fruit(10)
# except ValueError as e:
#     print("ValueError: {}".format(e))
#     # 출력: ValueError: 10 is not a valid Fruit
