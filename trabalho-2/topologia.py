#!/usr/bin/python
"""
Topologia:

     h1/h2/h3 - s1 ------ s2 - h4/h5/h6
                 |         |
        h7/h8 - s3        s4 - h9/h10

"""
from mininet.topo import Topo

class Topologia(Topo):
    def __init__( self ):

        # Inicializa topologia
        Topo.__init__( self )
        #adicionar switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        #adionar hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')

        # Adicionar conexoes
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)

        self.addLink(h4, s2)
        self.addLink(h5, s2)
        self.addLink(h6, s2)

        self.addLink(h7, s3)
        self.addLink(h8, s3)

        self.addLink(h9, s4)
        self.addLink(h10, s4)

        #adicionando conexoes
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s4, s1)

topos = { 'mytopo': ( lambda: Topologia() ) }