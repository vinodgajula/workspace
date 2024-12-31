docker build -t fastapi-app .

docker run -d -p 8000:8000 fastapi-app

http://localhost:8000

docker ps

docker logs b7d5af70b999

docker cp b7d5af70b999:/app "D:\vinod\docker copy local"

docker ps -a

docker rm b1c180613a3b




