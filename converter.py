import pandas as pd
import ast


def dc_to_pandas(response):
	print(response)
	datacenters = response['data']['dataCenters']
	records = list()

	for datacenter in datacenters:
		data = dict()
		data['id'] = datacenter['id']
		data['name'] = datacenter['name']
		data['location'] = datacenter['location']
		data['storage'] = datacenter['storage']
		data['storageSupport'] = datacenter['storageSupport']
		data['listed'] = datacenter['listed']
		availables = list()
		stock_status = list()
		type_ids = list()
		types = list()
		type_display_names = list()
		display_names = list()
		ids = list()
		for item in datacenter['gpuAvailability']:
			availables.append(item['available'])
			stock_status.append(item['stockStatus'])
			type_ids.append(item['gpuTypeId'])
			types.append(item['gpuType'])
			type_display_names.append(item['gpuTypeDisplayName'])
			display_names.append(item['displayName'])
			ids.append(item['id'])
		data['gpu_available'] = availables
		data['gpu_stockStatus'] = stock_status
		data['gpu_typeId'] = type_ids
		data['gpu_typeDisplayName'] = type_display_names
		data['gpu_displayName'] = display_names
		data['gpu_id'] = ids

		records.append(data.copy())

	dc_df = pd.DataFrame.from_records(records)

	return dc_df


def custom_dc_to_pandas(response):
	print(response)
	datacenters = response['data']['dataCenters']
	records = list()

	for datacenter in datacenters:
		data = dict()
		data['id'] = datacenter['id']
		data['location'] = datacenter['location']

		records.append(data.copy())

	dc_df = pd.DataFrame.from_records(records)

	return dc_df


def gpu_to_pandas(response):
	records = response['data']['gpuTypes']
	gpu_df = pd.DataFrame.from_records(records)

	return gpu_df


def cpu_to_pandas(response):
	records = response['data']['cpuTypes']
	cpu_df = pd.DataFrame.from_records(records)

	return cpu_df


def pod_to_pandas(response):
	print(response)


def cpu_flavor_to_pandas(response):
	records = response['data']['cpuFlavors']
	cpu_flavors_df = pd.DataFrame.from_records(records)

	return cpu_flavors_df


def machine_to_pandas(response):
	records = response['data']['machines']
	machines_df = pd.DataFrame.from_records(records)

	return machines_df
