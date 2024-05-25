function uploadFile() {
    const fileInput = document.getElementById('file');
    const file = fileInput.files[0];

    if (file) {
            const formData = new FormData();
            formData.append('file', file);
            const xhr = new XMLHttpRequest();
            xhr.open('POST', '/upload', true);
            xhr.onload = function () {
                if (xhr.status === 200) {
                    alert('文件上传成功');
                } else {
                    alert('文件上传失败');
                }
            };
            xhr.send(formData);
        } else {
            alert('请选择一个文件');
        }
    }