class Verify:

    @staticmethod
    def verify_same(expect,actual):
        if str(expect) == str(actual):
            return True
        else:
            return False

    @staticmethod
    def verify_exist(expect,actual):
        if expect in actual:
            return True
        else:
            return  False