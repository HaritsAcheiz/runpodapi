from runpodapi import RunpodAPI
from converter import dc_to_pandas, gpu_to_pandas
import os
from dotenv import load_dotenv

load_dotenv()

api = RunpodAPI(api_key=os.getenv("API_KEY_P"))
# print(api.get_cpuTypes())
# print(api.get_myself())

# GpuTypeFilter = {"Id": "xyz789"}
# print(api.get_gpuTypes())

# PodFilter = {"podId": "xyz789"}
# print(api.get_pods())

response = api.get_datacenters()
dc_df = dc_to_pandas(response)
print(dc_df.head())
