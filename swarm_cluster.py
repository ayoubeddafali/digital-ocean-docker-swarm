import digitalocean
import os, sys 
import warnings
warnings.filterwarnings("ignore")


DIGITAL_OCEAN_TOKEN = os.getenv("DO_TOKEN")

manager = digitalocean.Manager(token=DIGITAL_OCEAN_TOKEN)

my_droplets = manager.get_all_droplets()

for droplet in my_droplets:
    print("ID: {} \n Distributio : {} \n Name: {} \n Memory : {}".format(droplet.id, droplet.image["distribution"], droplet.name, droplet.memory))