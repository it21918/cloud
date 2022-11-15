# cloud

# 1. Install Kafka

## 1.1 Install java 
```
sudo apt update
sudo apt install default-jre
java -version
```

1.2 Set up JAVA_HOME variable
1.2.1 Setup environment variables by editing file ~/.bashrc.
vi ~/.bashrc 

1.2.2 Add the following environment variables:
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64

1.2.3 save the file
source ~/.bashrc

1.3
wget https://dlcdn.apache.org/kafka/3.3.1/kafka_2.12-3.3.1.tgz
1.4 Unzip the binary package to a installation folder.
tar -xvzf  kafka_2.13-3.2.0.tgz
1.5 Setup environment variables by editing file ~/.bashrc.
 vi ~/.bashrc
1.6 Add the following environment variables:
export KAFKA_HOME=~/kafka_2.13-3.2.0/
1.7 Save the file and source the changes.
source ~/.bashrc

2. Start Kafka
2.1 Start ZooKeeper services by running this command:
$KAFKA_HOME/bin/zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties
2.2 Open another WSL terminal and run the following command:
$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties
