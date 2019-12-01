from mininet.topo import Topo
from mininet.link import TCLink
import os

class Topology(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        os.system("figlet Lab3 Topo")
	
	# Add hosts into topology
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        # Add switches into topology
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
	s4 = self.addSwitch('s4')

        # Add links into topology
	# [TODO] Add contraints(bw, delay, loss) given in topo.png
        self.addLink(s1, h1, port1=1, port2=1)
        self.addLink(s1, s2, port1=2, port2=1)
        self.addLink(s1, s4, port1=3, port2=3)
        self.addLink(s4, h2, port1=1, port2=1)
        self.addLink(s4, s3, port1=2, port2=1)
        self.addLink(s3, s2, port1=2, port2=2)
	      

topos = {
    'topo': (lambda: Topology())
}
