import json

null = 0
dicts = {
    "message": {
        "message_text": {
            "link_type": "1",
            "comment_img": "",
            "source": "1",
            "add_time": null,
            "content": "顺道，打个卡"
        },
        "link": {
            "link_type": "1",
            "identify_url": "1",
            "image_size": "0",
            "type_imgs": "1",
            "message_uuid": "4028814b60675bb901613c36d37076e7",
            "uuid": "722a0370ee7048eebd5781517aed13c2",
            "url": "https://resource-insight.newrank.cn/insight/android/2018/01/28/ab6f495c000d27b15babf6d3aba4ef73.jpg",
            "thumbnail_suffix": ""
        }
    }
}
mList = list(dicts['message']['link'].keys())
print('pic' not in mList)
# print(mList, type(mList))
