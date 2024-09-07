class ABC:
    def abc(self, a):
        x = 1
        for i in range(1, a + 1):
            print(x + 2)
            x += 2

# Creating an instance of the ABC class
obj = ABC()

# Calling the abc method on the instance
obj.abc(6)
