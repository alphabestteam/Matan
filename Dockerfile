FROM tomcat:latest
COPY tomcat-users.xml /usr/local/tomcat/conf/

EXPOSE 8080