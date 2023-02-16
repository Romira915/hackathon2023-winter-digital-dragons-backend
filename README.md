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



## Instruction for inseting csv data to mysql db.

```bash
docker exec -it xxxxx bash
```

```bash
mysql --local-infile=1 -u root -p
```

```sql
create database test;
```

```sql
create table release;
```

```sql
create table test_table1 ( body TEXT, company_id int, company_name TEXT, created_at TEXT, lead_paragraph TEXT, main_category_id int, main_category_name TEXT, main_image TEXT, main_image_fastly TEXT
, pr_type TEXT, release_id int, sub_category_id int, sub_category_name TEXT, subtitle TEXT, title TEXT, url TEXT );
```