#include "trees.h"

using namespace std;

int main()
{
  node *parent = (node *)malloc(sizeof(node));
  // int nums[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18, 20, 21, 26, 28, 29, 30, 31, 32, 35, 36, 39, 42, 47, 49};
  int nums[] = {1, 2, 7, 10, 11, 13, 200};
  int length = sizeof(nums) / sizeof(nums[0]);
  parent->data = nums[0];
  parent->left = parent->right = NULL;

  for (int i = 1; i < length; i++)
  {
    insertNode(parent, nums[i]);
  }

  ll_node *head = (ll_node *)malloc(sizeof(ll_node));
  head->next = NULL;
  inorderToLinkedList(parent, head);
  head = head->next;

  int sorted[length];
  linkedListToArray(sorted, head);

  node *balancedTree = (node *)malloc(sizeof(node));
  toBalancedTree(sorted, length, balancedTree);

  cout << "Before Balancing, inorder and preorder traversals of tree are \n";
  cout << "Inorder: ";
  inorder(parent);
  cout << endl;
  cout << "Preorder: ";
  preorderCommas(parent);
  cout << endl;
  cout << "\nAfter balancing, the inorder and preorder traversals are \n";
  cout << "Inorder: ";
  inorder(balancedTree);
  cout << endl;
  cout << "Preorder: ";
  preorderCommas(balancedTree);
  cout << " Paste this into the preorder list in the python script " << endl;

  // Getting preorder traversal in array form
  ll_node *preorderLL = (ll_node *)malloc(sizeof(ll_node));
  preorderLL->next = NULL;
  preorderToLinkedList(balancedTree, preorderLL);
  preorderLL = preorderLL->next;
  int preordered[length];
  linkedListToArray(preordered, preorderLL);

  // Rebuilding Tree from only preorder traversal
  node *newTree = (node *)malloc(sizeof(node));
  newTree->data = preordered[0];
  newTree->left = newTree->right = NULL;
  for (int i = 1; i < length; i++)
  {
    insertNode(newTree, preordered[i]);
  }
  cout << getDepth(newTree) << " is the depth\n";
}
