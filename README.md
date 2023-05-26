# Balancing BST, Visualisation of BST using Python
This repo, contains C++ code, to take an array of integers, convert it to a Binary Search Tree, and Balance it so the BST is optimized for BST Functions. This repo also includes a Python Script, that takes the Preorder traversal of a BST and shows it graphically
===
# Numbers to Tree
You have an array of integers, which you want to convert to an optimised Binary Search Tree, how do you do it?  
* Find the line that says 
```cpp
int nums[] = {numbers_here};
```
Modify the array to suit your numbers, _No two numbers must be the same_  
* Compile and exceute the C++ program, the program should give the following output  
```text 
Before Balancing, inorder and preorder traversals of tree are 
Inorder: 1 2 7 10 11 13 200
Preorder: 1,2,7,10,11,13,200,

After balancing, the inorder and preorder traversals are
Inorder: 1 2 7 10 11 13 200
Preorder: 10,2,1,7,13,11,200, Paste this into the preorder list in the python script
3 is the depth
```
_This is an example output_, the output is pretty self-explanatory. The program outputs both the inorder and preorder traversals, so manual reconstruction of the tree is possible, if needed. However, a Binary Search Tree _can_ be reconstructed from only its preorder traversal, by nature of Binary Search Trees.  
* Paste the preorder traversal into the Python script, so it is stored in a list named `preorder`  
```py
preorder = [paste_here]
```
* Run the Python Script to get the visual representation of the tree
