# Copyright 2022 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
from fm.aicc_tools.ailog.log import service_logger


def set_cert(cert, cert_dict):
    """
    保存或刷新存量认证凭据
    """
    # 对认证信息明文进行组装
    cert_info = {
        'type': str(cert[0]),
        'ak': str(cert[1]),
        'sk': str(cert[2]),
        'endpoint': str(cert[3])
    }
    del cert
    update_info = {'scenario': cert_info}
    cert_dict.update(update_info)
    del cert_info
    del update_info


def get_cert(cert_dict, flatten_to_list=False):
    """
    获取认证凭据, 支持凭据平铺/字典映射模式
    """
    # 逐层获取认证信息
    if 'scenario' not in cert_dict:
        service_logger.error('scenario is missing in .fmrc file, check the file.')
        raise RuntimeError

    cert_info = cert_dict.get('scenario')
    del cert_dict

    if cert_info is None:
        service_logger.error('nothing in scenario, check the file.')
        raise RuntimeError

    cert_info_keys = list(cert_info.keys())

    if not cert_info_keys:
        service_logger.error('registry info in .fmrc file is empty, check the file.')
        raise RuntimeError

    for cert_info_value in cert_info.values():
        if cert_info_value is None:
            service_logger.error('find none value in .fmrc file, check the file.')
            raise RuntimeError
    del cert_info_value

    cert_type = cert_info.get('type')
    cert_ak = cert_info.get('ak')
    cert_sk = cert_info.get('sk')
    cert_endpoint = cert_info.get('endpoint')
    del cert_info

    cert = {'scenario': [cert_type, cert_ak, cert_sk, cert_endpoint]} if flatten_to_list else \
        {'scenario': {'type': cert_type, 'ak': cert_ak, 'sk': cert_sk, 'endpoint': cert_endpoint}}

    del cert_ak
    del cert_sk

    return cert
