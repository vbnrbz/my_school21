connection = "postgresql://postgres:qw12@localhost:5432/postgres"
task_1_sql = """select AVG(CASE WHEN measurements.drug = 'Плацебо' THEN measurements.condition_score END) - AVG(CASE WHEN measurements.drug != 'Плацебо' THEN measurements.condition_score end) from trials join measurements on measurements.trial_id = trials.trial_id group by trials.trial_id order by trials.start_date;"""
task_2_sql = """with date_bounds as (
	select max(m.measurement_date) as max_date, min(m.measurement_date) as min_date
	from measurements m
)
select
	sum(case when m.measurement_date = db.max_date and m.drug != 'Плацебо' then m.condition_score end) -
	sum(case when m.measurement_date = db.min_date and m.drug != 'Плацебо' then m.condition_score end) -
	(sum(case when m.measurement_date = db.max_date and m.drug = 'Плацебо' then m.condition_score end) -
	sum(case when m.measurement_date = db.min_date and m.drug = 'Плацебо' then m.condition_score end))
from 
	trials t
join
	measurements m on m.trial_id = t.trial_id 
join
	date_bounds db on 1 = 1
group by 
	t.trial_id
order by 
	t.start_date"""
