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

data = {}
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



DataInput = {}
Estimate = {}
DataInput = data
Estimate['data'] = data


def test_challenge1():
	assert(data['periodType']) == data['periodType']
	assert(data['reportedCases']) == data['reportedCases']

def test_challenge2():
	assert(data['timeToElapse']) == data['timeToElapse']
	assert(data['totalHospitalBeds']) == data['totalHospitalBeds']

def test_challenge3():
	assert(data['region']['avgDailyIncomeInUSD']) == data['region']['avgDailyIncomeInUSD']
	assert(data['region']['avgDailyIncomePopulation']) == data['region']['avgDailyIncomePopulation']

def estimator(data):

	currently_infected = data['reportedCases'] * 10
	impact = currently_infected
	severe_impact = data['reportedCases'] * 50

	if data['periodType'] == "days":
		if data['timeToElapse'] > 0:

			#challenge one
			factor = int(data['timeToElapse'] / 3)
			impact_infections_by_requested_time = int(impact * (2**factor))
			severe_impact_infections_by_requested_time = int(severe_impact * (2**factor))

			#challenge two
			severe_cases_by_requested_time = int((15 * impact_infections_by_requested_time) / 100)
			#reported_cases_by_requested_time = int(reported_cases * (2**factor))
			#severe_cases_by_requested_time = int((15 * reported_cases_by_requested_time) / 100)
			sixty_five_percent_hospital_bed = int((65 * data['totalHospitalBeds'] ) / 100)
			# ninety_percent_hospital_bed = int((90 * data['totalHospitalBeds']) / 100)
			# ninety_five_percent_hospital_bed = int((95 * data['totalHospitalBeds']) / 100)
			# thirty_five_percent_hospital_bed = int((35 * data['totalHospitalBeds']) / 100)

			currently_available_hospital_bed = int(data['totalHospitalBeds'] - sixty_five_percent_hospital_bed)
			hospital_beds_by_requested_time = int(currently_available_hospital_bed - severe_cases_by_requested_time)


			#challenge three
			cases_for_icu_by_requested_time = int((5 * impact_infections_by_requested_time) / 100)
			#reported_cases_by_requested_time = int(reported_cases * (2**factor))
			#cases_for_icu_by_requested_time = int((5 * reported_cases_by_requested_time) / 100)
			cases_for_ventilators_by_requested_time = int((2 * impact_infections_by_requested_time) / 100)
			#reported_cases_by_requested_time = int(reported_cases * (2**factor))
			#cases_for_icu_by_requested_time = int((2 * reported_cases_by_requested_time) / 100)

			if data['timeToElapse'] != 30:

				time_duration = data['timeToElapse']
				
				dollars_in_flight = int(data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation'] * time_duration)

			elif data['timeToElapse'] == 30:

				time_duration = 30
				dollars_in_flight = int(data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation'] * time_duration)
			else:

				print("Error, Please select a number of days")
		else:
			print("Error!, insert number of days to check")

	elif data['periodType'] == "weeks":
		if data['timeToElapse'] > 0:
			
			#challenge one
			convert_weeks_to_days = int(data['timeToElapse'] * 7)
			factor = int(convert_weeks_to_days / 3)
			impact_infections_by_requested_time = int(impact * (2**factor))
			severe_impact_infections_by_requested_time = int(severe_impact * (2**factor))

			#challenge two
			severe_cases_by_requested_time = int((15 * impact_infections_by_requested_time) / 100)
			#reported_cases_by_requested_time = int(reported_cases * (2**factor))
			#severe_cases_by_requested_time = int((15 * reported_cases_by_requested_time) / 100)
			sixty_five_percent_hospital_bed = int((65 * data['totalHospitalBeds'] ) / 100)
			# ninety_percent_hospital_bed = int((90 * data['totalHospitalBeds']) / 100)
			# ninety_five_percent_hospital_bed = int((95 * data['totalHospitalBeds']) / 100)
			# thirty_five_percent_hospital_bed = int((35 * data['totalHospitalBeds']) / 100)

			currently_available_hospital_bed = int(data['totalHospitalBeds'] - sixty_five_percent_hospital_bed)
			hospital_beds_by_requested_time = int(currently_available_hospital_bed - severe_cases_by_requested_time)

			#challenge three
			cases_for_icu_by_requested_time = int((5 * impact_infections_by_requested_time) / 100)
			#reported_cases_by_requested_time = int(reported_cases * (2**factor))
			#cases_for_icu_by_requested_time = int((5 * reported_cases_by_requested_time) / 100)
			cases_for_ventilators_by_requested_time = int((2 * impact_infections_by_requested_time) / 100)
			#reported_cases_by_requested_time = int(reported_cases * (2**factor))
			#cases_for_icu_by_requested_time = int((2 * reported_cases_by_requested_time) / 100)

			if data['timeToElapse'] > 0:

				time_duration = int(data['timeToElapse'] * 7)
				
				dollars_in_flight = int(data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation'] * time_duration)

			elif data['timeToElapse'] == 4:

				time_duration = 30
				dollars_in_flight = int(data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation'] * time_duration)
			else:

				print("Error, Please select the number of weeks")

		else:
			print("Error!, insert the number of weeks to check")


	elif data['periodType'] == "months":
		if data['timeToElapse'] > 0:


			#challenge one
			convert_months_to_days = int(data['timeToElapse'] * 30)
			factor = int(convert_months_to_days / 3)
			impact_infections_by_requested_time = int(impact * (2**factor))
			severe_impact_infections_by_requested_time = int(severe_impact * (2**factor))

			#challenge two
			severe_cases_by_requested_time = int((15 * impact_infections_by_requested_time) / 100)
			#reported_cases_by_requested_time = int(reported_cases * (2**factor))
			#severe_cases_by_requested_time = int((15 * reported_cases_by_requested_time) / 100)
			sixty_five_percent_hospital_bed = int((65 * data['totalHospitalBeds'] ) / 100)
			# ninety_percent_hospital_bed = int((90 * data['totalHospitalBeds']) / 100)
			# ninety_five_percent_hospital_bed = int((95 * data['totalHospitalBeds']) / 100)
			# thirty_five_percent_hospital_bed = int((35 * data['totalHospitalBeds']) / 100)

			currently_available_hospital_bed = int(data['totalHospitalBeds'] - sixty_five_percent_hospital_bed)
			hospital_beds_by_requested_time = int(currently_available_hospital_bed - severe_cases_by_requested_time)

			#challenge three
			cases_for_icu_by_requested_time = int((5 * impact_infections_by_requested_time) / 100)
			#reported_cases_by_requested_time = int(reported_cases * (2**factor))
			#cases_for_icu_by_requested_time = int((5 * reported_cases_by_requested_time) / 100)
			cases_for_ventilators_by_requested_time = int((2 * impact_infections_by_requested_time) / 100)
			#reported_cases_by_requested_time = int(reported_cases * (2**factor))
			#cases_for_icu_by_requested_time = int((2 * reported_cases_by_requested_time) / 100)

			if data['timeToElapse'] > 0:

				time_duration = int(data['timeToElapse'] * 30)
				
				dollars_in_flight = int(data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation'] * time_duration)

			elif data['timeToElapse'] == 1:

				time_duration = 30
				dollars_in_flight = int(data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation'] * time_duration)
			else:

				print("Error, Please select a number of days")
		else:
			print("Error!, insert the number of months to check")
			

	else:
		print("Error!, You did not select any Period Type")
		
	
	
	data = { 'ChallengeOne':{'impact': impact_infections_by_requested_time, 'severeimpact': severe_impact_infections_by_requested_time},
			'ChallengeTwo':{'severecases': severe_cases_by_requested_time, 'availablebeds': currently_available_hospital_bed, 'estimatebeds': hospital_beds_by_requested_time},
			'ChallengeThree':{'icucare': cases_for_icu_by_requested_time, 'ventilators': cases_for_ventilators_by_requested_time, 'dollarsinflight': dollars_in_flight}




	}
	
	return data
	

print(estimator(data))

