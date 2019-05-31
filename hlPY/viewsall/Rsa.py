# -*- encoding:utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto import Random
from happyPY import settings
# rsa算法生成实例
RANDOM_GENERATOR=Random.new().read
if __name__=='__main__':
    rsa = RSA.generate(1024, RANDOM_GENERATOR)
    # master的秘钥对的生成
    PRIVATE_PEM = rsa.exportKey()
    with open(settings.BASE_DIR+'/hlPY/statics/pem/master-private.pem', 'w+') as f:
        f.write(PRIVATE_PEM.decode())
    print(PRIVATE_PEM)
    PUBLIC_PEM = rsa.publickey().exportKey()
    print(PUBLIC_PEM)
    with open(settings.BASE_DIR+'/hlPY/statics/pem/master-public.pem', 'w+') as f:
        f.write(PUBLIC_PEM.decode())