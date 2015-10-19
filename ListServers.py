#!/usr/bin/python
# Script will list all instances, all security groups and their rules for desired profile
# Before using script, you need to create "profile" file, which is ~/.aws/credentials where you put your AWS keys like this:
#
# [dev]
# aws_access_key_id = *****
# aws_secret_access_key = *****
#===================================================
#18102015 by Roberto Carlos Reyes Fernandez @rctaptap
#====================================================

import boto.ec2
regiones = ["us-east-1","us-west-1","us-west-2","ap-northeast-1","ap-southeast-1","ap-southeast-2","eu-central-1","eu-west-1","sa-east-1"]
for region in regiones:

	conn=boto.ec2.connect_to_region(region)
	reservations = conn.get_all_instances()
	if reservations:
		print '==Servidores de ' + region + ' =='
		print '{| border="0" style="background:#ffffff" align="top" class="sortable wikitable"'
		print "|+ align=""center"" style=""background:DarkSlateBlue; color:white""|<big>'''AMAZON WEB'''</big>"
		print '! width="100 px" style="background:Lavender; color:Black"|SERVIDOR'
		print '! width="100 px" style="background:Lavender; color:Black"|IP PUBLICA'
		print '! width="100 px" style="background:Lavender; color:Black"|IP PRIVADA'
		print '! width="100 px" style="background:Lavender; color:Black"|LLAVE'
		print '! width="150 px" style="background:Lavender; color:Black"|ID'
		print '! width="400 px" style="background:Lavender; color:Black"|DESCRIPCION'
		print '! width="100 px" style="background:Lavender; color:Black"|SECURITY GROUPS'
		print '! width="100 px" style="background:Lavender; color:Black"|TIPO'
		print '! width="100 px" style="background:Lavender; color:Black"|SIS. OPERATIVO'
		print '|-'
	for res in reservations:
		for inst in res.instances:
			instanceType = conn.get_instance_attribute(inst.id,'instanceType')
			for group in inst.groups:
				sg = '|| ' + str(group.id) + " " + str(group.name) + " "
			ip = '|| ' + str(inst.ip_address) + ' '
			private_ip = '|| ' + str(inst.private_ip_address) + ' '
			key = '|| ' + str(inst.key_name) + ' '
			idec = '|| ' + str(inst.id) + ' '
			itype = '|| ' + str(inst.instance_type) + ' '
			if 'Name' in inst.tags:
				if inst.state == 'stopped':
					name= "|bgcolor=#FF0000|[[" + str(inst.tags['Name']) + ']]'
				else:
					name= "|bgcolor=#88ff00|[[" + str(inst.tags['Name']) + ']]'
			else:
				if inst.state == 'stopped':
					name= '|bgcolor=#FF0000|[[ NO NAME ]]'
				else:
					name= '|bgcolor=#88ff00|[[ NO NAME ]]'
			if 'Summary' in inst.tags:
				summ = '|| ' + str(inst.tags['Summary']) + ' '
			else:
				nosumm = '|| NO DESCRIPCION '
			if 'OS' in inst.tags:
				os = '|| ' + str(inst.tags['OS']) + ' '
			else:
				os = '|| NO OS '
			print "%s %s %s %s %s %s %s %s %s" % (name, ip, private_ip, key, idec, summ, sg, itype, os)
			print '|-'
	if reservations:
		print '|}'