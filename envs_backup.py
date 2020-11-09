import os
from datetime import datetime
import re

# envs_dir = r"dir containing conda envs folders"
# backups_dir = r"directory to store the backups"

envs_dir = r"/home/joao/anaconda3/envs"
backups_dir = r"/home/joao/Documents/python_envs_backups"

envs_names = [name for name in os.listdir(envs_dir) if os.path.isdir(os.path.join(envs_dir, name))]
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Cria diretório para backup do dia
current_date = datetime.now()
year_dir = os.path.join(backups_dir, str(current_date.year))
month_dir = os.path.join(year_dir, current_date.strftime('%B'))
day_dir = os.path.join(month_dir, str(current_date.day))

if not os.path.isdir(year_dir):
	os.mkdir(year_dir)
if not os.path.isdir(month_dir):
	os.mkdir(month_dir)
if not os.path.isdir(day_dir):
	os.mkdir(day_dir)

# Verifica quantos diretórios já tem mais de 1 ano
last_day = False
last_month = False
for root, dirs, files in os.walk(backups_dir):
	current_dir = os.path.basename(root)

	if re.match('\d{4}', current_dir):
		year = int(current_dir)

		if len(dirs) == 1:
			last_month = True
		else: 
			last_month = False

	elif current_dir in month_list:
		month_name = current_dir
		month_number = datetime.strptime(month_name, '%B').month

		if len(dirs) == 1:
			last_day = True
		else:
			last_day = False

	elif re.match('\d{1,2}', current_dir):
		day = int(current_dir)

	# Checa a data do diretório do dia
	if dirs == []:
		dir_date = datetime(year, month_number, day)
		date_diff = current_date - dir_date

		if date_diff.days > 365:
			for file in files:
				os.remove(os.path.join(root, file))
			os.rmdir(root)

			if last_day: 
				os.rmdir(os.path.dirname(root))

				if last_month:
					os.rmdir(os.path.dirname(os.path.dirname(root)))

# Faz o backup das envs na pasta do dia
for env in envs_names:
	env_file = os.path.join(day_dir, f'{env}.yml')
	os.system(f'conda activate {env} && conda env export > "{env_file}" && conda deactivate')

# Faz backup do ambiente base
base_env_file = os.path.join(day_dir, 'base.yml')
os.system(f'conda activate base && conda env export > "{base_env_file}" && conda deactivate')
