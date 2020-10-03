from time import sleep

from myutils import coroutine


@coroutine
def create_delivery_man(name, capacity=1):
    buffer = []
    while True:
        size = 0
        while size < capacity:
            pkg_name = yield
            if pkg_name:
                size += 1
                buffer.append(pkg_name)
                print('%s正在接受%s' % (name, pkg_name))
            else:
                break
        print('=====%s正在派送%d件包裹=====' % (name, len(buffer)))
        sleep(3)
        buffer.clear()


def create_package_center(consumer, max_packages):
    num = 0
    while num <= max_packages:
        print('快递中心准备派送%d号包裹' % num)
        consumer.send('包裹-%d' % num)
        num += 1
        if num % 10 == 0:
            sleep(5)
    consumer.send(None)


def main():
    print(create_delivery_man.__name__)
    dm = create_delivery_man('王大锤', 7)
    create_package_center(dm, 25)


if __name__ == '__main__':
    main()
