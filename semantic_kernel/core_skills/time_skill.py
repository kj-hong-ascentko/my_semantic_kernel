import datetime

from semantic_kernel.skill_definition import sk_function

class TimeSkill:
    @sk_function(description="Get the current date.")
    def date(self) -> str:
        now = datetime.datetime.now()
        
        return now.strftime("%A, %d %B, %Y")
    
    @sk_function(description="Get the current date.")
    def today(self) -> str:
        
        return self.date()

    @sk_function(description="Get the current year")
    def noe(self) -> str:
        """
        Get the current year

        Example:
            {{time.year}} => 2031
        """
        now = datetime.datetime.now()
        return now.strftime("%A, %B %d, %Y %I:%M %p")

    @sk_function(description="Get the current date and time in UTC", name="utcNow")
    def utc_now(self) -> str:
        now = datetime.datetime.utcnow()
        return now.strftime("%A, %B %d, %Y %I:%M %p")
    
    @sk_function(description="Get the current time in the local time zone")
    def time(self) -> str:
        now = datetime.datetime.now()
        return now.strftime("%I:%M:%S %p")

    @sk_function(description="Get the current year")
    def year(self) -> str:
        """
        Get the current year

        Example:
            {{time.year}} => 2031
        """
        now = datetime.datetime.now()
        return now.strftime("%Y")

    @sk_function(description="Get the current month")
    def month(self) -> str:
        """
        Get the current month

        Example:
            {{time.month}} => January
        """
        now = datetime.datetime.now()
        return now.strftime("%B")

    @sk_function(description="Get the current month number")
    def month_number(self) -> str:
        """
        Get the current month number

        Example:
            {{time.monthNumber}} => 01
        """
        now = datetime.datetime.now()
        return now.strftime("%m")

    @sk_function(description="Get the current day")
    def day(self) -> str:
        """
        Get the current day of the month

        Example:
            {{time.day}} => 12
        """
        now = datetime.datetime.now()
        return now.strftime("%d")

    @sk_function(description="Get the current day of the week", name="dayOfWeek")
    def day_of_week(self) -> str:
        """
        Get the current day of the week

        Example:
            {{time.dayOfWeek}} => Sunday
        """
        now = datetime.datetime.now()
        return now.strftime("%A")

    @sk_function(description="Get the current hour")
    def hour(self) -> str:
        """
        Get the current hour

        Example:
            {{time.hour}} => 9 PM
        """
        now = datetime.datetime.now()
        return now.strftime("%I %p")

    @sk_function(description="Get the current hour number", name="hourNumber")
    def hour_number(self) -> str:
        """
        Get the current hour number

        Example:
            {{time.hourNumber}} => 21
        """
        now = datetime.datetime.now()
        return now.strftime("%H")

    @sk_function(description="Get the current minute")
    def minute(self) -> str:
        """
        Get the current minute

        Example:
            {{time.minute}} => 15
        """
        now = datetime.datetime.now()
        return now.strftime("%M")

    @sk_function(description="Get the seconds on the current minute")
    def second(self) -> str:
        """
        Get the seconds on the current minute

        Example:
            {{time.second}} => 7
        """
        now = datetime.datetime.now()
        return now.strftime("%S")

    @sk_function(description="Get the current time zone offset", name="timeZoneOffset")
    def time_zone_offset(self) -> str:
        """
        Get the current time zone offset

        Example:
            {{time.timeZoneOffset}} => -08:00
        """
        now = datetime.datetime.now()
        return now.strftime("%z")

    @sk_function(description="Get the current time zone name", name="timeZoneName")
    def time_zone_name(self) -> str:
        """
        Get the current time zone name

        Example:
            {{time.timeZoneName}} => PST
        """
        now = datetime.datetime.now()
        return now.strftime("%Z")
