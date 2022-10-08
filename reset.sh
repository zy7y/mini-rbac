docker rm -f mini-web mini-rbac
docker rmi -f mini-rbac_backend mini-rbac_frontend mini-rbac-backend mini-rbac-frontend
docker-compose up -d
