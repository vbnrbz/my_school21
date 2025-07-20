SELECT 
	trials.trial_id,
	COUNT(measurements.trial_id) AS participants,
	SUM(CASE WHEN patients.gender = 'Male' THEN 1 ELSE 0 END) AS males,
	SUM(CASE WHEN patients.gender = 'Female' THEN 1 ELSE 0 END) AS females,
	ROUND(AVG(patients.age), 1) AS age,
	ROUND(AVG(CASE WHEN measurements.drug = 'Плацебо' THEN measurements.condition_score ELSE NULL END), 1) AS avg_placebo,
	round(AVG(CASE WHEN measurements.drug != 'Плацебо' THEN measurements.condition_score ELSE NULL END), 1) AS avg_real_drug,
	trials.trial_name
FROM
	trials
JOIN 
	measurements ON measurements.trial_id = trials.trial_id
JOIN
	patients ON measurements.patient_id  = patients.patient_id 	
GROUP BY 
	trials.trial_id
ORDER BY
	trials.trial_id;