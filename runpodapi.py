from httpx import Client
from dataclasses import dataclass
import os
from dotenv import load_dotenv

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
				response.raise_for_status()

				return response.json()
			except Exception as e:
				print(e)
				print(f'Retry...{str(i + 1)}/3')
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

	def get_gpuTypes(self, GpuTypeFilter=None):
		query = """
			query gpuTypes ($input: GpuTypeFilter) {
				gpuTypes(input: $input) {
					lowestPrice {
						gpuName
						gpuTypeId
						minimumBidPrice
						uninterruptablePrice
						minMemory
						minVcpu
						rentalPercentage
						rentedCount
						totalCount
						stockStatus
						minDownload
						minDisk
						minUpload
						countryCode
						supportPublicIp
						compliance
					}
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

		variables = {
			"input": GpuTypeFilter
		}

		return self.send_request(payload={"query": query, "variables": variables})

	def get_myself(self):
		query = """
			query myself {
				myself {
					pods {
						id
					}
					id
					authId
					email
					currentSpendPerHr
					machineQuota
					referralEarned
					signedTermsOfService
					spendLimit
					stripeSavedPaymentId
					stripeSavedPaymentLast4
					templateEarned
					multiFactorEnabled
					notifyPodsStale
					notifyPodsGeneral
					notifyLowBalance
					creditAlertThreshold
					notifyOther
				}
			}
		"""
		return self.send_request(payload={"query": query})

	def get_pods(self, PodFilter=None):
		query = """
			query pod($input: PodFilter) {
				pod(input: $input) {
					lowestBidPriceToResume
					aiApiId
					apiKey
					consumerUserId
					containerDiskInGb
					containerRegistryAuthId
					costMultiplier
					costPerHr
					createdAt
					adjustedCostPerHr
					desiredStatus
					dockerArgs
					dockerId
					env
					gpuCount
					gpuPowerLimitPercent
					gpus {
						id
					}
					id
					imageName
					lastStatusChange
					locked
					machineId
					memoryInGb
					name
					podType
					port
					ports
					registry {
						auth
					}
					templateId
					uptimeSeconds
					vcpuCount
					version
					volumeEncrypted
					volumeInGb
					volumeKey
					volumeMountPath
					lastStartedAt
					cpuFlavorId
					machineType
					slsVersion
					networkVolumeId
					cpuFlavor {
						id
					}
					machine {
						id
					}
					latestTelemetry {
						state
					}
					endpoint {
						id
					}
					networkVolume {
						id
					}
					savingsPlans {
						pod
					}
					runtime {
						container
					}
				}
			}
		"""

		variables = {
			"input": PodFilter
		}

		return self.send_request(payload={"query": query, "variables": variables})

	def get_datacenters(self):
		query = """
			query dataCenters {
				dataCenters {
					id
					name
					location
					storageSupport
					listed
					gpuAvailability{
						available
						stockStatus
						gpuTypeId
						gpuTypeDisplayName
						displayName
						id
					}
				}
			}
		"""

		return self.send_request(payload={"query": query})


if __name__ == '__main__':
	api = RunpodAPI(api_key=os.getenv('API_KEY'))
	print(api.get_cpuTypes())
	# print(api.get_myself())

	# GpuTypeFilter = {"Id": "xyz789"}
	print(api.get_gpuTypes())

	# PodFilter = {"podId": "xyz789"}
	# print(api.get_pods())

	print(api.get_datacenters())