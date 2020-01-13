#!/bin/bash


echo " Welcome to openstack ."

echo "Active Deployments:"
openstack server list
echo " instance name:"
read INSTANCE_NAME
cho "Images:"
openstack image list
echo "  image name:"
read IMAGE_NAME
echo "Flavors:"
openstack flavor list
echo " flavor name:"
read FLAVOR_NAME
echo "Networks:"
openstack network list
echo "network name:"
read NETWORK_NAME
echo "Keypair:"
echo "  keypair name:"
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

