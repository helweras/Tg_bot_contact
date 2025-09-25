class SwartzList:
    def __init__(self):
        self.swartz_list = []

    def add_in_list(self, user_id):
        if user_id not in self.swartz_list:
            self.swartz_list.append(user_id)
        else:
            return 'Уже в списке пидорасов'

    def out_swartz(self, user_id):
        if user_id in self.swartz_list:
            self.swartz_list.remove(user_id)
        else:
            return 'Нет в списке'
    def check_in_swartz(self, user_id):
        return user_id in self.swartz_list