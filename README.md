### 项目简介

本 `docker-compose` 项目基于 [HoangNV2001/Docker-Hadoop-Hive-Spark-Zeppelin-Hue-Superset](https://github.com/HoangNV2001/Docker-Hadoop-Hive-Spark-Zeppelin-Hue-Superset) 项目进行修改和优化，供本人学习大数据平台相关组件的搭建与使用。

### 项目改动

* **Hue 配置优化** ：修复了 `hue.ini` 文件中的配置错误，使 Hue 服务能够正常启动并连接 Hadoop，hive。
* **替换 Hive 执行引擎为 Spark** ：为了提升性能并避免由于 MapReduce 与当前环境不兼容引发的警报，已将 Hive 的默认执行引擎改为 Spark。
* **新增 HDFS 权限修复脚本** ：添加了 `Fixing HDFS permission.bat` 脚本，用于修复 HDFS 根目录权限不足导致 Hue 报错的问题。

### Fixing HDFS permission.bat 的说明

当在 Hue 中出现如下错误提示：

> hadoop.hdfs_clusters.default.webhdfs_url当前值：http://namenode:9870/webhdfs/v1
> 文件系统根目录“/”应归“hdfs”所有

可运行根目录下的 `Fixing HDFS permission.bat` 文件，以自动修复根目录权限为 hdfs 所有者。

### 使用声明

⚠ **本项目不保证稳定性及安全性，仅供个人学习与测试使用，禁止用于生产环境。**

---

### Project Overview

This `docker-compose` project is a customized and improved version of [HoangNV2001/Docker-Hadoop-Hive-Spark-Zeppelin-Hue-Superset](https://github.com/HoangNV2001/Docker-Hadoop-Hive-Spark-Zeppelin-Hue-Superset), designed for personal learning and experimentation with big data infrastructure components.

### Modifications

* **Improved Hue Configuration** : Fixed issues in the `hue.ini` file that previously caused configuration errors, ensuring Hue starts properly and connects with Hadoop.
* **Replaced Hive Execution Engine with Spark** : To improve performance and prevent compatibility warnings triggered by MapReduce, the default Hive execution engine has been switched to Spark.
* **Added HDFS Permission Fix Script** : A `Fixing HDFS permission.bat` script is included to address root directory permission errors that may prevent Hue from operating correctly.

### About Fixing HDFS permission.bat

If you encounter the following error in Hue:

> hadoop.hdfs_clusters.default.webhdfs_url current value: http://namenode:9870/webhdfs/v1
> The file system root “/” should be owned by “hdfs”

You can run the `Fixing HDFS permission.bat` script from the root directory to fix the ownership of `/` to `hdfs`.

### Disclaimer

⚠ **This project is intended solely for educational and testing purposes. Stability and security are not guaranteed. Do not use in production environments.**
