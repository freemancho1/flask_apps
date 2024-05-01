from datetime import date, datetime


def fmt_to_date(dt, fmt) -> date:
    return dt if isinstance(dt, date) else datetime.strptime(dt, fmt)