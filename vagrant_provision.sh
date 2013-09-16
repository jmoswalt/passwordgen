if [ -e "/home/vagrant/.provisioned" ] ; then
    echo "VM already provisioned. Remove /home/vagrant/.provisioned to force a new provision."
    exit 0
fi

echo "Provisioning"

apt-get install -y python-pip

echo "Provisioned on: `date`" >> /home/vagrant/.provisioned
