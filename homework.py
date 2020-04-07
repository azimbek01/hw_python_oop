import datetime as dt


class Record:
    def __init__(self, amount, comment, date = None):
        
        if date is None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date() 
        self.amount = amount
        self.comment = comment


class Calculator:    
    def __init__(self, limit):

        self.limit = int(limit)
        self.records = []

    def add_record(self, Record):
        self.records.append(Record)

    def get_today_stats(self):
        today_stats = 0
        for record in self.records:
            if record.date == dt.datetime.now().date():
                today_stats += record.amount
        return today_stats
    
    def get_week_stats(self):
        week_stats = 0
        today_day = dt.datetime.now().date()
        for record in self.records:
            if today_day - record.date < dt.timedelta(weeks=1):
                week_stats += record.amount
        return week_stats
        

class CashCalculator(Calculator):
    USD_RATE = 76.45
    EURO_RATE = 84.32

    def get_today_cash_remained(self, currency):
        if currency == 'rub':
            cash_of_balance = float(abs(self.limit - self.get_today_stats()))
            currency_name = 'руб'
        elif currency == 'usd':
            cash_of_balance = abs(self.limit - self.get_today_stats()) / \
                                self.USD_RATE
            currency_name = 'USD'
        elif currency == 'eur':
            cash_of_balance = abs(self.limit - self.get_today_stats()) / \
                                self.EURO_RATE
            currency_name = 'Euro'

        if self.limit > self.get_today_stats():                
            return f'На сегодня осталось {round(cash_of_balance, 2)} ' \
                    f'{currency_name}'
        elif self.limit == self.get_today_stats():
            return 'Денег нет, держись'
        elif self.limit < self.get_today_stats():
            return f'Денег нет, держись: твой долг - ' \
                    f'{round(cash_of_balance, 2)} {currency_name}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calorie_balance = self.limit - self.get_today_stats()
        if calorie_balance > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более ' \
                    f'{calorie_balance} кКал'
        elif calorie_balance <= 0:
            return 'Хватит есть!'