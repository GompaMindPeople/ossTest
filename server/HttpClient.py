from requests import Request, Session


class HttpClient:
    # 主机名,包括端口
    host = ""
    session = None

    # 构造一个session 并保存起来,同时需要传入主机地址,需要加入端口
    def MakeSession(self, host):
        self.session = Session()
        self.host = host

    # 设置的session 的cookies
    def SetSessionCookies(self, cookies):
        self.session.cookies = cookies

    # 发送request请求
    def SendRequest(self, route, method, header, data):
        resp = self.SendRequestByUrl(self.host + route, method, header, data)
        return resp

    def SendRequestByUrl(self, url, method, header, data):
        req = Request(method, url,
                      data=data,
                      headers=header,)

        prepped = self.session.prepare_request(req)
        resp = self.session.send(prepped)
        return resp

    # 通过post上传文件
    def RequestUploadByPost(self, url, header, data, files):
        post = self.session.post(url, data, files=files, headers=header)
        return post
