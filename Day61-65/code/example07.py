import pymongo


# BSON - Binary JSON - dict
def main():
    # client = pymongo.MongoClient('mongodb://120.77.222.217:27017')
    client = pymongo.MongoClient(host='120.77.222.217', port=27017)
    db = client.zhihu
    pages_cache = db.webpages
    """
    pages_cache.insert_many([
        {'_id': 1, 'url': 'http://www.baidu.com', 'content': 'shit'},
        {'_id': 2, 'url': 'http://www.qq.com', 'content': 'another shit'},
        {'_id': 3, 'url': 'http://www.qfedu.com', 'content': 'biggest shit'}
    ])
    
    print(pages_cache.update({'_id': 5}, {'$set': {'content': 'hello, world!'}}, upsert=True))
    # page_id = pages_cache.insert_one({'url': 'http://www.baidu.com', 'content': '<html></html>'})
    # print(page_id.inserted_id)
    # print(pages_cache.remove({'url': 'http://www.baidu.com'}))
    print(pages_cache.find().count())
    for doc in pages_cache.find().sort('_id'):
        print(doc)
    """
    pages_cache.insert_one({
        'url': 'http://www.baidu.com',
        'content': 'bull shit!',
        'owner': {
            'name': 'Lee Yanhong',
            'age': 50,
            'idcard': '110220196804091203'
        }
    })


if __name__ == '__main__':
    main()
