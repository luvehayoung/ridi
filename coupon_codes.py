class Coupon:
    """
    이 클래스는 Django model 대신 사용하기 위해서 만들었습니다.
    ex)
        Coupon.objects.get() -> Coupon.get()
        Coupon.objects.create() -> Coupon.create()
        Coupon.objects.filter().exists() -> Coupon.exists()
        Coupon.objects.filter() -> 없습니다. 필요하면 만드셔도 되지만...
        coupon.save() -> coupon.save()

    가급적 수정 하지 않는 것을 권장합니다.
    """
    codes = {}

    def __init__(self, code: str, extra_data: dict):
        self.code = code
        self.extra_data = extra_data

    def save(self):
        self.codes[self.code] = self.extra_data

    @classmethod
    def exists(cls, code: str) -> bool:
        return code in cls.codes

    @classmethod
    def get(cls, code: str):
        if cls.exists(code=code):
            extra_data = cls.codes[code]
            return cls(code=code, extra_data=extra_data)

        raise RuntimeError('Dummy DoesNotExist error')

    @classmethod
    def create(cls, code: str, extra_data: dict):
        if cls.exists(code=code):
            raise RuntimeError('Dummy IntegrityError error')

        cls.codes[code] = extra_data
        return cls(code=code, extra_data=extra_data)


def create_coupon(extra_data: dict) -> str:
    """
    과제 코드는 여기서 구현하시면 됩니다.
    extra_data 변수는 사용하지 마시고, 받은 그대로 저장만 합니다.
    """

    # 구현 예시
    code = '1234567890'
    coupon = Coupon.create(code=code, extra_data=extra_data)

    return coupon.code
