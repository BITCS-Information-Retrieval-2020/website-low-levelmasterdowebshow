import datetime


def UID():
    return '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())

# if __name__ == '__main__':
#     print(UID())

# class UID:
#
#     def __call__(self, *args, **kwargs):
#         return '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())
#
# if __name__ == '__main__':
#     print(UID())