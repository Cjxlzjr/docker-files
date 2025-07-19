echo "Fixing HDFS permission issues..."

echo "Checking namenode status..."
docker-compose ps namenode

echo "Waiting for namenode to fully start..."
sleep 30

echo "Exiting safe mode..."
docker-compose exec namenode hdfs dfsadmin -safemode leave

echo "Checking current root directory permissions..."
docker-compose exec namenode hdfs dfs -ls /

echo "Changing root directory owner to hdfs..."
docker-compose exec namenode hdfs dfs -chown hdfs:hdfs /

echo "Setting root directory permissions..."
docker-compose exec namenode hdfs dfs -chmod 755 /

echo "Verifying permission changes..."
docker-compose exec namenode hdfs dfs -ls /

echo "Creating necessary directories..."
docker-compose exec namenode hdfs dfs -mkdir -p /user
docker-compose exec namenode hdfs dfs -mkdir -p /user/hue
docker-compose exec namenode hdfs dfs -mkdir -p /tmp
docker-compose exec namenode hdfs dfs -mkdir -p /user/hive/warehouse

echo "Setting directory permissions..."
docker-compose exec namenode hdfs dfs -chown hdfs:hdfs /user
docker-compose exec namenode hdfs dfs -chown hue:hue /user/hue
docker-compose exec namenode hdfs dfs -chmod 777 /tmp
docker-compose exec namenode hdfs dfs -chown hive:hive /user/hive
docker-compose exec namenode hdfs dfs -chown hive:hive /user/hive/warehouse

echo "Final permission verification..."
docker-compose exec namenode hdfs dfs -ls -la /
echo "HDFS permission fix completed!"
