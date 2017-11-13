import pymysql

def connection():
    conn = pymysql.connect(host = 'localhost',
                           user = 'root',
                           passwd = 'bapatla950bpp',
                           db = 'MyDB')
    c = conn.cursor()

    return c, conn

if __name__ == '__main__':
    c, conn = connection()
    print('It worked!')
