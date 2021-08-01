class position():
    dic = dict()
    def set(self, key1, key2, val):
        if key1 not in self.dic:
            self.dic[key1] = {key2: val}
        else:
            self.dic[key1][key2] = val
    def get(self, key1, key2):
        if key1 not in self.dic:
            return None
        if key2 not in self.dic[key1]:
            return None
        return self.dic[key1][key2]
    def print(self, *key):
        _len = len(key)
        if _len == 0:
            print (f'[dictionary] position:')
            print (' - ', self.dic)
        elif _len == 1:
            print (f'[dictionary] position["{key[0]}"]:')
            for x, y in self.dic[key[0]].items():
                print(' - ', x, y)
        else:
            print (f'[dictionary] position["{key[0]}"]["{key[1]}"]:')
            print (' - ', self.dic[key[0]][key[1]])

class region():
    dic = dict()
    def set(self, xywh, *key):
        _len = len(key)
        if not _len:
            print ('[dictionary] region set ERROR')
            return
        _dic = {key[-1]: xywh}
        if _len == 1:
            self.dic = _dic
            return
        if _len > 2:
            for i in reversed(range(1, _len-1)):
                _dic = {key[i]: _dic}
        if key[0] in self.dic:
            print('exist', self.dic[key[0]])
            self.dic[key[0]] = [self.dic[key[0]], _dic]
        else:
            self.dic[key[0]] = _dic

    def print(self, *key):
        print (f'[dictionary] region:')
        _len = len(key)
        if _len == 0:
            print (' - ', self.dic)
            return
        _dic = self.dic[key[0]]
        if _len == 1:
            print (' - ', _dic)
        elif _len >= 2:
            for i in range(1, _len-1):
                _dic = _dic[key[i]]
            print (' - ', _dic[key[-1]])