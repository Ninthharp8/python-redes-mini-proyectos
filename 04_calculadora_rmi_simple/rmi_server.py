import Pyro4

@Pyro4.expose
class hitung(object):
    def Mul_func(self,num1,num2):
        return (num1*num2)
    def Sub_func(self,num1,num2):
        if(num1<num2):
            a = num2-num1
        else:
            a = num1-num2
        return a    
    def Add_func(self,num1,num2):
        return (num1+num2)
    def Div_func(self,num1,num2):
        return (num1/num2)


daemon = Pyro4.Daemon(host="192.168.1.4",port=8000)
ns = Pyro4.locateNS()
uri = daemon.register(hitung)
ns.register("penghitung", uri)

print("Ready.")
daemon.requestLoop()