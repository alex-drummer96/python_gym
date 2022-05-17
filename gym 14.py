class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars
    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('argument must be str')
        return args[0].strip(self.__chars)
ch = StripChars('!&? ')
res = ch('   dflgndbjnd!&?dfvjn   !&?')
print(res)
