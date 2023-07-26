from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch, Controller
from mininet.log import setLogLevel
from mininet.cli import CLI

class Topologia(Topo):
    def build(self):
        # Add switches
        self.s1 = self.addSwitch('s1', cls=OVSSwitch)
        self.s2 = self.addSwitch('s2', cls=OVSSwitch)
        self.s3 = self.addSwitch('s3', cls=OVSSwitch)
        self.s4 = self.addSwitch('s4', cls=OVSSwitch)

        # Add hosts
        h1 = self.addHost('h1', ip='10.0.0.1', mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', ip='10.0.0.2', mac='00:00:00:00:00:02')
        h3 = self.addHost('h3', ip='10.0.0.3', mac='00:00:00:00:00:03')
        h4 = self.addHost('h4', ip='10.0.0.4', mac='00:00:00:00:00:04')
        h5 = self.addHost('h5', ip='10.0.0.5', mac='00:00:00:00:00:05')
        h6 = self.addHost('h6', ip='10.0.0.6', mac='00:00:00:00:00:06')
        h7 = self.addHost('h7', ip='10.0.0.7', mac='00:00:00:00:00:07')
        h8 = self.addHost('h8', ip='10.0.0.8', mac='00:00:00:00:00:08')
        h9 = self.addHost('h9', ip='10.0.0.9', mac='00:00:00:00:00:09')
        h10 = self.addHost('h10', ip='10.0.0.10', mac='00:00:00:00:00:10')

        # Add conexoes
        self.addLink(h1, self.s1)
        self.addLink(h2, self.s1)
        self.addLink(h3, self.s1)

        self.addLink(h4, self.s2)
        self.addLink(h5, self.s2)
        self.addLink(h6, self.s2)
        self.addLink(h7, self.s3)
        self.addLink(h8, self.s3)

        self.addLink(h9, self.s4)
        self.addLink(h10, self.s4)

        # Add connections between switches
        self.addLink(self.s1, self.s2)
        self.addLink(self.s2, self.s3)
        self.addLink(self.s4, self.s1)

if __name__ == '__main__':
    setLogLevel('info')

    topo = Topologia()
    net = Mininet(topo=topo, switch=OVSSwitch, controller=Controller)
    net.start()
    
    # Acessar os switches e adicionar as regras do firewall
    s1 = net.get('s1')
    s1.cmd('ovs-ofctl add-flow s1 "priority=10,dl_type=0x0800,nw_src=10.0.0.1,nw_dst=10.0.0.5,actions=drop"')
    s1.cmd('ovs-ofctl add-flow s1 "priority=10,dl_type=0x0800,nw_src=10.0.0.5,nw_dst=10.0.0.1,actions=drop"')

    s3 = net.get('s3')
    s3.cmd('ovs-ofctl add-flow s2 "priority=10,dl_src=00:00:00:00:00:08,dl_dst=00:00:00:00:00:10,actions=drop"')
    s3.cmd('ovs-ofctl add-flow s2 "priority=10,dl_src=00:00:00:00:00:10,dl_dst=00:00:00:00:00:08,actions=drop"')

    h1 = net.get('h1')
    h1.cmd('python -m SimpleHTTPServer 80 &')

    h8 = net.get('h8')
    h8.cmd('python -m SimpleHTTPServer 80 &')

    # Teste de conectividade entre os hosts usando o pingall
    #net.pingAll()
    
    # Teste de ping entre h8 e h10
    #h8 = net.get('h8')
    #h10 = net.get('h10')
    #print(h8.cmd('ping -c 3 10.0.0.10'))

    # Iniciar a CLI do Mininet
    CLI(net)

    # Parar o controlador manualmente
    #net.controllers[0].stop()

    net.stop()