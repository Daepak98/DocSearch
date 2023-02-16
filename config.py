import yaml

config = {}
with open("config.yml", 'rt') as f:
    config = yaml.safe_load(f)

# print(config)