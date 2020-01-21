docker build -t image_service .
docker run -d --name mycontainer -p 8088:80 image_service
