import pandas as pd


def dc_to_pandas(response):
	datacenters = response['data']['dataCenters']
	records = list()

	for datacenter in datacenters:
		data = dict()
		data['id'] = datacenter['id']
		data['name'] = datacenter['name']
		data['location'] = datacenter['location']
		data['storageSupport'] = datacenter['storageSupport']
		data['listed'] = datacenter['listed']
		availables = list()
		stock_status = list()
		type_ids = list()
		type_display_names = list()
		display_names = list()
		ids = list()
		for item in datacenter['gpuAvailability']:
			availables.append(item['available'])
			stock_status.append(item['stockStatus'])
			type_ids.append(item['gpuTypeId'])
			type_display_names.append(item['gpuTypeDisplayName'])
			display_names.append(item['displayName'])
			ids.append(item['id'])
		data['gpu_available'] = availables
		data['gpu_stock_status'] = stock_status
		data['gpu_type_id'] = type_ids
		data['gpu_type_display_name'] = type_display_names
		data['gpu_display_name'] = display_names
		data['gpu_id'] = ids

		records.append(data.copy())

	dc_df = pd.DataFrame.from_records(records)

	return dc_df


def gpu_to_pandas(response):
	datacenters = response['data']['dataCenters']
	records = list()

	for datacenter in datacenters:
		data = dict()
		data['provider'] = '' #datacenter['']

		location = {
			"city": '', #datacenter[''],
			"country": datacenter['location'],
			"region": '' #datacenter['']
		}
		data['location'] = location

		networking = {
			"ports": '', #datacenter[''],
			"receive": '', #datacenter[''],
			"send": '' #datacenter['']
		}
		data['networking'] = networking

		specs = {
			"cpu": {
				"amount": '', #datacenter[''],
				"price": '', #datacenter[''],
				"type": '' #datacenter['']
			},
			"gpu": {
				"model-name": {
					"amount": '', #datacenter[''],
					"price": '' #datacenter['']
				}
			},
			"ram": {
				"amount": '', #datacenter[''],
				"price": '' #datacenter['']
			},
			"storage": {
				"amount": '', #datacenter[''],
				"price": '', #datacenter['']
			}
		}
		data['specs'] = specs

		status = {
			"listed": datacenter['listed'],
			"online": '', #datacenter[''],
			"report": '', #datacenter[''],
			"uptime": '' #datacenter['']
		}
		data['status'] = status
		records.append(data.copy())

	return records


def cpu_to_pandas(response):
	datacenters = response['data']['dataCenters']
	records = list()

	for datacenter in datacenters:
		data = dict()
		data['provider'] = '' #datacenter['']

		location = {
			"city": '', #datacenter[''],
			"country": datacenter['location'],
			"region": '' #datacenter['']
		}
		data['location'] = location

		networking = {
			"ports": '', #datacenter[''],
			"receive": '', #datacenter[''],
			"send": '' #datacenter['']
		}
		data['networking'] = networking

		specs = {
			"cpu": {
				"amount": '', #datacenter[''],
				"price": '', #datacenter[''],
				"type": '' #datacenter['']
			},
			"gpu": {
				"model-name": {
					"amount": '', #datacenter[''],
					"price": '' #datacenter['']
				}
			},
			"ram": {
				"amount": '', #datacenter[''],
				"price": '' #datacenter['']
			},
			"storage": {
				"amount": '', #datacenter[''],
				"price": '', #datacenter['']
			}
		}
		data['specs'] = specs

		status = {
			"listed": datacenter['listed'],
			"online": '', #datacenter[''],
			"report": '', #datacenter[''],
			"uptime": '' #datacenter['']
		}
		data['status'] = status
		records.append(data.copy())

	return records