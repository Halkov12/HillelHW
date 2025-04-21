# def age(self):
#     if self.birth_date:
#         return datetime.datetime.now().year - self.birth_date.year

# Не береться до уваги поточна дата і місяць.
# Тому, якщо студент народився пізніше в році, ніж поточна дата, обчислений вік буде неправильним.

# def age(self):
#     if self.birth_date:
#         today = datetime.date.today()
#         age = today.year - self.birth_date.year
#         if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
#             age -= 1
#         return age

