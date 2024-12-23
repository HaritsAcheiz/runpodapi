from runpodapi import RunpodAPI
from converter import *
import os
from dotenv import load_dotenv

load_dotenv()

api = RunpodAPI(api_key=os.getenv("API_KEY_P"))

print(api.get_myself())

# fetch CPU
# CpuFilter = {"cpuId": "xyz789"}
# response_cpu = api.get_cpuTypes()
# cpu_df = cpu_to_pandas(response_cpu)
# cpu_df.to_csv('data/cpu.csv', index=False)

# fetch datacenter
# response_dc = api.get_datacenters()
# dc_df = dc_to_pandas(response_dc)
# dc_df.to_csv('data/dc.csv', index=False)

# fetch GPU
# GpuTypeFilter = {"Id": "xyz789"}
# response_gpu = api.get_gpuTypes()
# gpu_df = gpu_to_pandas(response_gpu)
# gpu_df.to_csv('data/gpu.csv', index=False)

# fetch pod
# PodFilter = {"podId": "xyz789"}
# response_pod = api.get_pods()
# pod_df = pod_to_pandas(response_pod)
# pod_df.to_csv('data/pod.csv', index=False)

# fetch cpu flavor
# SpecificsInput = {"dataCenterId": "CA-MTL-1"}
# response_cpu_flavor = api.get_cpu_flavor()
# cpu_flavor_df = cpu_flavor_to_pandas(response_cpu_flavor)
# cpu_flavor_df.to_csv('data/cpu_flavors.csv', index=False)

# fetch datacenter storage
# response_datacenter_storage = api.get_datacenter_storage()
# print(response_datacenter_storage)
# cpu_flavor_df = cpu_flavor_to_pandas(response_cpu_flavor)
# cpu_flavor_df.to_csv('data/cpu_flavors.csv', index=False)

# transform()