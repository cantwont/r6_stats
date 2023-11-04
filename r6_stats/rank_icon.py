rjson = {
    "COPPER V": "https://imgur.com/5tMUlN8.png",
    "COPPER IV": "https://imgur.com/4FOsKqM.png",
    "COPPER III": "https://imgur.com/w4Zdkc4.png",
    "COPPER II": "https://imgur.com/doJaPHP.png",
    "COPPER I": "https://imgur.com/zeNn2EQ.png",
    "BRONZE V": "https://imgur.com/kOlkE7n.png",
    "BRONZE IV": "https://imgur.com/yqPsmmv.png",
    "BRONZE III": "https://imgur.com/1rG4FpF.png",
    "BRONZE II": "https://imgur.com/9nl8uJx.png",
    "BRONZE I": "https://imgur.com/ehnXLcR.png",
    "SILVER V": "https://imgur.com/NpBtpuL.png",
    "SILVER IV": "https://imgur.com/dXqDtfu.png",
    "SILVER III": "https://imgur.com/qEOIIhw.png",
    "SILVER II": "https://imgur.com/T1gj0oX.png",
    "SILVER I": "https://imgur.com/57Xg7xm.png",
    "GOLD V": "https://i.imgur.com/7pThZFx.png",
    "GOLD IV": "https://imgur.com/0nc7epN.png",
    "GOLD III": "https://imgur.com/hQzavB2.png",
    "GOLD II": "https://imgur.com/JN4MRjp.png",
    "GOLD I": "https://imgur.com/C7Wr3Ty.png",
    "PLATINUM V": "https://i.imgur.com/YvAyy0s.png",
    "PLATINUM IV": "https://i.imgur.com/FYoAbTw.png",
    "PLATINUM III": "https://imgur.com/5xKwhhB.png",
    "PLATINUM II": "https://imgur.com/YrDuNNC.png",
    "PLATINUM I": "https://imgur.com/jHKSXxD.png",
    "EMERALD V": "https://i.imgur.com/PeFVREp.png",
    "EMERALD IV": "https://i.imgur.com/1cQEwv5.png",
    "EMERALD III": "https://i.imgur.com/wGANDF6.png",
    "EMERALD II": "https://i.imgur.com/4lcrJKS.png",
    "EMERALD I": "https://i.imgur.com/iL7fj41.png",
    "DIAMOND V": "https://i.imgur.com/J4k8G8m.png",
    "DIAMOND IV": "https://i.imgur.com/NpmJe5S.png",
    "DIAMOND III": "https://imgur.com/u7bnEA1.png",
    "DIAMOND II": "https://imgur.com/jo5YKVm.png",
    "DIAMOND I": "https://imgur.com/h94nQF3.png",
    "CHAMPION": "https://imgur.com/Q5Qpcmt.png",
    "UNRANKED": "https://imgur.com/PvLQN8r.png"
}

def get_rank_image(rname):
    if rname in rjson:
        return rjson[rname]
    else:
        return rjson["UNRANKED"]
