#!/bin/bash

$KAFKA_HOME/bin/kafka-topics.sh --describe --zookeeper 10.30.3.2:2181,10.30.3.3:2181,10.30.4.4:2182
