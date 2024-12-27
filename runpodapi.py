from httpx import Client
from dataclasses import dataclass
import os
from dotenv import load_dotenv
import time

load_dotenv()


@dataclass
class RunpodAPI:
	base_api: str = 'https://api.runpod.io/graphql'
	api_key: str = None

	def send_request(self, payload):
		for i in range(3):
			try:
				with Client() as client:
					response = client.post(self.base_api, params={'api_key': self.api_key}, json=payload)

				return response.json()
			except Exception as e:
				print(e)
				print(f'Retry...{str(i + 1)}/3')
				time.sleep(3)
				continue

		print('Request Failed')

	def get_cpuTypes(self):
		query = """
			query cpuTypes {
				cpuTypes {
					id
					displayName
					manufacturer
					cores
					threadsPerCore
					groupId
				}
			}
		"""

		return self.send_request(payload={"query": query})

	def get_gpuTypes(self):
		query = """
			query gpuTypes{
				gpuTypes{
					maxGpuCount
					maxGpuCountCommunityCloud
					maxGpuCountSecureCloud
					minPodGpuCount
					id
					displayName
					manufacturer
					memoryInGb
					cudaCores
					secureCloud
					communityCloud
					securePrice
					communityPrice
					oneMonthPrice
					threeMonthPrice
					sixMonthPrice
					oneWeekPrice
					communitySpotPrice
					secureSpotPrice
				}
			}
		"""

		return self.send_request(payload={"query": query})

	def get_myself(self):
		query = """
			query myself {
				myself {
					id
					pods{
						id
					}
					machines{
						id
					}
					machinesSummary{
						id
					}
					authId
					email
					containerRegistryCreds{
						id
					}
					currentSpendPerHr
					machineQuota
					referralEarned
					signedTermsOfService
					spendLimit
					stripeSavedPaymentId
					stripeSavedPaymentLast4
					templateEarned
					multiFactorEnabled
					machineEarnings{
						machineId
					}
					datacenters{
						id
						name
						location
						storage{
							hostname
							ips
							pw
							type
							user
						}
						storageSupport
						listed
						gpuAvailability{
							available
							stockStatus
							gpuTypeId
							gpuType{
								maxGpuCount
								maxGpuCountCommunityCloud
								maxGpuCountSecureCloud
								minPodGpuCount
								id
								displayName
								manufacturer
								memoryInGb
								cudaCores
								secureCloud
								communityCloud
								securePrice
								communityPrice
								oneMonthPrice
								threeMonthPrice
								sixMonthPrice
								oneWeekPrice
								communitySpotPrice
								secureSpotPrice
							}
						}
						compliance
					}
				}
			}
		"""
		return self.send_request(payload={"query": query})

	def get_pods(self, PodFilter=None):
		query = """
			query pod{
				pod{
					id
				}
			}
		"""

		return self.send_request(payload={"query": query})

	def get_datacenters(self):
		query = """
			query dataCenters {
				dataCenters {
					id
					name
					location
					storage{
						hostname
						ips
						pw
						type
						user
						list{
							mnt
							pw
							servers
							type
							versions
							primary
						}
					}
					storageSupport
					listed
					gpuAvailability{
						available
						stockStatus
						gpuTypeId
						gpuType{
							maxGpuCount
							maxGpuCountCommunityCloud
							maxGpuCountSecureCloud
							minPodGpuCount
							id
							displayName
							manufacturer
							memoryInGb
							cudaCores
							secureCloud
							communityCloud
							securePrice
							communityPrice
							oneMonthPrice
							threeMonthPrice
							sixMonthPrice
							oneWeekPrice
							communitySpotPrice
							secureSpotPrice
						}
						gpuTypeDisplayName
						displayName
						id
					}
					compliance
				}
			}
		"""

		return self.send_request(payload={"query": query})

	def get_cpu_flavor(self, SpecificsInput=None):
		query = """
			query cpuFlavors($input: SpecificsInput){
				cpuFlavors{
					id
					groupId
					groupName
					displayName
					minVcpu
					maxVcpu
					vcpuBurstable
					ramMultiplier
					diskLimitPerVcpu
					specifics(input: $input){
						stockStatus
						securePrice
						slsPrice
					}
				}
			}
		"""
		variables = {
			"input": SpecificsInput
		}

		return self.send_request(payload={"query": query, "variables": variables})

	def get_machine(self):
		query = """
			query machines {
				machines {
					machineType
					gpuTypeId
					gpuTotal
					cpuTypeId
					cpuCount
					memoryTotal
					diskTotal
					vcpuTotal
					secureCloud
					gpuCloudPrice
					location
				}
			}
		"""

		return self.send_request(payload={"query": query})

	def get_podTemplateId(self):
		query = """
			query podTemplates{
				podTemplates{
					id
				}
			}
		"""

		return self.send_request(payload={"query": query})

	def get_gpuTypeById(self, lowestPriceInput, gpuTypesInput):
		query = """
			query SecureGpuTypes($lowestPriceInput: GpuLowestPriceInput, $gpuTypesInput: GpuTypeFilter) {
				gpuTypes (input: $gpuTypesInput){
					lowestPrice(input: $lowestPriceInput) {
						minimumBidPrice
						uninterruptablePrice
						minVcpu
						minMemory
						stockStatus
						compliance
						maxUnreservedGpuCount
						__typename
					}
					id
					displayName
					memoryInGb
					securePrice
					communityPrice
					oneMonthPrice
					oneWeekPrice
					threeMonthPrice
					sixMonthPrice
					secureSpotPrice
					__typename
				}
			}
		"""

		variables = {
			"gpuTypesInput": gpuTypesInput,
			"lowestPriceInput": lowestPriceInput
		}

		return self.send_request(payload={"query": query, "variables": variables})

	def get_podTemplate(self, podTemplate):
		query = """
			query getPodTemplate($id: String!) {
				podTemplate(id: $id) {
					advancedStart
					containerDiskInGb
					containerRegistryAuthId
					dockerArgs
					env {
						key
						value
						__typename
					}
					id
					imageName
					isPublic
					isServerless
					name
					ports
					readme
					startJupyter
					startScript
					startSsh
					volumeInGb
					volumeMountPath
					category
					__typename
				}
			}
		"""

		variables = podTemplate

		return self.send_request(payload={"query": query, "variables": variables})

	# customs
	def custom_get_datacenter(self):
		query = """
			query dataCenters {
				dataCenters {
					id
					location
					listed
				}
			}
		"""

		return self.send_request(payload={"query": query})


if __name__ == '__main__':
	api = RunpodAPI(api_key=os.getenv('API_KEY'))
	# print(api.get_cpuTypes())
	# print(api.get_myself())

	# GpuTypeFilter = {"Id": "xyz789"}
	# print(api.get_gpuTypes())

	# PodFilter = {"podId": "xyz789"}
	# print(api.get_pods())

	# print(api.get_datacenters())
