#!/bin/bash

echo ""
echo " Welcome to openstack deploying instance.."
echo ""

echo "Active Deployments:"
openstack server list
echo " Please enter an instance name:"
read INSTANCE_NAME

echo "Images:"
openstack image list
echo " Please enter an image name:"
read IMAGE_NAME

echo "Flavors:"
openstack flavor list
echo " Please enter a flavor name:"
read FLAVOR_NAME

echo "Networks:"
openstack network list
echo " Please enter a network name:"
read NETWORK_NAME

echo "Keypair:"
echo " Please enter a keypair name:"
read KEY_NAME
openstack keypair create $KEY_NAME >  ~/cloud/.ssh/$KEY_NAME
chmod 600 ~/cloud/.ssh/$KEY_NAME

openstack server create --key-name $KEY_NAME --image $IMAGE_NAME --flavor $FLAVOR_NAME --network $NETWORK_NAME $INSTANCE_NAME
sleep 20
FLOATING_IP=$(openstack floating ip create public | grep floating_ip_address | awk '{print $4}')

openstack server add floating ip $INSTANCE_NAME "$FLOATING_IP"

echo "******************************"
echo "Floating IP is: [$FLOATING_IP]"
echo "******************************"

echo "ssh -i ~/cloud/.ssh/$KEY_NAME ubuntu@$FLOATING_IP"

ssh -i ~/cloud/.ssh/$KEY_NAME ubuntu@"$FLOATING_IP"

