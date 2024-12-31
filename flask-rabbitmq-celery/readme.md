docker-compose up --build
Access Services:

Flask App: http://localhost:5000
Submit a Task:
curl -X POST http://localhost:5000/process -H "Content-Type: application/json" -d "{\"data\": \"Sample Task\"}"
Make a GET request to fetch the result:
curl -X GET http://localhost:5000/result/3ca11a6a-62fb-42c3-8cd5-74508b2a0af5

RabbitMQ Management Interface: http://localhost:15672 (Use credentials: user/password)


Use curl or a REST client to send a POST request to /process.
Monitor Task:

Check the RabbitMQ management interface to see queued tasks.
Observe the Celery worker logs in the terminal to verify task processing.
Fetch Results (Optional):

Remove all stopped containers:
docker container prune

Remove all unused images (dangling images):
docker images prune

remove all images
docker images -q
for /f %i in ('docker images -q') do docker rmi %i
