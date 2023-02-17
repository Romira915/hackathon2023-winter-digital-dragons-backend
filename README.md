# hackathon2023-winter-digital-dragons-backend

## Using

```Shell
cp .env.example .env
docker compose up -d --build
```

## API

- /api/releases
  - query param
    - limit: int

## prodction db restore

```Shell
docker compose exec mysql bash
mysqldump -p --databases digitaldragons > /mysql_dump.sql
exit
docker cp hackathon2023-winter-digital-dragons-backend-mysql-1:/mysql_dump.sql ./
scp mysql_dump.sql aws-ec2:~/
ssh aws-ec2 
mysql -u${USER} -h${HOST} -p < mysql_dump.sql
```
