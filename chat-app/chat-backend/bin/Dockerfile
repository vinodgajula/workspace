FROM openjdk:18-jdk-slim
WORKDIR /app
COPY target/chat-backend-1.0.0.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
