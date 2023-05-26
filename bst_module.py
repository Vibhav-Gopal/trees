import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QBrush, QPen
from PyQt6.QtCore import Qt
# TODO
# Zoom


class Node:
    currentLayer = 0
    depth = 0
    nodes = []

    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
        self.layer = 0
        pass

    def insertNode(self, value):

        if self.data:
            Node.currentLayer += 1
            if value < self.data:
                if self.left == None:
                    self.left = Node(value)
                    self.left.layer = Node.currentLayer
                    Node.depth = max(Node.depth, Node.currentLayer+1)
                    Node.nodes.append(self.left)
                else:
                    self.left.insertNode(value)
            elif value > self.data:
                if self.right == None:
                    self.right = Node(value)
                    self.right.layer = Node.currentLayer
                    Node.depth = max(Node.depth, Node.currentLayer+1)
                    Node.nodes.append(self.right)

                else:
                    self.right.insertNode(value)
        else:
            self.data = value
            Node.nodes.append(self)

        Node.currentLayer = 0
        pass

    def printInorder(self):
        if self.left:
            self.left.printInorder()
        print(self.data)
        if self.right:
            self.right.printInorder()

    def printPreorder(self):
        print(self.data, " layer ", self.layer)
        if self.left:
            self.left.printPreorder()
        if self.right:
            self.right.printPreorder()

    def printPostorder(self):
        if self.left:
            self.left.printPostorder()
        if self.right:
            self.right.printPostorder()
        print(self.data)


ellipses = []
lines = []
coordinates = []
radii = []
texts = []
layers = []
pen = QPen(Qt.GlobalColor.black)
pen.setWidth(2)
def renderTexts():
    for coordinate, radius, txt in zip(coordinates, radii, texts):

        text = QGraphicsTextItem(txt)
        text.setPos(coordinate[0]-radius/2, coordinate[1]-radius/2)
        if txt != "None":
            scene.addItem(text)


def makeNode(radius: int, xcoord=0, ycoord=0, text="test"):
    global ellipses, coordinates
    ellipse = QGraphicsEllipseItem(0, 0, radius, radius)
    ellipse.setPos(xcoord, ycoord)

    brush = QBrush(Qt.GlobalColor.white)
    ellipse.setBrush(brush)

    ellipse.setPen(pen)

    # ellipse.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
    ellipses.append(ellipse)
    coordinates.append([xcoord+radius/2, ycoord+radius/2])
    radii.append(radius)
    texts.append(text)

    scene.addItem(ellipse)
    renderTexts()