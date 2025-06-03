
class Utils:
    # x is often used for getting a field of an element (an element is often an object)
    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

