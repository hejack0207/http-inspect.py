run:
	sudo $(shell which python) cli.py --filter='host 10.0.50.166'
summary:
	sudo $(shell which python) cli.py --filter='host 10.0.50.166' --summary
