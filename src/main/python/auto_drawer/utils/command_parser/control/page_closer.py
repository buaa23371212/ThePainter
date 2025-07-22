def add_close_page_argument(subparsers):
    close_page_parser = subparsers.add_parser('close_page', help='关闭当前页面')

    return close_page_parser