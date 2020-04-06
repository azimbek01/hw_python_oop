import datetime as dt


class Record:
    def __init__(self, amount, comment, date = ''):
        
        if len(date) > 0:
            date = dt.datetime.strptime(date, '%d.%m.%Y').date()   
        else:
           date = dt.datetime.now().date()

        self.amount = amount
        self.comment = comment
        self.date = date


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
        seven_days_ago = today_day - dt.timedelta(7)
        for record in self.records:
            if record.date == today_day or record.date < today_day:
                if record.date > seven_days_ago or record.date == seven_days_ago:
                    week_stats += record.amount
        return week_stats
        

class CashCalculator(Calculator):
    USD_RATE = 76.45
    EURO_RATE = 84.32
    def get_today_cash_remained(self, currency):
        if currency == 'rub':
            cash_of_balance_rub = float(abs(self.limit - self.get_today_stats()))
            if self.limit > self.get_today_stats():                
                return (f'На сегодня осталось {round(cash_of_balance_rub, 2)} руб')
            elif self.limit == self.get_today_stats():
                return ('Денег нет, держись')
            elif self.limit < self.get_today_stats():
                return (f'Денег нет, держись: твой долг - {round(cash_of_balance_rub, 2)} руб')                            
        elif currency == 'usd':
            cash_of_balance_usd = abs(self.limit - self.get_today_stats()) / self.USD_RATE
            if self.limit > self.get_today_stats():                
                return (f'На сегодня осталось {round(cash_of_balance_usd, 2)} USD')
            elif self.limit == self.get_today_stats():
                return ('Денег нет, держись')
            elif self.limit < self.get_today_stats():
                return (f'Денег нет, держись: твой долг - {round(cash_of_balance_usd, 2)} USD')
        elif currency == 'eur':
            cash_of_balance_eur = abs(self.limit - self.get_today_stats()) / self.EURO_RATE 
            if self.limit > self.get_today_stats():          
                return (f'На сегодня осталось {round(cash_of_balance_eur, 2)} Euro')
            elif self.limit == self.get_today_stats():
                return ('Денег нет, держись')
            elif self.limit < self.get_today_stats():
                return (f'Денег нет, держись: твой долг - {round(cash_of_balance_eur, 2)} Euro') 


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calorie_balance = self.limit - self.get_today_stats()
        if self.limit > self.get_today_stats():
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calorie_balance} кКал')
        elif self.limit <= self.get_today_stats():
            return ('Хватит есть!')


# для CashCalculator 
cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment="Безудержный шопинг", date="08.03.2019"))
cash_calculator.add_record(Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019"))
cash_calculator.add_record(Record(amount=545, comment="Катание на такси"))

cash_calculator.get_today_stats()
cash_calculator.get_week_stats()
cash_calculator.get_today_cash_remained('rub')
cash_calculator.get_today_cash_remained('usd')
cash_calculator.get_today_cash_remained('eur')

# для CaloriesCalculator
calories_calculator = CaloriesCalculator(2500)
calories_calculator.add_record(Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019"))
calories_calculator.add_record(Record(amount=84, comment="Йогурт.", date="23.02.2019"))
calories_calculator.add_record(Record(amount=1140, comment="Баночка чипсов."))

calories_calculator.get_calories_remained()
