class Hash(object):
    def __init__(self, length) -> None:
        self.length = length
        self.data = {}
        self.hashcode = 0
        self.index = 0
        # for i in range(length):
        #     self.data[i] = []

    def getHashCode(self, key):
        if isinstance(key, str):
            for char in key:
                self.hashcode += ord(char)
            return self.hashcode
        else: raise Exception("string only")

    def convertToIndex(self, hashcode):
        self.index = hashcode % self.length
        return self.index

    def searchKey(self, index, key):
        # 안 만들어졌을 때 검색할경우 대처 기능 추가
        print(self.data[index])
        # if key in self.data[index]:
        #     return key
        # else: return NULL

    def put(self, key):
        hashcode = getHashCode(self, key)
        try:
            self.data[convertToIndex(self, hashcode)].append(key)
        except Exception as e:
            self.data[convertToIndex(self, hashcode)] = [key]
        # 중복 데이터 입력 방지 기능 추가

    def get(self, key):
        hashcode = getHashCode(self, key)
        index = convertToIndex(self, hashcode)
        return searchKey(self, index, key)



h = Hash(5)
# h.__dir__()
h.put("오명균ㄴㅎㅋㄷ")
h.get("오명균ㄴㅎㅋㄷ")