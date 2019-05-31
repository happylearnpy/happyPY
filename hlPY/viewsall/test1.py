from Crypto.PublicKey import RSA
import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import hlPY.viewsall.Rsa as rsa
from happyPY import settings



def jiemi(password):
    # 生成秘钥

    with open(settings.BASE_DIR+'/hlPY/statics/pem/master-private.pem') as f:
        key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    mw=cipher.decrypt(base64.b64decode(password),rsa.RANDOM_GENERATOR)
    print(mw)
    return mw.decode()

psd = b'Si6+7zGa012vOQWf/o2YKEFOFReJpUH1jeBqo0xJ+aIv5AruJGrKh+YVoiTzRboP/UFOT5VY8BggbOncE0S9EUfejY4L4LtJi4Kkju2bDpF0/om+jc3sRiAcp27xRuuxzfRfp/IVhojahy65f+OcWLCVxF2AMp5Ff8W3LO6Wxmw='
b = jiemi(psd)
password='itdUiRFRKF6Od7F/v00SpB9uYJ2WP70otlVmL5lXMTzDzCnmQiprlqMI0xujhVfm1bXZ/KSrrZCws+C7P0aKfmNLHFAE2KRuCNE2xSvCExBr4LLHFoKFEQD+1fEPzkq/1eEY8i/228BEtWH3y/dRvy+gqBYbyE1TtPidSVlLwbk='
a = jiemi(password)


