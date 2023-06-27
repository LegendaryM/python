# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: obs_client.py
@time: 2023/6/8 15:05
"""

from obs import ObsClient # pip install esdk-obs-python
import time

access_key_id = 'A0MGG9DHKC6DBJXZZSZN'
secret_access_key = 'JplniUNAiuHAVZgYcwAMjdjcIeec3L99CDHEZ0hM'
server = 'http://obs.cn-east-3.myhuaweicloud.com'
bucket = 'digital-public'


def upload_to_obs(local_file, remote_file):
    print('------- start to upload obs', local_file)
    start = time.time()
    obsClient = None
    try:
        # 创建ObsClient实例
        obsClient = ObsClient(
            access_key_id=access_key_id,  # 刚刚下载csv文件里面的Access Key Id
            secret_access_key=secret_access_key,  # 刚刚下载csv文件里面的Secret Access Key
            server=server  # 这里的访问域名就是我们在桶的基本信息那里记下的东西
        )
        # 使用访问OBS
        # 调用putFile接口上传对象到桶内
        resp = obsClient.putFile(bucket, remote_file, file_path=local_file)
        if resp.status < 300:
            # 输出请求Id
            print('requestId:', resp.requestId, 'success, cost:', (time.time() - start), ' s')
            return resp['body']['objectUrl']
        else:
            print('errorCode:', resp.errorCode, ', errorMessage', resp.errorMessage)
    except Exception as e:
        print(e)
    finally:
        if not obsClient:
            obsClient.close()


if __name__ == '__main__':
    upload_to_obs(r'E:\temp\audiolearning-master\1686207304335.wav', r'vpp/temp/1686207304335.wav')