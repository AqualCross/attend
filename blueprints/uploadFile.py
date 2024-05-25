from flask import Blueprint, request, render_template
import os


bp = Blueprint('login', __name__, url_prefix='/')


@bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return '无文件部分'

    file = request.files['file']

    if file.filename == '':
        return '没有可选择的文件'

    if file:
        # 设置文件存储路径
        upload_path = os.path.join('static/uploads', file.filename)

        # 检测路径是否存在，不存在则创建
        if not os.path.exists(os.path.dirname(upload_path)):
            os.makedirs(os.path.dirname(upload_path))

        # 存储文件
        file.save(upload_path)
        return '文件已上传'
