#!/bin/bash
set -e

# Ruta donde guardas las configuraciones en tu repo
CONF_SRC="/home/manuel/proyecto3Telematica/hadoop-config"

# Ruta oficial donde Hadoop carga sus configuraciones
CONF_DST="$HADOOP_HOME/etc/hadoop"

echo "==> Copiando archivos de configuración a Hadoop..."

cp "$CONF_SRC/core-site.xml" "$CONF_DST/"
cp "$CONF_SRC/hdfs-site.xml" "$CONF_DST/"
cp "$CONF_SRC/mapred-site.xml" "$CONF_DST/"
cp "$CONF_SRC/yarn-site.xml" "$CONF_DST/"

echo "==> Configuración actualizada correctamente."