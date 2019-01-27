# 说明

## 项目构建与解析

*系统及工程版本要求*

* Java7 及以上版本
* Spring Framework
* Maven 3.2

本文内容采用 Java 1.8.0_73、Sring Boot 1.3.7 调试通过

## springboot 配置文件加载顺序

1. 在命令行中传入的参数
2. SPRING_APPLICATION_JSON 中的属性。SPRING_APPLICATION_JSON 是以JSON格式配置在系统环境变量中的内容
3. java:comp/env 中的JNDI属性
4. Java的系统属性，可以通过System.getProperties() 获得的内容。
5. 操作系统的环境变量
6. 通过random.*配置的随机属性
7. 位于当前jar包之外，针对不同{profile}环境的配置文件内容，例如application-{profile}.properties

application-test.properties