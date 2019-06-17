#-*- coding:utf8 -*-
import os, sys, subprocess, tempfile, time,shutil



# 文件名
FileNum = int(time.time() * 1000)
# python编译器位置
EXEC = sys.executable

class TimeoutException(Exception): pass

# 获取python版本
def get_version():
    v = sys.version_info
    version = "python %s.%s" % (v.major, v.minor)
    return version


# 获得py文件名
def get_pyname():
    global FileNum
    return 'test_%d' % FileNum


# 接收代码写入文件
def write_file(pyname, code,username):
    # 创建临时文件夹,返回临时文件夹路径
    dir = os.path.join('E:\\temp',username)
    if not os.path.exists(dir):
        os.mkdir(dir)
    os.chdir(dir)
    fpath = os.path.join(dir, '%s.py' % pyname)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(code)
    return fpath


# 编码
def decode(s):
    try:
        return s.decode('utf-8')
    except UnicodeDecodeError:
        return s.decode('gbk')

        # 主执行函数


def main(code,username):
    r = dict()
    r["version"] = get_version()
    pyname = get_pyname()
    fpath = write_file(pyname, code,username)
    try:
        # subprocess.check_output 是 父进程等待子进程完成，返回子进程向标准输出的输出结果
        # stderr是标准输出的类型
        outdata = decode(subprocess.check_output([EXEC, fpath], stderr=subprocess.STDOUT, timeout=5))
    except subprocess.CalledProcessError as e:
        # e.output是错误信息标准输出
        # 错误返回的数据
        r["code"] = 'Error'
        r["output"] = decode(e.output).split('\n')[-2]
        return r
    except subprocess.TimeoutExpired as e:
        # e.output是错误信息标准输出
        # 错误返回的数据
        r["code"] = 'Error'
        r["output"] = '您的程序已超时'
        return r
    else:
        # 成功返回的数据
        r['output'] = outdata
        r["code"] = "Success"
        return r
    finally:
        # 删除文件(其实不用删除临时文件会自动删除)
        try:
            os.chdir('E:\\temp')
            dir = os.path.join('E:\\temp', username)
            shutil.rmtree(dir)
        except Exception as e:
            exit(1)


def correct(file):
    r = dict()
    r["version"] = get_version()
    pyname = get_pyname()
    try:
        print(EXEC)
        # subprocess.check_output 是 父进程等待子进程完成，返回子进程向标准输出的输出结果
        # stderr是标准输出的类型
        outdata = decode(subprocess.check_output([EXEC, file], stderr=subprocess.STDOUT, timeout=5))
    except subprocess.CalledProcessError as e:
        # e.output是错误信息标准输出
        # 错误返回的数据
        r["code"] = 'Error'
        r["output"] = decode(e.output).split('\n')[-2]
        return r
    except subprocess.TimeoutExpired as e:
        # e.output是错误信息标准输出
        # 错误返回的数据
        r["code"] = 'Error'
        r["output"] = '您的程序已超时'
        return r
    else:
        # 成功返回的数据
        r['output'] = outdata
        r["code"] = "Success"
        return r






if __name__ == '__main__':
  code = "open('test.txt','w+')"
  result = main(code,'111')
  #file = 'E:\\python\\happyPY\\hlPY\\results\\practice\\test.txt'
  #result1=correct(file)
  #print(result1)



