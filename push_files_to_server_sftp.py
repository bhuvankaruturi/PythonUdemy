import pysftp as sftp

def push_file_to_server():
    #cnopts = sftp.CnOpts()
    #cnopts.hostkeys.load('aws-pyTut-1-publicKey')
    #cnopts.hostkeys = None
    s = sftp.Connection(host='13.127.25.158', username='ubuntu',password='bapatla950bpp',cnopt=cnopts)
    local_path = "compare_1_3.py"
    remote_path = "/home/compare.py"
    s.put(local_path, remote_path)
    s.close()

#push_file_to_server()

def get_file_from_server():
    #cnopts = sftp.CnOpts()
    #cnopts.hostkeys.load('aws-pyTut-1-publicKey')
    #cnopts.hostkeys = None
    s = sftp.Connection(host='13.127.25.158', username='ubuntu',password='bapatla950bpp',cnopts=cnopts)
    local_path = "compare_1_3.py"
    remote_path = "/home/compare.py"
    s.get(remote_path, local_path)
    s.close()

#get_file_from_server()
