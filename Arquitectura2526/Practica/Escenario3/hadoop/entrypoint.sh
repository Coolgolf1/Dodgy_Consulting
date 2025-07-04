#!/bin/bash
set -e

export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop

if [ "$HADOOP_NODE" = "namenode" ]; then
  # Formatear NameNode sólo si no está formateado
  if [ ! -d "/tmp/hadoop/dfs/name/current" ]; then
    echo "Formateando NameNode..."
    $HADOOP_HOME/bin/hdfs --config $HADOOP_CONF_DIR namenode -format -force
  fi
  echo "Arrancando NameNode..."
  exec $HADOOP_HOME/bin/hdfs --config $HADOOP_CONF_DIR namenode
else
  echo "Arrancando DataNode..."
  exec $HADOOP_HOME/bin/hdfs --config $HADOOP_CONF_DIR datanode
fi

