#!/bin/bash
# 
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
set -e

fm enable-verify -e false
fm registry

# modelarts
fm config --scenario modelarts --app_config obs://**/app_config_test.yaml
fm show
fm stop --job_id 1203c47b-05b0-4056-8364-5fe6ae1bde45
fm delete --job_id aaeeb71f-6f90-4cc1-a15f-f4890dd877f1
fm show --job_id 1203c47b-05b0-4056-8364-5fe6ae1bde45
fm job-status --job_id 1203c47b-05b0-4056-8364-5fe6ae1bde45

fm finetune --scenario modelarts  --app_config obs://**/app_config_test.yaml --model_config_path obs://**/model_config_test.yaml
fm stop --scenario modelarts --app_config obs://**/app_config_test.yaml --job_id 1203c47b-05b0-4056-8364-5fe6ae1bde45
fm delete --scenario modelarts --app_config obs://**/app_config_test.yaml --job_id aaeeb71f-6f90-4cc1-a15f-f4890dd877f1
fm show --scenario modelarts --app_config obs://**/app_config_test.yaml
fm show --scenario modelarts --app_config obs://**/app_config_test.yaml --job_id 1203c47b-05b0-4056-8364-5fe6ae1bde45
fm job-status --scenario modelarts --app_config obs://**/app_config_test.yaml --job_id 1203c47b-05b0-4056-8364-5fe6ae1bde45