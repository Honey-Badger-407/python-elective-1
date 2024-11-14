class IntegerToRoman:
    def __init__(self):
        self.value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def int_to_roman(self, num):
        result = ""
        for value, numeral in self.value_map:
            while num >= value:
                result += numeral
                num -= value
        return result

converter = IntegerToRoman()
print(converter.int_to_roman(30))