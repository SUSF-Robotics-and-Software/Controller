class CommandCreator:
    def __init__(self):
        self.commands = []
        self.class_source = {}

    def create_class_source(self, class_inst):  # create dict of classes and their names
        objs = class_inst.__subclasses__()
        for obj in objs:
            self.class_source[obj.__name__] = obj
        print(self.class_source)

    def construct(self, class_name):  # return a class of given name
        target_class = self.class_source[class_name]
        instance = target_class()
        return instance
