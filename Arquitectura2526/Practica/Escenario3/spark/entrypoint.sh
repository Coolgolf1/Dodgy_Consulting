#!/bin/bash

if [ "$SPARK_ROLE" = "master" ]; then
  $SPARK_HOME/sbin/start-master.sh && tail -f $SPARK_HOME/logs/spark--org.apache.spark.deploy.master.*
elif [ "$SPARK_ROLE" = "worker" ]; then
  $SPARK_HOME/sbin/start-worker.sh spark://spark-master:7077 && tail -f $SPARK_HOME/logs/spark--org.apache.spark.deploy.worker.*
fi
