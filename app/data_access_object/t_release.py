def get_releases(limit: int = 100) -> list[dict]:
    press_release = []
    for _ in range(limit):
        press_release.append(
            {
                "company_name": "株式会社PR TIMES",
                "company_id": 1,
                "release_id": 1,
                "title": "[April Dream] 4月1日を夢の日に。1100社超が「夢」の発信に参加表明",
                "subtitle": "4月1日、企業の夢がプレスリリースで、個人の夢がSNSで順次発信されます。",
                "url": "https://prtimes.jp/main/html/rd/p/000001201.000000112.html",
                "lead_paragraph": "string",
                "body": "<p id=\"p-iframe-image-33626-1\"><span class=\"no-edit center\" contenteditable=\"false\" id=\"iframe-image-area-33626-1\" style=\"margin-left: 57.5px; margin-right: 57.5px;\" xx=\"prtimes\">...",
                "main_image": "https://prtimes.jp/i/112/1078/resize/d112-1078-443228-0.jpg",
                "main_image_fastly": "https://prcdn.freetls.fastly.net/release_image/112/1167/112-1167-3219ae855548b936461c3ec288263aed-722x378.png?format=jpeg&auto=webp&quality=85&width=1950&height=1350&fit=bounds",
                "main_category_id": 58,
                "main_category_name": "広告・宣伝・PR",
                "sub_category_id": 4,
                "sub_category_name": "ネットサービス",
                "pr_type": "商品サービス",
                "created_at": "2021-04-01 00:00"
            }
        )

    return press_release
