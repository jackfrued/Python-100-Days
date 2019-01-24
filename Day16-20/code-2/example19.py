"""
扩展性系统性能
- 垂直扩展 - 增加单节点处理能力
- 水平扩展 - 将单节点变成多节点（读写分离/分布式集群）
并发编程 - 加速程序执行 / 改善用户体验
耗时间的任务都尽可能独立的执行，不要阻塞代码的其他部分
- 多线程
1. 创建Thread对象指定target和args属性并通过start方法启动线程
2. 继承Thread类并重写run方法来定义线程执行的任务
3. 创建线程池对象ThreadPoolExecutor并通过submit来提交要执行的任务
第3种方式可以通过Future对象的result方法在将来获得线程的执行结果
也可以通过done方法判定线程是否执行结束
- 多进程
- 异步I/O
"""
import glob
import os
import time

from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from PIL import Image


# class ThumbnailThread(Thread):

#     def __init__(self, infile):
#         self.infile = infile
#         super().__init__()

#     def run(self):
#         file, ext = os.path.splitext(self.infile)
#         filename = file[file.rfind('/') + 1:]
#         for size in (32, 64, 128):
#             outfile = f'thumbnails/{filename}_{size}_{size}.png'
#             image = Image.open(self.infile)
#             image.thumbnail((size, size))
#             image.save(outfile, format='PNG')


def gen_thumbnail(infile):
    file, ext = os.path.splitext(infile)
    filename = file[file.rfind('/') + 1:]
    for size in (32, 64, 128):
        outfile = f'thumbnails/{filename}_{size}_{size}.png'
        image = Image.open(infile)
        image.thumbnail((size, size))
        image.save(outfile, format='PNG')


# def main():
#     start = time.time()
#     threads = []
#     for infile in glob.glob('images/*'):
#         # t = Thread(target=gen_thumbnail, args=(infile, ))
#         t = ThumbnailThread(infile)
#         t.start()
#         threads.append(t)
#     for t in threads:
#         t.join()
#     end = time.time()
#     print(f'耗时: {end - start}秒')


def main():
    pool = ThreadPoolExecutor(max_workers=30)
    futures = []
    start = time.time()
    for infile in glob.glob('images/*'):
        # submit方法是非阻塞式的方法 
        # 即便工作线程数已经用完，submit方法也会接受提交的任务 
        future = pool.submit(gen_thumbnail, infile)
        futures.append(future)
    for future in futures:
        # result方法是一个阻塞式的方法 如果线程还没有结束
        # 暂时取不到线程的执行结果 代码就会在此处阻塞
        future.result()
    end = time.time()
    print(f'耗时: {end - start}秒')
    # shutdown也是非阻塞式的方法 但是如果已经提交的任务还没有执行完
    # 线程池是不会停止工作的 shutdown之后再提交任务就不会执行而且会产生异常
    pool.shutdown()


if __name__ == '__main__':
    main()







