# Balancing BST, Visualisation of BST using Python  

This repo, contains C++ code, to take an array of integers, convert it to a Binary Search Tree, and Balance it so the BST is optimized for BST Functions. This repo also includes a Python Script, that takes the Preorder traversal of a BST and shows it graphically
***
# Numbers to Tree
You have an array of integers, which you want to convert to an optimised Binary Search Tree, how do you do it?  
## Dependencies
* Python Dependency - `PyQt6` for generating GUI tree 
## Procedure
* Find the line that says 
```cpp
int nums[] = {numbers_here};
```
Modify the array to suit your numbers, __No two numbers must be the same__  
* Compile and execute the C++ program, the program should give the following output  
```text 
Before Balancing, inorder and preorder traversals of tree are 
Inorder: 1 2 7 10 11 13 200
Preorder: 1,2,7,10,11,13,200,

After balancing, the inorder and preorder traversals are
Inorder: 1 2 7 10 11 13 200
Preorder: 10,2,1,7,13,11,200, Paste this into the preorder list in the python script
3 is the depth
```
__This is an example output__, the output is pretty self-explanatory. The program outputs both the inorder and preorder traversals, so manual reconstruction of the tree is possible, if needed. However, a Binary Search Tree __can__ be reconstructed from only its preorder traversal, by nature of Binary Search Trees.  
* Paste the preorder traversal into the Python script, so it is stored in a list named `preorder`  
```py
preorder = [paste_here]
```
* Run the Python Script to get the visual representation of the tree
***
# Visual Customisation
To customise how the output looks,  
* **Layout**  
Modify `spreadFactor` value and `layerDist` Value in the python script, the code snippet is shown below. `spreadFactor` controls how far the nodes are spread apart on the X axis, whereas `layerDist` controls how far the layers of the tree are on the Y axis
```py
for layerNum in range(len(layers)):
    renderLayer(nodesInLayer=layers[layerNum],
                spreadFactor=5, layerNum=layerNum, layerDist=50)
```
* **Fill Color**  
Modify the following line to set background color of nodes in `makeNode()`
```py
brush = QBrush(Qt.GlobalColor.white)
```

* **Line Thickness**  
To set the global line thickness or line color, modify the following lines
```py
pen = QPen(Qt.GlobalColor.black)
pen.setWidth(2)
```

* **Visibility of circles for nodes**  
If you prefer not having circles bounding the numbers and prefer only numbers with lines for the tree, comment out this line in `makeNode()`  
```py
scene.addItem(ellipse)
```

* **To modify text styling**  
To change the text styling, modify the `QGraphicsTextItem` object attributes in `renderTexts()`, refer to `PyQt6` documentation for instructions on how to do that.  
  
* **Window Layout**
To change the size of the window, modify the lines of code
```py
width = 1000
height = 400
```
*** 
# Future Scope
Future plans 
* To implement zooming functionality in the window
* To implement panning functionality in the window
* To add a webpage, that provides a more interactive and comfortable display of the tree, along with other additional features such as, directly building the tree in a GUI environment, and then providing the various tree traversals so they can be reconstructed in other programs.
***
# Extra functions
There are a lot of helper functions written in `trees.h`, go through them if you wanna know more.