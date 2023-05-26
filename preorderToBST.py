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


preorder = [10, 2, 1, 7, 13, 11, 200]


root = Node(None)
for elem in preorder:
    root.insertNode(elem)
depth = Node.depth  # Change this if you want to pad it to a depth
pen = QPen(Qt.GlobalColor.black)
pen.setWidth(2)

width = 1000
height = 400

startX = width//2
startY = 0


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


app = QApplication(sys.argv)

scene = QGraphicsScene(0, 0, width, height)


def renderNodes():
    global startX, startY
    x = startX
    y = startY
    for i in range(depth):
        for node in Node.nodes:

            if node.layer == i:
                makeNode(30, x, y, str(node.data))
                x += 50
            else:
                continue
        y += 50
        x = startX


def renderNodesTest():
    global startX, startY
    x = startX
    y = startY
    for i in range(depth):
        for n in range(2**i):
            makeNode(30, x, y, "Dummy")
            x += 50
        y += 50
        x = startX


def layeriseNodes():
    layers = []  # index indicates level
    for height in range(depth):
        tmp = []
        for node in Node.nodes:
            if node.layer == height:
                tmp.append(node)
        layers.append(tmp)
    return layers


def padToDepth(root: Node, initialDepth=depth, finalDepth=depth, padded=False):
    if padded:
        return
    padded = True
    if root.layer < finalDepth-1 and not root.left:
        root.left = Node(None)
        root.left.layer = root.layer+1
        pos = Node.nodes.index(root)
        Node.nodes.insert(pos+1, root.left)
        padded = False
    if root.layer < finalDepth-1 and not root.right:
        root.right = Node(None)
        root.right.layer = root.layer+1
        pos = Node.nodes.index(root.left)

        Node.nodes.insert(pos+1, root.right)
        padded = False
    if root.layer < finalDepth-1:
        padToDepth(root.left)
        padToDepth(root.right)


def renderLayer(nodesInLayer: list, spreadFactor: float, layerNum: int, layerDist: int, x=startX, y=startY):
    global depth
    y += layerNum*layerDist
    spreadFactor *= 10
    spreadFactor *= depth/2.3
    x -= spreadFactor*layerNum
    for node in nodesInLayer:
        makeNode(30, x, y, str(node.data))
        nextNodeDist = 2*spreadFactor*layerNum
        try:
            nextNodeDist /= ((2**layerNum)-1)
        except:
            pass

        x += nextNodeDist


padToDepth(root)
layers = layeriseNodes()
for layerNum in range(len(layers)):
    renderLayer(nodesInLayer=layers[layerNum],
                spreadFactor=5, layerNum=layerNum, layerDist=50)

for i in range(1, len(coordinates)//2 + 1):

    scene.addLine(coordinates[i-1][0], coordinates[i-1][1]+radii[i]/2,
                  coordinates[2*i-1][0], coordinates[2*i-1][1]-radii[2*i-1]/2, pen)

    scene.addLine(coordinates[i-1][0], coordinates[i-1][1]+radii[i]/2,
                  coordinates[2*i][0], coordinates[2*i][1]-radii[2*i]/2, pen)


view = QGraphicsView(scene)
view.show()
app.exec()
