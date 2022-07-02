class db():
    ip = ""
    username = ""
    password = ""
    dbname = ""
    charset = "utf8"

    def dbpara(self):
        para_list = [self.ip, self.username, self.password, self.dbname, self.charset]
        return para_list