def add_png_saver_arguments(subparsers):
    png_saver_parser = subparsers.add_parser('save', help='将图片保存为./output目录下的png格式')
    png_saver_parser.add_argument(
        '-file_name',
        type=str,
        required=True,
        help='保存的文件名'
    )

    return png_saver_parser