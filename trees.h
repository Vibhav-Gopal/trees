#include <iostream>
#include <stdlib.h>

struct node
{
    int data;
    node *left;
    node *right;
};

void toBalancedTree(int *, int, node *);
struct ll_node
{
    int data;
    ll_node *next;
};
void preorder(node *root)
{
    if (root != NULL)
    {
        printf("%d ", root->data);
        preorder(root->left);

        preorder(root->right);
    }
}
void preorderCommas(node *root)
{
    if (root != NULL)
    {
        printf("%d,", root->data);
        preorderCommas(root->left);

        preorderCommas(root->right);
    }
}

void inorder(node *root)
{
    if (root != NULL)
    {
        inorder(root->left);
        printf("%d ", root->data);

        inorder(root->right);
    }
}

void postorder(node *root)
{
    if (root != NULL)
    {
        postorder(root->left);

        postorder(root->right);
        printf("%d ", root->data);
    }
}

void appendToLinkedList(ll_node *tmp, int val)
{
    while (tmp->next != NULL)
    {
        tmp = tmp->next;
    }
    tmp->next = (ll_node *)malloc(sizeof(ll_node));
    tmp = tmp->next;
    tmp->next = NULL;
    tmp->data = val;
}

void inorderToLinkedList(node *root, ll_node *head)
{
    if (root != NULL)
    {
        inorderToLinkedList(root->left, head);
        appendToLinkedList(head, root->data);

        inorderToLinkedList(root->right, head);
    }
}

void preorderToLinkedList(node *root, ll_node *head)
{
    if (root != NULL)
    {
        appendToLinkedList(head, root->data);
        preorderToLinkedList(root->left, head);

        preorderToLinkedList(root->right, head);
    }
}

void linkedListToArray(int *array, ll_node *head)
{
    int i = 0;
    while (head != NULL)
    {
        array[i++] = head->data;
        head = head->next;
    }
}

void rotate_left(node **root)
{
    node *right = (*root)->right;
    node *rightleft = right->left;
    (*root)->right = rightleft;
    right->left = (*root);

    *root = right;
}
void rotate_right(node **root)
{
    node *left = (*root)->left;
    node *leftright = left->right;
    (*root)->left = leftright;
    left->right = (*root);
    *root = left;
}
int getDepth(node *root)
{
    if (root == NULL)
        return 0;
    else
    {

        int lDepth = getDepth(root->left);
        int rDepth = getDepth(root->right);

        if (lDepth > rDepth)
            return (lDepth + 1);
        else
            return (rDepth + 1);
    }
}

void insertNode(node *root, int val)
{
    int initVal = (root)->data;
    node *current = root;

    if (val < initVal)
    {
        if (current->left == NULL)
        {
            node *tmp;
            current->left = (node *)malloc(sizeof(node));
            tmp = current->left;
            tmp->left = tmp->right = NULL;
            tmp->data = val;
        }
        else
        {
            insertNode(current->left, val);
        }
    }
    if (val > initVal)
    {
        if (current->right == NULL)
        {
            node *tmp;
            current->right = (node *)malloc(sizeof(node));
            tmp = current->right;
            tmp->left = tmp->right = NULL;
            tmp->data = val;
        }
        else
        {
            insertNode(current->right, val);
        }
    }
}

int balanceFactor(node *root)
{
    int bf = getDepth(root->left) - getDepth(root->right);
    return bf;
}

void makeTree(int leftSubtree[], int leftLength, node *root, int rightSubtree[], int rightLength, int mid)
{
    root->data = mid;
    if (leftLength != 0)
    {
        root->left = (node *)malloc(sizeof(node));
        toBalancedTree(leftSubtree, leftLength, root->left);
    }
    if (rightLength != 0)
    {
        root->right = (node *)malloc(sizeof(node));
        toBalancedTree(rightSubtree, rightLength, root->right);
    }
}

void toBalancedTree(int array[], int length, node *balanced)
{

    int mid = length / 2;
    int leftSize = mid;
    int rightSize = length - mid - 1;
    int leftSubtree[leftSize], rightSubtree[rightSize];
    int leftIndex, rightIndex;
    leftIndex = rightIndex = 0;
    for (int i = 0; i < length; i++)
    {

        if (i < mid)
        {
            leftSubtree[leftIndex++] = array[i];
        }
        if (i > mid)
        {
            rightSubtree[rightIndex++] = array[i];
        }

        int midVal = array[mid];
        // Left subtree, middle element, and right subtree are divided
        makeTree(leftSubtree, leftSize, balanced, rightSubtree, rightSize, midVal);
    }
}