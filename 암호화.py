from cryptography.fernet import Fernet


# 간단한 암호화/복호화 클래스를 정의합니다.
class SimpleEnDecrypt:
    # 초기화 메서드, key가 없을 경우 새로운 키를 생성합니다.
    def __init__(self, key=None):
        if key is None:  # 키가 주어지지 않은 경우
            key = Fernet.generate_key()  # 새 키를 생성합니다.
        self.key = key  # 키를 클래스 변수로 저장합니다.
        self.f = Fernet(self.key)  # Fernet 객체를 생성합니다.
    
    # 데이터 암호화 메서드
    def encrypt(self, data, is_out_string=True):
        if isinstance(data, bytes):  # 입력 데이터가 바이트 형태일 경우
            ou = self.f.encrypt(data)  # 바로 암호화합니다.
        else:
            ou = self.f.encrypt(data.encode('utf-8'))  # 문자열이면 UTF-8로 인코딩 후 암호화합니다.
        if is_out_string is True:  # 출력이 문자열 형태로 요청된 경우
            return ou.decode('utf-8')  # 암호화된 바이트 데이터를 문자열로 디코딩하여 반환합니다.
        else:
            return ou  # 출력이 바이트 형태로 요청된 경우 그대로 반환합니다.
        
    # 데이터 복호화 메서드
    def decrypt(self, data, is_out_string=True):
        if isinstance(data, bytes):  # 입력 데이터가 바이트 형태일 경우
            ou = self.f.decrypt(data)  # 바로 복호화합니다.
        else:
            ou = self.f.decrypt(data.encode('utf-8'))  # 문자열이면 UTF-8로 인코딩 후 복호화합니다.
        if is_out_string is True:  # 출력이 문자열 형태로 요청된 경우
            return ou.decode('utf-8')  # 복호화된 바이트 데이터를 문자열로 디코딩하여 반환합니다.
        else:
            return ou  # 출력이 바이트 형태로 요청된 경우 그대로 반환합니다.


# SimpleEnDecrypt 클래스의 인스턴스를 생성합니다.
simpleEnDecrypt = SimpleEnDecrypt()

# 사용자가 입력한 평문 데이터를 받아옵니다.
plain_text = input()
print(plain_text)  # 평문 데이터를 출력합니다.

# 평문 데이터를 암호화합니다.
encrypt_text = simpleEnDecrypt.encrypt(plain_text)
print(encrypt_text)  # 암호화된 데이터를 출력합니다.

# 암호화된 데이터를 복호화합니다.
decrypt_text = simpleEnDecrypt.decrypt(encrypt_text)
print(decrypt_text)  # 복호화된 데이터를 출력합니다.
