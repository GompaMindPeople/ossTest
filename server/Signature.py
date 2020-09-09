import hashlib
import hmac


class Signature:
    def makeSign(self, params, secret_key):
        params = sorted(params.items())
        query = ""
        for key in params:
            if key[0] != 'sign' and key[1] != '':
                query += (str(key[0]) + '=' + str(key[1]) + '&')
        query += "key=" + secret_key
        sign = hashlib.md5(query.encode('utf-8')).hexdigest().upper().encode('utf-8')
        sign = hmac.new(secret_key.encode('utf-8'), sign, hashlib.sha256).hexdigest().upper()
        return sign

    def verifySign(self, params, sign, secret_key):
        _sign = Signature.makeSign(params, secret_key)
        return _sign == sign

# if __name__ == '__main__':
#     print(Signature.makeSign(params={"hello": "nihao", "aa": "233", "bb": "cc", "ab": "fff"}, secret_key="123456"))
#     print(Signature.verifySign(params={"hello": "nihao", "aa": "233", "bb": "cc", "ab": "fff"},
#                                sign="5D9028327FC6AEA1C426D6688D6FC071D9281479251E753C11768E8CD24980A3",
#                                secret_key="123456"))
