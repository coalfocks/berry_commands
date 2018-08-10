from command import Command

class Pizza (Command):
    def do(self):
        pizza_type = self.args[0]
        result = 'Ordering a {} pizza'.format(pizza_type)
        print(result)
        return result

