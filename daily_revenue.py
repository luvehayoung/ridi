from datetime import date
from datetime import datetime
from typing import List
from typing import Optional
from typing import Tuple

Period = Tuple[datetime, datetime]


def daily_revenue(price: int, period: Period, refund_date: Optional[datetime]) -> List[Tuple[date, int]]:
    raise NotImplementedError()
