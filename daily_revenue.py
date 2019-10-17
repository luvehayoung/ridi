from datetime import date
from datetime import datetime, timedelta
from typing import List
from typing import Optional
from typing import Tuple

Period = Tuple[datetime, datetime]


def daily_revenue(price: int, period: Period, refund_date: Optional[datetime]) -> List[Tuple[date, int]]:

    answer = []

    period = period[2:-1].split(' ~ ')
    start_date = datetime.strptime(period[0], "%Y-%m-%d %H:%M:%S")
    end_date = datetime.strptime(period[1], "%Y-%m-%d %H:%M:%S")
    result = end_date - start_date
    days = int(result.days) + 2
    #앞 뒤 날짜 포함
    print(days)

    daily_gain = int(price)//days
    last_gain = int(price) - daily_gain * (days-1)

    print(daily_gain)
    print(last_gain)

    if refund_date != None:
        refund_date = refund_date[2:-1].split()
        refund_date= datetime.strptime(refund_date[0] + ' ' + refund_date[1], "%Y-%m-%d %H:%M:%S")
        print(refund_date)

    for i in range(0, days):

        date = start_date + timedelta(days=i)

        if int((date - refund_date).days) == 0:
            #예시에서는 4일에 환불해도, 3일에 처리가 됬는데, 4일에 환불되는 것으로 작성했습니다.
            answer.append((str(date.year) + "-" + str(date.month) + "-" + str(date.day), -daily_gain*i))
            break

        if i != days-1:
            answer.append((str(date.year) + "-" + str(date.month) + "-" + str(date.day), daily_gain))
        else:
            answer.append((str(date.year) + "-" + str(date.month) + "-" + str(date.day), last_gain))



    if (refund_date - end_date).days > 0:
        answer.append((str(refund_date.year) + "-" + str(refund_date.month) + "-" + str(refund_date.day), -int(price)))

    print(answer)

if __name__ == "__main__":
    value = list(map(str, input().split(',')))
    if len(value) == 3:
        daily_revenue(value[0], value[1], value[2])
    else:
        daily_revenue(value[0], value[1])

# 기간이 끝나기 전 환불: 9900, “2019-09-01 17:10:21 ~ 2019-10-01 08:35:48”, “2019-09-04 12:13:20 환불"

# 기간이 끝나고 나서 환불: 9900, “2019-09-01 17:10:21 ~ 2019-10-01 08:35:48”, “2019-10-5 12:13:20 환불"
# (언제든지 환불가능하다는 말을 기간이 끝나고나서도 환불이 가능하다는 것으로 이해하고 추가했습니다.)