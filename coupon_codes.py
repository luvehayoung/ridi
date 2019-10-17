import datetime

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
    # 쿠폰 발급에 필요한 것(어떤 쿠폰인지, 어떤 회원인지 -> 재발급인지 체크), 사용기간은 모두 30일인 것으로 가정
    # code번호 정하기, 중복해서 발급하지 않도록 쿠폰 이름이랑 아이디로 키 생성함
    code = extra_data['coupon_name'] + extra_data['id']

    if Coupon.exists(code):
        print("발급 받았던 쿠폰입니다! ")

        return code

    else:
        #시간 속성
        now = datetime.datetime.now()
        extra_data['start'] = now
        extra_data['expired'] = now + datetime.timedelta(days=30)

        #사용 여부 체크, 쿠폰을 생성할 시에는 사용여부 false 기본 생성
        extra_data['used'] = False

        coupon =  Coupon.create(code = code, extra_data = extra_data)
        # 구현 예시
        # code = '12345'
        # coupon = Coupon.create(code=code, extra_data=extra_data)

        return coupon.code


if __name__ == "__main__":

    #테스트 쿠폰 종류랑 아이디 입력은 여기서
    i = 0
    while i < 2:
        coupon_name = str(input("쿠폰 종류를 입력하세요: "))
        id = str(input("사용자의 아이디를 입력하세요: "))
        data = {"coupon_name": coupon_name, "id": id }
        print(create_coupon(data))
        i = i+1

