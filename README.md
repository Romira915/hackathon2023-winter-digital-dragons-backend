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

## やりたかったこと
- 検索ボックスに文字を打つと、キーワードがサジェストされる機能。
- 注目度がまだ低いプレスリリースにラベルを付けて注目を集めること。
  - ユーザーの希望条件で絞り込みをしたあとにそれぞれのプレスリリースのPV数の偏差値を算出して、偏差値が40以下のプレスリリースに「まだ注目度が低い記事」というラベルを付けたり、まだ記事化されていない記事に「記事化されていない」ラベルを付ける。
  - プレスリリースのデータ（テキスト、画像枚数、画像、動画本数等）から、注目度が高いプレスリリース(ランキング上位かどうか、PV数が多い（偏差値60以上、Q3以上）、いいね数の多さ、記事化されているかなどで決める)を予測するように学習させたモデルに予測させた際、まだ注目を集めていないのにも関わらず、誤って注目度が高い(確信度も高く)と予測したプレスリリースを「掘り出し記事かも？」というラベルをつけて注目を集める。
