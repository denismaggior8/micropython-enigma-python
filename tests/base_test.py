class BaseTest():

    flags = []
    
    def run(self):
        print("Running all test_* functions in {}".format(self.__class__.__name__))
        for name in dir(self.__class__):
            if name.startswith("test_"):
                method = getattr(self, name)
                if callable(method):
                    print(f"▶ Running {name}...")
                    self.set_up()
                    result = method()
                    self.tear_down()
                    self.flags.append((name, result))
        return self.flags                

    def set_up(self):
        pass
    
    def tear_down(self):
        pass