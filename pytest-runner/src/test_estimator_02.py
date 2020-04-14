import pytest

name = str(input())
avgAge = float(input())
avgDailyIncomeInUSD = float(input())
avgDailyIncomePopulation = float(input())
periodType = str(input())
timeToElapse = int(input())
reportedCases = int(input())
population = int(input())
totalHospitalBeds = int(input())

data = {
	'region': {
	'name': name,
	'avgAge': avgAge,
	'avgDailyIncomeInUSD': avgDailyIncomeInUSD,
	'avgDailyIncomePopulation': avgDailyIncomePopulation
  },
  'periodType': periodType,
  'timeToElapse': timeToElapse,
  'reportedCases': reportedCases,
  'population': population,
  'totalHospitalBeds': totalHospitalBeds
}

def test_challenge2():
	assert(data['timeToElapse']) == data['timeToElapse']
	assert(data['totalHospitalBeds']) == data['totalHospitalBeds']