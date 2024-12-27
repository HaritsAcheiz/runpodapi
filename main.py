from runpodapi import RunpodAPI
from converter import *
import os
from dotenv import load_dotenv
import json

load_dotenv()

api = RunpodAPI(api_key=os.getenv("API_KEY_P"))

# print(api.get_myself())

# fetch CPU
# CpuFilter = {"cpuId": "xyz789"}
# response_cpu = api.get_cpuTypes()
# cpu_df = cpu_to_pandas(response_cpu)
# cpu_df.to_csv('data/cpu.csv', index=False)

# fetch datacenter
response_dc = api.get_datacenters()
# dc_df = dc_to_pandas(response_dc)
# dc_df.to_csv('data/dc.csv', index=False)

# fetch GPU
# GpuTypeFilter = {"Id": "xyz789"}
# response_gpu1 = api.get_gpuTypes()
# print(response_gpu1)
# gpu_df = gpu_to_pandas(response_gpu)
# gpu_df.to_csv('data/gpu.csv', index=False)

# fetch pod
# PodFilter = {"podId": "xyz789"}
# response_pod = api.get_pods()
# print(response_pod)
# pod_df = pod_to_pandas(response_pod)
# pod_df.to_csv('data/pod.csv', index=False)

# fetch cpu flavor
# SpecificsInput = {"dataCenterId": "EU-RO-1"}
# response_cpu_flavor = api.get_cpu_flavor(SpecificsInput=SpecificsInput)
# print(response_cpu_flavor)
# cpu_flavor_df = cpu_flavor_to_pandas(response_cpu_flavor)
# cpu_flavor_df.to_csv('data/cpu_flavors.csv', index=False)

# fetch machine
# response_machine = api.get_machine()
# pod_df = machine_to_pandas(response_machine)
# pod_df.to_csv('data/machine.csv', index=False)

# transform()

# fetch volumes
# response_volumes = api.get_volumes()
# print(response_volumes)
# volumes_df = machine_to_pandas(response_machine)
# pod_df.to_csv('data/machine.csv', index=False)

# fetch datacenter id
# response_dc = api.custom_get_datacenter()
# dc_df = custom_dc_to_pandas(response_dc)
# print(dc_df)
# print(response_dc)
datacenters = response_dc['data']['dataCenters']
with open('dc_location.json', 'r') as file:
	location_dim = json.load(file)

result = list()
for datacenter in datacenters:
	gpus = datacenter['gpuAvailability']
	gpuTypeIds = list()
	for gpu in gpus:
		gpuTypeIds.append(gpu['gpuTypeId'])
	gpu_count = 0
	gpu_count_limit = False
	while (gpu_count < 10) & (~gpu_count_limit):
		gpu_count += 1
		data = dict()
		# fetch gpu type by id
		gpuTypesInput = {"ids": gpuTypeIds}
		lowestPriceInput = {
			"gpuCount": gpu_count,
			"minDisk": 0,
			"minMemoryInGb": 8,
			"minVcpuCount": 2,
			"secureCloud": True,
			"compliance": None,
			"dataCenterId": datacenter['id'],
			"globalNetwork": False
		}
		response_gpu = api.get_gpuTypeById(lowestPriceInput=lowestPriceInput, gpuTypesInput=gpuTypesInput)
		gpuTypes = response_gpu['data']['gpuTypes']
		if gpuTypes:
			for gpuType in gpuTypes:
				data['provider'] = 'runpod'
				data['location'] = location_dim[datacenter['id'].rsplit('-', 1)[0]]
				networking = {
					'ports': None,
					'receive': None,
					'send': None
				}
				data['networking'] = networking
				if gpuType['lowestPrice']['minVcpu']:
					cpu = {
						'amount': gpu_count * gpuType['lowestPrice']['minVcpu'],
						'price': None,
						'type': None
					}
				else:
					cpu = {
						'amount': gpu_count * 0,
						'price': None,
						'type': None
					}
				gpu_details = {
					'amount': gpu_count,
					'price': gpuType['lowestPrice']['uninterruptablePrice']
				}
				gpu = {
					gpuType['id']: gpu_details
				}
				ram = {
					'amount': gpuType['lowestPrice']['minMemory'],
					'price': None
				}
				storage = {
					'amount': None,
					'price': None
				}
				status = {
					'listed': datacenter['listed'],
					'online': None,
					'report': None,
					'uptime': None
				}
				specs = {
					'cpu': cpu,
					'gpu': gpu,
					'ram': ram,
					'storage': storage,
					'status': status
				}
				data['specs'] = specs
				if gpuType['lowestPrice']['uninterruptablePrice']:
					result.append(data.copy())
				else:
					gpu_count_limit = True
		else:
			data['provider'] = 'runpod'
			data['location'] = location_dim[datacenter['id'].rsplit('-', 1)[0]]
			networking = {
				'ports': None,
				'receive': None,
				'send': None
			}
			data['networking'] = networking
			cpu = {
				'amount': None,
				'price': None,
				'type': None
			}
			gpu_details = {
				'amount': None,
				'price': None
			}
			gpu = {
				'unknown': gpu_details
			}
			ram = {
				'amount': None,
				'price': None
			}
			storage = {
				'amount': None,
				'price': None
			}
			status = {
				'listed': datacenter['listed'],
				'online': None,
				'report': None,
				'uptime': None
			}
			specs = {
				'cpu': cpu,
				'gpu': gpu,
				'ram': ram,
				'storage': storage,
				'status': status
			}
			data['specs'] = specs
			result.append(data.copy())
			gpu_count_limit = True

with open('current_result.json', 'w') as file:
	json.dump(result, fp=file, indent=4)

# fetch podTemplate
# podTemplate = {"id": "runpod-vscode"}
# response_pod = api.get_podTemplate(podTemplate)
# print(response_pod)

# fetch podTemplateId
# response_pod_id = api.get_podTemplateId()
# print(response_pod_id)
