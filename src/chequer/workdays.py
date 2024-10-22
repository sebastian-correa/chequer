"""Operations with workdays."""

from datetime import date, datetime, timedelta

import holidays
from holidays.holiday_base import DateLike

from chequer._types import InclusiveType


class WorkdayCalculator:
    """Do arighmetic with datess, only considering workdays.

    Args:
        country_code (str): An ISO 3166-1 alpha-2 country used to define the country holidays.
    """

    def __init__(self, country_code: str) -> None:
        self.region_holidays = holidays.country_holidays(country_code)
        self._one_day = timedelta(days=1)

    def is_workday(self, date: DateLike) -> bool:
        """Check if a date is a workday.

        Args:
            date (DateLike): The date to check.

        Returns:
            bool: True if the date is a workday, False if not.
        """
        return self.region_holidays.is_working_day(date)

    def workdays_between(
        self, start: datetime, end: datetime, inclusive: InclusiveType
    ) -> timedelta:
        """Calculate the number of workdays between two dates.

        Args:
            start (datetime): The start date.
            end (datetime): The end date.
            inclusive (InclusiveType): How to treat start and end dates.

        Returns:
            int: The number of workdays between the two dates.

        Raises:
            ValueError: If start date is after end date.
        """
        if start > end:
            message = "Start date must be before or equal to end date."
            raise ValueError(message)

        start_date = start.date()
        end_date = end.date()
        start_working = self.is_workday(start_date)

        if start_date == end_date:
            workdays = 1 if start_working and inclusive in ["both", "left", "right"] else 0
            return timedelta(days=workdays)

        # Inclusive both.
        workdays = self.region_holidays.get_working_days_count(start_date, end_date)

        end_working = self.is_workday(end_date)
        if inclusive == "neither":
            workdays -= start_working + end_working
        elif inclusive == "right":
            workdays -= start_working
        elif inclusive in "left":
            workdays -= end_working

        return timedelta(days=workdays)

    def next_workday(self, date: datetime, *, inclusive: bool = True) -> date:
        """Get the next workday after a date.

        Args:
            date (datetime): The date to start from.
            inclusive (bool): If True and the date is a workday, it will be returned. If False, the
                next workday will be returned.

        Returns:
            date: The next workday.
        """
        next_date = date.date()
        if inclusive and self.is_workday(next_date):
            return next_date

        next_date += self._one_day
        while not self.is_workday(next_date):
            next_date += self._one_day
        return next_date
