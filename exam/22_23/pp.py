class AnagramStr(str):
    def __new__(cls, content):
        instance = super().__new__(cls, ''.join(sorted(content)))
        return instance
    
print (AnagramStr("sister") == AnagramStr("resist")) # True
print (AnagramStr("sister")) # eirsst