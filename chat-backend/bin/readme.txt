mvn clean package
mvn spring-boot:run
docker logs chat-backend

CREATE KEYSPACE IF NOT EXISTS chat_app
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
cqlsh localhost 9042